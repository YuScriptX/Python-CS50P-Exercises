# 🔟 Fetch 10 Pokémon names
# Gebruik API:
# https://pokeapi.co/api/v2/pokemon?limit=10
# Print alle Pokémon namen.

import requests

url = "https://pokeapi.co/api/v2/pokemon"
params = {
    "limit": 10   
}

response = requests.get(url, params=params)
data = response.json()

results = data["results"]  

print("First 10 Pokémon:\n")

for i, pokemon in enumerate(results, start=1):
    name = pokemon["name"].capitalize()
    print(f"{i}. {name}")
