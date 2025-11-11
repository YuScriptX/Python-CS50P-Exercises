# 5️⃣ Inputvalidatie – positief getal
# Vraag de gebruiker om een positief geheel getal.
# Blijf vragen met een while-loop tot de gebruiker een getal > 0 ingeeft.
# Print daarna: "Valid number: X".

while True:
    number = int(input("Enter a positive number: "))
    if number > 0:
        break

print(f"Valid number: {number}")