# CS50P – Lecture 4: Libraries

In deze lecture leer ik werken met verschillende externe libraries en modules in Python.  
Dit hoofdstuk focust op real-world toepassingen zoals API’s, JSON parsing, randomness en command-line arguments.

## 🧩 Onderwerpen die aan bod komen

- `import` statements  
- `requests` → API’s aanspreken  
- JSON-data verwerken (`.json()`, nested keys)  
- `random` → willekeurige waarden  
- `statistics` → gemiddelde, etc.  
- `sys.argv` → command-line arguments  
- error handling bij API calls  

---

## 📂 **Oefeningen (1 t/m 5)**

### ✔️ **1. Joke Fetcher**  
**Bestand:** `01_joke_fetcher.py`  
Haalt een willekeurige grap op via de Official Joke API en toont de setup + punchline.  
**Technieken:** requests, JSON.

---

### ✔️ **2. Random Dog Image**  
**Bestand:** `02_random_dog.py`  
Haalt een random hondenfoto op via de Dog CEO API en toont de afbeelding-URL.  
**Technieken:** API GET request, JSON parsing.

---

### ✔️ **3. Cat Fact Fetcher**  
**Bestand:** `03_cat_fact.py`  
Haalt een kattenfeit op via catfact.ninja en toont het op het scherm.  
**Technieken:** requests, dictionaries.

---

### ✔️ **4. Bitcoin Price Checker (CoinGecko)**  
**Bestand:** `04_bitcoin_price.py`  
Haalt de huidige Bitcoin-prijs in USD op via de CoinGecko API.  
**Technieken:** nested JSON, API parameters, GET request.

---

### ✔️ **5. Weather Checker (CLI Argument)**  
**Bestand:** `05_weather_city.py`  
Gebruiker geeft een stad mee via de command line.  
Het script toont de huidige temperatuur + beschrijving via wttr.in.  
**Technieken:** sys.argv, requests, nested JSON.

---

## 🧠 **Wat ik geleerd heb**

- Hoe je libraries importeert (bijv. `import requests`)  
- Werken met real-world API’s  
- JSON-data begrijpen en navigeren  
- Verschillen tussen lists & dictionaries herkennen in API’s  
- Omgaan met command-line arguments (`sys.argv`)  
- Problemen debuggen zoals `KeyError` en ongeldige API responses  

---

## ▶️ **Uitvoeren van scripts**

### Zonder argumenten:
```bash
python 01_joke_fetcher.py
