import requests

def get_track_and_artist_uris(song_title, artist_name):
    # Genius API endpoint for searching songs
    url = "https://api.genius.com/search"
    
    # Set up the request headers with your Genius API token
    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN"
    }
    
    # Set up the request parameters
    params = {
        "q": song_title + " " + artist_name
    }
    
    # Send the request to the Genius API
    response = requests.get(url, params=params, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Get the JSON data from the response
        data = response.json()
        
        # Check if there are any search results
        if "hits" in data and data["hits"]:
            # Get the first search result
            first_hit = data["hits"][0]["result"]
            
            # Get the track URI
            track_uri = first_hit["url"]
            
            # Get the artist URI
            primary_artist = first_hit["primary_artist"]
            artist_uri = primary_artist["url"]
            
            return track_uri, artist_uri
        else:
            print("No search results found.")
    else:
        print("Error:", response.status_code)

# Example usage
song_title = "Bohemian Rhapsody"
artist_name = "Queen"

track_uri, artist_uri = get_track_and_artist_uris(song_title, artist_name)
if track_uri and artist_uri:
    print("Track URI:", track_uri)
    print("Artist URI:", artist_uri)
