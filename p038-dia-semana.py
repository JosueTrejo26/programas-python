# p038-dia-semana.py
# Muestra el día de la semana correspondiente a un número del 1 al 7

dia = int(input("Dame un número del 1 al 7: "))

if dia == 1:
    print("El día es domingo.")
elif dia == 2:
    print("El día es lunes.")
elif dia == 3:
    print("El día es martes.")
elif dia == 4:
    print("El día es miércoles.")
elif dia == 5:
    print("El día es jueves.")
elif dia == 6:
    print("El día es viernes.")
elif dia == 7:
    print("El día es sábado.")
else:
    print("Error: El número ingresado está fuera del rango (1 a 7).")