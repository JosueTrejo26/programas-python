# p139-funcion-parametros.py
# Función con múltiples parámetros posicionales

def saluda(apaterno: str, nombre: str) -> None: 
    print(f'Hola {nombre} {apaterno}')

saluda('Perez', 'Juan')

# saluda('Juan') # Genera error (pocos parámetros)
# saluda('Pérez', 'Juan', 'Extra') # Error: demasiados argumentos
