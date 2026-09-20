# p080-compara-rendimiento-inversion.py
# Compara el crecimiento de dos fondos de inversión año tras año.

print("Fondo de Inversión A")
monto_a = float(input("Monto inicial: "))
tasa_a = float(input("Tasa de interés anual (%): "))

print("Fondo de Inversión B")
monto_b = float(input("Monto inicial: "))
tasa_b = float(input("Tasa de interés anual (%): "))

anios = int(input("Años a proyectar: "))

print("\nComparación de Rendimientos Anuales")
print("Año\t| Fondo A\t| Fondo B")

# Calculamos año con año el rendimiento de ambos fondos
for i in range(1, anios + 1):
    # Se calcula el rendimiento y se suma al monto acumulado
    monto_a = monto_a + (monto_a * (tasa_a / 100))
    monto_b = monto_b + (monto_b * (tasa_b / 100))
    
    # Se imprimen los valores tabulados limitados a 2 decimales (.2f)
    print(f"{i}\t| $ {monto_a:.2f}\t| $ {monto_b:.2f}")

print() # Salto de línea para dar formato

# Comparamos qué monto final es mayor para declarar un ganador
if monto_a > monto_b:
    print(f"Resultado final: El Fondo A (${monto_a:.2f}) superó al Fondo B (${monto_b:.2f}).")
elif monto_b > monto_a:
    print(f"Resultado final: El Fondo B (${monto_b:.2f}) superó al Fondo A (${monto_a:.2f}).")
else:
    print(f"Resultado final: Ambos fondos terminaron con el mismo monto (${monto_a:.2f}).")