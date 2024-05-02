"""Class for handling personal data from Spotify"""
import requests
import json
from datetime import datetime
from rfc3987 import match
from PKGClass import URI

class SpotifyFunctions:
    def __init__(self):
        self.temp_song=[]
        
    def read_json_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data
    
    def search_artist(self, artist_name, song_name):
        """sumary_line
        
        Keyword arguments:
        artist_name -- artist name
        song_name -- song name
        Return:
        artist_URI -- URI of the artist
        song_URI -- URI of the song
        """
        
        url = 'https://musicbrainz.org/ws/2/recording'
        params = {
            'query': f'"{artist_name}""{song_name}"',
            'fmt': 'json',  # Response format
            'limit': 8
        }
        response = requests.get(url, params=params)
        data = response.json()
        

        print(f"søker {artist_name} - {song_name}")
        

        if data.get('recordings'):
            for record in data['recordings']:
                print(record['artist-credit'][0]['artist']['name'], record['title'])
                if artist_name == record['artist-credit'][0]['artist']['name'] and song_name == record['title']:
                    artist_template = f"https://musicbrainz.org/artist/{record['artist-credit'][0]['artist']['id']}"
                    artist_uri = URI(artist_template.format(entity_name=artist_name))
                    song_template = f"https://musicbrainz.org/recording/{record['id']}"
                    song_uri = URI(song_template.format(entity_name=song_name))
                    print("fant", artist_uri, song_uri)
                    return artist_uri, song_uri
            print("fant ingenting")
        else:
            print("fikk ikke respons")
        return None, None
    
    def assign_URI(self, file_path):
        """sumary_line
        
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
        artist_URI_list_combined = []
        songs_checked = []
        track_URI_list = []
        artist_URI_list = []

        for track in data:
            artist_uri_list = [] 
            for artist in track["artists"]:
                artist_name = artist['name']
                song_name = track['name']
                artist_URI, song_URI = self.search_artist(artist_name, song_name)
                print("returned artist_URI", artist_URI, "returned song_URI", song_URI)
                if song_URI is not None and artist_URI is not None:
                    artist_uri_list.append(artist_URI)
                    if song_name in songs_checked and song_URI not in track_URI_list:
                        track_URI_list[-1] = song_URI
                    else:
                        track_URI_list.append(song_URI)
                else:
                    artist_uri_list.append("No:URI:found")
                    if song_name in songs_checked:
                        break
                    track_URI_list.append("No:URI:found")
                songs_checked.append(song_name)
            artist_URI_list.append(artist_uri_list)

        track_URI_list_combined.append(track_URI_list)
        artist_URI_list_combined.append(artist_URI_list)
        print("track_URI_list_combined", track_URI_list_combined, "\n")
        print("artist_URI_list_combined", artist_URI_list_combined)

        return data, track_URI_list_combined, artist_URI_list_combined

