# 6️⃣ Use pass in except
# Exercise 6: Using pass
# Schrijf een programma dat een lijst van strings heeft, bv. ["10", "hello", "20", "x"]
# Probeer elk element om te zetten naar een int.
# Gebruik try/except en 'pass' om foutieve waarden over te slaan.
# Print de geldige getallen in een lijst.


def main():
    items = ["10", "hello", "20", "x"]
    valid_numbers = []

    for item in items:
        try:
            number = int(item)
            valid_numbers.append(number)
        except ValueError:
            pass  

    print("Valid numbers:", valid_numbers)

main()