# 4️⃣ Square function
# Maak een functie square(n) die het kwadraat van n teruggeeft.
# Test de functie met een paar getallen.

def square(n):
    return n ** 2

number = int(input("Enter a number: "))
squared = square(number)
print(f"{number} is {squared}")