# 9️⃣ Public Holidays Fetcher (JSON list verwerken)
# Gebruik API:
# https://date.nager.at/api/v3/PublicHolidays/2023/BE
# Print alle Belgische feestdagen met datum + naam.

import requests

year = 2026
country_code = "BE"

url = f"https://date.nager.at/api/v3/PublicHolidays/{year}/{country_code}"

response = requests.get(url)
data = response.json()

print(f"Holidays in {country_code} for {year}:\n")

for holiday in data:
    data = holiday["date"]
    local_name = holiday["localName"]
    print(f"{data} - {local_name}")