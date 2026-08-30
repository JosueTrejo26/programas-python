# p037-numero-mayor.py
# Identifica el mayor de tres números enteros

print("Dame tres números separados por espacio: ", end="")
n1, n2, n3 = input().split()
n1, n2, n3 = int(n1), int(n2), int(n3)

# Asumimos inicialmente que el primero es el mayor
mayor = n1

# Comparamos con los demás usando condicionales
if n2 > mayor:
    mayor = n2
if n3 > mayor:
    mayor = n3

print(f"El mayor es {mayor}.")