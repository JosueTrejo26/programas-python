# p102-aplanar-matriz.py
# Recorre una matriz con ciclos anidados (Comprensión)

print('\033[H\033[J')

matriz = [[4, -2, 8], [0, 5, 1], [7, 3, 6]]

# Aplanar matriz completa
valores = [numero for fila in matriz for numero in fila]

# Aplanar matriz filtrando únicamente los positivos
positivos = [numero for fila in matriz for numero in fila if numero > 0]

print(f'Matriz: {matriz}')
print(f'Lista plana: {valores}')
print(f'Valores positivos: {positivos}')
