# 5️⃣ get_int function
# Schrijf een functie get_int(prompt)
# die de gebruiker vraagt om een geheel getal
# en blijft vragen tot de invoer geldig is (met try/except).
#
# Test:
# n = get_int("Enter a number: ")
# print(f"You entered {n}")

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("Enter a whole number: "))
        except ValueError:
            print("Is not a whole number!")
        else:
            break
    return x

main()