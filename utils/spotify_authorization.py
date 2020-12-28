import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth

scope = "user-read-currently-playing user-top-read user-read-recently-played user-read-playback-state " \
        "user-modify-playback-state streaming app-remote-control"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=os.getenv('SPOTIPY_CLIENT_ID'),
                                               client_secret=os.getenv('SPOTIPY_CLIENT_SECRET')))
results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
