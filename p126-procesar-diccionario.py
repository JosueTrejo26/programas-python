# p126-procesar-diccionario.py
# Muestra cómo crear un diccionario a partir de listas, iterarlo y realizar cálculos

# 1. Define dos listas
nombres = ['Juan', 'Pedro', 'Manuel', 'Elias', 'Maria', 'Felipe', 'Julia', 'Roberto']
sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]

# 2. Crea un diccionario nómina combinando ambas listas
nomina = dict(zip(nombres, sueldos))

# 3. Muestra el diccionario nómina
print("Diccionario de nómina:")
print(nomina)

# 4. Itera sobre el diccionario
print("\nIterando Llaves (keys)")
for llave in nomina.keys():
    print(llave)

print("\nIterando Valores (values)")
for valor in nomina.values():
    print(valor)

print("\nIterando Llave y Valor (accediendo por llave)")
for llave in nomina:
    print(f"{llave} -> {nomina[llave]}")

print("\nIterando Llave y Valor (items)")
for llave, valor in nomina.items():
    print(f"('{llave}', {valor})")

# 5. y 6. Calcula y muestra la suma total y el promedio
suma_total = sum(nomina.values())
promedio = suma_total / len(nomina)

print("\nCálculos")
print(f"Suma total de sueldos: {suma_total}")
print(f"Promedio de sueldos: {promedio:.2f}")
