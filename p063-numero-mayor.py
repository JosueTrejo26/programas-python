# p063-numero-mayor.py
# Leer una serie de números hasta el 0 y mostrar cuál fue el número más grande.

while True:
    print("Introduce números (0 para terminar):")
    mayor = float('-inf') # Inicializamos con el número más pequeño posible
    cuenta = 0
    
    while True:
        num = int(input("> "))
        if num == 0:
            break
            
        if cuenta == 0 or num > mayor:
            mayor = num
        cuenta += 1
        
    print("-" * 25)
    if cuenta > 0:
        print(f"El número mayor fue: {mayor}\n")
    else:
        print("No se introdujeron números válidos.\n")
        
    if input("¿Desea continuar (S/N)? ").upper() == 'N':
        break