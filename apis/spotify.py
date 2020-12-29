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


@spotify_ns.route('/next_song')
class NextSong(Resource):
    def get(self):
        start = time.time()
        sp.next_track()
        end = time.time()
        return f"This command took {end-start} seconds"


@spotify_ns.route('/previous_song')
class PreviousSong(Resource):
    def get(self):
        start = time.time()
        sp.previous_track()
        end = time.time()
        return f"This command took {end-start} seconds"


@spotify_ns.route('/pause_play')
class PausePlay(Resource):
    def get(self):
        start = time.time()
        if sp.currently_playing().get('is_playing'):
            sp.pause_playback()
        else:
            sp.start_playback()
        end = time.time()
        return f"This command took {end-start} seconds"


@spotify_ns.route('/current_song')
class CurrentSong(Resource):
    def get(self):
        data = sp.currently_playing()
        return data


@spotify_ns.route('/pulse_to_beat')
class PulseToBeat(Resource):
    def post(self):
        data = sp.currently_playing()
        start_time = time.time()
        progress_ms = data.get("progress_ms")/1000
        data = json.loads(request.data)
        track_id = data.get('id')
        color = tuple(data.get('color'))
        analysis = sp.audio_analysis(track_id)
        bars = analysis.get("beats")
        current_bar = 0
        for i, bar in enumerate(bars):
            current_song_time = time.time() - start_time + progress_ms
            if current_song_time < bar.get("start"):
                current_bar = i
                time.sleep(bar.get("start") - current_song_time)
                break
        one = time.time() - start_time + progress_ms
        two = bars[current_bar].get('start')
        while current_bar < len(bars) - 1:
            light_strand.flash_fade((0, 133, 133))
            duration = bars[current_bar].get('duration')
            one = time.time() - start_time + progress_ms
            two = bars[current_bar].get('start')
            current_bar += 1
            time.sleep(max(0, duration-.2043))
        print(len(bars))
        print(two-one)


