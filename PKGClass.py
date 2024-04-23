import requests
import json
import csv
import urllib.parse
from datetime import datetime
import imdb
from rfc3987 import match

API_URL = "https://rel.cs.ru.nl/api"

class PKGFunctions:
    """
    Class that contains functions for the PKG.
    """
    def __init__(self):
        pass

    def get_actor_imdb_id(self,actor_name):
        ia = imdb.IMDb()

        search_results = ia.search_person(actor_name)

        if search_results:
            actor = search_results[0]
            actor_id = actor.getID()
            return actor_id
        else:
            return None
    
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
            new_dates = []
            
            if len(dates) >= 2:
                dates.sort()
                i = 0
                k = i + 1
                
                while k <= len(dates):
                    print(f"checking {title} dates: {dates[i].date()} and {dates[k].date()}")
                    print(title)
                    if (dates[k].date() - dates[i].date()).days < 7 and dates[k].date().month == dates[i].date().month and dates[k].date().year == dates[i].date().year:
                        k += 1
                        if k == len(dates):
                            new_dates.append(dates[i])
                            break
                    else:
                        new_dates.append(dates[i])
                        i = k
                        k += 1
                        if k == len(dates):
                            new_dates.append(dates[k-1])
                            break
                        
            
            movies[title] = new_dates
            if len(movies[title]) >= 2: 
                liked_movies.append((title, movies[title]))

        print("liked movies",liked_movies)

        return hooks, liked_movies
    
    def read_json_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data
    
    def search_artist(self, artist_name, song_name):
        url = 'https://musicbrainz.org/ws/2/recording'
        print(f'"{artist_name}""{song_name}"')
        params = {
            'query': f'"{artist_name}""{song_name}"',
            'fmt': 'json'  # Response format
        }
        response = requests.get(url, params=params)
        data = response.json()
        if data['recordings'] is not None:
            for record in data['recordings']:
                if artist_name == record['artist-credit'][0]['artist']['name']:
                    artist_template = f"https://musicbrainz.org/artist/{record['artist-credit'][0]['artist']['id']}"
                    artist_uri = URI(artist_template.format(entity_name=artist_name))
                    song_template = f"https://musicbrainz.org/recording/{record['id']}"
                    song_uri = URI(song_template.format(entity_name=song_name))
                    return artist_uri, song_uri
                else:
                    return None, None
        else:
            return None, None
    
    def search_OMDb(self, query, type):
        url = 'http://www.omdbapi.com/'
        params = {
            'apikey': 'e3499921',
            't': query,
            'type': type
        }
        response = requests.get(url, params=params)
        data = response.json()
        if data.get('Response') == 'False':
            response = data.get('Response')
            info = {
                'Response': response
            }
            return info
        elif data.get('Response') == 'True': 
            movie = data.get('Title')
            actors = data.get('Actors')
            actor_list = actors.split(',')
            imdbID = data.get('imdbID')
            response = data.get('Response')
            info = {
                'Movie': movie,
                'Actors': actor_list,
                'ImdbID': imdbID,
                'Response': response
            }
            return info

    
    def get_REL_api_response(self, example_string):
        """
        Sends a request to the REL API and returns the response.
        """
        response = requests.get(API_URL)
        
        if response.status_code == 200:
            response = requests.post(
                API_URL, json={"text": example_string, "spans": []}
            )
            return response.json()
        else:
            return {"error": response.status_code}
        
    def link_entities(self, reference):
        """
        Creates URI links for entities, depending on the type of entity.
        """
        movie_actor_dict = {}  # Dictionary to store movie-actor associations
        for key, _  in reference.items():
            if key[:2] == 'tt':
                platform = "Netflix"
                break
        if platform == "Netflix":
            for key, value in reference.items():
                print(key, value)
                actors = []
                if key.startswith("tt"):
                    movie_ID = key
                    template = f"https://www.imdb.com/title/{movie_ID}/"
                    movie_uri = URI(template.format(entity_name=movie_ID))
                if 'Actors' in value:
                    for actor_name in value.get('Actors'):
                        actor_URI = self.get_actor_imdb_id(actor_name)
                        actors.append(URI(f"https://www.imdb.com/name/nm{actor_URI}/"))
                    movie_actor_dict[movie_uri] = {
                        'actor_uris': actors
                    }
        return movie_actor_dict      
       
    
    def process_entity_linking_response(self, NER_response, input_text):
        """
        Translates the input text into a tagged test based on the NER response.
        """
        print(NER_response)
        print(input_text)
        
        entity_dict = {}
        for entity in NER_response:
            start_index, end_index = entity[:2]
            entity_dict[(start_index, end_index)] = (entity[2], entity[3], entity[6])
        string_index = 0
        output_array = []
        count = 0
        
        for item in entity_dict.items():
            start = item[0][0]
            end = item[0][1] + start
            entity = input_text[start:end]
            output_array.append(input_text[string_index:start])
            
            if entity:
                text = f"<{item[1][2]}> {entity} </{item[1][2]}>"
                output_array.append(text)
                count += 1         
            string_index = end
            if count == len(entity_dict):
                output_array.append(input_text[string_index:]) 

        output_text = ''.join(output_array)
        return(output_text)
    





SPARQLQuery = str
class URI(str):
    def __new__(cls, *args, **kwargs):
        """Creates a new URI."""
        assert match(args[0], rule="IRI"), f"Invalid URI: {args[0]}"
        return super().__new__(cls, *args, **kwargs)
        