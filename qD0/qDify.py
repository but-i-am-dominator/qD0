# qD0 + Spotify == qDify?
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify API credentials stored in external json file.

class qDify:

    def __init__(self, creds_json):
        self.client_id = creds_json['clientid']
        self.client_secret = creds_json['client_secret']
        self.redirect_url = 'http://localhost:8888/callback'
        self.scope = 'user-read-playback-state'

    def get_currently_playing_track(self):
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.client_id, client_secret=self.client_id, redirect_uri=self.redirect_url, scope=self.scope))
        current_track = sp.current_playback()
        if current_track is not None:
            track_name = current_track['item']['name']
            artist_name = current_track['item']['artists'][0]['name']
            return track_name, artist_name
        else:
            return None
