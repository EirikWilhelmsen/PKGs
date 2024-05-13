import json
import uuid
import requests
import sys
sys.path.append('..')
import pprint

url = "http://127.0.0.1:5000/statements"


class statements:
    def __init__(self):
        pass
    def create_spotify_statement(self, top_tracks_short, track_URI_list, artist_URI_list, song_names):
        test_data_list = []
        i = 0
        for track in top_tracks_short:
            if len(track['artists']) == 3:
                subject = "http://example.com/test"
                predicate = {"value": {"description": "like"}}
                object = {"value": {"description": f"the song {song_names[i]} by {track['artists'][0]['name']}, {track['artists'][1]['name']}, and {track['artists'][2]['name']}",
                                    "related_entities": ["https://schema.org/artist", f"{artist_URI_list[i][0]}",
                                                        "https://schema.org/artist", f"{artist_URI_list[i][1]}",
                                                        "https://schema.org/artist", f"{artist_URI_list[i][2]}",
                                                        "https://schema.org/song", f"{track_URI_list[i][0]}"]}}
            elif len(track['artists']) == 2:
                subject = "http://example.com/test"
                predicate = {"value": {"description": "like"}}
                object = {"value": {"description": f"the song {song_names[i]} by {track['artists'][0]['name']}, and {track['artists'][1]['name']}",
                                    "related_entities": ["https://schema.org/artist", f"{artist_URI_list[i][0]}",
                                                        "https://schema.org/artist", f"{artist_URI_list[i][1]}",
                                                        "https://schema.org/song", f"{track_URI_list[i][0]}"]}}
            else:
                subject = "http://example.com/test"
                predicate = {"value": {"description": "like"}}
                object = {"value": {"description": f"the song {song_names[i]} by {track['artists'][0]['name']}",
                                    "related_entities": ["https://schema.org/artist", f"{artist_URI_list[i][0]}",
                                                        "https://schema.org/song", f"{track_URI_list[i][0]}"]}}
            data = {
                    "owner_uri": "http://example.com/test",
                    "owner_username": "test",
                    "description": f"I like the song {song_names[i]} by {track['artists'][0]['name']}",
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


                test_sample = {
                    "subject": subject,
                    "predicate": predicate,
                    "object": object 
                }
                test_data_list.append(test_sample)

        return test_data_list



    def create_apple_music_like_statement(Year, main_artist_names, entity_links_musicbrainz_artists, entity_links_musicbrainz_tracks, Cleaned_Songs, artist_queries):
        #To increase the number of correct statements, only the main artist and song is entity linked. This way it's avoided that individual, less known, feature artists ruin the data by creating false positives.  
        i=0
        data_list=[]
        # print(entity_links_musicbrainz_artists)
        for year in Year:
            
            if entity_links_musicbrainz_artists[i] == "Artist link not found" or entity_links_musicbrainz_artists[i] == "Artist not found":
                data_list.append("No data")
                
                if Year[i]==None:
                
                    data={
                            "owner_uri": "http://example.com/test",
                                "owner_username": "test",
                                "description": f"I like the song {Cleaned_Songs[i]} by {artist_queries[i]}",
                                "subject": "http://example.com/test",  
                                "predicate": {"value": {"description": "like"}},    
                                "object": {"value": {"description": f"the song {Cleaned_Songs[i]} by {artist_queries[i]}" 
                                }},
                                "preference": 1.0
                            }
                    data_list.append(data) 
                    i+=1
                else:

                    data={
                            "owner_uri": "http://example.com/test",
                                "owner_username": "test",
                                "description": f"I like the song {Cleaned_Songs[i]} by {artist_queries[i]}",
                                "subject": "http://example.com/test",  
                                "predicate": {"value": {"description": "like"}}, 
                                "object": {"value": {"description": f"the song {Cleaned_Songs[i]} by {artist_queries[i]}" 
                                }, "additional_info": {"primary_listening_years": year}},
                                "preference": 1.0
                            }
                    data_list.append(data)
                    i+=1
                
            else:
                if Year[i]==None:
                    data={
                        "owner_uri": "http://example.com/test",
                            "owner_username": "test",
                            "description": f"I like the song {Cleaned_Songs[i]} by {artist_queries[i]}",
                            "subject": "http://example.com/test",   
                            "predicate": {"value": {"description": "like"}},   
                            "object": {"value": {"description": f"the song {Cleaned_Songs[i]} by {artist_queries[i]}", 
                                                "related_entities": ["https://schema.org/MusicGroup", f"{entity_links_musicbrainz_artists[i]}", 
                                                                    "https://schema.org/MusicRecording", f"{entity_links_musicbrainz_tracks[i]}"]}},
                            "preference": 1.0
                        }
                    i+=1
                    

                    # pprint.pprint(data)
                    data_list.append(data)
                else:
                    data={
                        "owner_uri": "http://example.com/test",
                            "owner_username": "test",
                            "description": f"I like the song {Cleaned_Songs[i]} by {artist_queries[i]}",
                            "subject": "http://example.com/test",   
                            "predicate": {"value": {"description": "like"}},  
                            "object": {"value": {"description": f"the song {Cleaned_Songs[i]} by {artist_queries[i]}", 
                                                "related_entities": ["https://schema.org/MusicGroup", f"{entity_links_musicbrainz_artists[i]}", 
                                                                    "https://schema.org/MusicRecording", f"{entity_links_musicbrainz_tracks[i]}"]},
                                                                    "additional_info": {"primary_listening_years": year}},
                            "preference": 1.0
                        }
                    # print(data)
                    i+=1
                    data_list.append(data)
        data_list
        # print(data_list)
        return data_list



    # Statements to be called if we want to populate the PKG with disliked songs
    def create_apple_music_dislike_statement(main_artist_names, entity_links_musicbrainz_artists, entity_links_musicbrainz_tracks, Cleaned_Songs, artist_queries):
        i=0
        data_list=[]
        for clean_song in Cleaned_Songs:
            if entity_links_musicbrainz_artists[i] == "Artist not found" or entity_links_musicbrainz_artists[i] == "Artist not found":
                data={
                    "owner_uri": "http://example.com/test",
                        "owner_username": "test",
                        "description": f"I dislike the song {clean_song} by {artist_queries[i]}",
                        "subject": "http://example.com/test", 
                        "predicate": {"value": {"description": "dislike"}},   
                        "object": {"value": {"description": f"the song {clean_song} by {artist_queries[i]}", 
                                            }},
                        "preference": -1.0
                    }
                data_list.append(data)

                i+=1
            else:
                data={
                    "owner_uri": "http://example.com/test",
                        "owner_username": "test",
                        "description": f"I dislike the song {clean_song} by {artist_queries[i]}",
                        "subject": "http://example.com/test", 
                        "predicate": {"value": {"description": "dislike"}},   
                        "object": {"value": {"description": f"the song {clean_song} by {artist_queries[i]}", 
                                            "related_entities": ["https://schema.org/MusicGroup", f"{entity_links_musicbrainz_artists[i]}", 
                                                                "https://schema.org/MusicRecording", f"{entity_links_musicbrainz_tracks[i]}"]}},
                        "preference": -1.0
                    }
                data_list.append(data)
                i+=1
        return data_list

