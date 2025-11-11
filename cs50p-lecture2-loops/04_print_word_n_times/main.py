# 4️⃣ Print een woord N keer
# Vraag de gebruiker om een woord en een getal N.
# Gebruik een for-loop om het woord N keer te printen.
# Voorbeeld:
# Input: word = "hello", N = 3
# Output:
# hello
# hello
# hello

word = input("Enter a word: ")
number = int(input("Enter a number: "))

for i in range(number):
    print(word)
