import requests

url = "http://127.0.0.1:5000/statements"

class GroundTruthStatement:
    def __init__(self):
        pass
    def create_statement(self, platform):
        test_data_list = []

        if platform == "netflix":
            subject = "http://example.com/test"
            predicate = {"value": {"description": "like"}}
            object = {"value": {"description": "the movie 2 Fast 2 Furious starring Paul Walker, Tyrese Gibson, Cole Hauser",
                    "related_entities": ["https://schema.org/actor", "https://www.imdb.com/name/nm0908094/",
                                        "https://schema.org/actor", "https://www.imdb.com/name/nm0879085/",
                                        "https://schema.org/actor", "https://www.imdb.com/name/nm0369513/",
                                        "https://schema.org/Movie", "https://www.imdb.com/title/tt0322259/"]}}
            test_data = {
                "subject": subject,
                "predicate": predicate,
                "object": object['value']['related_entities'] 
            }
            test_data_list.append(test_data)

            ############################################################################################################

            subject = "http://example.com/test"
            predicate = {"value": {"description": "like"}}
            object = {"value": {"description": "the movie Titanic starring Leonardo DiCaprio, Kate Winslet, Billy Zane",
                    "related_entities": ["https://schema.org/actor", "https://www.imdb.com/name/nm0000138/",
                                        "https://schema.org/actor", "https://www.imdb.com/name/nm0000701/",
                                        "https://schema.org/actor", "https://www.imdb.com/name/nm0000708/",
                                        "https://schema.org/Movie", "https://www.imdb.com/title/tt0120338/"]}}
            test_data = {
                "subject": subject,
                "predicate": predicate,
                "object": object['value']['related_entities'] 
            }
            test_data_list.append(test_data)

            ############################################################################################################

            subject = "http://example.com/test"
            predicate = {"value": {"description": "like"}}
            object = {"value": {"description": "the movie Interstellar starring Matthew McConaughey, Anne Hathaway, Jessica Chastain",
                    "related_entities": ["https://schema.org/actor", "https://www.imdb.com/name/nm0000190/",
                                        "https://schema.org/actor", "https://www.imdb.com/name/nm0004266/",
                                        "https://schema.org/actor", "https://www.imdb.com/name/nm1567113/",
                                        "https://schema.org/Movie", "https://www.imdb.com/title/tt0816692/"]}}
            test_data = {
                "subject": subject,
                "predicate": predicate,
                "object": object['value']['related_entities']
            }
            test_data_list.append(test_data)

            ############################################################################################################

            subject = "http://example.com/test"
            predicate = {"value": {"description": "like"}}
            object = {"value": {"description": "the movie 10½ starring Claude Legault, Robert Naylor, Eugénie Beaudry",
                    "related_entities": ["https://schema.org/actor", "https://www.imdb.com/name/nm0499218/",
                                        "https://schema.org/actor", "https://www.imdb.com/name/nm2316151/",
                                        "https://schema.org/actor", "https://www.imdb.com/name/nm1799076/",
                                        "https://schema.org/Movie", "https://www.imdb.com/title/tt1591622/"]}}
            test_data = {
                "subject": subject,
                "predicate": predicate,
                "object": object['value']['related_entities']
            }
            test_data_list.append(test_data)

            ########################################## NEGATIVE TESTING ################################################

            pass

        elif platform == "spotify":
            subject = "http://example.com/test"
            predicate = {"value": {"description": "like"}}
            object = {"value": {"description": "the song Beverly Hills by Amara",
                    "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/62051d1b-50e6-43ce-bf51-6ed96b00e9fc", "https://schema.org/song", "No:URI:found"]}}

            test_data = {
                "subject": subject,
                "predicate": predicate,
                "object": object
            }
            test_data_list.append(test_data)

            ############################################################################################################

            subject = "http://example.com/test"
            predicate = {"value": {"description": "like"}}
            object = {"value": {"description": "the song MY EYES by Travis Scott",
                    "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/e4a51f17-a57b-47b1-b37b-f552d0f8e9e6", "https://schema.org/song", "https://musicbrainz.org/recording/8ff798b3-68c3-4d73-9d8b-34d8c0b1f8e0"]}}
            test_data = {
                "subject": subject,
                "predicate": predicate,
                "object": object 
            }
            test_data_list.append(test_data)

            ############################################################################################################

            subject = "http://example.com/test"
            predicate = {"value": {"description": "like"}}
            object = {"value": {"description": "the song FANTA (feat. Mariinomadeit!) by Ozzi, and Mariinomadeit!", 
                    "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/34f8899b-61a9-4802-813c-db3055509f5f",
                                        "https://schema.org/artist", "https://musicbrainz.org/artist/6a1c5825-2e6f-4668-9598-18af71c710cf", 
                                        "https://schema.org/song", "https://musicbrainz.org/recording/0edbbf06-6895-4d18-a328-29d868c5dcc1"]}}
            test_data = {
                "subject": subject,
                "predicate": predicate,
                "object": object 
            }
            test_data_list.append(test_data)

            ############################################################################################################

            subject = "http://example.com/test"
            predicate = {"value": {"description": "like"}}
            object = {"value": {"description": "the song farger by Dutty Dior, and Chirag", 
                    "related_entities": ["https://schema.org/artist", "https://musicbrainz.org/artist/daf0b012-0004-435b-9f7e-5e9ab40ec9a4",
                                        "https://schema.org/artist", "No:URI:found", "https://schema.org/artist", "No:URI:found",
                                        "https://schema.org/song", "No:URI:found"]}}
            test_data = {
                "subject": subject,
                "predicate": predicate,
                "object": object 
            }
            test_data_list.append(test_data)
            
        return test_data_list

