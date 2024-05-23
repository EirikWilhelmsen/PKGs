"""Class for handling personal data from Spotify"""
import re
import requests
import json
from rfc3987 import match
from PKGClass import URI
import time
import os

class SpotifyFunctions:
    def __init__(self):
        self.total_tracks = 0
        self.processed_tracks = 0
        self.artist_index = 0
        self.temp_song=[]
        self.current_song_name = ""
        self.load_artist_and_song_id()
        
    def read_json_file(self, file_path):
        """Reads a json file
        Keyword arguments:
        file_path -- path to the file
        Return: data -- data from the file
        """

        with open(file_path, 'r', encoding='utf-8') as json_file:
            print("fant fil", file_path)
            data = json.load(json_file)
        return data
    
    def load_artist_and_song_id(self):
        """Loads artists and songs from cache file"""
        
        try:
            with open(os.path.join(os.path.dirname(__file__), "data/cache_files/artist_and_song_id.json"), 'r', encoding='utf-8') as file:
                self.artist_and_song_id = json.load(file)
        except FileNotFoundError:
            self.artist_and_song_id = []
    
    def save_artist_and_song_id(self):
        """Saves artists and songs to cache file"""

        with open(os.path.join(os.path.dirname(__file__), "data/cache_files/artist_and_song_id.json"), 'w', encoding='utf-8') as file:
            json.dump(self.artist_and_song_id, file)
    
    def generate_variants(self,song_name):
        """Generates variants of the song name
        Keyword arguments:
        song_name -- song name
        Return: variants -- list of song name variants with different apostrophes
        """
        variants = [song_name]
        if "'" in song_name:
            variants.append(song_name.replace("'", "`"))
            variants.append(song_name.replace("'", "’"))
        elif "`" in song_name:
            variants.append(song_name.replace("`", "'"))
            variants.append(song_name.replace("`", "’"))
        elif "’" in song_name:
            variants.append(song_name.replace("’", "'"))
            variants.append(song_name.replace("’", "`"))
        return variants
    
    def remove_feat_part(self,song_title):
        """Removes feat or with part of the song title, musicbrainz does not recognize it
        
        Keyword arguments:
        song_title -- song title
        Return: song_title -- cleaned song title
        """
        
        pattern = r'\(feat[^\)]*\)|\(with[^\)]*\)'
        cleaned_title = re.sub(pattern, '', song_title)
        return cleaned_title.strip()

    
    def search_artist(self, artist_name, song_name):
        """searches musicbrainz for artist and song
        
        Keyword arguments:
        artist_name -- artist name
        song_name -- song name
        Return:
        artist_URI -- URI of the artist
        song_URI -- URI of the song
        """
        song_names = self.generate_variants(song_name)
        for item in self.artist_and_song_id:
            for variant in song_names:
                if item["artist_name"] == artist_name and item["song_name"] == variant:
                    print("Found in cache")
                    return item["artist_URI"], item["song_URI"], item["song_name"]

        print(len(song_names), song_names)
        
        url = 'https://musicbrainz.org/ws/2/recording'
        params = {
            'query': f'"{artist_name}" "{song_name}"',
            'fmt': 'json',  # Response format
            'limit': 8
        }
        response = requests.get(url, params=params)
        data = response.json()

        print(f"søker {artist_name} - {song_name}")

        time.sleep(1.1)

        # A lot of data is processed here to avoid searching musicbrainz multiple times

        if data.get('recordings'):
            for record in data['recordings']:
                for song_name in song_names:
                    if len(record['artist-credit']) > 1 and self.artist_index < len(record['artist-credit']):
                        if artist_name == record['artist-credit'][self.artist_index]['artist']['name'] and song_name == record['title']:
                            artist_template = f"https://musicbrainz.org/artist/{record['artist-credit'][self.artist_index]['artist']['id']}"
                            artist_uri = URI(artist_template.format(entity_name=artist_name))
                            song_template = f"https://musicbrainz.org/recording/{record['id']}"
                            song_uri = URI(song_template.format(entity_name=song_name))
                            if self.current_song_name in self.generate_variants(song_name):
                                song_name = self.current_song_name
                            self.artist_and_song_id.append({"artist_name": artist_name, "song_name": song_name, "artist_URI": artist_uri, "song_URI": song_uri})
                            self.save_artist_and_song_id()
                            self.artist_index += 1
                            return artist_uri, song_uri, song_name
                    elif artist_name == record['artist-credit'][0]['artist']['name'] and song_name == record['title']:
                        artist_template = f"https://musicbrainz.org/artist/{record['artist-credit'][0]['artist']['id']}"
                        artist_uri = URI(artist_template.format(entity_name=artist_name))
                        song_template = f"https://musicbrainz.org/recording/{record['id']}"
                        song_uri = URI(song_template.format(entity_name=song_name))
                        if self.current_song_name in self.generate_variants(song_name):
                            song_name = self.current_song_name
                        self.artist_and_song_id.append({"artist_name": artist_name, "song_name": song_name, "artist_URI": artist_uri, "song_URI": song_uri})
                        self.save_artist_and_song_id()
                        self.artist_index += 1
                        return artist_uri, song_uri, song_name
                self.artist_and_song_id.append({"artist_name": artist_name, "song_name": song_name, "artist_URI": "No:URI:found", "song_URI": "No:URI:found"})
                self.save_artist_and_song_id()
                self.artist_index += 1
                return None, None, song_name
        else:
            self.artist_index
            return "No response", "No response", "No response"

    def assign_URI(self, file_path):
        """assign the URI for the artist and song
        
        Keyword arguments:
        file_path -- path to the file
        Return: 
        data -- list of dictionaries with track information,
        track_URI_list -- list of track URIs 
        artist_URI_list -- list of artist URIs
        """
        
        with open(file_path, 'r') as file:
            data = json.load(file)

        track_URI_list_combined = []
        track_URI_list = []
        artist_URI_list = []
        song_names = []
        self.total_tracks = len(data)
        self.processed_tracks = 0

        for track in data:
            artist_uri_list = []
            track_uri_list = []
            self.artist_index = 0
            song_name = self.remove_feat_part(track['name'])
            for artist in track["artists"]: # in case of multiple artists
                artist_name = artist['name']
                artist_URI, song_URI, new_song_name = self.search_artist(artist_name, song_name)
                if artist_URI is None and song_URI is None:
                    artist_uri_list.append("No:URI:found")
                    track_uri_list.append("No:URI:found")
                elif artist_URI == "No response" and song_URI == "No response":
                    artist_uri_list.append("No response")
                    track_uri_list.append("No response")
                else:
                    artist_uri_list.append(artist_URI)
                    track_uri_list.append(song_URI)
                    self.current_song_name = new_song_name
                    song_name = new_song_name
                
            song_names.append(new_song_name)
                
            artist_URI_list.append(artist_uri_list)
            track_URI_list_combined.append(track_uri_list)
            self.processed_tracks += 1

        for i in range(len(track_URI_list)):
            if len(track_URI_list[i]) > 1:
                for j in range(1, len(track_URI_list[i])):
                    if track_URI_list[i][j] == "":
                        track_URI_list[i].pop(j)

            track_URI_list_combined.append(track_URI_list)

        return data, track_URI_list_combined, artist_URI_list, song_names

