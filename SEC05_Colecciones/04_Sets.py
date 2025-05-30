# Los sets son colecciones no ordenadas de elementos únicos.
# Son muy útiles para eliminar duplicados y para realizar operaciones
# matemáticas de teoría de conjuntos como unión, intersección, diferencia, etc.

# =====================================================
# 1. CREACIÓN DE SETS
# =====================================================
# Uso de llaves {} para crear un set (los elementos duplicados se eliminan automáticamente).
conjunto_numeros = {1, 2, 3, 2, 4, 5, 5}
print("Conjunto de números (únicos):", conjunto_numeros)

# También se pueden crear sets a partir de otras estructuras con la función set().
lista_frutas = ["manzana", "banana", "cereza", "manzana", "naranja"]
conjunto_frutas = set(lista_frutas)
print("Conjunto de frutas (únicos):", conjunto_frutas)

# =====================================================
# 2. ACCESO Y MODIFICACIÓN DE ELEMENTOS
# =====================================================
# Los sets no tienen orden, por lo que no podemos acceder a sus elementos por índice.
# Sin embargo, podemos verificar la pertenencia con "in" y recorrerlos con un bucle.

print("¿'banana' está en el conjunto de frutas?", "banana" in conjunto_frutas)

# Añadir elementos: se utiliza el método add().
conjunto_frutas.add("kiwi")
print("Después de añadir 'kiwi':", conjunto_frutas)

# Eliminar elementos:
# - remove() elimina el elemento y lanza un error si no existe.
conjunto_frutas.remove("cereza")
print("Después de eliminar 'cereza':", conjunto_frutas)

# - discard() elimina el elemento sin lanzar error si este no existe.
conjunto_frutas.discard("pera")
print("Después de intentar eliminar 'pera' con discard:", conjunto_frutas)

# =====================================================
# 3. OPERACIONES CON SETS
# =====================================================
# Se pueden realizar operaciones matemáticas estándar entre sets.

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Unión: todos los elementos presentes en cualquiera de los sets.
union_ab = set_a.union(set_b)
print("Unión de set_a y set_b:", union_ab)

# Intersección: elementos comunes a ambos sets.
interseccion_ab = set_a.intersection(set_b)
print("Intersección de set_a y set_b:", interseccion_ab)

# Diferencia: elementos en set_a que no están en set_b.
diferencia_ab = set_a.difference(set_b)
print("Diferencia de set_a menos set_b:", diferencia_ab)

# Diferencia simétrica: elementos que están en uno de los sets pero no en ambos.
diferencia_simetrica = set_a.symmetric_difference(set_b)
print("Diferencia simétrica entre set_a y set_b:", diferencia_simetrica)

# =====================================================
# 4. ITERACIÓN Y COMPRENSIÓN DE SETS
# =====================================================
# Puedes recorrer un set usando un bucle for.
print("Elementos de set_a:")
for elemento in set_a:
    print(elemento)

# Comprensión de sets: crear un set de cuadrados a partir de números.
cuadrados = {x**2 for x in range(1, 11)}
print("Set de cuadrados del 1 al 10:", cuadrados)

# =====================================================
# 5. CONVERSIÓN ENTRE SETS, LISTAS Y TUPLAS
# =====================================================
# Los sets se pueden convertir en listas o tuplas para ordenarlos o acceder a ellos por índices.
lista_cuadrados = list(cuadrados)
tupla_cuadrados = tuple(cuadrados)
print("Lista de cuadrados:", lista_cuadrados)
print("Tupla de cuadrados:", tupla_cuadrados)

# =====================================================
# 6. MINI TAREA
# =====================================================

# Ejercicio 1: Palabras únicas en una frase.
# Solicita al usuario una frase, separa las palabras y conviértelas en un set para obtener las únicas.
frase = input("Introduce una frase: ")
palabras = frase.split()  # Divide la frase en palabras.
conjunto_palabras = set(palabras)
print("Palabras únicas en la frase:", conjunto_palabras)
print("Número de palabras únicas:", len(conjunto_palabras))

# Ejercicio 2: Operaciones con conjuntos creados a partir de números.
# El usuario ingresa dos conjuntos de números (en formato de cadena separados por comas).
entrada_set1 = input("Introduce números para el primer set, separados por comas: ")
lista_set1 = [int(x.strip()) for x in entrada_set1.split(",")]
set1 = set(lista_set1)

entrada_set2 = input("Introduce números para el segundo set, separados por comas: ")
lista_set2 = [int(x.strip()) for x in entrada_set2.split(",")]
set2 = set(lista_set2)

print("Primer set:", set1)
print("Segundo set:", set2)
print("Unión:", set1.union(set2))
print("Intersección:", set1.intersection(set2))
print("Diferencia (set1 - set2):", set1.difference(set2))