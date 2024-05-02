import uuid
import requests
import sys
sys.path.append('..')


url = "http://127.0.0.1:5000/statements"


class statements:
    def __init__(self):
        pass
    def create_spotify_statement(self, top_tracks_short, track_URI_list, artist_URI_list):
        test_data_list = []
        i = 0
        for track in top_tracks_short:
            if len(track['artists']) == 3:
                subject = "http://example.com/test"
                predicate = {"value": {"description": "like"}}
                object = {"value": {"description": f"the song {track['name']} by {track['artists'][0]['name']}, {track['artists'][1]['name']}, and {track['artists'][2]['name']}",
                                    "related_entities": ["https://schema.org/artist", f"{artist_URI_list[i][0]}",
                                                        "https://schema.org/artist", f"{artist_URI_list[i][1]}",
                                                        "https://schema.org/artist", f"{artist_URI_list[i][2]}",
                                                        "https://schema.org/song", f"{track_URI_list[i]}"]}}
                data = {
                        "owner_uri": "http://example.com/test",
                        "owner_username": "test",
                        "description": f"I like the song {track['name']} by {track['artists'][0]['name']}, {track['artists'][1]['name']}, and {track['artists'][2]['name']}",
                        "subject": subject,
                        "predicate": predicate,
                        "object": object,
                        "preference": 1.0
                }
                response = requests.post(url, json=data)
                assert response.status_code == 200
                
                test_sample = {
                    "subject": subject,
                    "predicate": predicate,
                    "object": object
                }
                test_data_list.append(test_sample)

                i += 1
            elif len(track['artists']) == 2:
                subject = "http://example.com/test"
                predicate = {"value": {"description": "like"}}
                object = {"value": {"description": f"the song {track['name']} by {track['artists'][0]['name']}, and {track['artists'][1]['name']}",
                                    "related_entities": ["https://schema.org/artist", f"{artist_URI_list[i][0]}",
                                                        "https://schema.org/artist", f"{artist_URI_list[i][1]}",
                                                        "https://schema.org/song", f"{track_URI_list[i]}"]}}

                data = {
                        "owner_uri": "http://example.com/test",
                        "owner_username": "test",
                        "description": f"I like the song {track['name']} by {track['artists'][0]['name']}, and {track['artists'][1]['name']}",
                        "subject": subject,
                        "predicate": predicate,
                        "object": object,
                        "preference": 1.0
                }
                response = requests.post(url, json=data)
                assert response.status_code == 200

                test_sample = {
                    "subject": subject,
                    "predicate": predicate,
                    "object": object
                }
                test_data_list.append(test_sample)
                i += 1
            else:
                subject = "http://example.com/test"
                predicate = {"value": {"description": "like"}}
                object = {"value": {"description": f"the song {track['name']} by {track['artists'][0]['name']}",
                                    "related_entities": ["https://schema.org/artist", f"{artist_URI_list[i][0]}",
                                                        "https://schema.org/song", f"{track_URI_list[i]}"]}}

                data = {
                    "owner_uri": "http://example.com/test",
                    "owner_username": "test",
                    "description": f"I like the song {track['name']} by {track['artists'][0]['name']}",
                    "subject": subject,
                    "predicate": predicate,
                    "object": object,
                    "preference": 1.0
                }
                response = requests.post(url, json=data)
                assert response.status_code == 200

                test_sample = {
                    "subject": subject,
                    "predicate": predicate,
                    "object": object
                }
                test_data_list.append(test_sample)
                i += 1
        return test_data_list
    def create_netflix_statement(self, combined_data):
        test_data_list = []
        print(len(combined_data))
        for movie_info in combined_data:
                subject = "http://example.com/test"
                predicate = {"value": {"description": "like"}}
                object = {"value": {"description": f"the movie {movie_info[2][1]} starring {','.join(movie_info[0][1]['Actors'])}",
                                    "related_entities": ["https://schema.org/actor", f"{movie_info[1][1]['actor_uris'][0]}",
                                                        "https://schema.org/actor", f"{movie_info[1][1]['actor_uris'][1]}",
                                                        "https://schema.org/actor", f"{movie_info[1][1]['actor_uris'][2]}",
                                                        "https://schema.org/Movie", f"{movie_info[1][0]}"]}}

                data = {
                    "owner_uri": "http://example.com/test",
                    "owner_username": "test",
                    "description": f"I like the movie {movie_info[2][1]} starring {', '.join(movie_info[0][1]['Actors'])}",
                    "subject": subject,   # Single string when using URI
                    "predicate": predicate,    # Use dictionary when the field is a concept
                    "object": object,
                    "preference": 1.0
                }

                #response = requests.post(url, json=data)
                #assert response.status_code == 200 

                test_sample = {
                    "subject": subject,
                    "predicate": predicate,
                    "object": object['value']['related_entities'] 
                }
                test_data_list.append(test_sample)
                
        return test_data_list
