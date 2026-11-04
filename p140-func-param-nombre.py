# p140-func-param-nombre.py
# Uso de parámetros por nombre para alterar el orden

def saluda(apaterno: str, amaterno: str, nombre: str) -> None:
    print(f'Hola {nombre} {apaterno} {amaterno}')

# Llamada posicional normal
saluda('Lopez', 'Martinez', 'Ana')

# Llamada usando los nombres de los parámetros
saluda(nombre='Ana', amaterno='Martinez', apaterno='Lopez')
