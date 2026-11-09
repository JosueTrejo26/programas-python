# p156-mayores-promedio.py
# Función para obtener los números mayores al promedio de una lista

def promedio_lista(lista: list[float]) -> float:
    suma = 0.0
    if not lista:
        return 0.0
    for numero in lista:
        suma += numero
    return suma / len(lista)

def mayores_al_promedio(lista: list[float]) -> list[float]:
    prom = promedio_lista(lista)
    mayores = []
    for numero in lista:
        if numero > prom:
            mayores.append(numero)
    return mayores

# Ejemplo de uso
numeros = [1.5, 2.3, 3.7, 4.0, 5.5]
resultado = mayores_al_promedio(numeros)
print(f"Números mayores al promedio: {resultado}")
# Salida esperada: Números mayores al promedio: [4.0, 5.5]
