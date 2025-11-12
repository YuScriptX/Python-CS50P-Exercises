# 3️⃣ Try/Except met else
# Vraag de gebruiker om twee getallen en probeer ze te delen.
# Als er geen fout optreedt, print het resultaat in het "else"-blok.
# Als er een fout optreedt (zoals delen door nul), print een foutmelding.

try:
    x = int(input("Enter number 1: "))
    y = int(input("Enter number 2: "))
except ValueError:
    print("Invalid number!")
else:
    try:
        total = x / y
        print(f"Result: {total}")
    except ZeroDivisionError:
        print("Cannot divide by zero.")