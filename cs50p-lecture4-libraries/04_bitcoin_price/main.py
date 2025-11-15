# 4️⃣ Bitcoin prijs (simple)
# Haal de huidige Bitcoin prijs op van:
# https://api.coindesk.com/v1/bpi/currentprice.json
# Print de prijs in USD.

import requests

response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
data = response.json()
price = data["bitcoin"]["usd"]
print("Bitcoin price in USD:", price)
