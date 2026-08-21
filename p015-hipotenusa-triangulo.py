# p015-hipotenusa-triangulo
# Crea un programa que calcule la longitud de la hipotenusa de un triángulo rectángulo. El programa debe solicitar al usuario que ingrese la longitud de los dos lados (catetos) del triángulo. Para el cálculo, utiliza la siguientefórmula

import math

#solicitar al usuario que ingrese la longitud de los dos lados (catetos) del triángulo.
print("Cálculo de la hipotenusa de un triángulo rectángulo")
lognlado1 = float(input("Ingresa la longitud del primer lado (cateto 1): "))
lognlado2 = float(input("Ingresa la longitud del segundo lado (cateto 2): "))

# Realizar el cálculo
# La hipotenusa = raizcuadrada( longlado1 * lognlado1 + longlado2 * longlado2 )
hipotenusa = math.sqrt((lognlado1 * lognlado1) + (lognlado2 * lognlado2))

# Mostrar el resultado
print("La longitud de la hipotenusa es:", hipotenusa)