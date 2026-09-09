# p072-suma-mutiplos.py
# Imprime mutiplos de m entre 1 y n

while True:
    print('\033[H\033[J')
    print('Imprime mutiplos de m entre 1 y n')
    
    n = int(input('Hasta donde ? '))
    m = int(input('Que multiplos quieres ? '))
    
    cm = 0 # contador de múltiplos
    sm = 0 # suma de múltiplos
    
    print(f"Múltiplos de {m}: ", end="")
    for i in range(1, n + 1):
        if i % m == 0:
            print(i, end=' ')
            sm += i
            cm += 1
            
    print(f'\nFueron {cm} multiplos, los cuales suman {sm}')
    
    if input('\n\nDeseas continuar (S/N)? ').upper() == 'N':
        break
        
print('\nHemos llegado al final ....')