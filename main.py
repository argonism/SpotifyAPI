import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import json

class SpotifyClient:
  def __init__(self):
    self.set_environment_variables()
    credentiials = client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials()
    scope = "user-read-currently-playing,user-read-playback-state,user-modify-playback-state"
    # self.spotify = spotipy.Spotify(client_credentials_manager=credentiials)
    self.spotify = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=scope))

  def get_track_feature(self, track_id):
    return self.spotify.audio_features(music_id)
  
  def get_track(self, track_id):
    return self.spotify.track(track_id)
  
  def get_now_playing_track(self):
    return self.spotify.current_user_playing_track()

  def set_environment_variables(self):
    with open("config.json", "r") as file:
      config = json.load(file)
      for key in config:
        os.environ[key] = config[key]

if __name__ == "__main__":
    client = SpotifyClient()
    music_id = "0LkOCCPW3vyZwdng0qvfsX"
    feature = client.get_track_feature(music_id)
    track_info = client.get_track(music_id)
    playing = client.get_now_playing_track()

    print("\n ----- feature ------")
    for k in feature[0]:
      print(f"  {k}: {feature[0][k]}")
    print("\n ----- track_info ------")
    for k in track_info:
      print(f"  {k}: {track_info[k]}")
    print("\n ----- playing ------")
    for k in playing:
      print(f"  {k}: {playing[k]}")
      