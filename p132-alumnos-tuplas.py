# p131-alumnos-tuplas.py
# Registro escolar con tuplas anidadas

alumnos = (
    ("Ana", "ISC", (9, 10, 9)),
    ("Luis", "ISW", (8, 8, 9)),
    ("Mar", "ISC", (10, 9, 10)),
)

print('\033[H\033[J')
print("--- Registro escolar ---")
print("Total:", len(alumnos))

print("\n--- Promedios por alumno ---")
# Desempaquetado en el ciclo for
for nombre, carrera, notas in alumnos:
    promedio = sum(notas) / len(notas)
    print(f"{nombre} ({carrera}): {promedio:.2f}")

# Consultas específicas utilizando índices
print("\n--- Consultas específicas ---")
print("Primera persona:", alumnos[0][0])
print("Notas de Mar:", alumnos[-1][2])

# Comprensión para generar una nueva tupla con (nombre, promedio)
# Se usa un guion bajo '_' para omitir la carrera, ya que no se necesita
promedios = tuple((nombre, sum(notas) / len(notas)) for nombre, _, notas in alumnos)

print("\nPromedios consolidados:", promedios)

# Encontrar el mayor promedio usando lambda
# x[1] indica que debe evaluar el segundo elemento de cada sub-tupla (el promedio)
mejor = max(promedios, key=lambda x: x[1])
print("Mayor promedio:", mejor)

# Extraer solo los nombres
nombres = tuple(a[0] for a in alumnos)
print("Nombres registrados:", nombres)
