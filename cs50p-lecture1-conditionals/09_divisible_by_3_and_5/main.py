# 9️⃣ Divisible by both 3 and 5
# Vraag een getal.
# Controleer of het deelbaar is door zowel 3 als 5.
# Hint: gebruik modulo (%) en 'and'.

number = int(input("Choose a number: "))

if number % 3 == 0 and number % 5 == 0:
    print("Okey")
else:
    print("Not okey")