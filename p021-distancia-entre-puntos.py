#p021-distancia-entre-puntos
# Crea un programa que calcule la distancia entre dos puntos en un plano cartesiano.

#ingrese las coordenadas del punto A (x1,y1) y las coordenadas del punto B (x2,y2).
import math
print('Calculando la distancia entre dos puntos:\n')

# Solicitar las coordenadas del Punto A en una sola línea separadas por espacio
print('Dame las coordenadas del Punto A (x1 y1) separadas por un espacio:')
x1, y1 = input().split()
x1, y1 = float(x1), float(y1)

# Solicitar las coordenadas del Punto B en una sola línea separadas por espacio
print('Dame las coordenadas del Punto B (x2 y2) separadas por un espacio:')
x2, y2 = input().split()
x2, y2 = float(x2), float(y2)

# Calcular la distancia usando la fórmula  
# Usamos ** 2 para elevar al cuadrado
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Mostrar el resultado incluyendo las coordenadas ingresadas
print(f'El Punto A está en: ({x1}, {y1})')
print(f'El Punto B está en: ({x2}, {y2})')
print(f'La distancia entre los dos puntos es: {distancia}')

