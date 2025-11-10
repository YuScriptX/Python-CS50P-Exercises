# 8️⃣ Number in range
# Vraag een getal tussen 1 en 10.
# Gebruik if om te controleren of het getal in dat bereik ligt.
# Output:
# "Valid number" of "Out of range".

number = int(input("Choose a number between 1-10: "))

if number >= 1 and number <= 10:
    print("Valid number")
else:
    print("Out of range")