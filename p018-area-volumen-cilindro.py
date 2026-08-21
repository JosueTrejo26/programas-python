# p018-area-volumen-cilindro
# Crea un programa que calcule el área y volumen de un cilindro.

#Pide al usuario que ingrese el radio (R) y la altura (h) del cilindro.
import math

print("Cálculo de área y volumen de un cilindro")
radio = float(input("Ingresa el valor del radio (R): "))
altura = float(input("Ingresa el valor de la altura (h): "))

# Las fórmulas para el cálculo de área y de volumen son:
# Area = 2 π (R + h)
# Volumen = π * R2 * h
area = 2 * math.pi * (radio + altura)
volumen = math.pi * (radio * radio) * altura

#Mostrar los resultados
print("El área del cilindro es:", area)
print("El volumen del cilindro es:", volumen)