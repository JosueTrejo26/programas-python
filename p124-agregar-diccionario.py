# p124-agregar-diccionario.py
# Muestra cómo agregar nuevos elementos a un diccionario

# 1. Crea un diccionario llamado ventas
ventas = {
    'Juan': 1550, 
    'Jose': 2600, 
    'Maria': 2220
}

# 2. Muestra el diccionario
print("Ventas iniciales:")
print(ventas)

# 3. Agrega nuevos vendedores
ventas['Rocio'] = 2500        # Agrega Rocio: 2500 (usando [])
ventas['Mateo'] = 1567        # Agrega Mateo: 1567 (usando [])
ventas.update({'Andrea': 9567}) # Agrega Andrea: 9567 (usando update())
ventas.update({'Miguel': 1234}) # Agrega Miguel: 1234 (usando update())

# 4. Muestra el diccionario actualizado
print("\nVentas actualizadas:")
print(ventas)
