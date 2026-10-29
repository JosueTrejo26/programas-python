# p136-segundo-examen-parcial.py
# Sistema "AeroRegistro": Captura, procesamiento y análisis de vuelos

# --- FASE 1: Estructura y Captura ---
# Se inicializa la lista principal que almacenará el inventario completo como diccionarios.
vuelos = []

print("--- AeroRegistro Sistema de Vuelos ---")
print("Captura de datos de los vuelos (* o Enter para terminar)\n")

# Ciclo infinito para la captura continua de datos hasta que el usuario decida salir.
while True:
    numero_vuelo = input("Número de vuelo: ").strip()
    
    # Condición de ruptura del ciclo: entrada vacía o asterisco.
    if numero_vuelo == '*' or numero_vuelo == '':
        break
        
    origen = input("Origen: ").strip()
    destino = input("Destino: ").strip()
    aerolinea = input("Aerolínea: ").strip()
    
    # Bloque try-except para garantizar que las entradas numéricas no rompan el programa.
    try:
        pasajeros = int(input("Pasajeros: "))
        tarifa = float(input("Tarifa: $"))
    except ValueError:
        print("Error: Los pasajeros deben ser un número entero y la tarifa numérica. Intente de nuevo.\n")
        continue
        
    # Almacenamiento temporal de los datos del vuelo actual en un diccionario.
    datos_vuelo = {
        'numero_vuelo': numero_vuelo,
        'origen': origen,
        'destino': destino,
        'aerolinea': aerolinea,
        'pasajeros': pasajeros,
        'tarifa': tarifa
    }
    
    # Integración del diccionario a la lista principal.
    vuelos.append(datos_vuelo)
    print("Vuelo registrado correctamente.\n")


# --- FASE 2: Extracción de Colecciones Especiales ---
# Se inicializan las estructuras requeridas: un conjunto (set) y una lista para tuplas.
destinos_unicos = set()
registro_inmutable = []

# Se itera sobre el inventario para poblar las nuevas colecciones.
for vuelo in vuelos:
    # El set omite automáticamente cualquier ciudad que ya haya sido agregada previamente.
    destinos_unicos.add(vuelo['destino'])
    
    # Se genera una tupla (estructura inmutable) solo con los tres datos solicitados.
    datos_tupla = (vuelo['numero_vuelo'], vuelo['aerolinea'], vuelo['destino'])
    registro_inmutable.append(datos_tupla)


# --- FASE 3: Formateo y Visualización ---
# Impresión directa de las estructuras de datos generadas.
print("\nDatos (Lista de diccionarios):")
print(vuelos)

print("\nDestinos Únicos (Conjunto):")
print(destinos_unicos)

print("\nRegistro Inmutable (Tuplas):")
print(registro_inmutable)

print("\nTabla de datos:")
# Uso de f-strings con alineación (ej. :<12) para tabular uniformemente los encabezados.
print(f"{'No. Vuelo':<12} | {'Origen':<15} | {'Destino':<15} | {'Aerolínea':<15} | {'Pasajeros':<10} | {'Tarifa':<12}")
print("-" * 88)

# Iteración para imprimir cada registro respetando el espaciado tabular y el formato de moneda (,.2f).
for vuelo in vuelos:
    print(f"{vuelo['numero_vuelo']:<12} | {vuelo['origen']:<15} | {vuelo['destino']:<15} | {vuelo['aerolinea']:<15} | {vuelo['pasajeros']:<10} | ${vuelo['tarifa']:,.2f}")


# --- FASE 4: Analítica y Cálculos Matemáticos ---
print("\nResumen:")

total_vuelos = len(vuelos)
print(f"Vuelos totales: {total_vuelos}")

# Bloque condicional para evitar cálculos o divisiones por cero si no se registraron vuelos.
if total_vuelos > 0:
    # Diccionarios auxiliares para contar ocurrencias.
    conteo_aerolineas = {}
    conteo_destinos = {}
    
    # Variables acumuladoras para las sumas.
    suma_pasajeros = 0
    suma_tarifas = 0.0
    
    # Variables para identificar extremos (se inicializan con el primer elemento para comparar).
    vuelo_mas_caro = vuelos[0]
    vuelo_mas_barato = vuelos[0]

    for vuelo in vuelos:
        # Conteo dinámico: Si la llave existe, suma 1; si no, retorna 0 y suma 1.
        aero = vuelo['aerolinea']
        dest = vuelo['destino']
        conteo_aerolineas[aero] = conteo_aerolineas.get(aero, 0) + 1
        conteo_destinos[dest] = conteo_destinos.get(dest, 0) + 1
        
        # Acumulación de valores totales.
        suma_pasajeros += vuelo['pasajeros']
        suma_tarifas += vuelo['tarifa']
        
        # Actualización de los registros más caros y más baratos mediante comparación.
        if vuelo['tarifa'] > vuelo_mas_caro['tarifa']:
            vuelo_mas_caro = vuelo
        if vuelo['tarifa'] < vuelo_mas_barato['tarifa']:
            vuelo_mas_barato = vuelo

    # Cálculo de las medias aritméticas.
    promedio_pasajeros = suma_pasajeros / total_vuelos
    promedio_tarifas = suma_tarifas / total_vuelos

    # Impresión de los diccionarios de conteo desglosados.
    print("Aerolíneas:")
    for aero, cantidad in conteo_aerolineas.items():
        print(f"  {aero}: {cantidad}")

    print("Destinos:")
    for dest, cantidad in conteo_destinos.items():
        print(f"  {dest}: {cantidad}")

    # Resultados estadísticos finales con formato decimal y de moneda.
    print(f"Pasajeros -> Suma: {suma_pasajeros}, Promedio: {promedio_pasajeros:.2f}")
    print(f"Tarifa -> Suma: ${suma_tarifas:,.2f}, Promedio: ${promedio_tarifas:,.2f}")
    
    # Resultados de las comparaciones de máximos y mínimos.
    print(f"{vuelo_mas_caro['numero_vuelo']} de ${vuelo_mas_caro['tarifa']:,.2f} es el más caro, {vuelo_mas_barato['numero_vuelo']} de ${vuelo_mas_barato['tarifa']:,.2f} es el más barato.")
    