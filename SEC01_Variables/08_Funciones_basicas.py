"""
    FUNCIONES BÁSICAS MÁS USADAS EN PYTHON

    Estas funciones son integradas y se usan frecuentemente en casi todos los programas:

    print(): muestra información en pantalla
    input(): pide datos al usuario
    type(): muestra el tipo de dato
    len(): cuenta la cantidad de caracteres (en una cadena)
    int(), float(), str(): convierten tipos de datos
    in: verifica si un valor está contenido dentro de otro
"""

# print(): muestra datos
print("Hola mundo")

# input(): recibe datos del usuario
nombre = input("¿Cómo te llamás? ")

# type(): muestra tipo de dato
print(type(nombre))

# len(): cuenta caracteres
print(f"Tu nombre tiene {len(nombre)} letras")

# Conversión de tipos
edad = int(input("¿Cuántos años tenés? "))
altura = float(input("¿Cuál es tu altura en metros? "))

# Mostrar todo junto
print(f"{nombre} tiene {edad} años y mide {altura} metros")

# in: verificar si algo está dentro de una cadena
print("a" in nombre)  # True si la letra "a" está en el nombre

# EJERCICIO:
# Pedir al usuario su frase favorita y mostrar:
# - Cuántos caracteres tiene
# - Si contiene la palabra "Python"
# - La frase en mayúsculas

