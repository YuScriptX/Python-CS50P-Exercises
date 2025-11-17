# 6️⃣ Spotify Artist Search (zonder token via iTunes API)
# Gebruik:
# https://itunes.apple.com/search?term=<artist>&entity=song&limit=5
# Vraag de gebruiker een artiest via input of sys.argv.
# Print de song names.

import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Usage: python 06_itunes_artist_search.py <artist>")

artist = sys.argv[1]

url = "https://itunes.apple.com/search"
params = {
    "term": artist,
    "entity": "song",
    "limit": 5
}

response = requests.get(url, params=params)
data = response.json()

results = data["results"]

if not results:
    print(f"No songs found for '{artist}'.")
else:
    print(f"Top {len(results)} songs for '{artist}':\n")
    for i, track in enumerate(results, start=1):
        title = track.get("trackName", "Unknown title")
        album = track.get("collectionName", "Unknown album")
        print(f"{i}. {title} - {album}")