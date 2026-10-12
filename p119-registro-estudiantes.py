# p119-registro-estudiantes.py
# Crear una lista de diccionarios para representar un registro de estudiantes

grupo = [
    {'nombre': 'Carlos', 'edad': 45, 'carrera': 'Sistemas', 'promedio': 9.0},
    {'nombre': 'Rocio', 'edad': 35, 'carrera': 'Sistemas', 'promedio': 10.0}
]

print('\033[H\033[J')
print('Registro de Estudiantes\n')
print(f"Grupo de estudiantes inicial:\n{'-'*60}\n{grupo}\nTotal: {len(grupo)}")

print('\nCaptura de nuevos estudiantes')
print('-' * 60)

while True:
    print(f'\nDatos Estudiante:')
    datos = {}
    nombre = input('¿Nombre? (deja vacío para terminar): ')
    if nombre != '':
        datos['nombre'] = nombre
        datos['edad'] = int(input('¿Edad? '))
        datos['carrera'] = input('¿Carrera? ')
        datos['promedio'] = float(input('¿Promedio? '))
        grupo.append(datos)
    else:
        break

print(f"\nGrupo de estudiantes completo:\n{'-'*60}\n{grupo}\nTotal: {len(grupo)}")

print('\nDatos en forma de Tabla:')
print('-' * 60)
for k in grupo[0].keys():
    print(f'{k:<15}', end='')
print()

for alumno in grupo:
    for v in alumno.values():
        print(f'{v:<15}', end='')
    print()

print('\nDatos en forma de Registro y Cálculo de Promedios:')
print('-' * 60)
s = 0
for est in grupo:
    s += est['promedio']
    for k, v in est.items():
        print(f'{k:<10} : {v}')
    print('')

print('\nCálculo de Promedios Generales:')
print('-' * 60)
p = s / len(grupo) if len(grupo) > 0 else 0
print(f'La suma total de promedios es {s}')
print(f'El promedio general del grupo es {p:.2f}')

