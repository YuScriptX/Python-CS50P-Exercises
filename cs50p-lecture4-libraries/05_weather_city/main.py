# 5️⃣ Weather checker (met sys.argv)
# Gebruik sys.argv om een stad te lezen:
# python weather.py "Brussels"
# Gebruik API:
# https://wttr.in/<city>?format=j1
# Print temperatuur + weerbeschrijving.

import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Usage: python 05_weather_city.py <city>")

city = sys.argv[1]

url = f"https://wttr.in/<city>?format=j1"

response = requests.get(url)
data = response.json()

current = data["current_condition"][0]
temperature = current["temp_C"]
description = current["weatherDesc"][0]["value"]

print(f"Weather in {city}: {temperature}°C, {description}")