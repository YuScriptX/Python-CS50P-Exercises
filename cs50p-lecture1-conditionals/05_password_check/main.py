# 5️⃣ Password check
# Stel een wachtwoord in: secret = "python123"
# Vraag de gebruiker om het wachtwoord.
# Als het juist is → "Access granted"
# Anders → "Wrong password"

password = str(input("Enter a password: "))
secret = "python123"

if password == secret:
    print("Access granted")
else:
    print("Wrong password")