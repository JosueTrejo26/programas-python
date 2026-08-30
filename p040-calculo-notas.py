# p040-calculo-notas.py
# Calcula el promedio de 5 calificaciones y muestra un mensaje de evaluación

print("Ingresa 5 calificaciones separadas por espacio: ", end="")
c1, c2, c3, c4, c5 = map(float, input().split())

promedio = (c1 + c2 + c3 + c4 + c5) / 5
print(f"Promedio: {promedio:.1f}")

if promedio < 6:
    print("Quedas reprobado")
elif promedio < 7:
    print("Pasas de panzazo")
elif promedio < 8:
    print("Muy bien, puedes mejorar")
elif promedio < 9:
    print("Excelente, sigue así")
elif promedio <= 10:
    print("Perfecto, tu esfuerzo valió la pena")
else:
    print("Error: Promedio fuera de rango.")