# p041-aceptar-estudiante-v2.py
# Evalúa la admisión de una estudiante con base en múltiples criterios y reporta el rechazo

nombre = input("Nombre: ")
sexo = input("Sexo (h/m): ").lower()
edad = int(input("Edad: "))
print("Tres calificaciones separadas por espacio: ", end="")
c1, c2, c3 = map(float, input().split())

promedio = (c1 + c2 + c3) / 3

# Evaluamos los criterios de rechazo uno por uno para dar un mensaje específico
if sexo != 'm':
    print("Estudiante no aceptado. Razón: La universidad solo acepta mujeres.")
elif edad <= 21:
    print("Estudiante no aceptado. Razón: Debe ser mayor de 21 años.")
elif promedio < 8 or promedio > 9.5:
    print(f"Estudiante no aceptado. Razón: El promedio ({promedio:.1f}) no está en el rango de 8 a 9.5.")
else:
    print("Estudiante aceptado.")