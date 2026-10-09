# p104-procesar-notas.py
# Captura de calificaciones y análisis estadístico

notas = []

while True:
    try:
        nota = float(input("Introduzca nota (0 para detener): "))
        if nota == 0:
            break
        elif 0 <= nota <= 100:
            notas.append(nota)
        else:
            print("Entrada inválida, debe ser 0-100")
    except ValueError:
        print("Error: Ingrese un valor numérico.")

print("\n--- Resultados ---")
if notas:
    total_notas = len(notas)
    suma = sum(notas)
    promedio = suma / total_notas
    maxima = max(notas)
    minima = min(notas)
    
    # Filtrar notas menores al promedio usando comprensión de listas
    notas_menores = [n for n in notas if n < promedio]
    
    print(f"Total de notas introducidas: {total_notas}")
    print(f"Lista de notas: {notas}")
    print(f"Suma de notas: {suma}")
    print(f"Promedio de notas: {promedio}")
    print(f"Nota máxima: {maxima}")
    print(f"Nota mínima: {minima}")
    print(f"Notas menores al promedio ({promedio}): {len(notas_menores)}")
    print(f"Lista de notas menores al promedio: {notas_menores}")
else:
    print("No se introdujeron notas.")
    