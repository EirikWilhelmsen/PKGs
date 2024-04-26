subject = "http://example.com/test"
predicate = {"value": {"description": "like"}}
object_desription = '{"value": {"description": "the movie Titanic starring Leonardo DiCaprio, Kate Winslet, Billy Zane",'
object_related_entities =  ' related_entities: ["https://schema.org/actor", "https://www.imdb.com/name/nm0000138/", "https://schema.org/actor", "https://www.imdb.com/name/nm0000701/", "https://schema.org/actor", "https://www.imdb.com/name/nm0000708/", "https://schema.org/Movie", "https://www.imdb.com/title/tt0120338/"]}}'

test_data = {
    "subject": subject,
    "predicate": predicate,
    "object": object_desription + object_related_entities 
}

print(test_data["object"])

object = {"value": {"description": "the movie Titanic starring Leonardo DiCaprio, Kate Winslet, Billy Zane",
                    "related_entities": ["https://schema.org/actor", "https://www.imdb.com/name/nm0000138/",
                                        "https://schema.org/actor", "https://www.imdb.com/name/nm0000701/",
                                        "https://schema.org/actor", "https://www.imdb.com/name/nm0000708/",
                                        "https://schema.org/Movie", "https://www.imdb.com/title/tt0120338/"]}}
test_data = {
    "subject": subject,
    "predicate": predicate,
    "object": object["value"]["related_entities"] 
}
print(test_data["object"])
