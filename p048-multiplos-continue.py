# Ejemplo 5: Múltiplos de 10.
# p048-multiplos-continue.py
# Imprime solo los múltiplos de 10 hasta 200.

print(" Buscando múltiplos de 10 entre 1 y 200...")
c = 0
while c < 200:
    c += 1
    if c % 10 != 0:
        # "Ignora todo lo que sigue y salta a la siguiente iteración". 
        continue
    # Esta línea SÓLO se ejecuta si el 'if' fue falso (es decir, si es un múltiplo de 10). 
    print(f" {c}", end=" ")
print("\n Búsqueda finalizada.")