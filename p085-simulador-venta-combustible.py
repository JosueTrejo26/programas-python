# p085_SimuladorVentaCombustible.py
# Simulador de estación de servicio (gasolinera) con menú interactivo

print("Iniciando sistema de estación de servicio...")

# 1. Menú Principal: Ciclo infinito
while True:
    print("\n" + "="*45)
    print("        MENÚ PRINCIPAL GASOLINERA")
    print("="*45)
    print("1. Venta de Combustible")
    print("2. Simulación de Rendimiento")
    print("3. Clasificador de Cliente")
    print("4. Salir")
    print("="*45)
    
    opcion = input("Elige una opción (1-4): ")

    # ---------------------------------------------------------
    # OPCIÓN 1: Módulo de Venta
    # ---------------------------------------------------------
    if opcion == '1':
        print("\n--- 1. Venta de Combustible ---")
        tipo_combustible = input("Ingresa el tipo de combustible (Ej. Magna, Premium): ")
        precio_litro = float(input("Precio por litro: $"))
        litros = float(input("Cantidad de litros a cargar: "))
        
        # Validación de valores positivos
        if precio_litro <= 0 or litros <= 0:
            print("Error: El precio y los litros deben ser mayores a cero.")
            continue # Reinicia el menú
            
        total_pagar = precio_litro * litros
        
        # Uso de f-strings con alineación a la derecha (espacio de 10) y 2 decimales
        print("-" * 35)
        print(f"Combustible: {tipo_combustible}")
        print(f"Litros:      {litros:.2f} L")
        print(f"Total a pagar: ${total_pagar:>10.2f}")
        print("-" * 35)

    # ---------------------------------------------------------
    # OPCIÓN 2: Simulación de Rendimiento
    # ---------------------------------------------------------
    elif opcion == '2':
        print("\n--- 2. Simulación de Rendimiento (Desgaste Mensual) ---")
        km_inicial = int(input("Kilometraje inicial del vehículo: "))
        meses = int(input("Meses a proyectar: "))
        km_por_mes = int(input("Kilómetros promedio a recorrer por mes: "))
        rendimiento_base = float(input("Rendimiento original del vehículo (km/l): "))
        cap_tanque = float(input("Capacidad del tanque del vehículo (litros): "))
        
        if meses <= 0 or rendimiento_base <= 0 or cap_tanque <= 0:
            print("Error: Todos los valores deben ser positivos.")
            continue
            
        print("\nProyección de consumo mensual:")
        print(f"{'Mes':<5} | {'KM Acumulados':<15} | {'Lts Necesarios':<15} | {'Tanques Llenos':<15} | {'Lts Sobrantes':<15}")
        print("-" * 75)
        
        # Ciclo for con range para tabla proyectada
        for mes in range(1, meses + 1):
            km_actual = km_inicial + (km_por_mes * mes)
            
            # Operador de POTENCIA (**): El motor pierde 1% de eficiencia acumulativa cada mes
            factor_desgaste = 1.01 ** mes
            rendimiento_real = rendimiento_base / factor_desgaste
            litros_mes = km_por_mes / rendimiento_real
            
            # Operador de DIVISIÓN ENTERA (//) y RESIDUO (%): 
            # Desglosa los litros totales en tanques enteros que se deben pagar y el remanente
            tanques = int(litros_mes // cap_tanque)
            litros_sueltos = litros_mes % cap_tanque
            
            print(f"{mes:<5} | {km_actual:<15} | {litros_mes:<15.2f} | {tanques:<15} | {litros_sueltos:<15.2f}")

    # ---------------------------------------------------------
    # OPCIÓN 3: Clasificador de Cliente
    # ---------------------------------------------------------
    elif opcion == '3':
        print("\n--- 3. Clasificador de Cliente ---")
        volumen = float(input("Ingresa el volumen de compra mensual (litros): "))
        
        if volumen < 0:
            print("Error: El volumen no puede ser negativo.")
            continue
        elif volumen < 100:
            print(">>> Categoría asignada: REGULAR")
        elif volumen >= 100 and volumen <= 500:
            print(">>> Categoría asignada: PREMIUM")
        else:
            print(">>> Categoría asignada: FLOTILLA")

    # ---------------------------------------------------------
    # OPCIÓN 4: Salida Limpia
    # ---------------------------------------------------------
    elif opcion == '4':
        print("\nFinalizando el sistema... ¡Excelente turno!")
        break # Rompe el ciclo infinito
        
    # ---------------------------------------------------------
    # ERROR: Opción no válida
    # ---------------------------------------------------------
    else:
        print("\nError: Opción no válida. Por favor, selecciona del 1 al 4.")
        continue # Regresa al inicio del ciclo