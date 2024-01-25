# app.py

from datetime import datetime
from flask import Flask, render_template, redirect, url_for, session, request, jsonify
import requests
import json
import base64
import urllib.parse


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

# Scopes required for the Spotify API
SPOTIFY_SCOPES = ["user-top-read",
                  "user-read-private",
                  "user-read-email",
                  "playlist-read-private"]

# Flask routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/<platform>', methods=['GET','POST'])
def login(platform):
    if platform == 'spotify': 
        params = {
            'client_id': SPOTIFY_CLIENT_ID,
            'response_type': 'code',
            'redirect_uri': SPOTIFY_REDIRECT_URI,
            'scope': ' '.join(SPOTIFY_SCOPES),
            'show_dialog': True # Force user to approve app again if they've already done so
        }
        auth_url = f"{SPOTIFY_AUTH_URL}?{urllib.parse.urlencode(params)}"
        return redirect(auth_url)
    
    elif platform == 'netflix':
        pass
    elif platform == 'soundcloud':
        pass

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
    if platform == 'spotify': 
        if 'access_token' not in session:
            return redirect(url_for('login'))
        if datetime.now().timestamp() > session['expires_at']:
            return redirect(url_for('/refresh_token'))

        # Get the user's top X tracks from Spotify
        headers = {'Authorization': f'Bearer {session["access_token"]}'}

        top_tracks_response = requests.get(f"{SPOTIFY_API_ME_URL}/top/tracks?time_range=medium_term&limit=10", headers=headers)

        # Get user information from Spotify
        user_info_response = requests.get(SPOTIFY_API_ME_URL, headers=headers)

        # Get user's playlists from Spotify
        playlists_response = requests.get(SPOTIFY_API_PLAYLISTS_URL, headers=headers)


        if any(response.status_code != 200 for response in [top_tracks_response, user_info_response, playlists_response]):
            return f"Error fetching data from Spotify. Check the console for details."

        top_tracks = top_tracks_response.json().get('items', [])
        user_info = user_info_response.json()
        playlists = playlists_response.json().get('items', [])

        return render_template('/profile/spotify.html', top_tracks=top_tracks, user_info=user_info, playlists=playlists)

if __name__ == '__main__':
    app.run(debug=True)
