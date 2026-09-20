# p083-rombo-caracter.py
# Dibuja un rombo a partir de una altura impar ingresada por el usuario.

n = int(input("Dame un número impar para la altura: "))
car = input("¿Qué carácter quieres usar? ")

# Calculamos matemáticamente la fila que será la mitad (la más ancha)
# Por ejemplo, si n es 5, mitad será (5 // 2) + 1 = 2 + 1 = 3
mitad = (n // 2) + 1

# PRIMERA PARTE: incluye la fila más ancha
for i in range(1, mitad + 1):
    espacios = mitad - i
    caracteres = (2 * i) - 1

    # Imprimimos los espacios de margen izquierdo
    for j in range(espacios):
        print(" ", end="")

    # Imprimimos el carácter indicado
    for k in range(caracteres):
        print(car, end="")

    # Pasamos al siguiente renglón
    print()

# SEGUNDA PARTE: decreciente
# Empezamos una fila abajo de la más ancha (mitad - 1) y bajamos hasta la fila 1
for i in range(mitad - 1, 0, -1):
    espacios = mitad - i
    caracteres = (2 * i) - 1

    # Imprimimos los espacios de margen izquierdo
    for j in range(espacios):
        print(" ", end="")

    # Imprimimos el carácter indicado
    for k in range(caracteres):
        print(car, end="")

    # Pasamos al siguiente renglón
    print()