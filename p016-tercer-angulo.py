#p016-tercer-angulo
#Escribe un programa que determine el tercer ángulo de un triángulo.

# ingrese las medidas de dos ángulos del triángulo.
print("Cálculo del tercer ángulo de un triángulo")
print("La suma de los ángulos de un triángulo es siempre 180°")
angulo1 = float(input("Ingresa la medida del primer ángulo: "))
angulo2 = float(input("Ingresa la medida del segundo ángulo: "))
    
# Utiliza la siguiente fórmula para encontrar el ángulo faltante:
# angulo3 = 180 – (angulo1 + angulo2)
angulo3 = 180 - (angulo1 + angulo2)

# Mostrar el resultado
print("La medida del tercer ángulo faltante es:", angulo3)