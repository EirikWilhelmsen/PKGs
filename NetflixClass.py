import requests
import csv
from datetime import datetime
import imdb
from rfc3987 import match
from PKGClass import URI
import os

class NetflixFunctions:
    def __init__(self):
        self.actors = []
        pass
    def get_actor_imdb_id(self,actor_name):
        """sumary_line
        
        Keyword arguments:
        actor_name -- name of the actor
        Return: 
        actor_id -- IMDb ID of the actor
        """
        ia = imdb.IMDb()
            
        for actor in self.actors:
            if actor["name"] == actor_name:
                return actor["id"]
                
        search_results = ia.search_person(actor_name)
        if search_results:
            actor_imdb_id = search_results[0].personID
            self.actors.append({"name": actor_name, "id": actor_imdb_id})
            return actor_imdb_id
        else:
            print("none") 
            return None
    
    def read_csv_file(self, file_path):
        """sumary_line
        
        Keyword arguments:
        file_path -- path to the file
        Return: 
        hooks -- list of hooks
        liked_movies -- list of movies watched more than two times 
        """
        
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
    
    def search_OMDb(self, query, type):
        """sumary_line
        
        Keyword arguments:
        query -- movie title
        type -- type (movie or series)
        Return: 
        info -- dictionary with additional OMDb movie information
        """
        
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
        
    def link_entities(self, reference):
        """sumary_line
        
        Keyword arguments:
        reference -- dictionary with movie-actor associations
        Return: movie_actor_dict -- dictionary with movie URI as key and actor URIs as values
        """
        
        movie_actor_dict = {}  
        for key, _  in reference.items():
            if key[:2] == 'tt':
                platform = "Netflix"
                break
        if platform == "Netflix":
            for key, value in reference.items():
                actors = []
                if key.startswith("tt"):
                    movie_ID = key
                    template = f"https://www.imdb.com/title/{movie_ID}/"
                    movie_uri = URI(template.format(entity_name=movie_ID))
                if 'Actors' in value:
                    for actor_name in value.get('Actors'):
                        if actor_name.startswith(" "):
                            actor_name = actor_name[1:]
                        actor_URI = self.get_actor_imdb_id(actor_name)
                        actors.append(URI(f"https://www.imdb.com/name/nm{actor_URI}/"))
                    movie_actor_dict[movie_uri] = {
                        'actor_uris': actors
                    }
        return movie_actor_dict