"""
En Python, las funciones pueden definirse para aceptar un número variable
de argumentos. Esto se logra mediante el uso de:
   - *args: Recibe argumentos posicionales adicionales en forma de tupla.
   - **kwargs: Recibe argumentos con clave adicionales en forma de diccionario.
Estos mecanismos permiten que las funciones sean más flexibles y reutilizables,
aceptando diferentes cantidades y tipos de datos sin modificar la definición de la función.
"""


# -----------------------------------------------------
# 1. USO BÁSICO DE *args
# -----------------------------------------------------
def sumar_todos(*args):
    """
    Suma todos los números pasados como argumentos posicionales.

    Parámetros:
      *args: Conjunto de números a sumar.

    Retorna:
      La suma total de los argumentos.
    """
    print("Argumentos posicionales recibidos:", args)
    suma = 0
    for numero in args:
        suma += numero
    return suma


resultado = sumar_todos(1, 2, 3, 4, 5)
print("La suma total es:", resultado)


# -----------------------------------------------------
# 2. USO BÁSICO DE **kwargs
# -----------------------------------------------------
def mostrar_informacion(**kwargs):
    """
    Imprime la información proporcionada en formato clave: valor.

    Parámetros:
      **kwargs: Argumentos de palabra clave.
    """
    print("Argumentos con clave recibidos:", kwargs)
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")


mostrar_informacion(nombre="Juan", edad=28, ciudad="Madrid")


# -----------------------------------------------------
# 3. COMBINANDO ARGUMENTOS REGULARES, *args Y **kwargs
# -----------------------------------------------------
def describir_persona(genero, *hobbies, **otros_datos):
    """
    Describe a una persona mostrando su género, hobbies y otros datos adicionales.

    Parámetros:
      genero (str): Género de la persona.
      *hobbies: Lista de hobbies (argumentos posicionales adicionales).
      **otros_datos: Información adicional (argumentos con clave).
    """
    print("Género:", genero)
    if hobbies:
        print("Hobbies:", hobbies)
    if otros_datos:
        print("Otros datos:")
        for clave, valor in otros_datos.items():
            print(f"  {clave}: {valor}")


describir_persona("Femenino", "Leer", "Bailar", nombre="Ana", edad=32)


# -----------------------------------------------------
# 4. DESENPAQUETAMIENTO DE ESTRUCTURAS CON * Y **
# -----------------------------------------------------
def producto(a, b, c):
    """Calcula el producto de tres números."""
    return a * b * c


# Desempaquetamiento de una lista con * para argumentos posicionales:
numeros = [2, 3, 4]
print("\nProducto usando desempaquetamiento con *:", producto(*numeros))

# Desempaquetamiento de un diccionario con ** para argumentos con clave:
parametros = {"a": 5, "b": 6, "c": 7}
print("Producto usando desempaquetamiento con **:", producto(**parametros))


# -----------------------------------------------------
# 5. MINI TAREA: FUNCIÓN CON ARGUMENTOS VARIABLES
# -----------------------------------------------------
# Definir una función llamada 'procesar_datos' que acepte:
#   - Un argumento obligatorio 'operacion' (cadena que indique la operación: "sumar" o "multiplicar").
#   - Un número variable de valores numéricos (*args).
#   - Argumentos adicionales (**kwargs), que incluyan un mensaje personalizado.
#
# La función debe:
#   - Realizar la operación indicada sobre los valores recibidos.
#   - Imprimir el mensaje (si se proporcionó) junto con el resultado.
#   - Retornar el resultado de la operación.

def procesar_datos(operacion, *args, **kwargs):
    """
    Realiza una operación (suma o multiplicación) sobre un conjunto de números.

    Parámetros:
      operacion (str): "sumar" o "multiplicar".
      *args: Números sobre los cuales aplicar la operación.
      **kwargs: Datos adicionales, por ejemplo un mensaje personalizado.

    Retorna:
      El resultado de la operación realizado sobre los números.
    """
    if operacion == "sumar":
        resultado = sum(args)
    elif operacion == "multiplicar":
        resultado = 1
        for num in args:
            resultado *= num
    else:
        print("Operación no soportada.")
        return None

    mensaje = kwargs.get("mensaje", "El resultado es:")
    print(mensaje, resultado)
    return resultado


# Prueba de la función 'procesar_datos'
procesar_datos("sumar", 10, 20, 30, mensaje="La suma total es:")
procesar_datos("multiplicar", 2, 3, 4, mensaje="El producto total es:")