from spotipy.oauth2 import SpotifyOAuth
import spotipy
from bs4 import BeautifulSoup
import requests

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")


# response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
response = requests.get("https://www.billboard.com/charts/india-songs-hotw/" + date)


soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

print(song_names)


# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="7bc23d01550a4cefa1e7271b4ceaf94a",
#                                                client_secret="161b21e828644b0a8c6959ffbf0cd6e5",
#                                                redirect_uri="http://example.com",
#                                                scope="playlist-modify-private",
#                                                show_dialog=True,
#                                                cache_path="token.txt",
#                                                username="31sls3ffj7kzbqh5im52g5ke4fxe"))

# # sp = spotipy.Spotify(auth_manager=)

# user_id = sp.current_user()["id"]
# # print(song_names[1])
# result = sp.search(q=song_names[1], type="track", limit=1)

# # print(type(result))
# print(result["tracks"].get("items"))

# print(result["tracks"]["items"][0]["uri"])

# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])
