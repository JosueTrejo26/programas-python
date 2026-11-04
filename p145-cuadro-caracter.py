# p145-cuadro-caracter.py
# Dados renglones, columnas y carácter, dibuja un cuadro

def dibuja_cuadro(renglones: int, columnas: int, caracter: str) -> None:
    for r in range(renglones):
        for c in range(columnas):
            # end='' evita que se haga un salto de línea en cada carácter
            print(caracter, end='') 
        # Salto de línea al final de cada renglón
        print('') 

# Solicita al usuario los datos
renglones = int(input('Ingrese el número de renglones del cuadro: ')) 
columnas = int(input('Ingrese el número de columnas del cuadro: ')) 
caracter = input('Ingrese el carácter para dibujar el cuadro: ') 

dibuja_cuadro(renglones, columnas, caracter)

# Ejemplo de uso:
# dibuja_cuadro(4, 10, '*') 
# dibuja_cuadro(3, 5, '#')
