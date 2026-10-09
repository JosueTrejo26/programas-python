# p107-listas-aleatorios-suma.py
# Suma de listas condicionada a que ambos elementos sean impares

import random

# Generar 2 listas de 10 números aleatorios (ej. de 1 a 20)
lista_a = [random.randint(1, 20) for _ in range(10)]
lista_b = [random.randint(1, 20) for _ in range(10)]
lista_c = []

for i in range(10):
    # Verificar si ambos elementos son impares
    if lista_a[i] % 2 != 0 and lista_b[i] % 2 != 0:
        lista_c.append(lista_a[i] + lista_b[i])
    else:
        lista_c.append(0)

print("\n--- Listas Generadas ---")
print(f"Lista A: {lista_a}")
print(f"Lista B: {lista_b}")
print("\n--- Resultados (Suma solo si A[i] y B[i] son impares) ---")
print(f"Lista C: {lista_c}")
