# 4️⃣ Age category
# Vraag de leeftijd van de gebruiker.
# Gebruik if/elif/else:
# <13 → Child
# 13–19 → Teenager
# 20–64 → Adult
# >=65 → Senior

age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age <= 19:          
    print("Teenager")
elif age <= 64:          
    print("Adult")
else:                    
    print("Senior")