# p091-lista-de-gastos.py
# Gestión de lista de gastos mensuales

gastos = []

while True:
    print("\n" + "="*30)
    print("      CONTROL DE GASTOS")
    print("="*30)
    print("1. Ver Gastos")
    print("2. Agregar Gasto")
    print("3. Modificar Gasto")
    print("4. Eliminar Gasto")
    print("5. Ver Total")
    print("6. Salir")
    
    opcion = input("Selecciona una opción (1-6): ")
    
    # ------------------------------------
    # OPCIÓN 1: Ver Gastos
    # ------------------------------------
    if opcion == '1':
        print("\n--- Lista de Gastos ---")
        if len(gastos) == 0:
            print("No hay gastos registrados aún.")
        else:
            print("Índice\t| Gasto")
            print("-" * 25)
            for i, gasto in enumerate(gastos):
                print(f"[{i}]\t| ${gasto:.2f}")

    # ------------------------------------
    # OPCIÓN 2: Agregar Gasto
    # ------------------------------------
    elif opcion == '2':
        try:
            nuevo_gasto = float(input("\nIngresa el monto del gasto: $"))
            if nuevo_gasto < 0:
                print("Error: El gasto no puede ser negativo.")
            else:
                gastos.append(nuevo_gasto)
                print("¡Gasto agregado exitosamente!")
        except ValueError:
            print("Error: Entrada inválida. Ingresa solo números.")

    # ------------------------------------
    # OPCIÓN 3: Modificar Gasto
    # ------------------------------------
    elif opcion == '3':
        if len(gastos) == 0:
            print("\nError: No hay gastos registrados para modificar.")
            continue
            
        try:
            # Mostrar la lista primero
            for i, gasto in enumerate(gastos):
                print(f"[{i}] -> ${gasto:.2f}")
                
            indice = int(input("\nIngresa el índice del gasto que deseas modificar: "))
            
            if 0 <= indice < len(gastos):
                nuevo_valor = float(input("Ingresa el nuevo monto: $"))
                if nuevo_valor < 0:
                     print("Error: El gasto no puede ser negativo.")
                else:
                    gastos[indice] = nuevo_valor
                    print("¡Gasto modificado exitosamente!")
            else:
                print("Error: Gasto no encontrado. Índice fuera de rango.")
        except ValueError:
            print("Error: Entrada inválida.")

    # ------------------------------------
    # OPCIÓN 4: Eliminar Gasto
    # ------------------------------------
    elif opcion == '4':
        if len(gastos) == 0:
            print("\nError: No hay gastos registrados para eliminar.")
            continue
            
        try:
            for i, gasto in enumerate(gastos):
                print(f"[{i}] -> ${gasto:.2f}")
                
            indice = int(input("\nIngresa el índice del gasto que deseas eliminar: "))
            
            if 0 <= indice < len(gastos):
                eliminado = gastos.pop(indice)
                print(f"¡Gasto de ${eliminado:.2f} eliminado exitosamente!")
            else:
                print("Error: Gasto no encontrado. Índice fuera de rango.")
        except ValueError:
            print("Error: Entrada inválida.")

    # ------------------------------------
    # OPCIÓN 5: Ver Total
    # ------------------------------------
    elif opcion == '5':
        total = 0
        for gasto in gastos:
            total += gasto
        print(f"\n--- TOTAL DE GASTOS ---")
        print(f"El total acumulado es: ${total:.2f}")

    # ------------------------------------
    # OPCIÓN 6: Salir
    # ------------------------------------
    elif opcion == '6':
        print("\nSaliendo del control de gastos... ¡Hasta pronto!")
        break
        
    else:
        print("\nError: Opción no válida. Por favor, selecciona del 1 al 6.")