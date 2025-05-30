"""
SISTEMA: VALOR POSITIVO O NEGATIVO EN PYTHON

Este programa evalúa si un número ingresado por el usuario es positivo, negativo o cero.

Métodos utilizados:
- Entrada del usuario con input() y conversión a float.
- Uso de condicionales (if, elif, else) para determinar la naturaleza del número.
"""

# Solicitar al usuario que ingrese un número (se usa float para admitir decimales)
numero = float(input("Ingresa un número: "))

# Evaluar y mostrar si el número es positivo, negativo o cero
if numero > 0:
    print("El valor es positivo.")
elif numero < 0:
    print("El valor es negativo.")
else:
    print("El valor es cero.")

# =====================================================
# MINITAREA:
# =====================================================
"""
Ejercicios para ampliar el programa:
1) Modificar el programa para que, si el número es entero, indique además si es par o impar.
   - Para ello, primero verifica si el número ingresado es entero (por ejemplo, comparando 
     int(numero) y numero).
   - Si es entero, utiliza el operador módulo (%) para determinar si es par (n % 2 == 0) o impar.
   
2) Ampliar el programa para que solicite repetidamente números hasta que el usuario ingrese
   la palabra "salir". Cada número debe evaluarse y mostrarse su condición (positivo, 
   negativo, cero y, en caso de ser entero, par o impar).

3) Agregar validaciones para asegurarte de que el usuario ingrese un valor numérico válido 
   o la palabra "salir", manejando adecuadamente entradas incorrectas.
"""