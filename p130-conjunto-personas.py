# p130-conjunto-personas.py
# Operaciones y comprobaciones lógicas con conjuntos de nombres

print('\033[H\033[J')

# 1. Crear conjuntos A y B a partir de las listas dadas
lista1 = ["Juan", "Maria", "Pedro", "Jose", "Rocio"]
lista2 = ["Pedro", "Juan", "Pablo", "Mateo", "Esther"]

A = set(lista1)
B = set(lista2)

print("--- Conjuntos Originales ---")
print(f"Conjunto A: {A}")
print(f"Conjunto B: {B}\n")

# 2. Calcular y mostrar los resultados de las operaciones
print("--- Operaciones Matemáticas de Conjuntos ---")
print(f"Unión (A | B): {A | B}")
print(f"Intersección (A & B): {A & B}")
print(f"Diferencia (A - B): {A - B}")
print(f"Diferencia Simétrica (A ^ B): {A ^ B}\n")

# 3. Verificar y mostrar el resultado (Verdadero/Falso) de afirmaciones
print("--- Comprobaciones Lógicas ---")

# ¿Es {Pablo, Mateo} un subconjunto de B?
es_subconjunto = {"Pablo", "Mateo"}.issubset(B)
print(f"¿Es {{'Pablo', 'Mateo'}} un subconjunto de B?: {es_subconjunto}")

# ¿Es A un superconjunto de {Reynaldo, Angelica}?
es_superconjunto = A.issuperset({"Reynaldo", "Angelica"})
print(f"¿Es A un superconjunto de {{'Reynaldo', 'Angelica'}}?: {es_superconjunto}")

# ¿Está "Pedro" en el conjunto A?
esta_pedro = "Pedro" in A
print(f"¿Está 'Pedro' en el conjunto A?: {esta_pedro}")

# ¿No está "Lilia" en el conjunto B?
no_esta_lilia = "Lilia" not in B
print(f"¿No está 'Lilia' en el conjunto B?: {no_esta_lilia}")
