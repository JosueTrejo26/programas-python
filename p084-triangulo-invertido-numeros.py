# p084-triangulo-invertido-numeros.py
# Imprime un triángulo rectángulo invertido de números sucesivos.

n = int(input("Dame un número: "))

# Ciclo externo: controla el límite numérico del renglón actual.
# Va desde 'n', bajando de 1 en 1, hasta llegar a 1.
for i in range(n, 0, -1):
    
    # Ciclo interno: imprime los números desde 1 hasta el límite actual (i)
    for j in range(1, i + 1):
        print(j, end=" ")
        
    # Salto de línea al terminar el renglón
    print()