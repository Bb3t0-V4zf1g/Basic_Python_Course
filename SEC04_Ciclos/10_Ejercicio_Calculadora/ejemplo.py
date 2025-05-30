"""
PROGRAMA: CALCULADORA BÁSICA EN PYTHON

Este programa permite al usuario realizar operaciones matemáticas como:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)

Métodos utilizados:
- Entrada del usuario con `input()`
- Conversión de datos con `float()`
- Uso de condicionales (`if-elif-else`)
- Manejo de errores con `try-except`
"""

print("Bienvenido a la Calculadora Básica")

# Solicitar números y operación al usuario
try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    operacion = input("Ingresa la operación (+, -, *, /): ")

    # Evaluar la operación ingresada
    if operacion == "+":
        resultado = num1 + num2
    elif operacion == "-":
        resultado = num1 - num2
    elif operacion == "*":
        resultado = num1 * num2
    elif operacion == "/":
        if num2 == 0:
            resultado = "Error: No se puede dividir entre cero."
        else:
            resultado = num1 / num2
    else:
        resultado = "Operación no válida."

    print("Resultado:", resultado)

except ValueError:
    print("Error: Ingresa valores numéricos válidos.")