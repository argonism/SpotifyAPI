import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import json

class SpotifyClient:
  def __init__(self, cache_path=None):
    self.set_environment_variables()
    if cache_path:
      oauth = SpotifyOAuth(cache_path=cache_path)
      self.spotify = spotipy.Spotify(auth_manager=oauth, requests_timeout=10)
    else:
      scope = "user-read-currently-playing,user-read-playback-state,user-modify-playback-state"
      self.spotify = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=scope), requests_timeout=10)

  def get_track_feature(self, track_id):
    return self.spotify.audio_features(music_id)
  
  def get_track(self, track_id):
    return self.spotify.track(track_id)
  
  def currently_playing(self):
    return self.spotify.currently_playing("JP")

  def get_now_playing_track(self):
    return self.spotify.current_user_playing_track()

  def current_track_id(self):
    return self.spotify.current_user_playing_track()

  def now_playing_feature(self):
    return self.get_track_feature(self.current_track_id())

  def track_analysis(self, track_id):
    return self.spotify.audio_analysis(track_id)

  def set_environment_variables(self):
    with open("config.json", "r") as file:
      config = json.load(file)
      for key in config:
        os.environ[key] = config[key]

if __name__ == "__main__":
    client = SpotifyClient()
    playing = client.get_now_playing_track()
    if not playing: 
      print("No track playing now")
      exit()
    playing = playing["item"]
    track_id = playing["id"]
    print("track_id:", track_id)
    print("track_id:", playing["name"])
    print("\n ----- playing ------")
    for k in playing:
      print(f"  {k}: {playing[k]}")

    analysis = client.track_analysis(track_id)["beats"]

    print("\n ----- analysis ------")
    print(analysis)