# p092-procesar-calificaciones.py
# Procesa calificaciones en una lista

print('\033[H\033[J')
print('Procesador de calificaciones de un curso\n')
print("Introduce calificaciones entre 0 y 10 (usa 99 para terminar):\n")

calificaciones = []
suma = 0.0

while True:
    try:
        n = float(input("Calificación > "))
        if n == 99:
            break
        if 0 <= n <= 10:
            calificaciones.append(n)
            suma += n
        else:
            print("Error: la calificación debe estar entre 0 y 10.")
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número.")

if not calificaciones:
    print("No se ingresaron calificaciones.")
else:
    promedio = suma / len(calificaciones)
    calif_max = max(calificaciones)
    calif_min = min(calificaciones)
    
    superan_promedio = 0
    for calif in calificaciones:
        if calif > promedio:
            superan_promedio += 1

    print("\n--- Resumen Estadístico ---")
    print(f"Calificaciones: {calificaciones}")
    print(f"Suma total: {suma:.2f}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Calificación más alta: {calif_max}")
    print(f"Calificación más baja: {calif_min}")
    print(f"Alumnos que superaron el promedio: {superan_promedio}")
    