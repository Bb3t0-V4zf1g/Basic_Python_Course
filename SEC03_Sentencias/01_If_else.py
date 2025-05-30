"""
    SENTENCIA IF-ELSE EN PYTHON

    La sentencia if-else permite ejecutar un bloque de código si se cumple
    una condición, y otro bloque en caso contrario.

    Estructura básica:

    if condición:
        # Código si la condición es verdadera
    else:
        # Código si la condición es falsa

    Ejemplo básico:

    edad = 18
    if edad >= 18:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")
"""

# Ejemplo 1: Determinar si un número es positivo o negativo
numero = int(input("Ingresa un número: "))

if numero > 0:
    print("El número es positivo.")
else:
    print("El número es negativo o cero.")

# Ejemplo 2: Verificación de acceso por edad
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Puedes acceder al contenido para adultos.")
else:
    print("Acceso restringido para menores de edad.")

# Ejemplo 3: Verificación de contraseña correcta
contraseña_guardada = "segura123"
contraseña_usuario = input("Ingresa la contraseña: ")

if contraseña_usuario == contraseña_guardada:
    print("Acceso permitido.")
else:
    print("Acceso denegado.")

# MINITAREA
"""
1) Pedir un número al usuario y verificar si es par o impar.
2) Preguntar al usuario su calificación en un examen (0-100). 
   Si es 60 o más, mostrar "Aprobaste", de lo contrario, "Reprobaste".
3) Solicitar dos números y mostrar cuál es el mayor o si son iguales.
4) Pedir un año y verificar si es bisiesto (divisible entre 4 pero no entre 100, 
   excepto si es divisible entre 400).
"""

print("Has aprendido sobre la sentencia if-else. Completa la mini tarea para reforzar tu conocimiento.")