# p154-calcula-factoriales.py
# Calcula el factorial de cada número en una lista

def leer_lista_enteros() -> list[int]:
    entrada = input("Dame los números (separados por espacio): ")
    return [int(x) for x in entrada.split()]

def factorial(numero: int) -> int:
    resultado = 1
    for i in range(2, numero + 1):
        resultado *= i
    return resultado

def calcular_factoriales(lista: list[int]) -> list[int]:
    return [factorial(num) for num in lista]

def main() -> None:
    numeros = leer_lista_enteros()
    factoriales = calcular_factoriales(numeros)
    print(f"La lista de números originales: {numeros}")
    print(f"La lista con los factoriales: {factoriales}")

if __name__ == "__main__":
    main()
    