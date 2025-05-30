"""
    La función input() permite al usuario ingresar datos desde el teclado.
    Siempre devuelve un string, por lo que a veces se debe convertir el tipo.
"""

# Pedir nombre y edad al usuario
nombre = input("¿Cuál es tu nombre? ")
edad = input("¿Cuántos años tenés? ")

# Convertimos edad a entero para operar con ella
edad = int(edad)

# Mostrar resultado
print(f"Hola {nombre}, el año que viene tendrás {edad + 1} años.")

# EJERCICIO:
# Pedir al usuario su nombre, ciudad y si le gusta Python, y mostrar un mensaje

nombre = input("¿Cómo te llamás? ")
ciudad = input("¿De qué ciudad sos? ")
gusta_python = input("¿Te gusta Python? (sí/no) ")

print(f"{nombre} vive en {ciudad} y {'sí le gusta' if gusta_python.lower() == 'sí' else 'no le gusta'} Python.")
