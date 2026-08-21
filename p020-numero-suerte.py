#p020-numero-suerte
# Diseña un programa que tome una cantidad de horas como un número entero.

print("Cálculo del número de la suerte")
print('Dame tu año de nacimiento de 4 dígitos:')

N1, N2, N3, N4 = input()
N1, N2, N3, N4 = int(N1), int(N2), int(N3), int(N4)

# Calcular la suma de los Numeros
suma = N1 + N2 + N3 + N4

# Mostrar los resultados
print(f'Los dígitos individuales son: "{N1}", "{N2}", "{N3}", "{N4}"')
print(f'La suma de los dígitos es: {suma}')