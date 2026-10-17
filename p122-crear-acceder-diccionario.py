# p122-acceder-diccionario.py
# Demuestra cómo crear un diccionario y acceder a sus elementos usando llaves y get()

# 1. Crea un diccionario llamado dias usando llaves numéricas
dias = {
    1: 'Lunes', 
    2: 'Martes', 
    3: 'Miércoles', 
    4: 'Jueves', 
    5: 'Viernes', 
    6: 'Sábado', 
    7: 'Domingo'
}

# 2. Muestra el diccionario completo
print("Diccionario inicial:")
print(dias)

print("\nAccediendo a elementos:")
# 3. Accede y muestra valores específicos
print(f"Llave 1 (con []): {dias[1]}")
print(f"Llave 7 (con []): {dias[7]}")
print(f"Llave 5 (con get()): {dias.get(5)}")
print(f"Llave 7 (con get()): {dias.get(7)}")

# 4. Vuelve a mostrar el diccionario completo
print("\nDiccionario final:")
print(dias)
