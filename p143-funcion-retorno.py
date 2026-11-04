# p143-funcion-retorno.py
# Uso de la instrucción return para devolver valores

def suma(n1: float, n2: float) -> float:
    return n1 + n2

print('\nSuma de dos numeros constantes: ')
# se guarda el valor retornado por la función 
suma_resultado = suma(10, 20)
print(f"La suma es {suma_resultado}")

print('\nDame dos numeros separados por enter: ')
a, b = float(input()), float(input())
# se imprime directamente el valor retornado por la función
print(f"La suma de los numeros es {suma(a, b)}")
