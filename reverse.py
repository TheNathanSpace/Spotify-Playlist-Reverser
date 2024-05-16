import os
import re

import spotipy
from dotenv import load_dotenv
from spotipy import SpotifyOAuth

load_dotenv()


def get_playlist_tracks(spotify, playlist_uri):
    # https://stackoverflow.com/a/39113522/7492795
    results = spotify.playlist_tracks(playlist_uri)
    tracks = results['items']
    while results['next']:
        results = spotify.next(results)
        tracks.extend(results['items'])
    return tracks


if __name__ == '__main__':
    CLIENT_ID = os.environ["CLIENT_ID"]
    CLIENT_SECRET = os.environ["CLIENT_SECRET"]

    playlist_url = input("Enter playlist URL: ")
    matched = re.match(string=playlist_url, pattern=".*open\.spotify\.com\/playlist\/([^?]*)")
    playlist_uri = "spotify:playlist:"
    if matched:
        playlist_uri += matched.group(1)
    else:
        print("Error: Playlist URL not valid")
        exit(-1)

    scope = "playlist-read-private,playlist-read-collaborative,playlist-modify-private,playlist-modify-public"
    auth = SpotifyOAuth(scope=scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                        redirect_uri="http://localhost:9090")
    spotify = spotipy.Spotify(auth_manager=auth)
    playlist = spotify.playlist(playlist_uri)
    playlist_tracks = get_playlist_tracks(spotify, playlist_uri)
    playlist_tracks = [track["track"]["name"] for track in playlist_tracks]
    playlist_size = len(playlist_tracks)

    for i in range(0, playlist_size):
        spotify.playlist_reorder_items(playlist_id=playlist_uri, range_start=playlist_size - 1, insert_before=i,
                                       range_length=1)
