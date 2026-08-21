# p019-calculo-tiempo
# Diseña un programa que tome una cantidad de horas como un número entero.

print("Conversor de horas a días, minutos y segundos")
horas = int(input("Ingresa una cantidad de horas (número entero): "))

# Días (considerando que 1 día tiene 24 horas)
dias = horas / 24
# Minutos (considerando que 1 hora tiene 60 minutos)
minutos = horas * 60
# Segundos (considerando que 1 minuto tiene 60 segundos)
segundos = minutos * 60

# Mostrar los resultados
print("El equivalente en días es:", dias)
print("El equivalente en minutos es:", minutos)
print("El equivalente en segundos es:", segundos)
