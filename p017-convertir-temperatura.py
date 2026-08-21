#p017-convertir-temperatura
#Desarrolla un programa que convierta una temperatura de grados Celsius a grados Fahrenheit.

# solicitar al usuario una temperatura en Celsius
print("Conversor de temperatura: Celsius a Fahrenheit")
celsius = float(input("Ingresa la temperatura en grados Celsius: "))

#La fórmula para la conversión es:
# farenheit = (celsius × 9/5) + 32
fahrenheit = (celsius * 9 / 5) + 32

# mostrar el resultado en Fahrenheit.
print("La temperatura en grados Fahrenheit es:", fahrenheit)