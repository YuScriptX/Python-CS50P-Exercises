# 1️⃣ Check even or odd
# Vraag een getal aan de gebruiker.
# Controleer met if of het even of oneven is.
# Gebruik modulo (%).
# Voorbeeld:
# Input: 7 → Output: Odd

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Oneven")