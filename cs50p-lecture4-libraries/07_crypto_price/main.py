# 7️⃣ Crypto Price Checker (sys.argv + try/except)
# Gebruik API:
# https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd
# Toon prijs van crypto die in sys.argv staat:
# python crypto.py bitcoin

import sys
import requests

if len(sys.argv)  != 2:
    sys.exit("Usage: python 07_crypto_price.py <coin-id>\nExample: python 07_crypto_price.py bitcoin")

coin_id = sys.argv[1].lower()

url = "https://api.coingecko.com/api/v3/simple/price"
params = {
    "ids": coin_id,
    "vs_currencies": "usd"
}

response = requests.get(url, params=params)
data = response.json()

if coin_id not in data:
    print(f"Coin '{coin_id}' not found. Check the id on CoinGecko. ")
else:
    price = data[coin_id]["usd"]
    print(f"Current {coin_id} price in USD: {price}")