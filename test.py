test = []

movie = 'The Matrix'
actors = 'Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving'
actor_list = actors.split(',')
imdbID = 'tt0133093'
response = 'True'

info = {
    'Movie': movie,
    'Actors': actor_list,
    'ImdbID': imdbID,
    'Response': response
}
test.append(info)

for movie in test:
    if movie['Movie'] == 'The Matrix':
        print(movie)
        break