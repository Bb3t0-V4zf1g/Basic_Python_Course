"""
    BUCLE WHILE EN PYTHON

    El bucle while se usa cuando se quiere repetir una acción mientras se cumple una condición.

    Sintaxis:

    while condición:
        # Código dentro del bucle

    Este bucle continuará ejecutándose hasta que la condición sea falsa.

    Ejemplo:

    contador = 1
    while contador <= 5:
        print("Iteración:", contador)
        contador += 1  # Incremento para evitar un bucle infinito
"""

# Ejemplo 1: Contar del 1 al 10 usando while
contador = 1
while contador <= 10:
    print("Número:", contador)
    contador += 1

# Ejemplo 2: Pedir al usuario una contraseña hasta que sea correcta
contraseña_correcta = "python123"
contraseña = input("Ingresa la contraseña: ")

while contraseña != contraseña_correcta:
    print("Contraseña incorrecta. Inténtalo de nuevo.")
    contraseña = input("Ingresa la contraseña: ")

print("Acceso permitido.")

# Ejemplo 3: Validar entrada numérica
numero = int(input("Ingresa un número positivo: "))

while numero <= 0:
    print("El número debe ser positivo.")
    numero = int(input("Ingresa un número positivo: "))

print("Número válido:", numero)

# Ejemplo 4: Sumar números ingresados hasta que el usuario escriba "0"
suma = 0
num = int(input("Ingresa un número (0 para salir): "))

while num != 0:
    suma += num
    num = int(input("Ingresa otro número (0 para salir): "))

print("Suma total:", suma)

# MINITAREA
"""
1) Crear un bucle que imprima los números del 100 al 90 en orden descendente.
2) Pedir una palabra y repetirla cinco veces usando while.
3) Hacer un programa que pida al usuario un número y siga pidiendo hasta que ingrese un múltiplo de 7.
4) Crear un juego donde el usuario debe adivinar un número secreto (definido por el programador).
"""

print("Has aprendido sobre el bucle while en Python. Completa la mini tarea para reforzar tu conocimiento.")