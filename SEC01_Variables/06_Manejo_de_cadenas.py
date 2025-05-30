"""
    Una cadena (string) es una secuencia de caracteres.
    Podemos acceder a cada carácter usando índices y realizar operaciones básicas sobre las cadenas.
"""

mensaje = "Hola Mundo"

# Acceder a caracteres individuales (indexado)
print(mensaje[0])  # H
print(mensaje[-1]) # o (último carácter)

# Cortar la cadena (slicing)
print(mensaje[0:4])    # Hola
print(mensaje[5:])     # Mundo
print(mensaje[:])      # Hola Mundo (copia completa)
print(mensaje[::-1])   # odnuM aloH (reversa)

# Concatenar cadenas
nombre = "Ana"
saludo = "Hola " + nombre
print(saludo)

# Repetir cadenas
eco = "Hey! " * 3
print(eco)

# Interpolación con f-string
edad = 25
print(f"{nombre} tiene {edad} años.")

# EJERCICIO:
# Crear una variable tipo string con tu nombre completo, mostrar tu nombre completo al revés, y luego mostrar solo tu primer nombre.

