# 4️⃣ Reprompt until valid number
# Gebruik een while-loop met try/except.
# Blijf de gebruiker vragen om een geldig geheel getal (int).
# Als de invoer geldig is, breek uit de loop en print het getal.
#
# Voorbeeld:
# Input: "abc" → "Invalid input, try again."
# Input: "5" → "You entered 5"

while True:
    try:
        x = int(input("Enter a whole number: "))
    except ValueError:
        print("Is not a whole number!")
    else:
        break

print(f"x is {x}")