# app.py

from datetime import datetime
import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, redirect, url_for, session, request, jsonify
import requests
import urllib.parse
from PKGClass import PKGFunctions
import requests
from Statements import statements

from GroundTruthNetflix import groundTruthNetflix
from NetflixClass import NetflixFunctions

from GroundTruthSpotify import groundTruthSpotify
from SpotifyClass import SpotifyFunctions

import pandas as pd
from AppleMusic import AppleMusic

pkg_functions = PKGFunctions()
netflix_functions = NetflixFunctions()

spotify_functions = SpotifyFunctions()

pkg_statements = statements()
ground_truth_Netflix_statements = groundTruthNetflix()
ground_truth_Spotify_statements = groundTruthSpotify()

url = "http://127.0.0.1:5000/statements"


app = Flask(__name__)
app.secret_key = "lrip4pJM10OMJHdaHZ9c5w"  # Change this to a secure, random key

# Spotify API credentials
SPOTIFY_CLIENT_ID = "13793570c33c4c2885ee1735e4749ac3"
SPOTIFY_CLIENT_SECRET = "9b0dcf81e61b4e66990cc3d3c29b76dd"
SPOTIFY_REDIRECT_URI = "http://127.0.0.1:7000/callback"

# Spotify API endpoints
SPOTIFY_API_BASE_URL = "https://api.spotify.com/v1"
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_ME_URL = SPOTIFY_API_BASE_URL + "/me"
SPOTIFY_API_PLAYLISTS_URL = SPOTIFY_API_BASE_URL + "/me/playlists"

app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['test_files'] = 'tests'

# API URL
API_URL = "https://rel.cs.ru.nl/api"


# Flask routes
@app.route('/')
def index():
    if 'SPOTIFY_LOGIN_PRESSED' in app.config and app.config['SPOTIFY_LOGIN_PRESSED']:
        return render_template('index.html', spotify_login_pressed=True)
    else:
        return render_template('index.html', spotify_login_pressed=False)

@app.route('/login/<platform>', methods=['GET', 'POST'])
def login(platform):
    if platform == 'spotify':
        app.config['SPOTIFY_LOGIN_PRESSED'] = True
        return redirect(url_for('index'))
    elif platform == 'netflix':
        return redirect(url_for('profile', platform='netflix'))
    elif platform == 'Entity_Linking':
        return redirect(url_for('profile', platform='Entity_Linking'))
    else:
        return redirect(url_for('index'))

@app.route('/proceed', methods=['POST'])
def proceed():
    print("proceed")
    if request.method == 'POST':
        platform = request.form.get('platform')
        print(platform)
        if platform == 'spotify-API':
            username_checked = 'usernameCheckbox' in request.form
            playlists_checked = 'playlistsCheckbox' in request.form
            songs_checked = 'songsCheckbox' in request.form

            SPOTIFY_SCOPES = []

            # Store the selected options in session variables
            session['username_checked'] = username_checked
            session['playlists_checked'] = playlists_checked
            session['songs_checked'] = songs_checked

            if songs_checked:
                num_songs = int(request.form['numSongsInput'])
                session['num_songs'] = num_songs
                SPOTIFY_SCOPES.append("user-top-read")
            if playlists_checked:
                SPOTIFY_SCOPES.append("playlist-read-private")
            if username_checked:
                SPOTIFY_SCOPES.append("user-read-private")
                SPOTIFY_SCOPES.append("user-read-email")
                SPOTIFY_SCOPES.append("user-follow-read")

            params = {
                'client_id': SPOTIFY_CLIENT_ID,
                'response_type': 'code',
                'redirect_uri': SPOTIFY_REDIRECT_URI,
                'scope': ' '.join(SPOTIFY_SCOPES),
                'show_dialog': True # Force user to approve app again if they've already done so
            }
            auth_url = f"{SPOTIFY_AUTH_URL}?{urllib.parse.urlencode(params)}"
            return redirect(auth_url)
        
        elif platform == 'netflix-upload':
            if 'file' not in request.files:
                return 'No file part'
            file = request.files['file']
            if file.filename == '':
                return 'No selected file'
            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                return redirect(url_for('profile', platform='netflix', file_path=file_path))

        elif platform == 'applemusic-upload':
            if 'file' not in request.files:
                return 'No file part'
            file = request.files['file']
            if file.filename == '':
                return 'No selected file'
            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                return redirect(url_for('profile', platform='applemusic', file_path=file_path))
            

        elif platform == 'Entity_Linking':
            example_string = request.form.get('statement', '')
            return redirect(url_for('profile', platform='Entity_Linking', example_string=example_string))
    return redirect(url_for('index'))

@app.route('/proceed_test', methods=['POST'])
def proceed_test():
    if request.method == 'POST':
        platform = request.form.get('platform')
        print(platform)
        if platform == 'spotify-TEST':
            return redirect(url_for('test', platform='spotify-TEST'))
        elif platform == 'netflix-TEST':
            return redirect(url_for('test', platform='netflix-TEST'))
    return redirect(url_for('index'))

@app.route('/progress-spotify')
def progress_spotify():
    print(spotify_functions.processed_tracks, spotify_functions.total_tracks)
    return jsonify(
        {
            'processed': spotify_functions.processed_tracks,
            'total': spotify_functions.total_tracks
        }
    )


@app.route('/progress-netflix')
def progress_netflix():
    print(netflix_functions.processed_movies, netflix_functions.total_movies)
    return jsonify(
        {
            'processed': netflix_functions.processed_movies,
            'total': netflix_functions.total_movies
        }
    )
            


@app.route('/callback')
def callback():
    if 'code' in request.args:
        req_body = {
            'grant_type': 'authorization_code',
            'code': request.args.get('code'),
            'redirect_uri': SPOTIFY_REDIRECT_URI,
            'client_id': SPOTIFY_CLIENT_ID,
            'client_secret': SPOTIFY_CLIENT_SECRET
        }
    
        response = requests.post(SPOTIFY_TOKEN_URL, data=req_body)
        token_info = response.json()

        session['access_token'] = token_info['access_token']
        session['refresh_token'] = token_info['refresh_token']
        session['expires_at'] = datetime.now().timestamp() + token_info['expires_in']

        return redirect(url_for('profile',platform='spotify'))

@app.route('/error')
def error():
    error_message = request.args.get('error', 'Unknown error')
    return f'Error: {error_message}', 400

@app.route('/profile/<platform>')
def profile(platform):
    ###############
    ### Spotify ###
    ###############

    if platform == 'spotify': 
        if 'access_token' not in session:
            return redirect(url_for('login'))
        if datetime.now().timestamp() > session['expires_at']:
            return redirect(url_for('refresh_token'))

        # Get the user's top X tracks from Spotify
        headers = {'Authorization': f'Bearer {session["access_token"]}'}

        # Retrieve session variables
        username_checked = session.get('username_checked', False)
        playlists_checked = session.get('playlists_checked', False)
        songs_checked = session.get('songs_checked', False)
        num_songs = session.get('num_songs', 0)

        top_tracks_short = []
        top_tracks_medium = []
        top_tracks_long = []
        user_info = {}
        playlists = []
        following_users = []

        if songs_checked:
            top_tracks_short_response = requests.get(f"{SPOTIFY_API_ME_URL}/top/tracks?time_range=short_term&limit={num_songs}", headers=headers)
            top_tracks_medium_response = requests.get(f"{SPOTIFY_API_ME_URL}/top/tracks?time_range=medium_term&limit={num_songs}", headers=headers)
            top_tracks_long_response = requests.get(f"{SPOTIFY_API_ME_URL}/top/tracks?time_range=long_term&limit={num_songs}", headers=headers)

            if all(response.status_code == 200 for response in [top_tracks_short_response, top_tracks_medium_response, top_tracks_long_response]):
                top_tracks_short = top_tracks_short_response.json().get('items', [])
                top_tracks_medium = top_tracks_medium_response.json().get('items', [])
                top_tracks_long = top_tracks_long_response.json().get('items', [])
            
            list_of_ranges = [top_tracks_short, top_tracks_medium, top_tracks_long]
            

            track_URI_list_combined = []
            artist_URI_list_combined = []
            song_names_combined = []
            songs_checked = []
             
            
            for track_data in list_of_ranges:
                track_URI_list = []
                artist_URI_list = []
                song_names = []
                songs_checked = []
                track_URI_list = []
                artist_URI_list = []

                for track in track_data:
                    artist_uri_list = []
                    track_uri_list = []
                    spotify_functions.artist_index = 0
                    song_name = spotify_functions.remove_feat_part(track['name'])
                    for artist in track["artists"]: # in case of multiple artists
                        artist_name = artist['name']
                        artist_URI, song_URI, new_song_name = spotify_functions.search_artist(artist_name, song_name)
                        if artist_URI is None and song_URI is None:
                            artist_uri_list.append("No:URI:found")
                            track_uri_list.append("No:URI:found")
                        elif artist_URI == "No response" and song_URI == "No response":
                            artist_uri_list.append("No response")
                            track_uri_list.append("No response")
                        else:
                            artist_uri_list.append(artist_URI)
                            track_uri_list.append(song_URI)
                            spotify_functions.current_song_name = new_song_name
                            song_name = new_song_name
                    artist_URI_list.append(artist_uri_list)
                    track_URI_list.append(track_uri_list)
                    song_names.append(song_name)

                for i in range(len(track_URI_list)):
                    if len(track_URI_list[i]) > 1:
                        for j in range(1, len(track_URI_list[i])):
                            if track_URI_list[i][j] == "No:URI:found":
                                track_URI_list[i].pop(j)

                pkg_statements.create_spotify_statement(track_data, track_URI_list, artist_URI_list, song_names)
                track_URI_list_combined.append(track_URI_list)
                artist_URI_list_combined.append(artist_URI_list)
                song_names_combined.append(song_names)
                            


        if username_checked:
            user_info_response = requests.get(SPOTIFY_API_ME_URL, headers=headers)
            following_users_response = requests.get(f"{SPOTIFY_API_ME_URL}/following?type=artist", headers=headers)

            if all(response.status_code == 200 for response in [user_info_response, following_users_response]):
                user_info = user_info_response.json()
                following_users = following_users_response.json().get('artists', {}).get('items', [])

        if playlists_checked:
            playlists_response = requests.get(SPOTIFY_API_PLAYLISTS_URL, headers=headers)

            if playlists_response.status_code == 200:
                playlists = playlists_response.json().get('items', [])
        
        if songs_checked == False and playlists_checked == False and username_checked == False:
            return redirect(url_for('error'), error='Oops, seems like you did not select any data to retrieve from Spotify')

        return render_template('/profile/spotify.html', 
                                top_tracks_short=top_tracks_short, 
                                top_tracks_medium=top_tracks_medium,
                                top_tracks_long=top_tracks_long, 
                                user_info=user_info, 
                                playlists=playlists,
                                following_users=following_users,
                                track_URI_list=track_URI_list_combined, 
                                artist_URI_list=artist_URI_list_combined,
                                song_names=song_names_combined
                                )        
    ###############
    ### Netflix ###    
    ###############

    elif platform == 'netflix':
        file_path = request.args.get('file_path')
        csv_file_path = file_path
        hooks, liked_movies= netflix_functions.read_csv_file(csv_file_path)
        movies_info = []
        movie_titles = {}
        movie_actor_list = {}
        print("found liked movies", len(liked_movies))
        i = 0
        for movie_title, _ in liked_movies:
            print(movie_title)
            movie_info = netflix_functions.search_OMDb(movie_title, 'movie')
            if movie_info['Response'] == 'True':
                movies_info.append(movie_info)
                movie_titles[movie_title] = movie_info['Movie']
                movie_actor_list[movie_info['ImdbID']] = {
                    'Actors': movie_info['Actors']
                }
            i += 1
        movie_actor_uris = netflix_functions.link_entities(movie_actor_list)

        combined_data = list(zip(movie_actor_list.items(), movie_actor_uris.items(), movie_titles.items()))
        if liked_movies:
            #pkg_statements.create_netflix_statement(combined_data)

            return render_template('/profile/netflix.html', 
                                        combined_data=combined_data
                                        )
        else: 
            return redirect(url_for('error', error = 'Does not seem like you have watched any movies on Netflix twice'))


    #####################
    #### Apple Music ####
    #####################

    elif platform == 'applemusic':

        print(platform)
        file_path='.\\uploads\\Apple_Music_-_Play_History_Daily_Tracks.csv'
        df=pd.read_csv(file_path)


        if os.path.exists(file_path):
            os.remove(file_path)
            print("File has been deleted.")
        else:
            print("The file does not exist.")
        
        
        # unit tests
        df = {
    'Country': ['Norway', 'Norway', 'Norway', 'Norway', 'Norway'],
    'Track Identifier': [1208759373, 1207120448, 1207120538, 1210094302, 1210094305],
    'Media type': ['AUDIO', 'AUDIO', 'AUDIO', 'AUDIO', 'AUDIO'],
    'Date Played': ['20170419', '20170419', '20170419', '20170419', '20170419'],
    'Hours': ['16, 21', '16, 21', '16, 21', '17, 21', '12'],
    'Play Duration Milliseconds': [497602, 494444, 443128, 425018, 555555],
    'Source Type': ['IPHONE', 'IPHONE', 'IPHONE', 'IPHONE', 'IPHONE'],
    'Play Count': [2, 2, 2, 2, 3],
    'Skip Count': [0, 0, 0, 0, 1],
    'Ignore For Recommendations': [None, None, None, None, None],
    'Track Reference': [1.208759e+09, 1.207120e+09, 1.207121e+09, 1.210094e+09, 1210094e+09],
    'Track Description': [
        'Symphony by Clean Bandit',  # No dashes
        'Coldplay - Viva la Vida - Live Version',  # Two dashes
        'John Cena - Pippi Langstrømpe the anthem',  # Fake song
        'Maroon 5 - Cold (feat. Future)',  # feat.
        '0 - ' # one dash without right element 
    ]
}
        df=pd.DataFrame(df)
        Year, Song_Names, Artists_and_Groups = AppleMusic.liked_songs(df)    
        main_artist_names, entity_links_musicbrainz_artists, entity_links_musicbrainz_tracks, Cleaned_Songs, Queries, artist_queries = AppleMusic.search_track_musicbrainz(Song_Names, Artists_and_Groups)


        statements.create_apple_music_like_statement(Year, main_artist_names, entity_links_musicbrainz_artists, entity_links_musicbrainz_tracks, Cleaned_Songs, artist_queries)
        
        
        if main_artist_names:
            return render_template('/profile/applemusic.html', Cleaned_Songs=Cleaned_Songs,
                                main_artist_names=main_artist_names,
                                artist_queries = artist_queries,
                                entity_links_musicbrainz_artists=entity_links_musicbrainz_artists,
                                entity_links_musicbrainz_tracks=entity_links_musicbrainz_tracks
                                # ,
                                # Year=Year
                                )
        else: 
            return redirect(url_for('error'))
    

    ######################
    ### Entity Linking ###
    ######################

    elif platform == 'Entity_Linking':
        example_string = request.args.get('example_string')
        entity_recognitions = pkg_functions.get_REL_api_response(example_string)
        processed_NER = pkg_functions.process_entity_linking_response(entity_recognitions, example_string)
        return render_template('/profile/EntityLinking.html', processed_NER=processed_NER)

@app.route('/test/<platform>/')
def test(platform):
    if platform == 'spotify-TEST':
        file_path = os.path.join(os.path.dirname(__file__), 'test_files', 'spotify_test_file.json')

        top_tracks_short, track_URI_list, artist_URI_list, song_names = spotify_functions.assign_URI(file_path)

        test_data = pkg_statements.create_spotify_statement(top_tracks_short, track_URI_list, artist_URI_list, song_names)
        
        combined_artists = []
        combined_artists.append(artist_URI_list)
        combined_tracks = []
        combined_tracks.append(track_URI_list)
        combined_songs = []
        combined_songs.append(song_names)
        
        ground_truth_data = ground_truth_Spotify_statements.create_statement()

        pkg_functions.compute_precision_recall(ground_truth_data, test_data, test_type="Related_entities")
          
        pkg_functions.compute_precision_recall(ground_truth_data, test_data, test_type="Description")
         
        pkg_functions.compute_precision_recall(ground_truth_data, test_data, "songs_movies")

        pkg_functions.compute_precision_recall(ground_truth_data, test_data, "artists_actors")          
            
        return render_template('/profile/spotify.html', top_tracks_short=top_tracks_short, track_URI_list=combined_tracks, artist_URI_list=combined_artists, song_names=combined_songs)
    
    elif platform == 'netflix-TEST':
        file_path = os.path.join(os.path.dirname(__file__), 'test_files', 'test.csv')

        hooks, liked_movies= netflix_functions.read_csv_file(file_path)
        movies_info = []
        movie_titles = {}
        movie_actor_list = {}
        print("found liked movies", len(liked_movies))
        i = 0
        for movie_title, _ in liked_movies:
            movie_info = netflix_functions.search_OMDb(movie_title, 'movie')
            if movie_info['Response'] == 'True':
                movies_info.append(movie_info)
                movie_titles[movie_title] = movie_info['Movie']
                movie_actor_list[movie_info['ImdbID']] = {
                    'Actors': movie_info['Actors']
                }
            i += 1
        movie_actor_uris = netflix_functions.link_entities(movie_actor_list)

        combined_data = list(zip(movie_actor_list.items(), movie_actor_uris.items(), movie_titles.items()))

        if liked_movies:
            test_data = pkg_statements.create_netflix_statement(combined_data)
            ground_truth_data = ground_truth_Netflix_statements.create_statement()
            
            # test all related_entities
            pkg_functions.compute_precision_recall(ground_truth_data, test_data, "Related_entities")
            
            # test all descriptions
            pkg_functions.compute_precision_recall(ground_truth_data, test_data, "Description")

            # test all movies
            pkg_functions.compute_precision_recall(ground_truth_data, test_data, "songs_movies")

            pkg_functions.compute_precision_recall(ground_truth_data, test_data, "artists_actors")

            
            

            return render_template('/profile/netflix.html', 
                                        combined_data=combined_data
                                        )
        else: 
            return redirect(url_for('error', error = 'Does not seem like you have watched any movies on Netflix twice'))
            
        


if __name__ == '__main__':
    app.run(debug=True, port=7000)
