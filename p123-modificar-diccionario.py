# p123-modificar-diccionario.py
# Demuestra cómo modificar los valores existentes en un diccionario

# 1. Crea un diccionario llamado paises
paises = {
    'Argentina': 100, 
    'Brasil': 200,
    'Colombia': 300, 
    'Chile': 400, 
    'Ecuador': 500, 
    'Bolivia': 600, 
    'Jamaica': 700
}

# 2. Muestra el diccionario inicial
print("Diccionario inicial:")
print(paises)

# 3. Modifica los valores
paises['Brasil'] = 250        # Cambia el valor de Brasil a 250 (usando [])
paises['Chile'] = 450         # Cambia el valor de Chile a 450 (usando [])
paises.update({'Bolivia': 650}) # Cambia el valor de Bolivia a 650 (usando update())
paises.update({'Jamaica': 750}) # Cambia el valor de Jamaica a 750 (usando update())

# 4. Muestra el diccionario modificado
print("\nDiccionario modificado:")
print(paises)
