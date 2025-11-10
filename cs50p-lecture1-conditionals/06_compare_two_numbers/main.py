# 6️⃣ Compare two numbers
# Vraag twee getallen.
# Print welk getal groter is, of dat ze gelijk zijn.

number1 = int(input("Enter a number a: "))
number2 = int(input("Enter a number b: "))

if number1 > number2 and number2 < number1:
    print(number1)
elif number1 < number2 and number2 > number1:
    print(number2)
else:
    print("Numbers are the same")