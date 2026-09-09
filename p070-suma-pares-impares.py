# p070-suma-pares-impares.py
# Imprimir los números pares y números impares, su suma también en un rango determinado

while True:
    print('\033[H\033[J')
    print('Imprimir la suma de pares e impares en un rango de 1 a n')
    
    n = int(input('Dame el valor final? '))
    sp = si = 0
    cp = ""
    ci = ""
    
    for i in range(1, n + 1):
        if i % 2 == 0: # es par
            cp += str(i) + " "
            sp += i
        else: # es impar
            ci += str(i) + " "
            si += i
            
    print(f'\nLos pares: {cp}')
    print(f'Suma de pares: {sp}')
    print(f'\nLos impares: {ci}')
    print(f'Suma de impares: {si}')
    
    if input("\n\nDeseas continuar (S/N)? ").upper() == 'N':
        break
        
print('\nHemos llegado al final ....')