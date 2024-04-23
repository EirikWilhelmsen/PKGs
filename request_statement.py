import requests

url = "http://127.0.0.1:5000/statements"

platform = input("Enter the platform: ").lower()

if platform == "netflix":
    data = {
        "owner_uri": "http://example.com/test",
        "owner_username": "test",
        "description": "I like the movie Titanic starring Leonardo DiCaprio, Kate Winslet, Billy Zane",
        "subject": "http://example.com/test",   # Single string when using URI
        "predicate": {"value": {"description": "like"}},    # Use dictionary when the field is a concept
        "object": {"value": {"description": "the movie Titanic starring Leonardo DiCaprio, Kate Winslet, Billy Zane", 
                            "related_entities": ["https://schema.org/Movie","https://www.imdb.com/title/tt0120338/",
                                                "https://schema.org/actor", "https://www.imdb.com/name/nm0000138/", 
                                                "https://schema.org/actor", "https://www.imdb.com/name/nm0000701/", 
                                                "https://schema.org/actor", "https://www.imdb.com/name/nm0000708/"]}},
        "preference": 1.0
    }
    response = requests.post(url, json=data)
    assert response.status_code == 200
elif platform == "spotify":
    data = {
        "owner_uri": "http://example.com/test",
        "owner_username": "test",
        "description": "I like the song Beverly Hills by Amara",
        "subject": "http://example.com/test",   # Single string when using URI
        "predicate": {"value": {"description": "like"}},    # Use dictionary when the field is a concept
        "object": {"value": {"description": "the song Beverly Hills by Amara", 
                            "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/62051d1b-50e6-43ce-bf51-6ed96b00e9fc", 
                                                "https://schema.org/song", "No:URI:found"]}},
        "preference": 1.0
    }
    response = requests.post(url, json=data)
    assert response.status_code == 200
    data = {
        "owner_uri": "http://example.com/test",
        "owner_username": "test",
        "description": "I like the song MY EYES by Travis Scott",
        "subject": "http://example.com/test",   # Single string when using URI
        "predicate": {"value": {"description": "like"}},    # Use dictionary when the field is a concept
        "object": {"value": {"description": "the song MY EYES by Travis Scott", 
                            "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/e4a51f17-a57b-47b1-b37b-f552d0f8e9e6",
                                                "https://schema.org/song", "https://musicbrainz.org/recording/8ff798b3-68c3-4d73-9d8b-34d8c0b1f8e0"]}},
        "preference": 1.0
    }
    response = requests.post(url, json=data)
    assert response.status_code == 200  
    data = {
        "owner_uri": "http://example.com/test",
        "owner_username": "test",
        "description": "I like the song FANTA (feat. Mariinomadeit!) by Ozzi, and Mariinomadeit!",
        "subject": "http://example.com/test",   # Single string when using URI
        "predicate": {"value": {"description": "like"}},    # Use dictionary when the field is a concept
        "object": {"value": {"description": "the song FANTA (feat. Mariinomadeit!) by Ozzi, and Mariinomadeit!", 
                            "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/62051d1b-50e6-43ce-bf51-6ed96b00e9fc",
                                                "https://schema.org/artist", "https://musicbrainz.org/artist/6a1c5825-2e6f-4668-9598-18af71c710cf", 
                                                "https://schema.org/song", "https://musicbrainz.org/recording/0edbbf06-6895-4d18-a328-29d868c5dcc1"]}},
        "preference": 1.0
    
    }
    response = requests.post(url, json=data)
    assert response.status_code == 200

    data = {
        "owner_uri": "http://example.com/test",
        "owner_username": "test",
        "description": "I like the song farger by Dutty Dior, and Chirag",
        "subject": "http://example.com/test",   # Single string when using URI
        "predicate": {"value": {"description": "like"}},    # Use dictionary when the field is a concept
        "object": {"value": {"description": "the song farger by Dutty Dior, and Chirag", 
                            "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/daf0b012-0004-435b-9f7e-5e9ab40ec9a4",
                                                 "https://schema.org/artist", "No:URI:found", "https://schema.org/song", "No:URI:found"]}},
        "preference": 1.0
    }
    response = requests.post(url, json=data)
    assert response.status_code == 200


    # 

