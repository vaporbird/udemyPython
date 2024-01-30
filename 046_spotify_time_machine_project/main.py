import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
from format_date import FormatDate
import os

date = FormatDate.input_and_return_formated()

bilboard_url = f"https://www.billboard.com/charts/hot-100/{date}"
website = requests.get(bilboard_url).text

soup = BeautifulSoup(website, features="lxml", parser="html.parser")
filtered_html = soup.select("li h3.c-title")
songs = []

for song in filtered_html:
    songs.append(song.text.strip())

#####################################################################################################

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=os.environ.get("SPOTIPY_REDIRECT_URI"),
        client_id=os.environ.get("SPOTIPY_CLIENT.ID"),
        client_secret=os.environ.get("SPOTIPY_CLIENT_SECRET"),
        show_dialog=True,
        cache_path="token.txt",
        username=os.environ.get("SPOTIPY_USERNAME"), 
    )
)
user_id = sp.current_user()["id"]
songs_uri = []
for song in songs:
    try:
        track = sp.search(q=song, type="track", limit=1)
        songs_uri.append(track["tracks"]["items"][0]["external_urls"]["spotify"])
    except IndexError:
        continue

###################################################################################################
#this has to have public=False for some reason
new_playlist = sp.user_playlist_create(user=sp.current_user()["id"], name=f"{date} Billboard top 100", description="bilboard's top 100 songs of a date", public="False")
playlist_id = new_playlist["id"]

sp.playlist_add_items(playlist_id=playlist_id, items=songs_uri)
