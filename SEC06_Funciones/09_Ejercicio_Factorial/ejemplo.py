"""
PROGRAMA: CÁLCULO DEL FACTORIAL CON RECURSIVIDAD

Este programa define una función recursiva para calcular el factorial de un número.

Métodos utilizados:
- Definición de funciones con `def`
- Uso de recursividad para calcular el factorial
- Manejo de errores para garantizar que el usuario ingrese un número válido
"""

def factorial(n):
    """
    Calcula el factorial de un número de manera recursiva.

    Parámetro:
      n (int): Número entero para calcular su factorial.

    Retorna:
      int: Factorial de n.

    Casos:
      - factorial(0) = 1  (caso base)
      - factorial(n) = n * factorial(n - 1)  para n > 0
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    if n == 0 or n == 1:
        return 1  # Caso base
    return n * factorial(n - 1)

try:
    numero = int(input("Ingresa un número entero para calcular su factorial: "))
    print(f"\n✅ El factorial de {numero} es: {factorial(numero)}")
except ValueError:
    print("❌ Error: Ingresa un número entero válido.")