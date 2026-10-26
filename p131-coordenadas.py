# p131-coordenadas.py
# Registro de coordenadas usando tuplas

zacatecas = ("Zacatecas", 22.77, -102.58)
guadalupe = ("Guadalupe", 22.75, -102.52)

print("--- Coordenadas ---")
print("Tipo:", type(zacatecas))
print("Ciudad:", zacatecas[0])
print("Latitud:", zacatecas[1])
print("Longitud:", zacatecas[-1])

# Desempaquetado de la tupla
nombre, lat, lon = zacatecas
print(f"{nombre}: ({lat}, {lon})")

print("\n--- Recorriendo ubicaciones ---")
for lugar in (zacatecas, guadalupe):
    # lugar[1:] es un slicing que obtiene desde la posición 1 hasta el final
    print(lugar[0], "->", lugar[1:])

# Desempaquetar coordenadas para cálculo
lat1, lon1 = zacatecas[1:] # Slicing para omitir el nombre
lat2, lon2 = guadalupe[1:]

# Punto medio aproximado
centro = ((lat1 + lat2) / 2, (lon1 + lon2) / 2)
print("\nPunto medio:", centro)

# Verificar pertenencia
print("¿'Zacatecas' está en la tupla?:", "Zacatecas" in zacatecas)

# Crear otra tupla con datos extra (concatenación)
# Nota: La coma en ("ZAC",) es obligatoria para que Python lo reconozca como tupla
ampliada = zacatecas + ("ZAC",)
print("\nAmpliada:", ampliada)
print("Original:", zacatecas)