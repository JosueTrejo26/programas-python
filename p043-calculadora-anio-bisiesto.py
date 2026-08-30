# p043-calculadora-anio-bisiesto.py
# Determina si un año ingresado es bisiesto aplicando reglas matemáticas

anio = int(input("Año: "))

# Un año es bisiesto si es divisible por 4 pero NO por 100, O si es divisible por 400
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f"El año {anio} es bisiesto.")
else:
    print(f"El año {anio} NO es bisiesto.")