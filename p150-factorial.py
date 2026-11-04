# p150-factorial.py
# Dado un número entero calcular su factorial

def factorial(numero: int) -> int:
    resultado = 1
    for i in range(2, numero + 1): 
        resultado *= i
    return resultado

def main() -> None:
    numero = int(input("Introduce un número entero para calcular su factorial: ")) 
    if numero < 0:
        print("El factorial no está definido para números negativos.") 
        return
    
    resultado = factorial(numero)
    print(f"El factorial de {numero} es {resultado}")

if __name__ == "__main__":
    main()
    