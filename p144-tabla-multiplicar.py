# p144-tabla-multiplicar.py
# Dada una tabla y un límite de la tabla, imprime la tabla hasta el límite

def tabla_multiplicar(tabla: int, limite: int) -> None:
    print(f'Tabla de multiplicar del {tabla} hasta el {limite}:')
    for i in range(1, limite + 1):
        resultado = tabla * i
        print(f'{tabla} x {i} = {resultado}')
    print('')

# Solicita al usuario la tabla y el límite
tabla = int(input('Ingrese la tabla de multiplicar que desea (ej. 5): '))
limite = int(input('Ingrese el límite hasta donde desea multiplicar (ej. 10): ')) 
tabla_multiplicar(tabla, limite)

# Ejemplo de uso duro: 
# tabla_multiplicar(5, 10)
