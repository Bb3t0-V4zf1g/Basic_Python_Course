# =====================================================
# 1. CREACIÓN DE TUPLAS
# =====================================================
# Las tuplas son secuencias ordenadas de elementos, definidas usando paréntesis ()
# o simplemente separando los elementos por comas. A diferencia de las listas, las
# tuplas son inmutables, es decir, una vez creadas, no pueden modificarse.
tupla_frutas = ("manzana", "banana", "cereza", "naranja")
print("Tupla de frutas:", tupla_frutas)

# =====================================================
# 2. ACCESO A ELEMENTOS
# =====================================================
# Al igual que las listas, se accede a los elementos de una tupla mediante índices.
# El primer elemento tiene índice 0 y también se pueden usar índices negativos.
print("Primer elemento:", tupla_frutas[0])
print("Último elemento:", tupla_frutas[-1])

# =====================================================
# 3. INMUTABILIDAD DE LAS TUPLAS
# =====================================================
# Al ser inmutables, intentar modificar un elemento de la tupla genera un error.
try:
    tupla_frutas[1] = "kiwi"
except TypeError as e:
    print("Error al intentar modificar una tupla:", e)

# Para "modificar" una tupla, se debe crear una nueva a partir de la existente, por ejemplo:
nueva_tupla_frutas = tupla_frutas[:2] + ("kiwi",) + tupla_frutas[3:]
print("Nueva tupla de frutas:", nueva_tupla_frutas)

# =====================================================
# 4. SLICING (REBANADO) DE TUPLAS
# =====================================================
# El slicing funciona de la misma manera que con las listas. Permite extraer subtuplas.
tupla_numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Primeros cinco números:", tupla_numeros[0:5])
print("Subtupla (índices 3 a 7):", tupla_numeros[3:8])
print("Tupla con cada dos elementos:", tupla_numeros[::2])

# =====================================================
# 5. OPERACIONES CON TUPLAS
# =====================================================
# Aunque las tuplas son inmutables, se pueden realizar operaciones como la concatenación
# y la repetición, y se pueden usar algunos métodos propios.
tupla_a = (1, 2, 3)
tupla_b = (4, 5)
# Concatenación de tuplas:
concatenada = tupla_a + tupla_b
print("Tupla concatenada:", concatenada)
# Repetición de una tupla:
repeticion = tupla_a * 3
print("Tupla repetida:", repeticion)
# Métodos count() e index():
print("El número 1 aparece en tupla_a:", tupla_a.count(1), "vez")
print("El índice del número 2 en tupla_a:", tupla_a.index(2))

# =====================================================
# 6. DESEMPAQUETADO (TUPLE UNPACKING)
# =====================================================
# El desempaquetado permite asignar cada elemento de la tupla a una variable.
fruta1, fruta2, fruta3, fruta4 = tupla_frutas
print("Desempaquetado de la tupla de frutas:")
print("Fruta 1:", fruta1)
print("Fruta 2:", fruta2)
print("Fruta 3:", fruta3)
print("Fruta 4:", fruta4)

# =====================================================
# MINI TAREA
# =====================================================

# Ejercicio 1: Crear una tupla a partir de nombres de frutas ingresados por el usuario,
# y mostrar el primer y el último elemento.
print("\n--- Ejercicio 1: Tupla de Frutas del Usuario ---")
entrada_frutas = input("Introduce nombres de frutas separados por comas: ")
# Se convierte la entrada en una lista, eliminando espacios extra y luego se transforma en tupla.
lista_frutas_usuario = [fruta.strip() for fruta in entrada_frutas.split(",")]
tupla_frutas_usuario = tuple(lista_frutas_usuario)
print("Primera fruta:", tupla_frutas_usuario[0])
print("Última fruta:", tupla_frutas_usuario[-1])

# Ejercicio 2: A partir de una entrada de números, convierte la cadena en una tupla de enteros,
# y muestra la suma total, el número máximo y el mínimo.
print("\n--- Ejercicio 2: Tupla de Números ---")
entrada_numeros = input("Introduce números separados por comas: ")
lista_numeros_usuario = [int(n.strip()) for n in entrada_numeros.split(",")]
tupla_numeros_usuario = tuple(lista_numeros_usuario)
print("Suma total:", sum(tupla_numeros_usuario))
print("Máximo:", max(tupla_numeros_usuario))
print("Mínimo:", min(tupla_numeros_usuario))

# Ejercicio 3: Invertir una tupla de números y mostrar la tupla invertida.
print("\n--- Ejercicio 3: Invertir la Tupla ---")
# Utiliza slicing para invertir la tupla.
tupla_invertida = tupla_numeros_usuario[::-1]
print("Tupla invertida:", tupla_invertida)