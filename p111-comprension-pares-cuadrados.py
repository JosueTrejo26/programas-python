# p111-comprension-pares-cuadrados.py
# Generación de cuadrados de números pares en un rango

n = int(input("Introduzca el límite n: "))

# Rango completo convertido a lista
lista_original = list(range(1, n + 1))

# Comprensión de listas para obtener los cuadrados de los números pares
cuadrados_pares = [x ** 2 for x in lista_original if x % 2 == 0]

print("\n--- Resultados ---")
print(f"Lista original (1 a {n}): {lista_original}")
print(f"Cuadrados de números pares: {cuadrados_pares}")
print(f"Suma de cuadrados: {sum(cuadrados_pares)}")
