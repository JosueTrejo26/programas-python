# p042-precio-entrada-cine.py
# Determina el precio de la entrada al cine según la edad del cliente

edad = int(input("Edad del cliente: "))

if edad < 5:
    precio = 0
elif edad <= 12:
    precio = 5
elif edad <= 64:
    precio = 10
else: # 65 años o más
    precio = 7

if precio == 0:
    print("El precio de la entrada es: ¡Gratis!")
else:
    print(f"El precio de la entrada es ${precio}.")