# Spotify Playlist Reverser

A simple Python script to reverse the order of a Spotify playlist, without removing/re-adding songs. This way, the
associated metadata (when the song was added, and by who) remains.

## Installation

Clone/download the repo.

Install Python dependencies: `pip install -r requirements.txt`

The main dependency is `spotipy==2.23.0` so you could also probably just do that.

## Usage

`python reverse.py`

It will open a Spotify webpage for you to sign in, granting the app access to edit your playlists.

It will then prompt you for a playlist URL, for example: `https://open.spotify.com/playlist/3lz19sJjvc4US5UjyfS4fJ`

## License

Licensed under GPLv3 to the fullest extent possible.