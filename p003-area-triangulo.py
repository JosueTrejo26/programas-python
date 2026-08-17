# p003-area-triangulo.py
# Calcular el área de un triángulo

print('Calculando el área de un triangulo:\n')
print('Dame la base y la altura separados por un Enter')

base, altura = int(input()), int(input())
area = base * altura / 2

print(f'El triángulo de base {base} y altura {altura} tiene un area de {area}')