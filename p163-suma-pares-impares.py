# p152-suma-pares-impares.py
# Suma números pares o impares dentro de un rango especificado

def suma_pares_impares(inicio: int, fin: int, tipo: str) -> int:
    suma = 0
    for numero in range(inicio, fin + 1):
        if tipo == 'P' and numero % 2 == 0:
            suma += numero
        elif tipo == 'I' and numero % 2 != 0:
            suma += numero
    return suma

def main() -> None:
    print("***")
    print("Suma en Rango")
    print("***")
    inicio = int(input("Introduce el número inicial: "))
    fin = int(input("Introduce el número final: "))
    tipo = input("¿Qué deseas sumar? (P) ares o (I) mpares: ").strip().upper()
    
    resultado = suma_pares_impares(inicio, fin, tipo)
    if tipo == 'P':
        print(f"La suma de los números pares entre {inicio} y {fin} es: {resultado}")
    elif tipo == 'I':
        print(f"La suma de los números impares entre {inicio} y {fin} es: {resultado}")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
    