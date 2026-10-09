# p108-ciudades.py
# Gestión y análisis de una lista de ciudades

ciudades = []

while True:
    ciudad = input("Introduzca nombre de ciudad ($ para detener): ").strip()
    if ciudad == '$':
        break
    if ciudad:
        ciudades.append(ciudad)

# Crear una copia para ordenar de forma descendente sin alterar la original
ciudades_desc = ciudades.copy()
ciudades_desc.sort(reverse=True)

# Identificar ciudades que inician con consonante
vocales = "AEIOUaeiou"
ciudades_consonante = [c for c in ciudades if c[0].isalpha() and c[0] not in vocales]

print("\n--- Resultados ---")
print(f"Total de ciudades introducidas: {len(ciudades)}")
print(f"Lista original: {ciudades}")
print(f"Lista ordenada descendente: {ciudades_desc}")
print(f"Ciudades que inician con consonante: {len(ciudades_consonante)}")
print(f"Lista de ciudades con consonante inicial: {ciudades_consonante}")
