# p121-area-figuras.py
# Crear un diccionario de diccionarios para representar figuras geométricas y calcular sus áreas
import math

figuras = {
    "Circulo": {"radio": 0, "formula": "math.pi * r ** 2"},
    "Triangulo": {"base": 0, "altura": 0, "formula": "0.5 * b * a"},
    "Rectangulo": {"largo": 0, "ancho": 0, "formula": "l * a"}
}

print('\033[H\033[J')
print('Área de Figuras Geométricas\n')
print("Calculadora dinámica de áreas")
print("Figuras disponibles:")

for k, v in figuras.items():
    print(f'{k:<12} Fórmula: {v["formula"]}')

while True:
    fig = input('\nElige una Figura: ').title()
    if fig in figuras:
        break
    print("Error: Figura no válida. Intenta de nuevo.")

area = 0

if fig == 'Circulo':
    r = int(input('Radio: '))
    # Reemplaza la 'r' en la fórmula por el valor ingresado y lo evalúa
    formula_lista = figuras[fig]['formula'].replace('r', str(r))
    area = eval(formula_lista)

elif fig == 'Triangulo':
    b = int(input('Base: '))
    a = int(input('Altura: '))
    # Reemplaza la 'b' y la 'a' en la fórmula
    formula_lista = figuras[fig]['formula'].replace('b', str(b)).replace('a', str(a))
    area = eval(formula_lista)

elif fig == 'Rectangulo':
    l = int(input('Largo: '))
    a = int(input('Ancho: '))
    # Reemplaza la 'l' y la 'a' en la fórmula
    formula_lista = figuras[fig]['formula'].replace('l', str(l)).replace('a', str(a))
    area = eval(formula_lista)

print(f'\nEl Área del {fig} es: {area:.4f}')

