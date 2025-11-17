CS50P – Lecture 4: Libraries

In deze lecture leer ik werken met verschillende externe libraries en modules in Python.
Dit hoofdstuk focust op real-world toepassingen zoals API’s, JSON parsing, randomness en command-line arguments.

🧩 Onderwerpen die aan bod komen

import statements

requests → API’s aanspreken

JSON-data verwerken (.json(), nested keys)

random → willekeurige waarden

statistics → gemiddelde, etc.

sys.argv → command-line arguments

error handling bij API calls

📂 Oefeningen (1 t/m 10)
✔️ 1. Joke Fetcher

Bestand: 01_joke_fetcher.py
Haalt een willekeurige grap op via de Official Joke API en toont de setup + punchline.
Technieken: requests, JSON.

✔️ 2. Random Dog Image

Bestand: 02_random_dog.py
Haalt een random hondenfoto op via de Dog CEO API en toont de afbeelding-URL.
Technieken: API GET request, JSON parsing.

✔️ 3. Cat Fact Fetcher

Bestand: 03_cat_fact.py
Haalt een kattenfeit op via catfact.ninja en toont het op het scherm.
Technieken: requests, dictionaries.

✔️ 4. Bitcoin Price Checker (CoinGecko)

Bestand: 04_bitcoin_price.py
Haalt de huidige Bitcoin-prijs in USD op via de CoinGecko API.
Technieken: nested JSON, API parameters, GET request.

✔️ 5. Weather Checker (CLI Argument)

Bestand: 05_weather_city.py
Gebruiker geeft een stad mee via de command line.
Het script toont de huidige temperatuur + beschrijving via wttr.in.
Technieken: sys.argv, requests, nested JSON.

✔️ 6. iTunes Artist Search (Top 5 Songs)

Bestand: 06_itunes_artist_search.py
Zoekt naar de top 5 nummers van een artiest via de iTunes Search API.
Technieken: query parameters, JSON lists, sys.argv.

✔️ 7. Crypto Price Checker (CoinGecko)

Bestand: 07_crypto_price.py
Leest een coin-id (bijv. bitcoin, ethereum) via de CLI en toont de prijs in USD.
Technieken: sys.argv, API parameters, JSON dictionaries.

✔️ 8. Random User Info

Bestand: 08_random_user.py
Haalt willekeurige gebruikersdata op (naam, leeftijd, land, e-mail) via randomuser.me.
Technieken: nested JSON, dictionaries, data extraction.

✔️ 9. Belgian Public Holidays

Bestand: 09_holidays.py
Toont alle Belgische feestdagen voor een jaar via de Nager.Date API.
Technieken: JSON lists, loops, data filtering.

✔️ 10. Pokémon List (First 10 Pokémon)

Bestand: 10_pokemon_list.py
Haalt de eerste tien Pokémon op via de PokeAPI en toont hun namen.
Technieken: JSON parsing, API parameters, loops, enumerate.

🧠 Wat ik geleerd heb

Hoe je libraries importeert (bijv. import requests)

Werken met real-world API’s

JSON-data begrijpen, navigeren en fouten voorkomen

Verschillen herkennen tussen lists & dictionaries

Omgaan met command-line arguments (sys.argv)

Robust scripts bouwen (checking arguments, validatie)

Praktisch werken met nested JSON-structuren

Debuggen van API errors zoals KeyError, TypeError en response-fouten

▶️ Uitvoeren van scripts
Zonder argumenten:
python 01_joke_fetcher.py
python 02_random_dog.py
python 03_cat_fact.py
python 04_bitcoin_price.py
python 08_random_user.py
python 09_holidays.py
python 10_pokemon_list.py

Met command-line argumenten:
python 05_weather_city.py Brussels
python 06_itunes_artist_search.py eminem
python 07_crypto_price.py bitcoin