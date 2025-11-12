# 2️⃣ Prevent NameError
# Probeer een variabele te gebruiken die niet bestaat.
# Gebruik try/except om de fout "NameError" op te vangen.
# Print "Variable not defined" als het gebeurt.

try:
    x = int(input("Enter a number: "))
except ValueError:
    print("That's not a number!")
    x = None  

if x is not None:
    print(f"You entered: {x}")