"""
Las funciones recursivas se utilizan para resolver problemas dividiéndolos en
instancias de un problema similar, pero de menor complejidad. Cada función recursiva
debe definir:
  - Un caso base que detiene la recursión.
  - Un caso recursivo en el que la función se llama a sí misma con parámetros
    reducidos o modificados.
A continuación se presentan varios ejemplos de funciones recursivas.
"""


# -----------------------------------------------------
# Ejemplo 1: Factorial
# -----------------------------------------------------
def factorial(n):
    """
    Calcula el factorial de un número n (n!) de forma recursiva.

    Parámetro:
      n (int): Un entero no negativo.

    Retorna:
      int: El valor de n!.

    Casos:
      - factorial(0) = 1  (caso base)
      - factorial(n) = n * factorial(n - 1)  para n > 0
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    if n == 0 or n == 1:
        return 1  # Caso base
    return n * factorial(n - 1)


print("Factorial de 5 es:", factorial(5))


# -----------------------------------------------------
# Ejemplo 2: Secuencia de Fibonacci
# -----------------------------------------------------
def fibonacci(n):
    """
    Retorna el n-ésimo número de la secuencia de Fibonacci de forma recursiva.

    Parámetro:
      n (int): Índice en la secuencia (donde fibonacci(0)=0 y fibonacci(1)=1).

    Retorna:
      int: El n-ésimo número de la secuencia.

    Casos:
      - fibonacci(0) = 0, fibonacci(1) = 1  (casos base)
      - fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2) para n > 1
    """
    if n < 0:
        raise ValueError("El índice de Fibonacci no puede ser negativo.")
    if n == 0:
        return 0  # Caso base
    if n == 1:
        return 1  # Caso base
    return fibonacci(n - 1) + fibonacci(n - 2)


print("El 7º número de Fibonacci es:", fibonacci(7))


# -----------------------------------------------------
# Ejemplo 3: Suma de dígitos de un número
# -----------------------------------------------------
def suma_digitos(n):
    """
    Calcula la suma de los dígitos de un número de manera recursiva.

    Parámetro:
      n (int): Un número entero.

    Retorna:
      int: La suma de los dígitos del número.

    Ejemplo:
      suma_digitos(1234) retorna 1 + 2 + 3 + 4 = 10.
    """
    n = abs(n)  # Asegurarse de trabajar con el valor absoluto
    if n < 10:
        return n  # Caso base: solo un dígito.
    return (n % 10) + suma_digitos(n // 10)


print("La suma de los dígitos de 1234 es:", suma_digitos(1234))


# -----------------------------------------------------
# Ejemplo 4: Cálculo de potencia
# -----------------------------------------------------
def potencia(b, e):
    """
    Calcula b elevado a la e (b^e) de forma recursiva.

    Parámetros:
      b (float): La base.
      e (int): El exponente, asumiendo que e es un entero no negativo.

    Retorna:
      float: El resultado de b^e.

    Casos:
      - potencia(b, 0) = 1  (caso base)
      - potencia(b, e) = b * potencia(b, e - 1) para e > 0
    """
    if e < 0:
        raise ValueError("Este ejemplo solo maneja exponentes no negativos.")
    if e == 0:
        return 1  # Caso base
    return b * potencia(b, e - 1)


print("2 elevado a 5 es:", potencia(2, 5))


# -----------------------------------------------------
# Ejemplo 5: Máximo Común Divisor (MCD) usando el algoritmo de Euclides
# -----------------------------------------------------
def mcd(a, b):
    """
    Calcula el Máximo Común Divisor (MCD) de dos números a y b usando recursión.

    Parámetros:
      a (int): Primer número.
      b (int): Segundo número.

    Retorna:
      int: El MCD de a y b.

    Algoritmo:
      - MCD(a, 0) = |a|
      - MCD(a, b) = MCD(b, a % b)
    """
    a, b = abs(a), abs(b)  # Trabajar con valores absolutos
    if b == 0:
        return a  # Caso base
    return mcd(b, a % b)


print("El MCD de 48 y 18 es:", mcd(48, 18))


# -----------------------------------------------------
# Ejemplo 6: Suma de elementos en una lista de forma recursiva
# -----------------------------------------------------
def suma_lista(lista):
    """
    Suma recursivamente todos los elementos de una lista.

    Parámetro:
      lista (list): Lista de números.

    Retorna:
      int o float: La suma total de la lista.

    Caso base:
      - Si la lista está vacía, retorna 0.
    """
    if not lista:
        return 0  # Caso base: lista vacía
    return lista[0] + suma_lista(lista[1:])


print("La suma de la lista [1, 2, 3, 4, 5] es:", suma_lista([1, 2, 3, 4, 5]))