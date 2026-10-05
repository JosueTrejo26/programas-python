# p098-cuadrados-lista.py
# Genera cuadrados usando una comprensión

print('\033[H\033[J')
print('Cuadrados de números\n')

n = int(input('¿Hasta qué número? '))
numeros = list(range(1, n + 1))

# Comprensión de lista para calcular los cuadrados
cuadrados = [numero ** 2 for numero in numeros]

print(f'Números: {numeros}')
print(f'Cuadrados: {cuadrados}')
