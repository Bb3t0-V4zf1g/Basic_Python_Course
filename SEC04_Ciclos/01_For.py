"""
    BUCLE FOR EN PYTHON

    El bucle for se usa para iterar sobre una secuencia (listas, cadenas, rangos, etc.).

    Sintaxis básica:

    for variable in secuencia:
        # Código dentro del bucle

    Ejemplo:

    for i in range(5):
        print("Iteración:", i)
"""

# Ejemplo 1: Iterar sobre una lista
frutas = ["manzana", "banana", "uva", "naranja"]
for fruta in frutas:
    print("Fruta:", fruta)

# Ejemplo 2: Iterar sobre una cadena de texto
palabra = "Python"
for letra in palabra:
    print("Letra:", letra)

# Ejemplo 3: Usar range para generar números
for numero in range(1, 6):  # Del 1 al 5
    print("Número:", numero)

# Ejemplo 4: Iterar con valores en una lista y aplicar una operación
precios = [10, 20, 30, 40]
for precio in precios:
    precio_con_descuento = precio * 0.9  # Aplicar 10% de descuento
    print("Precio original:", precio, "- Con descuento:", precio_con_descuento)

# Ejemplo 5: Recorrer índices con range y len
colores = ["rojo", "verde", "azul"]
for i in range(len(colores)):
    print(f"Color en índice {i}: {colores[i]}")

# MINITAREA
"""
1) Pedir una palabra al usuario y mostrar cada letra en una línea.
2) Solicitar un número y generar su tabla de multiplicar (del 1 al 10).
3) Crear una lista de nombres y mostrar solo los que tengan más de 5 letras.
4) Generar una lista de números del 1 al 20 y mostrar solo los pares.
"""

print("Has aprendido sobre el bucle for en Python. Completa la mini tarea para reforzar tu conocimiento.")