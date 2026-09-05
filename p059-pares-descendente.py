# p059-pares-descendente.py
# Imprimir los números pares y su suma total en un rango descendente desde 100.

while True:
    n = int(input("Introduce un número límite (menor a 100): "))
    c = 100
    suma = 0
    salida = ""
    
    while c >= n:
        if c % 2 == 0:
            salida += str(c) + ", "
            suma += c
        c -= 1
        
    print(f"Números pares: {salida[:-2]}")
    print(f"La suma de los pares es: {suma}\n")
    
    if input("¿Desea continuar (S/N)? ").upper() == 'N':
        break