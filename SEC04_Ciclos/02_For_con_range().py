"""
    FOR CON RANGE() EN PYTHON

    La función range() genera una secuencia de números y se usa comúnmente en bucles for.

    Sintaxis básica:

    for variable in range(inicio, fin, paso):
        # Código dentro del bucle

    - inicio: número inicial (opcional, por defecto es 0)
    - fin: número donde se detiene la secuencia (no incluido)
    - paso: incremento o decremento (opcional, por defecto es 1)

    Ejemplo:

    for i in range(1, 6):
        print("Número:", i)  # Muestra los números del 1 al 5
"""

# Ejemplo 1: Contar del 1 al 10
for i in range(1, 11):
    print(i)

# Ejemplo 2: Contar de 0 a 4 usando range(5) (sin inicio)
for i in range(5):
    print("Índice:", i)

# Ejemplo 3: Contar de 10 en 10 hasta 100
for i in range(0, 101, 10):
    print("Número:", i)

# Ejemplo 4: Contar en reversa desde 10 hasta 1
for i in range(10, 0, -1):
    print(i)

# Ejemplo 5: Sumar los números del 1 al 100
suma = 0
for i in range(1, 101):
    suma += i
print("La suma de los números del 1 al 100 es:", suma)

# MINITAREA
"""
1) Usar range() para imprimir los números pares del 2 al 20.
2) Contar regresivamente desde 50 hasta 0 de 5 en 5.
3) Crear un rango que muestre los múltiplos de 3 del 3 al 30.
4) Generar la tabla de multiplicar de un número ingresado por el usuario (del 1 al 10).
"""

print("Has aprendido sobre for con range(). Completa la mini tarea para reforzar tu conocimiento.")