# p134-alumnos-tuplas.py
# Gestión de registros escolares modelados como tuplas anidadas

print('\033[H\033[J')

# 1. Crear y mostrar la tupla externa con los tres registros escolares
alumnos = (
    ("Ana", "ISC", (9, 10, 9, 8)),
    ("Luis", "ISW", (8, 8, 9, 10)),
    ("Mar", "ISC", (10, 9, 10, 10))
)

print(f"Registros de alumnos: {alumnos}")
print(f"Total de alumnos: {len(alumnos)}\n")

pares_nombre_promedio = []
mejor_promedio = 0
mejor_alumno = ""

# 2. Recorrer los registros mediante desempaquetado y mostrar el promedio
for nombre, carrera, calificaciones in alumnos:
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"Nombre: {nombre}, Carrera: {carrera}, Promedio: {promedio:.2f}")
    
    # Acumular los pares en una lista temporal para construir la tupla más adelante
    pares_nombre_promedio.append((nombre, promedio))
    
    # Lógica para identificar el promedio más alto
    if promedio > mejor_promedio:
        mejor_promedio = promedio
        mejor_alumno = nombre

# 3. Construir y mostrar una nueva tupla con pares (nombre, promedio)
tupla_pares = tuple(pares_nombre_promedio)
print(f"\nPares (nombre, promedio): {tupla_pares}")
print(f"Alumno con mejor promedio: {mejor_alumno} con {mejor_promedio}\n")

# 4. Consultar calificaciones usando índices de tuplas anidadas (count e index)
# Accedemos manualmente vía índices para la demostración i.e., alumnos[i][2] son las calificaciones
for i in range(len(alumnos)):
    nombre_actual = alumnos[i][0]
    calificaciones_actual = alumnos[i][2]
    
    conteo_dieces = calificaciones_actual.count(10)
    # Obtenemos el índice de la primera calificación que sacó
    indice_primera = calificaciones_actual.index(calificaciones_actual[0]) 
    
    print(f"{nombre_actual} -> Conteo de 10s: {conteo_dieces}, Índice de primera calificación: {indice_primera}")

# 5. Ordenar los pares (nombre, promedio) de menor a mayor usando sorted()
# Se usa lambda x: x[1] para indicar que debe ordenar tomando en cuenta el valor del promedio (posición 1 del par)
ordenados_por_prom = tuple(sorted(tupla_pares, key=lambda x: x[1]))

print(f"\nOrdenados por promedio: {ordenados_por_prom}")
print(f"Tupla original intacta: {alumnos}")

# 6. Formar y mostrar una tupla nueva con los datos de "Eva"
eva = ("Eva", "ISC", (9, 9, 10))
alumnos_actualizados = alumnos + (eva,)

print(f"\nNueva tupla con Eva: {alumnos_actualizados}")

