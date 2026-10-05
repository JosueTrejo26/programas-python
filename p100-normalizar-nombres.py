# p100-normalizar-nombres.py
# Limpia nombres mediante una comprensión

print('\033[H\033[J')

nombres = [' ana', 'LUIS ', '', 'maría josé', 'Pedro']

# Se aplica strip() y title(), y se filtran los que no estén vacíos
normalizados = [nombre.strip().title() for nombre in nombres if nombre.strip()]

print(f'Datos originales: {nombres}')
print(f'Nombres normalizados: {normalizados}')
