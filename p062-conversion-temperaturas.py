# p062-conversion-temperaturas.py
# Convertir temperaturas en grados Celsius a Fahrenheit en un rango dado.

while True:
    ti = int(input("Introduce la temperatura inicial en °C: "))
    tf = int(input("Introduce la temperatura final en °C: "))
    print("-" * 25)
    
    c = ti
    while c <= tf:
        f = (c * 9/5) + 32
        print(f"{c}°C = {f}°F")
        c += 1
    print()
    
    if input("¿Desea continuar (S/N)? ").upper() == 'N':
        break