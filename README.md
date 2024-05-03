# Spotify Playlist Reverser

A simple Python script to reverse the order of a Spotify playlist, without removing/re-adding songs. This way, the
associated metadata (when the song was added, and by who) remains.

## Installation

1. Clone/download the repo.
2. Install Python dependencies: `pip install -r requirements.txt`
3. Create a Spotify developer app with redirect URI `http://localhost:9090`.
4. Create a `.env` file on the same level as `reverse.py` with the contents (from the created Spotify app):

```properties
CLIENT_ID=a97ga979874a29498h298h4aah2
CLIENT_SECRET=af98h8498428h2aha48h
```
## Usage

`python reverse.py`

It will open a Spotify webpage for you to sign in, granting the app access to edit your playlists.

It will then prompt you for a playlist URL, for example: `https://open.spotify.com/playlist/3lz19sJjvc4US5UjyfS4fJ`

## License

Licensed under GPLv3 to the fullest extent possible.