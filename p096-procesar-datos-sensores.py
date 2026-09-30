# p096-procesar-datos-sensores.py
# Simulación de recolección y procesamiento de datos de sensores 
import random

# --- 1. Generación de Datos Simulados
print('\033[H\033[J')
print("Simulando la recolección de datos de dos sensores...")

sensor_a_datos = []
sensor_b_datos = []

for _ in range(10):
    sensor_a_datos.append(random.randint(1, 100)) # Llena la lista del sensor A
    sensor_b_datos.append(random.randint(1, 100)) # Llena la lista del sensor B
    
print("\n--- Datos Originales de los Sensores ---")
print(f"Sensor A: {sensor_a_datos}")
print(f"Sensor B: {sensor_b_datos}")

# --- 2. Transformación y Combinación de Datos
sensor_a_trans = []
sensor_b_trans = []
datos_combinados = []

for i in range(10):
    # Elevar al cuadrado
    trans_a = sensor_a_datos[i] ** 2
    trans_b = sensor_b_datos[i] ** 2
    
    sensor_a_trans.append(trans_a)
    sensor_b_trans.append(trans_b)
    
    # Suma combinada
    datos_combinados.append(trans_a + trans_b)

print("\n--- Datos Transformados (Al cuadrado) ---")
print(f"Sensor A: {sensor_a_trans}")
print(f"Sensor B: {sensor_b_trans}")

print("\n--- Lista Combinada Final (Suma) ---")
print(f"Combinación: {datos_combinados}")
