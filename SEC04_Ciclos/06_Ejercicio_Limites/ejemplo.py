"""
EJERCICIO: VERIFICACIÓN DE LÍMITES EN PYTHON

Este programa solicita un número al usuario y verifica si está dentro de un rango permitido.

Definición de límites:
- Si el número está entre 10 y 50, se considera dentro del rango.
- Si es menor que 10, se considera fuera del límite inferior.
- Si es mayor que 50, se considera fuera del límite superior.

Métodos utilizados:
- Entrada del usuario con `input()`
- Conversión de datos con `float()`
- Uso de condicionales (`if-elif-else`)
- Validaciones para evitar errores de entrada
"""

try:
    numero = float(input("Ingresa un número: "))

    # Evaluación del número con respecto a los límites
    if 10 <= numero <= 50:
        print("El número está dentro del rango permitido (10-50).")
    elif numero < 10:
        print("El número está fuera del límite inferior.")
    else:
        print("El número está fuera del límite superior.")

except ValueError:
    print("Error: Ingresa un número válido.")