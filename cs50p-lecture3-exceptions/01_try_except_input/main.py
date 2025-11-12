# 1️⃣ Handle invalid input (Try/Except)
# Vraag de gebruiker om een getal.
# Gebruik try/except om ValueError op te vangen als de gebruiker tekst invoert.
# Voorbeeld:
# Input: "ten" → Output: "That's not a number!"
# Input: "5" → Output: "You entered: 5"

try:
    x = int(input("Enter a number: "))
    print(f"You entered:{x} ")
except ValueError:
    print("That's not a number!")