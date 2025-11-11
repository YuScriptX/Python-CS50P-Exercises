# 7️⃣ Tel even en oneven getallen
# Maak een lijst met getallen, bv. [1, 4, 7, 10, 13, 16].
# Gebruik een for-loop om:
#   - te tellen hoeveel even getallen er zijn
#   - te tellen hoeveel oneven getallen er zijn
# Gebruik len() om het totaal aantal getallen te tonen.
# Verwachte output (voorbeeld):
# Even: 3, Odd: 3, Total: 6

numbers = [1, 4, 7, 10, 13, 16]
even_numbers = []
odd_numbers = []

for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

print(f"Even numbers:", even_numbers)
print(f"Odd numbers:", odd_numbers)
print("Total numbers:", len(numbers))