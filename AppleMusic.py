import re
import pandas as pd
import requests
import math
import time
from Statements import statements
# import pprint
import json
import os

from flask import render_template



url = "http://127.0.0.1:5000/statements"


pd.options.mode.copy_on_write = True
pd.set_option('display.max_rows', None)


class AppleMusicFunctions:
    
######################
## Song Extraction ###
######################

# FINDS DISLIKED SONGS, AND MAKES THEM READY FOR THE ENTITY LINKER
    def __init__(self):
        self.processed_track = 0
        self.total_tracks = 0
        self.load_cache()
    
    def load_cache(self):
        try:
            with open(os.path.join(os.path.dirname(__file__), "data/cache_files/AppleMcache.json"), 'r', encoding='utf-8') as file:
                self.cache = json.load(file)
        except FileNotFoundError:
            self.cache = {}

    def save_cache(self, cache):
        with open(os.path.join(os.path.dirname(__file__), "data/cache_files/AppleMcache.json"), 'w', encoding='utf-8') as file:
            json.dump(self.cache, file, indent=4)

    def read_csv(self, file_path):
        df = pd.read_csv(file_path)
        return df

    def disliked_songs(self, df):
        """sumary_line
        
        Keyword arguments:
        df -- dataframe 
        Return: return_description
        """
        
        # Checks for songs played shorter than 30 seconds:
        df_less_than_30000ms = df[df['Play Duration Milliseconds']<=30000]
        # Checks for skipped songs played shorter than 30 seconds:
        sum_skipped_songs = df_less_than_30000ms.groupby(['Track Identifier', 'Track Description'])['Skip Count'].sum().reset_index()
        # Gets total playcount for each song
        total_play_count = df.groupby(['Track Identifier', 'Track Description'])['Play Count'].sum().reset_index()

        # Merges sum_skipped_song with total_play_count to be able to compare skips with total play count
        merged_df = total_play_count.merge(sum_skipped_songs, on=['Track Identifier', 'Track Description'], how='left')
        # Compares Skip count with play count
        merged_df['More Skips than Plays'] = merged_df['Skip Count'] > merged_df['Play Count']
        # Gets rid of songs skipped only once
        skipped_more_than_played = merged_df[merged_df['More Skips than Plays'] & (merged_df["Skip Count"]>1)]


# CREATES LISTS OF DISLIKED SONGS TO BE SENT FOR ENTITY LINKING
        Song_Names = []
        Artists_and_Groups = []
        Songs_ignored=0
        for description in skipped_more_than_played['Track Description']:
            parts = description.split(" - ")
            if len(parts) == 2:
                artist_or_group, song_name = parts
                if song_name != None and artist_or_group != None:
                    Song_Names.append(song_name.strip())
                    Artists_and_Groups.append(artist_or_group.strip())
                else: Songs_ignored+=1        
            else: Songs_ignored+=1
        
        return Song_Names, Artists_and_Groups



    def liked_songs(self, df):
        
        # Gets total playcount for each song
        total_play_count = df.groupby(['Track Identifier', 'Track Description'])['Play Count'].sum().reset_index()
        # Sorts total_play_count in descending order
        sorted_total_play_count = total_play_count.sort_values(by='Play Count', ascending=False)
        
        # Convert 'Date Played' column to datetime type if it's not already
        df['Date Played'] = pd.to_datetime(df['Date Played'], format='%Y%m%d')
        # Extracts year from 'Date Played' column
        df['Year'] = df['Date Played'].dt.year.astype(str)
        # Groups by track identifier, track description, and year, then count occurrences
        play_count_by_year = df.groupby(['Track Identifier', 'Year'])['Play Count'].sum().reset_index()
        # Sorts in descending order
        play_count_by_year=play_count_by_year.sort_values(by='Play Count', ascending=False)
        # Counts number of unique songs by track id
        unique_songs = df['Track Identifier'].nunique()

        sorted_total_play_count_filtered = sorted_total_play_count
        play_count_by_year_filtered= play_count_by_year
        
        # USED FOR TESTING LESS SONGS:
        # sorted_total_play_count_filtered = sorted_total_play_count[sorted_total_play_count['Play Count'] >= 30]
        # play_count_by_year_filtered= play_count_by_year[play_count_by_year['Play Count'] >= 30]

        if len(play_count_by_year_filtered) == 0:
            return "Not enough data"
        elif 0 < len(play_count_by_year_filtered):#< 37:
            # Filters out the songs with play counts lower than 30 
            merged_df = pd.merge(sorted_total_play_count_filtered, play_count_by_year_filtered[['Track Identifier', 'Year']], on='Track Identifier', how='left')
            # Fills NaN values in 'Year' with empty strings
            merged_df['Year'] = merged_df['Year'].fillna('')

            # Groups the dataframe by 'Track Identifier' and adds the 'Year' column values into single strings. Separates years within with commas
            merged_df['Year'] = merged_df.groupby('Track Identifier')['Year'].transform(lambda x: ','.join(x.astype(str)))

            # Gets rid of duplicates

            enjoyed_songs_df = merged_df.drop_duplicates()
            
            # print(enjoyed_songs_df)

            # Removes duplicates and sorts the years
            result = enjoyed_songs_df.groupby('Track Description').agg({
                'Year': lambda x: ', '.join(map(str, sorted(set(x))))  
            }).reset_index()
            # print(len(play_count_by_year_filtered))

        elif len(play_count_by_year_filtered)>=37:
        
            #The top 5 percent of songs for the user: 
            top_5_percent=math.ceil(unique_songs/20)
            #Top 20
            top_20_percent=math.ceil(unique_songs/5)

            # Gets the relative top songs  
            top_5_percent_songs = sorted_total_play_count.head(top_5_percent)
            play_count_by_year_top_20_percent = play_count_by_year.head(top_20_percent)

            # Merges to get songs who's years where within top 20% and the top 5% in total listens. The top 5% get the years from the top 20%
            merged_df = pd.merge(top_5_percent_songs, play_count_by_year_top_20_percent[['Track Identifier', 'Year']], on='Track Identifier', how='left')

            # Fills NaN values in 'Year' with empty strings
            merged_df['Year'] = merged_df['Year'].fillna('')

            # Groups the dataframe by 'Track Identifier' and adds the 'Year' column values into single strings. Separates years in years column with commas
            merged_df['Year'] = merged_df.groupby('Track Identifier')['Year'].transform(lambda x: ','.join(x.astype(str)))

            # Gets rid of duplicates
            enjoyed_songs_df = merged_df.drop_duplicates()
            result = enjoyed_songs_df.groupby('Track Description').agg({
                'Year': lambda x: ', '.join(map(str, sorted(set(x))))  # Removes duplicates and sorts the years
            }).reset_index()
            # return enjoyed_songs_df
        
        Year = []
        # Splitting song names from artists:
        Song_Names = []
        Artists_and_Groups = []
        # Artists_and_Groups_Underscore=[]
        i=0
        Songs_ignored=0
        # Splits on ( - ) and puts the parts in two lists
        for description in result['Track Description']:
            parts = description.split(" - ")
            if len(parts) == 2:
                artist_or_group, song_name = parts
                Song_Names.append(song_name.strip())
                Artists_and_Groups.append(artist_or_group.strip())
                Year.append(enjoyed_songs_df['Year'][i])
            else: 
                print(parts)
                Songs_ignored+=1    
            i+=1

        # Code for checking the ignored songs 
        # Songs_ignored=str(Songs_ignored)
        # print("Songs ignored: "+Songs_ignored)
        # print("Song name length: "+str(len(Song_Names)))
        # for song in Song_Names:
        #     print(song)
        # print(Song_Names)
        self.total_tracks = len(Song_Names)
        print("Total tracks: ", self.total_tracks)
        return Year, Song_Names, Artists_and_Groups


######################
### entity linking ###
######################

###################################
### Music Brainz entity linking ###
###################################


    def extract_and_clean_name(self, song_name):
        # featured_artists=[]
        # Regular expressions to find featured artists within parentheses
        featured_artists = re.findall(r'\(feat\.? ([^)]+)\)', song_name)
        # Cleans the song name by removing the section in parenthesis
        cleaned_name = re.sub(r'\s*\(feat\.? [^)]+\)\s*', ' ', song_name).strip()
        if (re.findall(r'\[feat\.? ([^)]+)\]', song_name))!=[]:
            featured_artists.append(re.findall(r'\[feat\.? ([^)]+)\]', song_name))
        cleaned_name = re.sub(r'\s*\[feat\.? [^)]+\]\s*', ' ', cleaned_name).strip()
        # Extracts any strings within brackets
        tags = re.findall(r'\[(.*?)\]', cleaned_name)
        # Cleans the song name by removing the tags
        cleaned_name = re.sub(r'\s*\[.*?\]\s*', ' ', cleaned_name).strip()
        return cleaned_name, featured_artists, tags


    def artist_check_musicbrainz(self, artist):
        # Checks if the artist exists in MusicBrainz
        url_artist = 'https://musicbrainz.org/ws/2/artist'
        params = {'query': f'"{artist}"', 'fmt': 'json'}
        response = requests.get(url_artist, params=params)
        data = response.json()
        # Prevents too quick requests to the MusicBrainz API (Too many requests lead to musicbrainz halting their responses)
        time.sleep(1)
        # If there's no artist data, it returns None, otherwise it returns the artist data
        if 'artists' in data and len(data['artists']) > 0:
            return data['artists'][0]
        return None

    def handle_artists(self, artist_string):
        # Tries combinations of artist names to find a match

        if self.artist_check_musicbrainz(artist_string):
            return [artist_string]
        parts = artist_string.split(', ')
        artists_listed = []
        
        for part in parts:
            # Tests each part individually first
            if self.artist_check_musicbrainz(part):
                artists_listed.append(part)
            elif '&' in part:
                # If the part contains '&', splits again
                subparts = part.split(' & ')
                
                # Checks the combined form "Artist1 & Artist2"
                if not self.artist_check_musicbrainz(part):
                    # Checks each artist individually if combined fails
                    for subpart in subparts:
                        if self.artist_check_musicbrainz(subpart):
                            artists_listed.append(subpart)
                else:
                    artists_listed.append(part)
                    
        return artists_listed

    def search_track_musicbrainz(self, song_names, artists_and_groups):
        # Searches for the songs in the cache, and if there's no entry of it, to the MusicBrainz API
        url = 'https://musicbrainz.org/ws/2/recording'
        url_musicbrainz_track = 'https://musicbrainz.org/recording/'
        url_musicbrainz_artist = 'https://musicbrainz.org/artist/'
        search_results = []
        main_artist_names = []
        entity_links_musicbrainz_tracks = []
        entity_links_musicbrainz_artists = []
        Cleaned_Songs=[]
        Queries=[]
        artist_queries=[]
        
        
        for song_name, artists in zip(song_names, artists_and_groups):

            # print(song_name)
            self.processed_track += 1
            print("processed track: ", self.processed_track)
            # Loads the cache (creates the cache if it's not there)
            
            key=song_name+artists
            # Checks for entry in the cache
            if key not in self.cache:
                # Gets the song name, artists from the song part, and any tags.
                song_cleaned, featured_artists, tags = self.extract_and_clean_name(song_name)
                
                Cleaned_Songs.append(song_cleaned)

                artists = self.handle_artists(artists.strip(', '))
                
                # Takes out what's most likely the main artist (leftmost artist in the title) 
                main_artist_data = self.artist_check_musicbrainz(artists[0])
                if main_artist_data is None:
                    # print(f"Main artist not found: {main_artist_name}")
                    main_artist_names.append('Artist not found')
                    pass
                else:
                    # print("Main artist found")
                    main_artist_names.append(artists[0])
                
                featured_artists=str(featured_artists)
                
                featured_artists=featured_artists.strip("'[]\"")
                featured_artists = self.handle_artists(featured_artists.strip(', '))
                
                
                # Adds featured artists to the list
                if featured_artists!=[]:
                    
                    artists += featured_artists
                
                # Puts quotes around artists from a list and adds them to a variable
                artist_query_part = ' '.join(f'"{artist}"' for artist in artists)

                # Constructs the query with all artists, song name, and tags (if any)        
                if tags==[]:
                    query = f'"{song_cleaned}" {artist_query_part}'
                else: 
                    tags=str(tags).strip("'[]\"")
                    query = f'"{song_cleaned}"{artist_query_part} {tags}'
                params = {'query': query, 'fmt': 'json'}
                Queries.append(query)
                print("hei",query)
                # Makes the artists ready to be put in the statement
                artist_query_part=artist_query_part.split('" "')
                artist_query_part='", "'.join(artist_query_part)
                artist_query_part=artist_query_part.replace('"','')
                artist_queries.append(artist_query_part)   

          
                response = requests.get(url, params=params)
                data = response.json()
                # Checks if there's a response with a recording
                if 'recordings' in data and data['recordings']:
                    # Gets the first element in the response
                    recording = data['recordings'][0]
                    recording_main_artist_id = recording['artist-credit'][0]['artist']['id']
                    
                    # print(recording_main_artist_id)
                    # print(main_artist_data['id'])
                    # Checks if the obtained recording artist matches the main from the start
                    try: 
                        if recording_main_artist_id == main_artist_data['id']:
                            search_results.append(recording)
                            
                            
                            track_entity_link=url_musicbrainz_track+data['recordings'][0]['id']
                            entity_links_musicbrainz_tracks.append(track_entity_link)
                            # print(entity_links_musicbrainz_tracks)

                            artist_entity_link=url_musicbrainz_artist+main_artist_data['id']
                            entity_links_musicbrainz_artists.append(artist_entity_link)
                            # print(entity_links_musicbrainz_artists)
                        
                            # print(recording)
                        else:
                            # print(f"Artist ID mismatch for {song_name}: {recording_main_artist_id} != {main_artist_data['id']}")
                            entity_links_musicbrainz_tracks.append("Track link not found")
                            entity_links_musicbrainz_artists.append("Artist link not found")
                            main_artist_names=main_artist_names[0:-1]
                            main_artist_names.append("Wrong artist found")

                    except:
                        # print(f"Artist ID mismatch for {song_name}: {recording_main_artist_id} != {main_artist_data['id']}")
                        entity_links_musicbrainz_tracks.append("Track link not found")
                        entity_links_musicbrainz_artists.append("Artist link not found")
                        main_artist_names=main_artist_names[0:-1]
                        main_artist_names.append("Wrong artist found")
                else:
                    # print('No recordings found for', song_name)
                    entity_links_musicbrainz_tracks.append("Track not found")
                    entity_links_musicbrainz_artists.append("Artist not found")
                    main_artist_names=main_artist_names[0:-1]
                    main_artist_names.append("Wrong artist found")

                # Updates the cache  
                self.cache[key] = {
                    'main_artist_name': main_artist_names[-1],
                    'entity_link_artist': entity_links_musicbrainz_artists[-1],
                    'entity_link_track': entity_links_musicbrainz_tracks[-1],
                    'cleaned_song': Cleaned_Songs[-1],
                    'artist_queries': artist_queries[-1]
                }

                self.save_cache(self.cache)
                
                
            else: 
                # print(cache[key])
                # Returns the cache data when it's there
                main_artist_names.append(self.cache[key]['main_artist_name'])
                entity_links_musicbrainz_artists.append(self.cache[key]['entity_link_artist'])
                entity_links_musicbrainz_tracks.append(self.cache[key]['entity_link_track'])
                Cleaned_Songs.append(self.cache[key]['cleaned_song'])
                artist_queries.append(self.cache[key]['artist_queries'])
        
        return main_artist_names, entity_links_musicbrainz_artists, entity_links_musicbrainz_tracks, Cleaned_Songs, Queries, artist_queries

