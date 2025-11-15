# 2️⃣ Dog Picture Downloader
# Gebruik requests om een random dog image URL op te halen via:
# https://dog.ceo/api/breeds/image/random
# Print de image URL.

import requests

response = requests.get("https://dog.ceo/api/breeds/image/random")
data = response.json()
print(data["message"])