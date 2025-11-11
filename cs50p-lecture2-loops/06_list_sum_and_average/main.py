# 6️⃣ Lijst van getallen – som en gemiddelde
# Maak een lijst met getallen, bv. [10, 20, 30, 40, 50].
# Gebruik een for-loop om:
#   - de som te berekenen (zonder sum())
#   - het gemiddelde te berekenen met som / len(lijst)
# Print de lijst, de som en het gemiddelde.

numbers = [10, 20, 30, 40, 50]
total = 0

for n in numbers:
    total += n

average = total / len(numbers)

print("Numbers:", numbers)
print(f"Sum = {total}")
print(f"Average = {average}")