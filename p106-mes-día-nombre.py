# p106-mes-dia-nombre.py
# Mostrar el nombre del mes y sus días utilizando listas predefinidas

# Listas predefinidas de nombres y días
nombres_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
                 "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

try:
    mes = int(input("Introduzca un número de mes (1-12): "))
    if 1 <= mes <= 12:
        # El índice es mes - 1 porque las listas inician en el índice 0
        indice = mes - 1
        print("\n--- Resultados ---")
        print(f"Mes: {nombres_meses[indice]}")
        print(f"Días: {dias_meses[indice]}")
    else:
        print("Error: El número de mes debe estar entre 1 y 12.")
except ValueError:
    print("Error: Ingrese un número entero.")
    