# p105-listas-multiplica.py
# Multiplicación de elementos correspondientes de dos listas

# Leer cadenas, dividirlas por espacios y convertirlas a float
entrada_a = input("Introduzca 5 números para la Lista A (separados por espacio): ").split()
entrada_b = input("Introduzca 5 números para la Lista B (separados por espacio): ").split()

# Convertir a listas de números
lista_a = [float(x) for x in entrada_a[:5]]
lista_b = [float(x) for x in entrada_b[:5]]

lista_c = []
# Multiplicar los elementos correspondientes
for i in range(len(lista_a)):
    lista_c.append(lista_a[i] * lista_b[i])

print("\n--- Resultados ---")
print(f"Lista A: {lista_a}")
print(f"Lista B: {lista_b}")
print(f"Lista C (AxB): {lista_c}")
