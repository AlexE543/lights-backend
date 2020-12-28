from flask import request
from flask_restx import Resource, Namespace
from utils.shared import light_strand
import time
import json
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth

spotify_ns = Namespace("spotify", description="spotify control")

scope = "user-read-currently-playing user-top-read user-read-recently-played user-read-playback-state " \
            "user-modify-playback-state streaming app-remote-control user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=os.getenv('SPOTIPY_CLIENT_ID'),
                                                client_secret=os.getenv('SPOTIPY_CLIENT_SECRET')))


@spotify_ns.route('/test')
class Test(Resource):
    def get(self):
        start = time.time()
        print(sp.current_playback())
        print(sp.currently_playing())
        end = time.time()
        return f"This command took {end-start} seconds"


@spotify_ns.route('/next_song')
class NextSong(Resource):
    def get(self):
        start = time.time()
        print(sp.next_track())
        end = time.time()
        return f"This command took {end-start} seconds"


@spotify_ns.route('/previous_song')
class PreviousSong(Resource):
    def get(self):
        start = time.time()
        print(sp.previous_track())
        end = time.time()
        return f"This command took {end-start} seconds"


@spotify_ns.route('/pause_play')
class PausePlay(Resource):
    def get(self):
        start = time.time()
        print(sp.currently_playing())
        if sp.currently_playing():
            print(sp.pause_playback())
        else:
            print(sp.start_playback())
        end = time.time()
        return f"This command took {end-start} seconds"
