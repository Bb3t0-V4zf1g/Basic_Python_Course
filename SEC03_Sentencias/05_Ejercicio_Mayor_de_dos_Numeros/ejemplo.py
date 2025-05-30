"""
EJERCICIO: MAYOR ENTRE DOS NÚMEROS USANDO FUNCIONES EN PYTHON

Este programa define una función que recibe dos números y determina cuál es mayor.

Métodos utilizados:
- Definición de funciones con `def`
- Entrada del usuario con `input()`
- Conversión de datos con `float()`
- Uso de condicionales (`if-elif-else`)
- Validaciones para evitar datos incorrectos
"""

def obtener_mayor(num1, num2):
    """
    Compara dos números y determina cuál es mayor.

    Parámetros:
        num1 (float): Primer número.
        num2 (float): Segundo número.

    Retorna:
        str: Mensaje indicando cuál número es mayor o si son iguales.
    """
    if num1 > num2:
        return f"El número mayor es: {num1}"
    elif num2 > num1:
        return f"El número mayor es: {num2}"
    else:
        return "Ambos números son iguales."

def solicitar_numeros():
    """
    Solicita dos números al usuario, valida la entrada y retorna los valores convertidos a float.

    Retorna:
        tuple: Contiene dos números ingresados por el usuario.
    """
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        return num1, num2
    except ValueError:
        print("Error: Ingresa valores numéricos válidos.")
        return None, None

# Ejecutar el programa
numero1, numero2 = solicitar_numeros()
if numero1 is not None and numero2 is not None:
    print(obtener_mayor(numero1, numero2))

# =====================================================
# MINITAREA:
# =====================================================
"""
Ejercicios para mejorar el programa:
1) Modificar la función `obtener_mayor` para que, si los números son enteros, indique si son pares o impares.
2) Permitir comparar una lista de números en lugar de solo dos, agregando una función `mayor_en_lista(lista)`.
3) Hacer que el programa repita la comparación hasta que el usuario ingrese "salir".
"""