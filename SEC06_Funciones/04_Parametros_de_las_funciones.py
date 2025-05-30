# En este curso se explica cómo definir funciones usando diversos tipos
# de parámetros en Python para lograr mayor flexibilidad en las llamadas.

# -----------------------------------------------------
# 1. PARÁMETROS OBLIGATORIOS
# -----------------------------------------------------
def saludar(nombre):
    """
    Imprime un saludo usando un parámetro obligatorio.

    Parámetro:
      nombre (str): El nombre de la persona a saludar.
    """
    print("Hola,", nombre)


# Uso de la función con el parámetro obligatorio.
saludar("Alberto")


# La llamada sin argumentos, saludar(), generaría un error.

# -----------------------------------------------------
# 2. PARÁMETROS CON VALORES POR DEFECTO
# -----------------------------------------------------
def saludar_con_default(nombre="Usuario"):
    """
    Saluda utilizando un valor por defecto si no se proporciona el nombre.

    Parámetro:
      nombre (str): Nombre de la persona. Por defecto es "Usuario".
    """
    print("Hola,", nombre)


# Llamadas:
saludar_con_default()  # Usa el valor por defecto.
saludar_con_default("Ana")  # Sobrescribe el valor por defecto.


# -----------------------------------------------------
# 3. PARÁMETROS POSICIONALES ÚNICAMENTE
# -----------------------------------------------------
# Disponibles en Python 3.8 y superiores, se utilizan el símbolo "/"
# para indicar que los parámetros anteriores deben pasarse únicamente de forma posicional.
def dividir(numerador, denominador, /):
    """
    Divide dos números obligando a que se invoque con argumentos posicionales.

    Parámetros:
      numerador (numérico): El numerador.
      denominador (numérico): El denominador.

    Retorna:
      float: El resultado de numerador / denominador.
    """
    return numerador / denominador


resultado = dividir(10, 2)  # Llamada correcta.
print("El resultado de dividir es:", resultado)


# La siguiente llamada produciría error, ya que se están usando nombres:
# dividir(numerador=10, denominador=2)

# -----------------------------------------------------
# 4. PARÁMETROS OBLIGATORIOS COMO KEYWORD-ONLY
# -----------------------------------------------------
# Utilizando un asterisco (*) en la definición, se fuerza a que los parámetros que siguen
# deben especificarse como argumentos con palabra clave.
def configurar_persona(*, nombre, edad):
    """
    Requiere que los parámetros se pasen como argumentos de palabra clave.

    Parámetros:
      nombre (str): Nombre de la persona.
      edad (int): Edad de la persona.
    """
    print(f"Nombre: {nombre}, Edad: {edad}")


# Uso correcto: los argumentos se pasan con clave.
configurar_persona(nombre="Mariana", edad=25)


# La siguiente llamada causaría error:
# configurar_persona("Mariana", 25)

# -----------------------------------------------------
# 5. COMBINACIÓN DE PARÁMETROS: REGULARES, *args Y **kwargs
# -----------------------------------------------------
def ejemplo_completo(a, b=2, *args, c, d=4, **kwargs):
    """
    Función que combina varios tipos de parámetros:
      - a: Parametro obligatorio.
      - b: Parámetro con valor por defecto.
      - *args: Argumentos posicionales adicionales.
      - c: Parámetro obligatorio que debe pasarse como keyword (después del *).
      - d: Parámetro keyword-only con valor por defecto.
      - **kwargs: Argumentos adicionales con claves.

    Muestra cada uno de los parámetros recibidos.
    """
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("c (keyword-only obligatoria):", c)
    print("d (keyword-only, default=4):", d)
    print("kwargs:", kwargs)


# Llamada combinada:
ejemplo_completo(1, 3, 5, 7, c=10, d=20, e=30, f=40)


# -----------------------------------------------------
# 6. ANOTACIONES DE TIPOS EN LOS PARÁMETROS
# -----------------------------------------------------
def potencia(base: float, exponente: int) -> float:
    """
    Calcula la potencia de una base elevada a un exponente.

    Parámetros:
      base (float): La base numérica.
      exponente (int): El exponente.

    Retorna:
      float: El resultado de base ** exponente.
    """
    return base ** exponente


resultado = potencia(2.0, 3)
print("2.0 elevado a 3 es:", resultado)