# p036-numeros-consecutivos.py
# Determina si tres números enteros ingresados son consecutivos

print("Dame tres números separados por espacio: ", end="")
n1, n2, n3 = input().split()

# Convertimos las entradas a enteros
n1, n2, n3 = int(n1), int(n2), int(n3)

# Verificamos si cada número es exactamente una unidad mayor que el anterior
if n1 + 1 == n2 and n2 + 1 == n3:
    print(f"Los números {n1}, {n2}, {n3} son consecutivos.")
else:
    print(f"Los números {n1}, {n2}, {n3} NO son consecutivos.")