import unittest
import sys
import pandas as pd
sys.path.append('..')
from AppleMusic import AppleMusicFunctions

class TestAppleMusicClass(unittest.TestCase):
    def setUp(self):
        self.applemusic = AppleMusicFunctions()


    def test_find_artists(self):
        query="Eminem, Candice Pillay & Anderson .Paak"
        result = self.applemusic.handle_artists(query)
        
        # Assert
        self.assertEqual(result, ["Eminem", "Candice Pillay", "Anderson .Paak"])
    
    def test_double_dash(self):
        df= {
        'Country': ['Norway'],
        'Track Identifier': [1210094305],
        'Media type': ['AUDIO'],
        'Date Played': ['20170419'],
        'Hours': ['12'],
        'Play Duration Milliseconds': [255555],
        'Source Type': ['IPHONE'],
        'Play Count': [3],
        'Skip Count': [1],
        'Ignore For Recommendations': [None],
        'Track Reference': [1.210094e+09],
        'Track Description': ['Coldplay - Viva la Vida - Live Version']  # Two dashes
        }

        df=pd.DataFrame(df)

        result = self.applemusic.liked_songs(df)
        # Assert
        self.assertEqual(result, ([], [], []))
        
    def test_no_dash(self):
        df= {
        'Country': ['Norway'],
        'Track Identifier': [1210094305],
        'Media type': ['AUDIO'],
        'Date Played': ['20170419'],
        'Hours': ['12'],
        'Play Duration Milliseconds': [255555],
        'Source Type': ['IPHONE'],
        'Play Count': [3],
        'Skip Count': [1],
        'Ignore For Recommendations': [None],
        'Track Reference': [1.210094e+09],
        'Track Description': ['Symphony by Clean Bandit']  # No dashes
        }
        df=pd.DataFrame(df)

        result = self.applemusic.liked_songs(df)
        # Assert
        self.assertEqual(result, ([], [], []))
    
    
    def test_negative_handle_artists(self):
        # Arrange
        query = "fkfbklar"
        # Act
        result = self.applemusic.artist_check_musicbrainz(query)
        
        # Assert
        self.assertEqual(result, None)
    
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
        song = ["BUTTERFLY EFFECT"]

        # Act
        main_artist_names, entity_links_musicbrainz_artists, entity_links_musicbrainz_tracks, Cleaned_Songs, Queries, artist_queries = self.applemusic.search_track_musicbrainz(song, artist)
        
        # Assert
        self.assertEqual(entity_links_musicbrainz_artists, ['https://musicbrainz.org/artist/e4a51f17-a57b-47b1-b37b-f552d0f8e9e6'])
        self.assertEqual(entity_links_musicbrainz_tracks, ['https://musicbrainz.org/recording/d467d9f6-f59d-463b-b3ce-37143ca1d291'])
    
    def test_search_norwegian_musicbrainz(self):
        # Arrange
        artist = ['Amara']
        song = ["Holmenkollen Hills"] 

        # Act
        main_artist_names, entity_links_musicbrainz_artists, entity_links_musicbrainz_tracks, Cleaned_Songs, Queries, artist_queries = self.applemusic.search_track_musicbrainz(song, artist)
        
        # Assert
        self.assertEqual(entity_links_musicbrainz_artists, ['https://musicbrainz.org/artist/62051d1b-50e6-43ce-bf51-6ed96b00e9fc'])
        self.assertEqual(entity_links_musicbrainz_tracks, ['https://musicbrainz.org/recording/2af8236b-2c05-488e-9ee5-691d747e45c6'])
    
    
if __name__ == '__main__':
    unittest.main()