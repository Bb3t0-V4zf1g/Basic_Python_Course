"""
    WHILE NOT EN PYTHON

    La estructura while permite ejecutar un bloque de código repetidamente
    mientras se cumpla una condición. La combinación con `not` invierte la lógica,
    ejecutando el bucle mientras la condición NO sea verdadera.

    Sintaxis básica:

    while not condición:
        # Código dentro del bucle

    Ejemplo:

    contraseña = ""
    while not contraseña:
        contraseña = input("Ingresa tu contraseña: ")
    print("Contraseña guardada correctamente.")
"""

# Ejemplo 1: Repetir hasta que el usuario ingrese un número mayor a 10
numero = int(input("Ingresa un número mayor a 10: "))

while not numero > 10:
    print("Número inválido. Debe ser mayor a 10.")
    numero = int(input("Intenta nuevamente: "))

print("Número válido:", numero)

# Ejemplo 2: Esperar a que el usuario introduzca una respuesta válida
respuesta = input("Escribe 'sí' para continuar: ")

while not respuesta.lower() == "sí":
    print("Entrada inválida. Debes escribir 'sí'.")
    respuesta = input("Intenta nuevamente: ")

print("¡Continuamos con el programa!")

# Ejemplo 3: Validar una contraseña hasta que sea correcta
contraseña_correcta = "python123"
contraseña = input("Ingresa la contraseña: ")

while not contraseña == contraseña_correcta:
    print("Contraseña incorrecta. Intenta de nuevo.")
    contraseña = input("Ingresa la contraseña: ")

print("Acceso concedido.")

# MINITAREA
"""
1) Pedir un número al usuario y repetir hasta que ingrese un número positivo.
2) Solicitar una palabra y repetir hasta que contenga al menos 5 caracteres.
3) Pedir una temperatura y repetir hasta que el usuario ingrese un valor mayor a 0.
4) Crear un sistema que pida un código de acceso hasta que el usuario ingrese 'admin123'.
"""

print("Has aprendido sobre while not en Python. Completa la mini tarea para reforzar tu conocimiento.")