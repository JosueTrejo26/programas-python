# p158-aleatorios.py
# Genera dos listas de números aleatorios y crea una tercera lista que sea la suma de las dos primeras.
import random

def generar_numeros_aleatorios(n: int, minimo: int, maximo: int) -> list[int]:
    numeros_aleatorios = []
    for _ in range(n):
        numero = random.randint(minimo, maximo)
        numeros_aleatorios.append(numero)
    return numeros_aleatorios

def sumar_listas(lista1: list[int], lista2: list[int]) -> list[int]:
    # Precondición: ambas listas tienen la misma longitud.
    suma = []
    for a, b in zip(lista1, lista2):
        suma.append(a + b)
    return suma

# Ejemplo de uso
lista1 = generar_numeros_aleatorios(5, 1, 10)
lista2 = generar_numeros_aleatorios(5, 50, 100)
lista3 = sumar_listas(lista1, lista2)

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Suma de listas: {lista3}")
