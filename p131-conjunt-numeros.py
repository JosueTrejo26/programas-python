# p131-conjunto-numeros.py
# Operaciones y comprobaciones con múltiples conjuntos de números

print('\033[H\033[J')

# 1. Crear conjuntos A, B y C a partir de las listas numéricas
lista1 = [50, 60, 70, 80, 90, 100, 200]
lista2 = [60, 90, 100, 300, 400, 500]
lista3 = [10, 20, 60, 90, 70, 100, 600, 700]

A = set(lista1)
B = set(lista2)
C = set(lista3)

print("--- Conjuntos Originales ---")
print(f"Conjunto A: {A}")
print(f"Conjunto B: {B}")
print(f"Conjunto C: {C}\n")

# 2. Calcular y mostrar los resultados de operaciones combinadas
print("--- Operaciones Matemáticas de Conjuntos ---")
print(f"Unión (A | B): {A | B}")
print(f"Unión (B | C): {B | C}")
print(f"Diferencia (A - C): {A - C}")
print(f"Diferencia Simétrica (B ^ C): {B ^ C}")
print(f"Intersección (B & C): {B & C}\n")

# 3. Verificar y mostrar el resultado de afirmaciones lógicas
print("--- Comprobaciones Lógicas ---")

# ¿Es A subconjunto de B?
print(f"¿Es A subconjunto de B?: {A.issubset(B)}")

# ¿Es C subconjunto de A?
print(f"¿Es C subconjunto de A?: {C.issubset(A)}")

# ¿Está el número 100 en A?
print(f"¿Está el número 100 en A?: {100 in A}")

# ¿Está el número 60 en A, B y C?
esta_en_todos = (60 in A) and (60 in B) and (60 in C)
print(f"¿Está el número 60 en A, B y C?: {esta_en_todos}")

# ¿No está el número 900 en C?
print(f"¿No está el número 900 en C?: {900 not in C}")
