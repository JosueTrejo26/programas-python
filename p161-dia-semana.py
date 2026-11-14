# p150-dia-semana.py
# Recibe un número entero entre 1 y 7 y devuelve el día de la semana

def dia_semana(dia: int) -> str:
    if dia == 1:
        return "Lunes"
    elif dia == 2:
        return "Martes"
    elif dia == 3:
        return "Miércoles"
    elif dia == 4:
        return "Jueves"
    elif dia == 5:
        return "Viernes"
    elif dia == 6:
        return "Sábado"
    elif dia == 7:
        return "Domingo"
    else:
        return "Error: El número debe estar entre 1 y 7."

def main() -> None:
    num = int(input("Introduce un número del 1 al 7: "))
    resultado = dia_semana(num)
    if "Error" in resultado:
        print(resultado)
    else:
        print(f"El día es: {resultado}")

if __name__ == "__main__":
    main()
    