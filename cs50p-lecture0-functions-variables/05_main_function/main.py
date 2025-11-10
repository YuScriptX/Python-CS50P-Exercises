# 5️⃣ Define a main function
# Maak een functie main() die de gebruiker vraagt om een getal
# en daarna de square(n)-functie oproept om het kwadraat te tonen.
# Zorg dat het programma alleen draait als het bestand direct wordt uitgevoerd.
# Hint: gebruik if __name__ == "__main__":

def square(n):
    return n ** 2

def main():
    number = float(input("Enter a number: "))
    result = square(number)
    print(f"The square of {number} is {result}")

if __name__ == "__main__":
    main()