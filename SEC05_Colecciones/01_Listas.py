# 1. CREACIÓN DE LISTAS
# Se crea una lista de cadenas para almacenar nombres de frutas.
frutas = ["manzana", "banana", "cereza", "naranja"]
print("Lista de frutas:", frutas)


# 2. ACCESO A ELEMENTOS
# Las listas se indexan a partir de 0. También se pueden usar índices negativos para acceder desde el final.
print("Primer elemento (índice 0):", frutas[0])
print("Último elemento (índice -1):", frutas[-1])


# 3. MODIFICACIÓN DE LISTAS
# Como las listas son mutables, se pueden modificar después de su creación.
frutas[1] = "kiwi"              # Se cambia el elemento en la posición 1.
frutas.append("mango")          # Se añade un elemento al final.
frutas.insert(2, "limón")       # Se inserta un elemento en la posición 2.
frutas.remove("cereza")         # Se elimina el elemento "cereza" por su valor.
elemento_eliminado = frutas.pop(0)  # Se elimina el primer elemento y se guarda en una variable.
print("Elemento eliminado:", elemento_eliminado)
print("Lista tras modificaciones:", frutas)


# 4. SLICING (REBANADO) DE LISTAS
# El slicing permite obtener sublistas a partir de la lista original.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primeros_cinco = numeros[0:5]   # Toma los elementos del índice 0 al 4.
print("Primeros cinco números:", primeros_cinco)
sublista = numeros[3:8]         # Toma los elementos del índice 3 al 7 (el 8 es exclusivo).
print("Sublista (índices 3 a 7):", sublista)
cada_dos = numeros[::2]         # Toma todos los elementos, avanzando de 2 en 2.
print("Elementos con paso 2:", cada_dos)


# 5. RECORRIDO DE LISTAS
# Se pueden recorrer los elementos de una lista usando un bucle for.
print("Recorrido directo de la lista 'frutas':")
for fruta in frutas:
    print("Fruta:", fruta)

# También es posible iterar utilizando los índices.
print("Recorrido usando índices:")
for i in range(len(frutas)):
    print(f"Índice {i}:", frutas[i])


# 6. MÉTODOS ÚTILES DE LISTAS
# Python ofrece métodos nativos para manipular listas.
numeros_metodo = [3, 1, 4, 1, 5, 9, 2]
numeros_metodo.sort()      # Ordena la lista en forma ascendente.
print("Lista ordenada:", numeros_metodo)
numeros_metodo.reverse()   # Invierte el orden de la lista.
print("Lista invertida:", numeros_metodo)
indice_5 = numeros_metodo.index(5)   # Retorna el índice de la primera aparición del número 5.
print("Índice del número 5:", indice_5)
conteo_1 = numeros_metodo.count(1)     # Cuenta cuántas veces aparece el número 1.
print("El número 1 aparece:", conteo_1, "veces")


# MINI TAREA

# Ejercicio 1: Solicita al usuario una cadena de números separados por comas,
# luego convierte la cadena en una lista de enteros y muestra el número mayor y menor.
cadena_numeros = input("Introduce una cadena de números separados por comas (ej: 4,8,15,16,23,42): ")
lista_numeros = [int(n.strip()) for n in cadena_numeros.split(",")]
print("Número mayor:", max(lista_numeros))
print("Número menor:", min(lista_numeros))


# Ejercicio 2: Crea una lista de nombres, recórrela y muestra cada nombre en mayúsculas.
nombres = ["Alberto", "Juan", "Mariana", "Sofía", "Catalina"]
print("Nombres en mayúsculas:")
for nombre in nombres:
    print(nombre.upper())


# Ejercicio 3: Genera una lista de números del 1 al 20 y crea otra lista que
# contenga solo los números pares.
lista_numeros = list(range(1, 21))
pares = [num for num in lista_numeros if num % 2 == 0]
print("Números pares del 1 al 20:", pares)