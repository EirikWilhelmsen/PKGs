import json
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
            print(track['name'], "by", track['artists'][0]['name'])
            if len(track['artists']) == 3:
                subject = "http://example.com/test"
                predicate = {"value": {"description": "like"}}
                object = {"value": {"description": f"the song {track['name']} by {track['artists'][0]['name']}, {track['artists'][1]['name']}, and {track['artists'][2]['name']}",
                                    "related_entities": ["https://schema.org/artist", f"{artist_URI_list[i][0]}",
                                                        "https://schema.org/artist", f"{artist_URI_list[i][1]}",
                                                        "https://schema.org/artist", f"{artist_URI_list[i][2]}",
                                                        "https://schema.org/song", f"{track_URI_list[i][0]}"]}}
            elif len(track['artists']) == 2:
                subject = "http://example.com/test"
                predicate = {"value": {"description": "like"}}
                object = {"value": {"description": f"the song {track['name']} by {track['artists'][0]['name']}, and {track['artists'][1]['name']}",
                                    "related_entities": ["https://schema.org/artist", f"{artist_URI_list[i][0]}",
                                                        "https://schema.org/artist", f"{artist_URI_list[i][1]}",
                                                        "https://schema.org/song", f"{track_URI_list[i][0]}"]}}
            else:
                subject = "http://example.com/test"
                predicate = {"value": {"description": "like"}}
                object = {"value": {"description": f"the song {track['name']} by {track['artists'][0]['name']}",
                                    "related_entities": ["https://schema.org/artist", f"{artist_URI_list[i][0]}",
                                                        "https://schema.org/song", f"{track_URI_list[i][0]}"]}}
            data = {
                    "owner_uri": "http://example.com/test",
                    "owner_username": "test",
                    "description": f"I like the song {track['name']} by {track['artists'][0]['name']}",
                    "subject": subject,
                    "predicate": predicate,
                    "object": object,
                    "preference": 1.0
            }
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
                    "object": object 
                }
                test_data_list.append(test_sample)

        return test_data_list


    def create_apple_music_like_statement(Year, main_artist_names, entity_links_musicbrainz_artists, entity_links_musicbrainz_tracks, Cleaned_Songs):
        #To increase the number of correct statements, only the main artist and song is entity linked. This way it's avoided that individual, less known, feature artists ruin the data by creating a false positive. 
        i=0
        data_list=[]
        print(entity_links_musicbrainz_artists)
        for year in Year:
            
            if entity_links_musicbrainz_artists[i] == "Artist not found":
                data_list.append("No data")
                i+=1
                print("####################### ####################################")
                print("No DATA")
            else:
                if Year[i]==None:
                    data={
                        "owner_uri": "http://example.com/test",
                            "owner_username": "test",
                            "description": f"I like the song {Cleaned_Songs[i]}",
                            "subject": "http://example.com/test",   # Single string when using URI
                            "predicate": {"value": {"description": "like"}},    # Use dictionary when the field is a concept
                            "object": {"value": {"description": f"the song {Cleaned_Songs[i]} by {main_artist_names[i]}", 
                                                "related_entities": ["https://schema.org/MusicGroup", f"{entity_links_musicbrainz_artists[i]}", 
                                                                    "https://schema.org/MusicRecording", f"{entity_links_musicbrainz_tracks[i]}"]}},
                            "preference": 1.0
                        }
                    i+=1
                    print("###################################################")
                    print(data)
                    data_list.append(data)
                else:
                    data={
                        "owner_uri": "http://example.com/test",
                            "owner_username": "test",
                            "description": f"I like the song {Cleaned_Songs[i]}",
                            "subject": "http://example.com/test",   # Single string when using URI
                            "predicate": {"value": {"description": "like"}},    # Use dictionary when the field is a concept
                            "object": {"value": {"description": f"the song {Cleaned_Songs[i]} by {main_artist_names[i]}", 
                                                "related_entities": ["https://schema.org/MusicGroup", f"{entity_links_musicbrainz_artists[i]}", 
                                                                    "https://schema.org/MusicRecording", f"{entity_links_musicbrainz_tracks[i]}"]},
                                                                    "additional_info": {"primary_listening_years": year}},
                            "preference": 1.0
                        }
                    print("#####################################")
                    print(data)
                    i+=1
                    data_list.append(data)
        return data_list

    def create_apple_music_dislike_statement(main_artist_names, entity_links_musicbrainz_artists, entity_links_musicbrainz_tracks, Cleaned_Songs):
        i=0
        data_list=[]
        for clean_song in Cleaned_Songs:
            if entity_links_musicbrainz_artists[i] == "Artist not found":
                data_list.append("No data")
                i+=1
            else:
                data={
                    "owner_uri": "http://example.com/test",
                        "owner_username": "test",
                        "description": f"I dislike the song {clean_song}",
                        "subject": "http://example.com/test",   # Single string when using URI
                        "predicate": {"value": {"description": "dislike"}},    # Use dictionary when the field is a concept
                        "object": {"value": {"description": f"the song {clean_song} by {main_artist_names[i]}", 
                                            "related_entities": ["https://schema.org/MusicGroup", f"{entity_links_musicbrainz_artists[i]}", 
                                                                "https://schema.org/MusicRecording", f"{entity_links_musicbrainz_tracks[i]}"]}},
                        "preference": -1.0
                    }
                data_list.append(data)
                i+=1
        return data_list

