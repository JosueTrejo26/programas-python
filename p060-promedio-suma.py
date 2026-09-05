# p060-promedio-suma.py
# Leer números introducidos por el usuario hasta que ingrese un 0 para calcular promedio.

while True:
    print("Introduce números (0 para terminar):")
    suma = 0
    cuenta = 0
    
    while True:
        num = float(input("> "))
        if num == 0:
            break
        suma += num
        cuenta += 1
        
    print("-" * 25)
    print(f"Se introdujeron {cuenta} números.")
    print(f"La suma es: {suma}")
    
    # Evitamos la división por cero si el primer número fue 0
    if cuenta > 0:
        print(f"El promedio es: {suma / cuenta}")
    else:
        print("El promedio es: 0")
    print()
    
    if input("¿Desea continuar (S/N)? ").upper() == 'N':
        break