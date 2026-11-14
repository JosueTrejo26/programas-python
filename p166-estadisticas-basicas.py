# p155-estadisticas-basicas.py
# Calcula estadísticas básicas (poblacionales) para una lista de números

def leer_lista_enteros() -> list[int]:
    entrada = input("Dame números (separados por espacio): ")
    return [int(x) for x in entrada.split()]

def numero_mayor(lista: list[int]) -> int:
    mayor = lista[0]
    for num in lista:
        if num > mayor:
            mayor = num
    return mayor

def numero_menor(lista: list[int]) -> int:
    menor = lista[0]
    for num in lista:
        if num < menor:
            menor = num
    return menor

def media(lista: list[int]) -> float:
    suma = 0
    for num in lista:
        suma += num
    return suma / len(lista)

def varianza_poblacional(lista: list[int]) -> float:
    m = media(lista)
    suma_cuadrados = 0
    for num in lista:
        suma_cuadrados += (num - m) ** 2
    return suma_cuadrados / len(lista)

def desviacion_estandar_poblacional(lista: list[int]) -> float:
    return varianza_poblacional(lista) ** 0.5

def main() -> None:
    numeros = leer_lista_enteros()
    if not numeros:
        print("No se ingresaron números.")
        return
        
    m = media(numeros)
    mayor_val = numero_mayor(numeros)
    menor_val = numero_menor(numeros)
    var_val = varianza_poblacional(numeros)
    desv_val = desviacion_estandar_poblacional(numeros)
    
    print(f"Lista de números: {numeros}")
    print("Estadísticas:")
    print(f"Media              : {m}")
    print(f"Mayor              : {mayor_val}")
    print(f"Menor              : {menor_val}")
    print(f"Varianza           : {var_val:.3f}")
    print(f"Desviación estándar: {desv_val:.3f}")

if __name__ == "__main__":
    main()
    