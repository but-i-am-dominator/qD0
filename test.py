import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Replace these with your actual Spotify API credentials
SPOTIPY_CLIENT_ID = '75b18f85db7e41f3a23036f800ed962e'
SPOTIPY_CLIENT_SECRET = '3dec5f3af4ed458eadd4b6743b1514de'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'

scope = 'user-read-playback-state'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope))

def get_currently_playing_track():
    current_track = sp.current_playback()
    if current_track is not None:
        track_name = current_track['item']['name']
        artist_name = current_track['item']['artists'][0]['name']
        return f"Currently playing: {track_name} by {artist_name}"
    else:
        return "No track currently playing."

# Example usage
if __name__ == "__main__":
    print(get_currently_playing_track())