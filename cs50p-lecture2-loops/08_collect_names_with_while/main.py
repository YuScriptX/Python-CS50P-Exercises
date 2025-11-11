# 8️⃣ Namen verzamelen met while + lijst
# Maak een lege lijst names = [].
# Gebruik een while-loop:
#   - Vraag de gebruiker om een naam.
#   - Stop als de gebruiker "stop" typt (case-insensitive).
#   - Voeg elke andere naam toe aan de lijst.
# Na de loop:
#   - Print hoeveel namen er zijn met len(names).
#   - Print alle namen met een for-loop (één per lijn).

names = []

while True:
    name = str(input("Enter your name: "))

    if name.lower() == 'stop':
        break

    names.append(name)

print(f"\nYou entered {len(names)} names: ")

for n in names:
    print("-", n)