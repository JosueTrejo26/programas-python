# p058-impares-ascendente.py
# Imprimir los números impares y su suma total en un rango ascendente.

while True:
    n = int(input("Introduce un número límite: "))
    c = 1
    suma = 0
    salida = ""
    
    while c <= n:
        if c % 2 != 0:
            salida += str(c) + ", "
            suma += c
        c += 1
        
    # [:-2] se utiliza para quitar la última coma y espacio de la cadena de texto
    print(f"Números impares: {salida[:-2]}")
    print(f"La suma de los impares es: {suma}\n")
    
    if input("¿Desea continuar (S/N)? ").upper() == 'N':
        break