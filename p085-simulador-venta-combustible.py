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
    
    opcion = input("Elige una opción (1-4): ").strip()

    # ---------------------------------------------------------
    # OPCIÓN 1: Módulo de Venta
    # ---------------------------------------------------------
    if opcion == '1':
        print("\n--- 1. Venta de Combustible ---")
        tipo_combustible = input("Ingresa el tipo de combustible (Ej. Magna, Premium): ").strip()
        
        if tipo_combustible == "":
            print("Error: El tipo de combustible no puede estar vacío.")
            continue

        # Implementación de try/except para evitar colapsos
        try:
            precio_litro = float(input("Precio por litro: $"))
            litros = float(input("Cantidad de litros a cargar: "))
        except ValueError:
            print("Error: Entrada inválida. Debes ingresar números (ej. 24.50).")
            continue
            
        # Validación de valores positivos
        if precio_litro <= 0 or litros <= 0:
            print("Error: El precio y los litros deben ser mayores a cero.")
            continue
            
        total_pagar = precio_litro * litros
        
        # Uso de f-strings con alineación a la derecha
        print("-" * 40)
        print(f"{'Combustible:':<18} {tipo_combustible}")
        print(f"{'Precio por litro:':<18} ${precio_litro:>10.2f}")
        print(f"{'Litros:':<18} {litros:>10.2f} L")
        print(f"{'Total a pagar:':<18} ${total_pagar:>10.2f}")
        print("-" * 40)

    # ---------------------------------------------------------
    # OPCIÓN 2: Simulación de Rendimiento
    # ---------------------------------------------------------
    elif opcion == '2':
        print("\n--- 2. Simulación de Rendimiento (Desgaste Mensual) ---")
        
        # Validación de entradas numéricas en masa
        try:
            km_inicial = int(input("Kilometraje inicial del vehículo: "))
            meses = int(input("Meses a proyectar: "))
            km_por_mes = int(input("Kilómetros promedio a recorrer por mes: "))
            rendimiento_base = float(input("Rendimiento original del vehículo (km/l): "))
            cap_tanque = float(input("Capacidad del tanque del vehículo (litros): "))
        except ValueError:
            print("Error: Entrada inválida. Debes ingresar exclusivamente números.")
            continue
            
        # Validación de lógicas de negocio
        if km_inicial < 0 or meses <= 0 or km_por_mes <= 0 or rendimiento_base <= 0 or cap_tanque <= 0:
            print("Error: Los valores ingresados no son lógicos (deben ser mayores a cero).")
            continue
            
        print("\nProyección de consumo mensual:")
        print(f"{'Mes':<5} | {'KM Acumulados':<15} | {'Lts Necesarios':<15} | {'Tanques Llenos':<15} | {'Lts Sobrantes':<15}")
        print("-" * 75)
        
        # Ciclo for con range para tabla proyectada
        for mes in range(1, meses + 1):
            km_actual = km_inicial + (km_por_mes * mes)
            
            # Operador de POTENCIA (**): Pérdida de 1% de eficiencia mensual
            factor_desgaste = 1.01 ** mes
            rendimiento_real = rendimiento_base / factor_desgaste
            litros_mes = km_por_mes / rendimiento_real
            
            # Operadores de DIVISIÓN ENTERA (//) y RESIDUO (%)
            tanques = int(litros_mes // cap_tanque)
            litros_sueltos = litros_mes % cap_tanque
            
            print(f"{mes:<5} | {km_actual:<15} | {litros_mes:<15.2f} | {tanques:<15} | {litros_sueltos:<15.2f}")

    # ---------------------------------------------------------
    # OPCIÓN 3: Clasificador de Cliente
    # ---------------------------------------------------------
    elif opcion == '3':
        print("\n--- 3. Clasificador de Cliente ---")
        
        # Validación para evitar caídas si se ingresa texto
        try:
            volumen = float(input("Ingresa el volumen de compra mensual (litros): "))
        except ValueError:
            print("Error: Debes ingresar un valor numérico para el volumen.")
            continue
            
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
        break 
        
    # ---------------------------------------------------------
    # ERROR: Opción no válida
    # ---------------------------------------------------------
    else:
        print("\nError: Opción no válida. Por favor, selecciona del 1 al 4.")
        continue