# 3️⃣ Cat Fact Fetcher
# Haal één willekeurige cat fact op van:
# https://catfact.ninja/fact
# Print alleen de fact.

import requests

response = requests.get("https://catfact.ninja/fact")
data = response.json()
print(data["fact"])