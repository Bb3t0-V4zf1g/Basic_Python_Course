"""
EJERCICIO: MAYOR DE EDAD USANDO FUNCIONES EN PYTHON

Este programa solicita la edad del usuario y determina si es mayor o menor de edad,
permitiendo reutilizar la lógica mediante funciones.

Métodos utilizados:
- Definición de funciones con `def`
- Entrada del usuario con `input()`
- Conversión de datos con `int()`
- Uso de condicionales (`if-elif-else`)
- Validaciones para evitar datos incorrectos
"""

def verificar_mayoria_edad(edad):
    """
    Evalúa si la edad ingresada corresponde a una persona mayor o menor de edad.

    Parámetro:
        edad (int): Edad ingresada por el usuario.

    Retorna:
        str: Mensaje indicando si es mayor, menor de edad o si la entrada es inválida.
    """
    if edad < 0:
        return "Error: La edad no puede ser negativa."
    elif edad >= 18:
        return "Eres mayor de edad."
    else:
        return f"Eres menor de edad. Te faltan {18 - edad} años para ser mayor de edad."

def solicitar_edad():
    """
    Solicita la edad al usuario y la valida.

    Retorna:
        int: Edad ingresada por el usuario o None si la entrada no es válida.
    """
    try:
        edad = int(input("Ingresa tu edad: "))
        return edad
    except ValueError:
        print("Error: Ingresa un número válido.")
        return None

# Ejecutar el programa
edad_usuario = solicitar_edad()
if edad_usuario is not None:
    print(verificar_mayoria_edad(edad_usuario))

# =====================================================
# MINITAREA:
# =====================================================
"""
Ejercicios para mejorar el programa:
1) Agregar una opción que permita evaluar si el usuario puede acceder a contenido restringido (mayores de 21 años).
2) Modificar el programa para que permita repetir la consulta hasta que el usuario ingrese "salir".
3) Incorporar validaciones adicionales, como impedir que el usuario ingrese edades irreales (ejemplo: más de 120 años).
"""