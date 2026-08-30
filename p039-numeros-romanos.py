# p039-numeros-romanos.py
# Convierte un número del 1 al 10 a su equivalente en número romano

num = int(input("Dame un número del 1 al 10: "))

if num == 1:
    print("El número 1 en romano es I.")
elif num == 2:
    print("El número 2 en romano es II.")
elif num == 3:
    print("El número 3 en romano es III.")
elif num == 4:
    print("El número 4 en romano es IV.")
elif num == 5:
    print("El número 5 en romano es V.")
elif num == 6:
    print("El número 6 en romano es VI.")
elif num == 7:
    print("El número 7 en romano es VII.")
elif num == 8:
    print("El número 8 en romano es VIII.")
elif num == 9:
    print("El número 9 en romano es IX.")
elif num == 10:
    print("El número 10 en romano es X.")
else:
    print("Error: El número debe estar estrictamente entre 1 y 10.")