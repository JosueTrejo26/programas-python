# p071-suma-promedio-numeros.py
# Suma de n numeros introducidos por el usuario usando ciclo for

while True:
    print('\033[H\033[J')
    cuantos = int(input('Cuantos números deseas procesar? '))
    suma = 0
    cadnum = ""
    
    for i in range(1, cuantos + 1):
        n = int(input(f'Número[{i}] = '))
        suma += n
        cadnum += str(n) + " "
        
    print(f'\nLos numeros que introdujiste fueron: {cadnum}')
    if cuantos > 0:
        print(f'La suma es {suma}, el promedio es {suma / cuantos}')
    
    if input('\n\nDeseas continuar (S/N)? ').upper() == 'N':
        break
        
print('\nHemos llegado al final ....')