# p082-cuadro-hueco-caracter.py
# Dibuja el contorno de un cuadrado usando un carácter específico.

lado = int(input("¿De qué tamaño será el lado del cuadrado? "))
car = input("¿Qué carácter quieres usar? ")

# filas
for i in range(1, lado + 1):
    
    # Ciclo interno para las columnas
    for j in range(1, lado + 1):
        # Condición para dibujar el contorno: 
        # i == 1 (primer renglón), i == lado (último renglón)
        # j == 1 (primera columna), j == lado (última columna)
        if i == 1 or i == lado or j == 1 or j == lado:
            print(car, end="")
        else:
            # En el interior del cuadrado imprimimos un espacio en blanco
            print(" ", end="")
            
    # Salto de línea al terminar de imprimir todas las columnas del renglón
    print()