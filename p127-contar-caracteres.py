# p127-contar-caracteres.py
# Cuenta la frecuencia de cada carácter en una cadena usando un diccionario

# 1. Pide al usuario que ingrese una cadena de texto
cadena = input("Ingrese una cadena: ")

# 2. Crea un diccionario vacío
frecuencia_caracteres = {}

# 3. y 4. Itera sobre cada carácter y cuenta las apariciones
for caracter in cadena:
    # Si el carácter no existe como llave, lo agrega con valor 1
    if caracter not in frecuencia_caracteres:
        frecuencia_caracteres[caracter] = 1
    # Si ya existe, incrementa su valor en 1
    else:
        frecuencia_caracteres[caracter] += 1

# 5. Muestra el diccionario resultante
print("Resultado:")
print(frecuencia_caracteres)
