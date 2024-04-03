import requests
import json
import csv
import urllib.parse
from datetime import datetime

API_URL = "https://rel.cs.ru.nl/api"

class PKGFunctions:
    def __init__(self):
        pass
    
    def read_csv_file(self, file_path):
        print(file_path)
        hooks = []
        movies = {}
        liked_movies = []

        with open(file_path, 'r', newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  # Skip the header

            for row_index, row in enumerate(csvreader):
                title = row[4]
                date = row[1]
                video_type = row[5]
                if video_type.lower() in ['trailer', 'teaser_trailer', 'recap']:
                    continue  
                elif video_type.lower() == 'hook':
                    hooks.append((title, date))
                else:
                    if title.count(":") < 2:  # movie
                        date_obj = datetime.strptime(date.split()[0], '%Y-%m-%d')  # Extracting date 
                        if title not in movies:
                            movies[title] = [date_obj]
                        else:
                            movies[title].append(date_obj)

        for title, dates in movies.items():
            if len(dates) >= 2:
                dates.sort()
                if (dates[-1].date() - dates[0].date()).days < 7 and dates[-1].date().month == dates[0].date().month:
                    movies[title] = [dates[-1]]
                else:
                    liked_movies.append((title, movies[title]))

        return hooks, liked_movies
    
    def read_json_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data
    
    def search_artist(self, artist_name):
        url = 'https://musicbrainz.org/ws/2/artist'
        params = {
            'query': artist_name,
            'fmt': 'json'  # Response format
        }
        response = requests.get(url, params=params)
        data = response.json()
        if data['artists']:
            return data['artists'][0]
        else:
            return None
    
    def search_OMDb(self, query, type):
        url = 'http://www.omdbapi.com/'
        params = {
            'apikey': 'e3499921',
            't': query,
            'type': type
        }
        response = requests.get(url, params=params)
        data = response.json()
        return data
    
    def get_api_response(self):
        # Make a GET request to the API endpoint
        response = requests.get(API_URL)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Print the response content
            response = requests.post(
                API_URL, json={"text": "I dislike all movie with Tom Cruise", "spans": []}
            )
            return response.json()
        else:
            return {"error": response.status_code}
