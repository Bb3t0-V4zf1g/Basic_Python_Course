# Estas funciones se definen utilizando "def" y pueden aceptar parámetros y retornar valores.
def saludar():
    """Función simple que imprime un saludo."""
    print("¡Hola! Esta es una función definida de forma convencional.")


def sumar(a, b):
    """Suma dos números y retorna el resultado."""
    return a + b


# Uso de funciones convencionales:
saludar()
resultado = sumar(3, 7)
print("La suma es:", resultado)

# =====================================================
# 2. FUNCIONES LAMBDA (ANÓNIMAS)
# =====================================================
# Las funciones lambda son funciones pequeñas, anónimas, definidas en una sola línea.
# Se usan cuando se requiere una función sencilla y no es necesaria su reutilización.
cuadrado = lambda x: x ** 2
suma_lambda = lambda a, b: a + b

print("\nEl cuadrado de 5 (lambda) es:", cuadrado(5))
print("La suma (lambda) de 10 y 15 es:", suma_lambda(10, 15))


# =====================================================
# 3. FUNCIONES RECURSIVAS
# =====================================================
# Una función recursiva se llama a sí misma para resolver un problema dividiéndolo en subproblemas.
def factorial(n):
    """
    Calcula el factorial de un número de manera recursiva.

    Parámetro:
        n (int): Un entero no negativo.

    Retorna:
        int: Factorial de n.
    """
    # Caso base: 0! o 1! = 1
    if n == 0 or n == 1:
        return 1
    else:
        # Llamada recursiva
        return n * factorial(n - 1)


print("\nEl factorial de 5 es:", factorial(5))


# =====================================================
# 4. FUNCIONES GENERADORAS
# =====================================================
# Las funciones generadoras permiten crear iteradores utilizando la palabra clave yield,
# retornando valores uno a la vez y pausando su estado hasta la siguiente iteración.
def generador_fibonacci(cantidad):
    """
    Genera una secuencia de números de Fibonacci.

    Parámetro:
        cantidad (int): Número de elementos a generar.

    Yields:
        int: El siguiente número en la secuencia Fibonacci.
    """
    a, b = 0, 1
    for _ in range(cantidad):
        yield a
        a, b = b, a + b


print("\nSecuencia Fibonacci (primeros 10 números):")
for numero in generador_fibonacci(10):
    print(numero, end=" ")
print()


# =====================================================
# 5. FUNCIONES DE ORDEN SUPERIOR
# =====================================================
# Las funciones de orden superior son aquellas que pueden recibir otras funciones
# como parámetros o retornar funciones.
#
# Ejemplo 1: Función que recibe otra función y la aplica a cada elemento de una lista.
def aplicar_funcion(func, lista):
    """
    Aplica la función 'func' a cada elemento de 'lista' y retorna una lista con los resultados.

    Parámetros:
        func (function): Función a aplicar.
        lista (list): Lista de elementos.

    Retorna:
        list: Lista con los resultados.
    """
    return [func(item) for item in lista]


# Utilizando una función lambda para obtener el doble de cada número.
numeros = [1, 2, 3, 4, 5]
dobles = aplicar_funcion(lambda x: x * 2, numeros)
print("\nDoble de cada número:", dobles)


# Ejemplo 2: Función que retorna otra función (closure).
def crear_multiplicador(factor):
    """
    Retorna una función que multiplica su argumento por un 'factor' dado.

    Parámetro:
        factor (int o float): El factor de multiplicación.

    Retorna:
        function: Una función que multiplica su entrada por 'factor'.
    """

    def multiplicar(numero):
        return numero * factor

    return multiplicar


# Crear una función que duplica
duplicar = crear_multiplicador(2)
print("Duplicar 7:", duplicar(7))
# Crear una función que triplica
triplicar = crear_multiplicador(3)
print("Triplicar 7:", triplicar(7))