"""
    GENERADOR DE NOMBRES EN PYTHON SIN LISTAS

    Este programa solicita información al usuario y genera un nombre combinando
    los datos ingresados con algunas operaciones básicas.

    Métodos utilizados:
    - Concatenación de cadenas (`+`)
    - Uso de variables con `input()`
    - Generación de valores numéricos con operaciones básicas
"""

# Solicitar datos al usuario
nombre = input("Ingresa tu primer nombre: ")
apellido = input("Ingresa tu apellido: ")
año_nacimiento = int(input("Ingresa tu año de nacimiento: "))

# Generación de identificador basado en datos del usuario
identificador = año_nacimiento % 100  # Últimos dos dígitos del año
nombre_generado = nombre + apellido + str(identificador)

print("Nombre generado:", nombre_generado)

# MINITAREA
"""
1) Pedir un nombre y un número, luego concatenarlos para formar un identificador único.
2) Solicitar dos palabras y unirlas con un guion entre ellas.
3) Generar un nombre basado en iniciales (primeras letras del nombre y apellido).
4) Pedir un nombre y mostrarlo en mayúsculas junto con su cantidad de caracteres.
"""

print("Has aprendido a generar nombres sin colecciones en Python. Completa la mini tarea para reforzar tu conocimiento.")