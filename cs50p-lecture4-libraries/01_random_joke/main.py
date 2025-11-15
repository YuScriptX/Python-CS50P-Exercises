# 1️⃣ Joke Fetcher
# Gebruik requests om 1 random joke op te halen via:
# https://official-joke-api.appspot.com/random_joke
# Print setup + punchline.

import requests

response = requests.get("https://official-joke-api.appspot.com/random_joke")
joke = response.json()
print(joke["setup"])
print(joke["punchline"])