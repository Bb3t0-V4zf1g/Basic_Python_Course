"""
    OPERADOR TERNARIO EN PYTHON

    El operador ternario permite escribir una condición if-else en una sola línea.

    Sintaxis:

    resultado = valor_si_verdadero if condición else valor_si_falso

    Ejemplo:

    edad = 20
    mensaje = "Eres mayor de edad." if edad >= 18 else "Eres menor de edad."
    print(mensaje)
"""

# Ejemplo 1: Verificar si un número es positivo, negativo o cero
numero = int(input("Ingresa un número: "))
resultado = "Positivo" if numero > 0 else "Negativo o Cero"
print("El número es:", resultado)

# Ejemplo 2: Verificar si un usuario puede acceder a contenido restringido
edad = int(input("Ingresa tu edad: "))
acceso = "Acceso permitido" if edad >= 18 else "Acceso denegado"
print(acceso)

# Ejemplo 3: Determinar si un número es par o impar
num = int(input("Ingresa un número: "))
tipo = "Par" if num % 2 == 0 else "Impar"
print("El número es:", tipo)

# MINITAREA
"""
1) Pedir un número y mostrar si es múltiplo de 5 o no.
2) Solicitar una temperatura y decir si es alta (mayor o igual a 30) o baja.
3) Pedir al usuario su salario y determinar si supera el promedio (mayor o igual a 15,000).
4) Solicitar una contraseña y verificar si coincide con una contraseña predefinida.
"""

print("Has aprendido sobre el operador ternario en Python. Completa la mini tarea para reforzar tu conocimiento.")