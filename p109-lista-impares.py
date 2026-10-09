# p109-lista-impares.py
# Generación de lista de impares y análisis de divisibilidad

n = int(input("Introduzca la cantidad de números impares (n): "))

# Llenar la lista con los primeros n números impares
impares = [2 * i + 1 for i in range(n)]

print("\n--- Generación de Lista ---")
print(f"Lista de los primeros {n} números impares: {impares}")

# Cálculos generales
suma = sum(impares)
promedio = suma / n if n > 0 else 0

print("\n--- Cálculos ---")
print(f"Suma de los números: {suma}")
print(f"Promedio de los números: {promedio}")

# Divisibles entre 3
divisibles_3 = [num for num in impares if num % 3 == 0]
suma_div3 = sum(divisibles_3)

print("\n--- Divisibles entre 3 ---")
print(f"Números divisibles entre 3: {divisibles_3}")
print(f"Suma de los números divisibles entre 3: {suma_div3}")

# Búsqueda
print("\n--- Búsqueda ---")
buscar = int(input("Introduzca elemento a buscar: "))
if buscar in impares:
    indice = impares.index(buscar)
    print(f"Resultado: El elemento {buscar} está en la lista en la posición (índice) {indice}.")
else:
    print(f"Resultado: El elemento {buscar} no se encuentra en la lista.")
    