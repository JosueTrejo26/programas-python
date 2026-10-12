# p118-lote-autos.py
# Crear una lista de diccionarios para representar un lote de autos

autos = [
    {'marca': 'Ford', 'modelo': 'Mustang', 'año': 1964},
    {'marca': 'VW', 'modelo': 'Jetta', 'año': 2015}
]
autos.append({'marca': 'Ford', 'modelo': 'Focus', 'año': 2000})

print('\033[H\033[J')
print('=' * 50)
print('Listado de Autos')
print('=' * 50)

print(f'\nTodos los autos: {autos} \nTotal: {len(autos)}')
print('\nCada auto dentro del lote:')
print('-' * 50)
for auto in autos:
    print(auto)

print('\nDatos en forma de Tabla:')
print('-' * 50)
# Encabezados de la tabla (usando las llaves del primer auto)
for k in autos[0].keys():
    print(f'{k:<15}', end='')
print() # Salto de línea

# Filas de la tabla (usando los valores de cada auto)
for auto in autos:
    for v in auto.values():
        print(f'{v:<15}', end='')
    print() # Salto de línea

print('\nDatos en forma de Registro')
print('-' * 50)
for auto in autos:
    for k, v in auto.items():
        print(f'{k:<12} : {v}')
    print('')

    