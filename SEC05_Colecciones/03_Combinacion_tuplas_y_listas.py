# Explicación y ejemplos sobre listas y tuplas, incluyendo conversión entre
# estructuras, combinación y manipulación de datos.

# =====================================================
# 1. CREACIÓN DE LISTAS Y TUPLAS
# =====================================================
# LISTAS: Son estructuras mutables, se definen con corchetes []
lista_frutas = ["manzana", "banana", "cereza"]
print("Lista de frutas:", lista_frutas)

# TUPLAS: Son estructuras inmutables, se definen con paréntesis ()
tupla_frutas = ("manzana", "banana", "cereza")
print("Tupla de frutas:", tupla_frutas)

# =====================================================
# 2. ACCESO A ELEMENTOS EN LISTAS Y TUPLAS
# =====================================================
# Ambos tipos de datos permiten acceder a sus elementos usando índices
print("Primer elemento de la lista:", lista_frutas[0])
print("Último elemento de la tupla:", tupla_frutas[-1])

# =====================================================
# 3. MODIFICACIÓN DE LISTAS VS. INMUTABILIDAD DE TUPLAS
# =====================================================
# Modificación en listas
lista_frutas[1] = "kiwi"
lista_frutas.append("mango")
print("Lista modificada:", lista_frutas)

# Intento de modificación en tuplas (esto genera un error)
try:
    tupla_frutas[1] = "kiwi"
except TypeError as e:
    print("Error al modificar tupla:", e)

# Alternativa: crear una nueva tupla con valores modificados
nueva_tupla_frutas = tupla_frutas[:1] + ("kiwi",) + tupla_frutas[2:]
print("Nueva tupla:", nueva_tupla_frutas)

# =====================================================
# 4. SLICING (REBANADO) EN LISTAS Y TUPLAS
# =====================================================
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tupla_numeros = tuple(numeros)

print("Primeros cinco números (lista):", numeros[0:5])
print("Primeros cinco números (tupla):", tupla_numeros[0:5])
print("Cada dos elementos en la lista:", numeros[::2])
print("Cada dos elementos en la tupla:", tupla_numeros[::2])

# =====================================================
# 5. RECORRIDO DE LISTAS Y TUPLAS
# =====================================================
# Recorrer una lista
print("Recorrido de lista:")
for fruta in lista_frutas:
    print("Fruta:", fruta)

# Recorrer una tupla
print("Recorrido de tupla:")
for fruta in tupla_frutas:
    print("Fruta:", fruta)

# =====================================================
# 6. MÉTODOS ÚTILES EN LISTAS Y TUPLAS
# =====================================================
# Métodos útiles en listas
numeros_lista = [3, 1, 4, 1, 5, 9, 2]
numeros_lista.sort()
print("Lista ordenada:", numeros_lista)

numeros_lista.reverse()
print("Lista invertida:", numeros_lista)

# Métodos útiles en tuplas (count, index)
numeros_tupla = (3, 1, 4, 1, 5, 9, 2)
print("El número 1 aparece:", numeros_tupla.count(1), "veces")
print("El índice del número 5 es:", numeros_tupla.index(5))

# =====================================================
# 7. COMBINACIÓN DE LISTAS Y TUPLAS
# =====================================================
# LISTA CON TUPLAS INTERNAS
productos = [("Laptop", 1200), ("Mouse", 25), ("Teclado", 45)]
print("Lista con tuplas internas:")
for producto in productos:
    print(f"Producto: {producto[0]}, Precio: {producto[1]}")

# TUPLA CON LISTAS INTERNAS (listas dentro de una tupla)
datos = (["Juan", 25], ["María", 30], ["Carlos", 28])
datos[0][1] = 26  # Modificar un valor dentro de la lista
print("Tupla con listas internas modificada:", datos)

# =====================================================
# 8. USO DE ZIP() PARA COMBINAR DATOS
# =====================================================
# Combinar dos listas en una lista de tuplas
nombres = ["Ana", "Luis", "Elena"]
edades = [22, 30, 27]
combinados = list(zip(nombres, edades))
print("Lista de tuplas combinadas:", combinados)

# Extraer listas separadas desde una lista de tuplas
nombres_extraidos, edades_extraidas = zip(*combinados)
print("Nombres extraídos:", nombres_extraidos)
print("Edades extraídas:", edades_extraidas)

# =====================================================
# MINI TAREA: EJERCICIOS PRÁCTICOS
# =====================================================

# Ejercicio 1: Solicitar nombres al usuario, convertirlos en una tupla y mostrar el primero y último.
print("\n--- Ejercicio 1: Tupla de Nombres ---")
entrada_nombres = input("Introduce nombres separados por comas: ")
tupla_nombres_usuario = tuple(entrada_nombres.split(","))
print("Primer nombre:", tupla_nombres_usuario[0])
print("Último nombre:", tupla_nombres_usuario[-1])

# Ejercicio 2: Crear una lista de tuplas con productos y precios, y mostrar los productos caros.
print("\n--- Ejercicio 2: Productos Caros ---")
productos_usuario = [("Laptop", 1200), ("Mouse", 25), ("Teclado", 45), ("Monitor", 200)]
print("Productos con precio mayor a $50:")
for producto in productos_usuario:
    if producto[1] > 50:
        print(producto[0])

# Ejercicio 3: Solicitar dos listas al usuario y combinarlas con zip().
print("\n--- Ejercicio 3: Combinar Listas con ZIP() ---")
entrada_nombres = input("Introduce nombres separados por comas: ").split(",")
entrada_edades = input("Introduce edades separadas por comas: ").split(",")

# Convertir edades a enteros
lista_edades = [int(edad.strip()) for edad in entrada_edades]
tuplas_combinadas = list(zip(entrada_nombres, lista_edades))

print("Lista de tuplas combinadas:", tuplas_combinadas)