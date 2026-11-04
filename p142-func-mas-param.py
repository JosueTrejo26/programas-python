# p142-func-mas-param.py
# Uso de *args para recibir múltiples argumentos variables

def saludatodos(*todos: str) -> None:
    # todos es una tupla, por ejemplo: ('Juan', 'Pedro', 'Luis') 
    for nombre in todos:
        print(f"Saludos a {nombre}")

saludatodos("Juan", "Pedro", "Luis")
