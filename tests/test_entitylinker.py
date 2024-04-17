import unittest
import sys
sys.path.insert(0, '/Users/eirikwilhelmsen/Documents/Semester6/PKGs')
from PKGClass import PKGFunctions

pkg_functions = PKGFunctions()

class TestEntityLinker(unittest.TestCase):

    def test_get_actor_imdb_id(self):
        test_actor_name = "Tom Hanks"
        test_actor_imdb_id = pkg_functions.get_actor_imdb_id(test_actor_name)

        assert test_actor_imdb_id == "0000158"
    
    def test_search_OMDb_true(self):
        test_movie_name = "The Matrix"
        test_movie_data = pkg_functions.search_OMDb(test_movie_name, 'movie')
        
        assert test_movie_data['Movie'] == "The Matrix"
        assert [test_actor.strip() for test_actor in test_movie_data['Actors']] == ['Keanu Reeves', 'Laurence Fishburne', 'Carrie-Anne Moss']
        assert test_movie_data['ImdbID'] == "tt0133093"
        assert test_movie_data['Response'] == "True"
    
    def test_search_OMDb_false(self):
        test_movie_name = "The Matriks"
        test_movie_data = pkg_functions.search_OMDb(test_movie_name, 'movie')
        
        assert test_movie_data['Response'] == "False"

    def test_link_entities_movie(self):
        test_reference = {
            'tt0322259': {
                'Actors': ['Paul Walker', ' Tyrese Gibson', ' Cole Hauser']
            }
        }
        test_linked_entities = pkg_functions.link_entities(test_reference)
        for movie_url, movie_info in test_linked_entities.items():
            assert movie_url == 'https://www.imdb.com/title/tt0322259/'
            assert [test_actor_uri.strip() for test_actor_uri in movie_info['actor_uris']] == ['https://www.imdb.com/name/nm0908094/', 'https://www.imdb.com/name/nm0879085/', 'https://www.imdb.com/name/nm0369513/']



if __name__ == '__main__':
    unittest.main()