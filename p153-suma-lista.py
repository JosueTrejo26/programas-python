# p153-suma-lista.py
# Función para sumar los elementos de una lista de números
# Python 3.9+: list[...]

def suma_lista(lista: list[float]) -> float:
    suma = 0.0
    for numero in lista:
        suma += numero
    return suma

# Ejemplo de uso
numeros = [1.5, 2.3, 3.7, 4.0]
resultado = suma_lista(numeros)
print(f"La suma de la lista es: {resultado}")
# Salida esperada: La suma de la lista es: 11.5
