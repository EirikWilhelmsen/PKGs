# app.py

from datetime import datetime, timedelta
import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, redirect, url_for, session, request, jsonify
import requests
import json
import base64
import urllib.parse
import csv
from PKGClass import PKGFunctions

pkg_functions = PKGFunctions() 


app = Flask(__name__)
app.secret_key = "lrip4pJM10OMJHdaHZ9c5w"  # Change this to a secure, random key

# Spotify API credentials
SPOTIFY_CLIENT_ID = "13793570c33c4c2885ee1735e4749ac3"
SPOTIFY_CLIENT_SECRET = "9b0dcf81e61b4e66990cc3d3c29b76dd"
SPOTIFY_REDIRECT_URI = "http://127.0.0.1:5000/callback"

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
    elif platform == 'instagram':
        return redirect(url_for('profile', platform='instagram'))
    elif platform == 'Entity_Linking':
        return redirect(url_for('profile', platform='Entity_Linking'))
    else:
        # Handle unknown platform, for example, redirect to the index page
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
        elif platform == 'Entity_Linking':
            example_string = request.form.get('statement', '')
            return redirect(url_for('profile', platform='Entity_Linking', example_string=example_string))
        
        elif platform == 'netflix-TEST':
            file_path = os.path.join(os.path.dirname(__file__), 'test_files', 'test.csv')
            
            hooks, liked_movies= pkg_functions.read_csv_file(file_path)
        
        elif platform == 'spotify-TEST':
            file_path = os.path.join(os.path.dirname(__file__), 'test_files', 'spotify_test_file.json')

            with open(file_path, 'r') as file:
                data = json.load(file)

                # Now 'data' contains the contents of the JSON file
            track_URI_list = []
            artist_URI_list = []
            for track in data:
                artist_name = track['artists'][0]['name']
                song_name = track['name']
                artist_URI, song_URI = pkg_functions.search_artist(artist_name, song_name)
                if song_URI is not None and artist_URI is not None:
                    track_URI_list.append(song_URI)
                    artist_URI_list.append(artist_URI)
                else:
                    track_URI_list.append("No URI found")
                    artist_URI_list.append("No URI found")
            print("track_uri_list",track_URI_list)
            print("artist_uri_list",artist_URI_list)
            return render_template('/profile/spotify.html', top_tracks_short=data, track_URI_list=track_URI_list, artist_URI_list=artist_URI_list)

        return redirect(auth_url)


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
            
            # Iterate through the top tracks
            list_of_ranges = [top_tracks_short, top_tracks_medium, top_tracks_long]
            

            track_URI_list_combined = []
            artist_URI_list_combined = []
            for track in list_of_ranges:
                track_URI_list = []
                artist_URI_list = []
                for track_data in track:
                    artist_name = track_data['artists'][0]['name']
                    song_name = track_data['name']
                    artist_URI, song_URI = pkg_functions.search_artist(artist_name, song_name)
                    if song_URI is not None and artist_URI is not None:
                        track_URI_list.append(song_URI)
                        artist_URI_list.append(artist_URI)
                    else:
                        track_URI_list.append("No URI found")
                        artist_URI_list.append("No URI found")

                track_URI_list_combined.append(track_URI_list)
                artist_URI_list_combined.append(artist_URI_list)
            
            print(track_URI_list_combined[0][0])
            print(artist_URI_list_combined[0][0])
            print(track_URI_list_combined[1][0])
            print(artist_URI_list_combined[1][0])
            print(track_URI_list_combined[2][0])
            print(artist_URI_list_combined[2][0])


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

        return render_template('/profile/spotify.html', 
                                top_tracks_short=top_tracks_short, 
                                top_tracks_medium=top_tracks_medium,
                                top_tracks_long=top_tracks_long, 
                                user_info=user_info, 
                                playlists=playlists,
                                following_users=following_users, 
                                track_URI_list=track_URI_list_combined, 
                                artist_URI_list=artist_URI_list_combined
                                )        
    ###############
    ### Netflix ###    
    ###############

    elif platform == 'netflix':
        file_path = request.args.get('file_path')
        csv_file_path = file_path
        hooks, liked_movies= pkg_functions.read_csv_file(csv_file_path)
        movies_info = []
        actorIDs = []
        movie_titles = {}
        movie_actor_list = {}
        print("found liked movies", len(liked_movies))
        i = 0
        for movie_title, _ in liked_movies:
            print(i)
            movie_info = pkg_functions.search_OMDb(movie_title, 'movie')
            if movie_info['Response'] == 'True':
                movies_info.append(movie_info)
                movie_titles[movie_title] = movie_info['Movie']
                movie_actor_list[movie_info['ImdbID']] = {
                    'Actors': movie_info['Actors']
                }
            i += 1
        print("alle filmer funnet")
        movie_actor_uris = pkg_functions.link_entities(movie_actor_list)
        print("enheter linket")


        print("begynner å kombinere nå")
        combined_data = list(zip(movie_actor_list.items(), movie_actor_uris.items(), movie_titles.items()))
        print("ferdig med å kombinere")
        """
        combined_data =
        [
            (
                ('tt0322259', {'Actors': ['Paul Walker', ' Tyrese Gibson', ' Cole Hauser']}), 
                ('https://www.imdb.com/title/tt0322259/', {'actor_uris': ['https://www.imdb.com/name/nm0908094/', 'https://www.imdb.com/name/nm0879085/', 'https://www.imdb.com/name/nm0369513/']}), 
                ('2 Fast 2 Furious', '2 Fast 2 Furious')
            ), 
            (
                ('tt0120338', {'Actors': ['Leonardo DiCaprio', ' Kate Winslet', ' Billy Zane']}), 
                ('https://www.imdb.com/title/tt0120338/', {'actor_uris': ['https://www.imdb.com/name/nm0000138/', 'https://www.imdb.com/name/nm0000701/', 'https://www.imdb.com/name/nm0000708/']}), 
                ('Titanic', 'Titanic')
            )
        ]
        """



        if liked_movies:
            print("hei")
            return render_template('/profile/netflix.html', 
                                        combined_data=combined_data
                                        )
        else: 
            return redirect(url_for('error'))
    
    #################
    ### Instagram ###
    #################

    elif platform == 'instagram':
        json_file_path = 'instagram-eirik/personal_information/personal_information/personal_information.json'
        user_info = pkg_functions.read_json_file(json_file_path)['profile_user'][0]
        json_file_path = 'instagram-eirik/personal_information/information_about_you/account_based_in.json'
        account_based_in = pkg_functions.read_json_file(json_file_path)['inferred_data_primary_location'][0]
        json_file_path = 'instagram-eirik/your_instagram_activity/content/posts_1.json'
        posts = pkg_functions.read_json_file(json_file_path).get('media', [])
        json_file_path = 'instagram-eirik/preferences/your_topics/your_topics.json'
        topics = pkg_functions.read_json_file(json_file_path)['topics_your_topics']

        return render_template('/profile/instagram.html', user_info=user_info, account_based_in=account_based_in, posts=posts, topics=topics)

    ######################
    ### Entity Linking ###
    ######################

    elif platform == 'Entity_Linking':
        example_string = request.args.get('example_string')
        entity_recognitions = pkg_functions.get_REL_api_response(example_string)
        processed_NER = pkg_functions.process_entity_linking_response(entity_recognitions, example_string)
        return render_template('/profile/EntityLinking.html', processed_NER=processed_NER)


if __name__ == '__main__':
    app.run(debug=True)
