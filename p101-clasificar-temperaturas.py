# p101-clasificar-temperaturas.py
# Clasifica datos con una expresión condicional

print('\033[H\033[J')

temperaturas = [8, 14, 18, 22, 27, 35]

# Comprensión con if-else anidado para múltiples condiciones
clasificacion = [
    'Fría' if t < 15 else
    'Templada' if t <= 25 else
    'Caliente'
    for t in temperaturas
]

print(f'Temperaturas: {temperaturas}')
print(f'Clasificación: {clasificacion}')
