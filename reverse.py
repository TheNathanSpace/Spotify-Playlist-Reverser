import json
import os
import re
from pathlib import Path

import spotipy
from dotenv import load_dotenv
from spotipy import SpotifyClientCredentials, SpotifyOAuth

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
    matched = re.match(string=playlist_url, pattern=".*open\.spotify\.com\/playlist\/(.*)(\?(.*))?")
    playlist_uri = "spotify:playlist:"
    if matched:
        playlist_uri += matched.group(1)
    else:
        print("Error: Playlist URL not valid")
        exit(-1)

    scope = "playlist-read-private,playlist-read-collaborative,playlist-modify-private,playlist-modify-public"
    auth = SpotifyOAuth(scope=scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                        redirect_uri="http://localhost:9090")
    spotify = spotipy.Spotify(
        auth_manager=auth)
    token = auth.get_cached_token()
    print(f"Token: {token['access_token']}")
    playlist = spotify.playlist(playlist_uri)
    print(f"Start snapshot ID: {playlist['snapshot_id']}")
    playlist_tracks = get_playlist_tracks(spotify, playlist_uri)
    playlist_tracks = [track["track"]["name"] for track in playlist_tracks]
    Path("playlist.json").write_text(json.dumps(playlist_tracks, indent=4))
    playlist_size = len(playlist_tracks)

    result = spotify.playlist_reorder_items(playlist_id=playlist_uri, range_start=playlist_size - 1, insert_before=0,
                                            range_length=1, snapshot_id=playlist["snapshot_id"])
    print(f"End snapshot ID:   {result['snapshot_id']}")
    exit()

    for i in range(0, playlist_size):
        print(f"Moving {playlist_size - i} to before {0}")
        spotify.playlist_reorder_items(playlist_id=playlist_uri, range_start=playlist_size - 1, insert_before=0,
                                       range_length=1)
