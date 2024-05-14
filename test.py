import requests

url = "http://127.0.0.1:5000/statements"

data={
    "owner_uri": "http://example.com/test",
    "owner_username": "test",
    "description": "I like the song ee by aaa",
    "subject": "http://example.com/test",   
    "predicate": {"value": {"description": "like"}},  
    "object": {"value": {"description": f"the song ee by aaa", 
                        "related_entities": ["https://schema.org/MusicGroup", "https://musicbrainz.org/recording/ee",
                                            "https://schema.org/MusicRecording", "https://musicbrainz.org/recording/ee"]}},
    "additional_info": {"primary_listening_years": 2222},
    "preference": 1.0
}

response = requests.post(url, json=data)
assert response.status_code == 200