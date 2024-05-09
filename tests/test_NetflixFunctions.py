import unittest
import sys
sys.path.append('..')
from NetflixClass import NetflixFunctions


class TestNetflixClass(unittest.TestCase):
    def setUp(self):
        self.netflix = NetflixFunctions()
    
    def test_search_OMDb_positive(self):
        # Arrange
        query = "The Godfather"
        
        # Act
        result = self.netflix.search_OMDb(query, 'movie')
        
        # Assert
        self.assertIsInstance(result, dict)
        self.assertEqual(result['Movie'], 'The Godfather')
        self.assertIsInstance(result['Actors'], list)
        self.assertIsInstance(result['ImdbID'], str)
        self.assertEqual(result['Response'], 'True')
    
    def test_search_OMDb_negative(self):
        # Arrange
        query = "Invalid Movie"
        
        # Act
        result = self.netflix.search_OMDb(query, 'movie')
        
        # Assert
        self.assertIsInstance(result, dict)
        self.assertEqual(result['Response'], 'False')

if __name__ == '__main__':
    unittest.main()