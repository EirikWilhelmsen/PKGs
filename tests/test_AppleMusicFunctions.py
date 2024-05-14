import unittest
import sys
sys.path.append('..')
from AppleMusic import AppleMusicFunctions

class TestAppleMusicClass(unittest.TestCase):
    def setUp(self):
        self.applemusic = AppleMusicFunctions()
    
    def test_negative_handle_artists(self):
        # Arrange
        query = "fkfbklar"
        # Act
        result = self.applemusic.handle_artists(query)
        
        # Assert
        self.assertEqual(result, [])
    
    def test_positive_handle_artists(self):
        # Arrange
        query = "Alan Walker"
        # Act
        result = self.applemusic.handle_artists(query)
        
        # Assert
        self.assertEqual(result, ['Alan Walker'])
    
    # def test_tricky_handle_artists(self):
    #     # Arrange
    #     query = "Dance 'n Sweet"
    #     # Act
    #     result = self.applemusic.handle_artists(query)
    #     
    #     # Assert
    #     self.assertEqual(result, ['Dance ’n Sweet'])
    
    def test_search_musicbrainz(self):
        # Arrange
        artist = ['Travis Scott']
        song = ["Butterfly Effect"]

        # Act
        main_artist_names, entity_links_musicbrainz_artists, entity_links_musicbrainz_tracks, Cleaned_Songs, Queries, artist_queries = self.applemusic.search_track_musicbrainz(song, artist)
        
        # Assert
        self.assertEqual(entity_links_musicbrainz_artists, ['https://musicbrainz.org/artist/e4a51f17-a57b-47b1-b37b-f552d0f8e9e6'])
        self.assertEqual(entity_links_musicbrainz_tracks, ['https://musicbrainz.org/recording/303107f3-8bf0-4850-a0db-6b906954475f'])
    
    def test_search_norwegian_musicbrainz(self):
        # Arrange
        artist = ['Amara']
        song = ["Holmenkollen Hills"] 

        # Act
        main_artist_names, entity_links_musicbrainz_artists, entity_links_musicbrainz_tracks, Cleaned_Songs, Queries, artist_queries = self.applemusic.search_track_musicbrainz(song, artist)
        
        # Assert
        self.assertEqual(entity_links_musicbrainz_artists, ['https://musicbrainz.org/artist/e4a51f17-a57b-47b1-b37b-f552d0f8e9e6'])
        self.assertEqual(entity_links_musicbrainz_tracks, ['https://musicbrainz.org/recording/303107f3-8bf0-4850-a0db-6b906954475f'])
    
    
if __name__ == '__main__':
    unittest.main()