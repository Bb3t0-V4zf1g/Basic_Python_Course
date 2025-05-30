# Estos mecanismos son muy útiles para crear funciones flexibles y reutilizables,
# permitiendo que la función acepte más argumentos de los que se definieron inicialmente.

# =====================================================
# 1. USO DE *args
# =====================================================
def imprimir_argumentos(*args):
    """
    Imprime todos los argumentos posicionales recibidos.

    *args: Una tupla que contiene todos los argumentos posicionales adicionales.
    """
    print("Argumentos posicionales recibidos:", args)


# Uso del *args
imprimir_argumentos(1, 2, 3, "cuatro", [5, 6], {"siete": 7})


# =====================================================
# 2. USO DE **kwargs
# =====================================================
def imprimir_kwargs(**kwargs):
    """
    Imprime todos los argumentos con clave recibidos.

    **kwargs: Un diccionario que contiene todos los argumentos nombrados adicionales.
    """
    print("Argumentos clave-valor recibidos:", kwargs)


# Uso del **kwargs
imprimir_kwargs(nombre="Alberto", edad=30, ciudad="Colima")


# =====================================================
# 3. COMBINANDO ARGUMENTOS REGULARES, *args Y **kwargs
# =====================================================
def funcion_completa(a, b, *args, **kwargs):
    """
    Demuestra cómo combinar:
    - Parámetros requeridos: a, b.
    - Argumentos posicionales adicionales (*args).
    - Argumentos con clave adicionales (**kwargs).

    Parámetros:
      a, b: Argumentos obligatorios.
      *args: Tupla con argumentos posicionales extra.
      **kwargs: Diccionario con argumentos de palabra clave extra.
    """
    print("Argumento a:", a)
    print("Argumento b:", b)
    print("Argumentos posicionales adicionales (*args):", args)
    print("Argumentos con clave adicionales (**kwargs):", kwargs)


# Llamada combinada
funcion_completa(10, 20, 30, 40, 50, clave1="valor1", clave2="valor2")

# =====================================================
# 4. DESEMPACAR ESTRUCTURAS CON * Y **
# =====================================================
# 4.1 Desempaquetar una lista o tupla usando *
lista_numeros = [1, 2, 3, 4, 5]


def sumar(a, b, c, d, e):
    """Suma cinco números."""
    return a + b + c + d + e


# Usamos * para desempaquetar la lista y pasar cada elemento como argumento
print("\nSuma de lista (usando *):", sumar(*lista_numeros))

# 4.2 Desempaquetar un diccionario usando **
# Definimos un diccionario con los parámetros requeridos por la función
parametros = {"a": 10, "b": 20}


def multiplicar(a, b):
    """Multiplica dos números."""
    return a * b


# Usamos ** para desempaquetar el diccionario y pasar cada par clave-valor como argumento
print("Producto (usando **):", multiplicar(**parametros))


# =====================================================
# 5. MINI TAREA
# =====================================================
# Ejercicio:
# Define una función llamada "estadisticas" que reciba un número variable de valores
# y un número variable de parámetros con clave. La función debe:
#   - Calcular y retornar el promedio de los valores recibidos por *args.
#   - Imprimir los parámetros adicionales recibidos por **kwargs.
# Por ejemplo:
#   estadisticas(10, 20, 30, nombre="Alberto", curso="Python")
# Debe mostrar:
#   Promedio: 20.0
#   Parámetros adicionales: {'nombre': 'Alberto', 'curso': 'Python'}

def estadisticas(*args, **kwargs):
    """
    Calcula el promedio de los valores en *args y muestra los **kwargs.

    Parámetros:
      *args: Una secuencia de números.
      **kwargs: Parámetros adicionales en forma de diccionario.

    Retorna:
      float: El promedio de los elementos de *args.
    """
    if args:
        promedio = sum(args) / len(args)
    else:
        promedio = 0

    print("Parámetros adicionales recibidos:", kwargs)
    return promedio


# Prueba de la función "estadisticas"
promedio_resultado = estadisticas(10, 20, 30, 40, nombre="Alberto", curso="Python")
print("Promedio:", promedio_resultado)