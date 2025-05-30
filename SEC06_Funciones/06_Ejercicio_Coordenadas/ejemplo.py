"""
PROGRAMA: MANEJO DE COORDENADAS (X, Y) CON FUNCIÓN

Este programa define una función que recibe dos parámetros `x` e `y` y retorna la coordenada formateada.
"""

def obtener_coordenadas(x, y):
    """
    Recibe dos valores numéricos y los retorna en formato de coordenadas (x, y).

    Parámetros:
      x (float): Valor de la coordenada X.
      y (float): Valor de la coordenada Y.

    Retorna:
      tuple: Coordenadas en formato (x, y).
    """
    return (x, y)

# Solicitar datos al usuario
try:
    x = float(input("Ingresa el valor de X: "))
    y = float(input("Ingresa el valor de Y: "))
    coordenada = obtener_coordenadas(x, y)
    print(f"\n✅ Coordenada ingresada: {coordenada}")
except ValueError:
    print("❌ Error: Ingresa valores numéricos válidos.")