# p110-comprension-filtra-palabras.py
# Filtro de palabras por longitud usando comprensión de listas

entrada = input("Introduzca palabras separadas por espacios: ")
# Separar la cadena en una lista
palabras = entrada.split()

# Comprensión de lista para filtrar palabras > 4 caracteres y volverlas mayúsculas
filtradas = [p.upper() for p in palabras if len(p) > 4]

print("\n--- Resultados ---")
print(f"Lista original: {palabras}")
print(f"Lista filtrada (>4 caracteres en mayúsculas): {filtradas}")
