import unittest
import sys
sys.path.append('..')
from SpotifyClass import SpotifyFunctions


class TestSpotifyClass(unittest.TestCase):
    def setUp(self):
        self.spotify= SpotifyFunctions()
    
    def test_search_artist_negative(self):
        # Arrange
        artist_name = "hfeklfbemeewfe"
        song_name = "hfeklfbemeewfe"
        
        # Act
        result = self.spotify.search_artist(artist_name, song_name)
        
        # Assert
        self.assertEqual(result, ('No response', 'No response', 'No response'))

    def test_search_artist_positive(self):
        # Arrange
        artist_name = "Amara"
        song_name = "Holmenkollen Hills"
        
        # Act
        result = self.spotify.search_artist(artist_name, song_name)
        
        # Assert
        self.assertEqual(result, ('https://musicbrainz.org/artist/62051d1b-50e6-43ce-bf51-6ed96b00e9fc','https://musicbrainz.org/recording/2af8236b-2c05-488e-9ee5-691d747e45c6', 'Holmenkollen Hills'))

    def test_search_song_with_apostrophe_positive(self):
        # Arrange
        artist_name = "Travis Scott"
        song_name = "CAN'T SAY"

        # Deliberately misspelled the song name apostrophe to test the function's ability to correct it
        
        # Act
        result = self.spotify.search_artist(artist_name, song_name)
        
        # Assert
        self.assertEqual(result, ('https://musicbrainz.org/artist/e4a51f17-a57b-47b1-b37b-f552d0f8e9e6','https://musicbrainz.org/recording/bfde919d-541d-4003-8cbf-03e36832f1bc', 'CAN’T SAY'))
    def test_search_song_with_feature_positive(self):
        artists = ["Travis Scott", "Kacy Hill"]
        song_name = "90210 (feat. Kacy Hill)"
        song_name = self.spotify.remove_feat_part(song_name)
        output = [('https://musicbrainz.org/artist/e4a51f17-a57b-47b1-b37b-f552d0f8e9e6','https://musicbrainz.org/recording/92155ba2-b134-4f38-b964-1d80eb1bd75e', '90210'), 
                  ('https://musicbrainz.org/artist/f33e8fd2-8536-42e8-9169-fae50f850dd9','https://musicbrainz.org/recording/92155ba2-b134-4f38-b964-1d80eb1bd75e', '90210')]
        for artist_name in artists:
            result = self.spotify.search_artist(artist_name, song_name)
            index = artists.index(artist_name)  # Get index of artist name
            expected_output = output[index]  # Get corresponding expected output
            self.assertEqual(result, expected_output)
            if artist_name == artists[0]:  # Check if it's the first iteration
                print(expected_output) 


if __name__ == '__main__':
    unittest.main()