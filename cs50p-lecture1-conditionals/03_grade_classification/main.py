# 3️⃣ Grade classification
# Vraag een score van 0–100.
# Gebruik if/elif/else:
# 90–100 → A
# 80–89 → B
# 70–79 → C
# 60–69 → D
# lager dan 60 → F

score = int(input("Choose a number between 0-100: "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
