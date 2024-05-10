import unittest
import sys
sys.path.append('..')
from NetflixClass import NetflixFunctions


class TestNetflixClass(unittest.TestCase):
    def setUp(self):
        self.netflix = NetflixFunctions()
    
    def test_search_OMDb_positive(self):
        # Arrange
        query = "10½"
        actors = []
        # Act
        result = self.netflix.search_OMDb(query, 'movie')
        for actor in result['Actors']:
            actors.append(actor)
        
        # Assert
        self.assertIsInstance(result, dict)
        self.assertEqual(result['Movie'], '10½')
        self.assertEqual(result['Actors'], ['Claude Legault', ' Robert Naylor', ' Eugénie Beaudry']) #["nm0499218","nm2316151","nm1799076"]
        self.assertEqual(result['ImdbID'], "tt1591622")
        self.assertEqual(result['Response'], 'True')
    
    def test_get_actor_imdb_id_positive(self):
        # Arrange
        actors_id = []
        actors = []
        query = "10½"
        
        # Act
        result = self.netflix.search_OMDb(query, 'movie')
        for actor in result['Actors']:
            actors.append(actor)
        for actor in actors:
            actors_id.append(self.netflix.get_actor_imdb_id(actor))
        
        # Assert
        self.assertIsInstance(actors_id, list)
        self.assertEqual(actors_id, ["0499218","2316151","1799076"])
    
    def test_search_OMDb_negative(self):
        # Arrange
        query = "ghj"
        
        # Act
        result = self.netflix.search_OMDb(query, 'movie')
        
        # Assert
        self.assertIsInstance(result, dict)
        self.assertEqual(result['Response'], 'False')
    
    def test_search_norwegian_title(self):
        # Arrange
        query = "Lego filmen"
        
        # Act
        result = self.netflix.search_OMDb(query, 'movie')
        
        # Assert
        self.assertIsInstance(result, dict)
        self.assertEqual(result['Response'], 'False')

if __name__ == '__main__':
    unittest.main()