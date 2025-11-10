# 7️⃣ Area of a rectangle
# Maak een functie area(length, width) die de oppervlakte berekent.
# Vraag de gebruiker om lengte en breedte.
# Print daarna het resultaat.

def area(length, width):
    return length * width

length = float(input("Enter a number for length: "))
width = float(input("Enter a number for width: "))

areas = area(length, width)
print(areas)
