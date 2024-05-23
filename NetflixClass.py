import requests
import csv
from datetime import datetime
import json
import imdb
from PKGClass import URI
import os

class NetflixFunctions:
    def __init__(self):
        self.load_actors_id()
        self.total_movies = 0
        self.processed_movies = 0
        self.load_movies()
        pass
    
    def load_actors_id(self):
        """loads actor names and their IMDb IDs from cache file into self.actors"""
        
        try:
            with open(os.path.join(os.path.dirname(__file__), "data/cache_files/actors.json"), 'r', encoding='utf-8') as file:
                self.actors = json.load(file)
        except FileNotFoundError:
            self.actors = []

    
    def load_movies(self):
        """loads movie titles and their IMDb IDs from cache file into self.movies"""

        try:
            with open(os.path.join(os.path.dirname(__file__), "data/cache_files/movies.json"), 'r', encoding='utf-8') as file:
                self.movies = json.load(file)
        except FileNotFoundError:
            self.movies = []

    
    def save_actors_id(self):
        """saves actor names and their IMDb IDs to cache file"""
        
        with open(os.path.join(os.path.dirname(__file__), "data/cache_files/actors.json"), 'w', encoding='utf-8') as file:
            json.dump(self.actors, file)

    
    def save_movies(self):
        """saves movie titles and their IMDb IDs to cache file"""

        with open(os.path.join(os.path.dirname(__file__), "data/cache_files/movies.json"), 'w', encoding='utf-8') as file:
            json.dump(self.movies, file)

    
    def find_movie_id_and_actors(self, liked_movies):
        """assigns IMDb IDs to movies and actors anc creates a dict for each
        
        Keyword arguments:
        liked_movies -- list of movies watched more than two times, which we want to assing IMDb IDs to
        Return: 
        movie_actor_uris -- dictionary with movie URI as key and actor URIs as values
        movie_titles -- dictionary with movie titles as keys and IMDb movie titles as values
        movie_actor_list -- dictionary with IMDb IDs as keys and actors as values
        """
        
        movies_info = []
        movie_titles = {}
        movie_actor_list = {}
        i = 0
        self.total_movies = len(liked_movies)
        for movie_title, _ in liked_movies:
            print(movie_title)
            movie_info = self.search_OMDb(movie_title, 'movie')
            if movie_info['Response'] == 'True':
                movies_info.append(movie_info)
                movie_titles[movie_title] = movie_info['Movie']
                movie_actor_list[movie_info['ImdbID']] = {
                    'Actors': movie_info['Actors']
                }
            i += 1
        movie_actor_uris = self.link_entities(movie_actor_list)
        return movie_actor_uris, movie_titles, movie_actor_list

    def get_actor_imdb_id(self,actor_name):
        """searches imdbPY module for actor IMDb ID
        
        Keyword arguments:
        actor_name -- name of the actor
        Return: 
        actor_id -- IMDb ID of the actor
        """
            
        for actor in self.actors:
            if actor["name"] == actor_name:
                return actor["id"]
                
        ia = imdb.IMDb()
        search_results = ia.search_person(actor_name)
        if search_results:
            actor_imdb_id = search_results[0].personID
            self.actors.append({"name": actor_name, "id": actor_imdb_id})
            self.save_actors_id()
            return actor_imdb_id
        else:
            print("none") 
            return None
    
    def read_csv_file(self, file_path):
        """reads the provided CSV file and extracts hooks and movies watched more than two times in a duration of a week
        
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
        """searched OMDb API for movie information, primarily for IMDb ID and actors
        
        Keyword arguments:
        query -- movie title
        type -- type (movie or series)
        Return: 
        info -- dictionary with additional OMDb movie information
        """
        
        for movie in self.movies:
            if movie['Movie'] == query:
                return movie
        
        print(f"søker {query}")
        
        url = 'http://www.omdbapi.com/'
        params = {
            'apikey': 'e3499921',
            't': query,
            'type': type
        }
        response = requests.get(url, params=params)
        data = response.json()
        if data.get('Response') == 'False':
            print("fant ikke film")
            response = data.get('Response')
            info = {
                'Response': response
            }
            return info
        elif data.get('Response') == 'True':
            movie = data.get('Title')
            print("fant film", movie)
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
            self.movies.append(info)
            self.save_movies()
            return info
        else:
            print("fikk ikke respons")
            return None
        
    def link_entities(self, reference):
        """creates URI for movies and actors
        
        Keyword arguments:
        reference -- dictionary with movie-actor associations
        Return: movie_actor_dict -- dictionary with movie URI as key and actor URIs as values
        """
        self.total_movies = len(reference)
        self.processed_movies = 0
        
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
                        print("returnerte", actor_URI)
                        actors.append(URI(f"https://www.imdb.com/name/nm{actor_URI}/"))
                    movie_actor_dict[movie_uri] = {
                        'actor_uris': actors
                    }
                self.processed_movies += 1
        return movie_actor_dict