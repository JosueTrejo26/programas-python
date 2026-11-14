# p151-medidas-longitud.py
# Conversor de unidades de longitud con menú y funciones separadas

def pulgadas_a_centimetros(pulgadas: float) -> float:
    return pulgadas * 2.54

def metros_a_pies(metros: float) -> float:
    return metros * 3.281

def main() -> None:
    while True:
        print("***")
        print("Conversor de Unidades")
        print("1. Pulgadas a Centímetros")
        print("2. Metros a Pies")
        print("3. Salir")
        print("***")
        
        try:
            opcion = int(input("Elige una opción: "))
        except ValueError:
            print("Opción inválida.")
            continue
            
        if opcion == 1:
            pulgadas = float(input("Introduce la cantidad en pulgadas: "))
            cm = pulgadas_a_centimetros(pulgadas)
            print(f"{pulgadas} pulgadas equivalen a {cm} centímetros.")
        elif opcion == 2:
            metros = float(input("Introduce la cantidad en metros: "))
            pies = metros_a_pies(metros)
            print(f"{metros} metros equivalen a {pies} pies.")
        elif opcion == 3:
            print("Saliendo del conversor...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
