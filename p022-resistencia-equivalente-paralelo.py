#p022-resistencia-equivalente-paralelo
#Crea un programa que calcule la resistencia total o equivalente de un circuito con cuatro resistencias en paralelo.

#solicitar al usuario que ingrese el valor de cada una de las cuatro resistencias (R1, R2, R3 y R4).
print('Calculando la resistencia equivalente en paralelo:\n')
print('Dame los valores de R1, R2, R3 y R4 separados por espacios:')
r1, r2, r3, r4 = input().split()

# Convertimos los valores a números flotantes ya que las resistencias pueden tener decimales
r1, r2, r3, r4 = float(r1), float(r2), float(r3), float(r4)

#calcular la resistencia total usando la siguiente fórmula:
# rt = 1 / ((1 / r1) + (1 / r2) + (1 / r3) + (1 / r4))
rt = 1 / ((1 / r1) + (1 / r2) + (1 / r3) + (1 / r4))

# Mostrar el resultado incluyendo las resistencias ingresadas
print(f'Las resistencias ingresadas son: R1={r1}, R2={r2}, R3={r3}, R4={r4}')
print(f'La resistencia total o equivalente es: {rt}')

