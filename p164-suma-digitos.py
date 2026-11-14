# p153-suma-digitos.py
# Procesa una lista de números y suma los dígitos individuales de cada uno

def leer_lista_enteros() -> list[int]:
    entrada = input("Dame los números (separados por espacio): ")
    return [int(x) for x in entrada.split()]

def suma_digitos(numero: int) -> int:
    numero = abs(numero)
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma += digito
        numero //= 10
    return suma

def procesar_suma_digitos(lista: list[int]) -> list[int]:
    return [suma_digitos(num) for num in lista]

def main() -> None:
    numeros = leer_lista_enteros()
    sumas = procesar_suma_digitos(numeros)
    print(f"La lista de números original:\n{numeros}")
    print(f"La lista con las suma de dígitos de los números:\n{sumas}")

if __name__ == "__main__":
    main()