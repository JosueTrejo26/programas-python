# p133-coordenadas-tuplas.py
# Representación y manipulación de coordenadas geográficas usando tuplas

print('\033[H\033[J')

# 1. Crear y mostrar las tuplas de Zacatecas y Guadalupe con sus coordenadas
zacatecas = ('Zacatecas', 22.77, -102.58)
guadalupe = ('Guadalupe', 22.75, -102.52)

print(f"Tupla Zacatecas: {zacatecas}, Tipo: {type(zacatecas)}")
print(f"Tupla Guadalupe: {guadalupe}, Tipo: {type(guadalupe)}")

# 2. Consultar nombre, latitud y longitud usando índices positivos y negativos
print("\nAcceso por índices (Zacatecas):")
print(f"Positivos -> Nombre: {zacatecas[0]}, Latitud: {zacatecas[1]}, Longitud: {zacatecas[2]}")
print(f"Negativos -> Nombre: {zacatecas[-3]}, Latitud: {zacatecas[-2]}, Longitud: {zacatecas[-1]}")

# 3. Desempaquetar cada tupla en variables e imprimir las coordenadas
nombre_z, lat_z, lon_z = zacatecas
nombre_g, lat_g, lon_g = guadalupe

print(f"\n{nombre_z}: ({lat_z}, {lon_z})")
print(f"{nombre_g}: ({lat_g}, {lon_g})")

# 4. Recorrer ambas ubicaciones con un ciclo y mostrar nombre y tupla obtenida con slicing
print()
ubicaciones = (zacatecas, guadalupe)
for ubi in ubicaciones:
    # ubi[0] extrae el nombre, ubi[1:] crea una nueva tupla recortada con las coordenadas
    print(f"Ubicación: {ubi[0]}, Coordenadas: {ubi[1:]}")

# 5. Calcular e imprimir el punto medio aproximado
lat_medio = (lat_z + lat_g) / 2
lon_medio = (lon_z + lon_g) / 2
print(f"\nPunto medio aproximado: ({lat_medio:.2f}, {lon_medio:.2f})")

# 6. Crear una nueva tupla para Zacatecas que incluya el código "ZAC"
# Se concatena la tupla original con una nueva tupla que contiene un solo elemento ('ZAC',)
zacatecas_nueva = zacatecas + ('ZAC',)
print(f"\nNueva tupla Zacatecas: {zacatecas_nueva}")
print(f"Original sin cambios: {zacatecas}")

# 7. Verificar pertenencia
pertenece = 'Zacatecas' in zacatecas
print(f"\n'Zacatecas' pertenece a la tupla: {pertenece}")

# Nota: Intentar modificar un elemento directamente arroja TypeError (las tuplas son inmutables).
# Si intentáramos hacer: zacatecas[1] = 23.00, el programa colapsaría con un TypeError.
