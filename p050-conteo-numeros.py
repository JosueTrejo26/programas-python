# Ejemplo 7: Conteo de números .
# p050-conteo-numeros.py
# Lee números hasta ingresar 999, luego, muestra un resumen estadístico

cuenta = 0
suma = 0
cuenta_positivos = 0
cuenta_negativos = 0
cuenta_ceros = 0

print(" Analizador de Números (escribe 999 para finalizar)")

while True:
    num = int(input('Introduce un número entero: '))
    
    if num == 999: # Condición de salida
        print("Detectado código de salida (999)")
        break # Rompe el ciclo infinito.
        
    # Proceso
    cuenta += 1
    suma += num
    
    if num > 0:
        cuenta_positivos += 1
    elif num < 0:
        cuenta_negativos += 1
    else:
        cuenta_ceros += 1

# Reporte final según el planteamiento del problema
print("\n--- Reporte Final ---")
print(f"Total de números introducidos: {cuenta}")
print(f"Suma de todos los números: {suma}")
print(f"Positivos: {cuenta_positivos} | Negativos: {cuenta_negativos} | Ceros: {cuenta_ceros}")