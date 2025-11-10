# 7️⃣ Combine two conditions (and/or)
# Vraag leeftijd en of de gebruiker een ticket heeft ("yes"/"no").
# Toegang = leeftijd >= 18 AND ticket == "yes".
# Gebruik if met 'and' om te controleren.

age = int(input("What is your age: "))
ticket = str(input("Do you have a ticket (yes/no): ")).lower()

if age >= 18 and ticket == "yes":
    print("Access to enter")
else:
    print("Don't have access to enter")