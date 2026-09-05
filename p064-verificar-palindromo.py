# p064-verificar-palindromo.py
# Determinar si un número entero es un palíndromo invirtiéndolo matemáticamente.

while True:
    num = int(input("Introduce un número para verificar si es palíndromo: "))
    original = num
    inverso = 0
    temp = num
    
    # Invertimos el número utilizando operaciones matemáticas dentro del while
    while temp > 0:
        digito = temp % 10
        inverso = (inverso * 10) + digito
        temp = temp // 10
        
    if original == inverso:
        print(f"El número {original} es un palíndromo.\n")
    else:
        print(f"El número {original} no es un palíndromo.\n")
        
    if input("¿Desea continuar (S/N)? ").upper() == 'N':
        break