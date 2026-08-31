# Ejemplo 4: Conteo descendente v2
# p047-conteo-descendente-v2.py
# Imprime los números de n a 1, en decrementos de m, usando un ci45clo while

print(" Iniciando cuenta regresiva...")
n = int(input("Desde donde ? "))
m = int(input("De cuanto en cuanto ? "))
c = n
while c >= 1:
    print(f" {c}", end=" ") 
    c -= m
print("\n ¡Despegue!")