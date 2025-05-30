# Las funciones son bloques de código reutilizables que realizan
# una tarea específica. Permiten organizar y estructurar mejor el código.
# =====================================================
# 1. DEFINICIÓN DE FUNCIONES BÁSICAS
# =====================================================
def saludar():
    """Imprime un saludo simple."""
    print("Hola, bienvenido a Python!")


# Llamamos a la función
saludar()


# =====================================================
# 2. FUNCIONES CON PARÁMETROS
# =====================================================
def saludar_persona(nombre):
    """Imprime un saludo personalizado.

    Parámetro:
        nombre (str): El nombre de la persona a saludar.
    """
    print(f"Hola, {nombre}!")


saludar_persona("Alberto")


# =====================================================
# 3. FUNCIONES CON VALORES DE RETORNO
# =====================================================
def sumar(a, b):
    """Suma dos números y retorna el resultado.

    Parámetros:
        a (int o float): Primer número.
        b (int o float): Segundo número.

    Retorna:
        int o float: La suma de a y b.
    """
    return a + b


resultado = sumar(3, 5)
print("La suma es:", resultado)


# =====================================================
# 4. PARÁMETROS POR DEFECTO
# =====================================================
def saludar_con_nombre(nombre="Usuario"):
    """Saluda utilizando un nombre, usando un valor por defecto si no se especifica."""
    print(f"Hola, {nombre}!")


# Llamada sin pasar argumento, usa el valor por defecto.
saludar_con_nombre()
# Llamada pasando un argumento.
saludar_con_nombre("Ana")


# =====================================================
# 5. ARGUMENTOS VARIABLES
# =====================================================
# 5.1 Uso de *args para recibir un número variable de argumentos posicionales.
def sumar_varios(*numeros):
    """Suma todos los números recibidos como argumentos.

    Parámetro:
        *numeros: Secuencia de números a sumar.

    Retorna:
        int o float: La suma total.
    """
    suma = 0
    for n in numeros:
        suma += n
    return suma


print("Suma de varios números (1, 2, 3, 4):", sumar_varios(1, 2, 3, 4))


# 5.2 Uso de **kwargs para recibir argumentos con clave.
def imprimir_informacion(**info):
    """Imprime pares clave:valor de la información proporcionada.

    Parámetro:
        **info: Argumentos de palabra clave (ej. nombre="Alberto", edad=30).
    """
    for clave, valor in info.items():
        print(f"{clave}: {valor}")


print("\nInformación del usuario:")
imprimir_informacion(nombre="Alberto", edad=30, ciudad="Colima")

# =====================================================
# 6. FUNCIONES LAMBDA (ANÓNIMAS)
# =====================================================
# Las funciones lambda son funciones pequeñas definidas en una sola línea.
cuadrado = lambda x: x ** 2
print("\nEl cuadrado de 5 es:", cuadrado(5))

# Otra lambda que sume dos números:
suma_lambda = lambda a, b: a + b
print("La suma (lambda) de 7 y 8 es:", suma_lambda(7, 8))


# =====================================================
# 7. DOCUMENTACIÓN DE FUNCIONES (DOCSTRINGS)
# =====================================================
def multiplicar(a, b):
    """
    Multiplica dos números y retorna el resultado.

    Parámetros:
        a (int o float): Primer número.
        b (int o float): Segundo número.

    Retorna:
        int o float: Resultado de la multiplicación.
    """
    return a * b


print("\nEl producto de 4 y 5 es:", multiplicar(4, 5))
print("Documentación de la función 'multiplicar':")
print(multiplicar.__doc__)


# =====================================================
# 8. FUNCIONES RECURSIVAS
# =====================================================
def factorial(n):
    """
    Calcula el factorial de un número de forma recursiva.

    Parámetro:
        n (int): Un número entero no negativo.

    Retorna:
        int: Factorial de n.

    Ejemplo:
        factorial(5) retorna 120 porque 5! = 5 * 4 * 3 * 2 * 1 = 120.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print("\nEl factorial de 5 es:", factorial(5))


# =====================================================
# 9. MINI TAREA
# =====================================================
# Ejercicio 1:
# Define una función que reciba una lista de números y retorne el promedio de sus valores.
def promedio(lista):
    """
    Calcula el promedio de una lista de números.

    Parámetro:
        lista (list): Lista de números (int o float).

    Retorna:
        float: Promedio de los números. Retorna None si la lista está vacía.
    """
    if not lista:
        return None
    return sum(lista) / len(lista)


numeros_usuario = [10, 20, 30, 40, 50]
print("\nEl promedio de", numeros_usuario, "es:", promedio(numeros_usuario))


# Ejercicio 2:
# Crea una función que reciba una cadena y retorne un diccionario,
# donde las claves sean los caracteres y los valores la cantidad de veces que aparecen en la cadena.
def frecuencia_caracteres(cadena):
    """
    Calcula la frecuencia de cada carácter en una cadena.

    Parámetro:
        cadena (str): La cadena a analizar.

    Retorna:
        dict: Un diccionario con cada carácter y su frecuencia de aparición.
    """
    frecuencia = {}
    for char in cadena:
        frecuencia[char] = frecuencia.get(char, 0) + 1
    return frecuencia


cadena_ejemplo = "hola mundo"
print("\nFrecuencia de caracteres en '{}':".format(cadena_ejemplo))
print(frecuencia_caracteres(cadena_ejemplo))