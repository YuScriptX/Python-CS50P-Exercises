# 8️⃣ Random User Info
# Gebruik API:
# https://randomuser.me/api/
# Print: name, age, country, email.

import requests

response = requests.get("https://randomuser.me/api/")
data = response.json()

user = data["results"][0]

first = user["name"]["first"]
last = user["name"]["last"]
age = user["dob"]["age"]
country = user["location"]["country"]
email = user["email"]

print("Random user:")
print(f"Name   : {first} {last}")
print(f"Age    : {age}")
print(f"Country: {country}")
print(f"Email  : {email}")