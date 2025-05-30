# Los diccionarios son colecciones de pares clave:valor.
# Son mutables y permiten acceder a los datos mediante sus claves, lo que facilita
# la organización y búsqueda de información.

# =====================================================
# 1. CREACIÓN DE DICCIONARIOS
# =====================================================
# Se pueden crear diccionarios usando llaves {} o la función dict().
diccionario_vacio = {}  # Diccionario vacío
persona = {"nombre": "Alberto", "edad": 30, "ciudad": "Colima"}
print("Diccionario 'persona':", persona)

# =====================================================
# 2. ACCESO A VALORES
# =====================================================
# Acceder a los valores a través de sus claves:
print("Nombre:", persona["nombre"])
# Usando el método get(), que retorna None o un valor por defecto si la clave no existe:
print("Edad:", persona.get("edad"))
print("Profesión (con get, valor por defecto):", persona.get("profesion", "No especificada"))

# =====================================================
# 3. MODIFICACIÓN Y ADICIÓN DE ELEMENTOS
# =====================================================
# Modificar el valor de una clave existente:
persona["edad"] = 31
# Añadir un nuevo par clave:valor:
persona["profesion"] = "Ingeniero"
print("Diccionario 'persona' modificado:", persona)

# =====================================================
# 4. ELIMINAR ELEMENTOS
# =====================================================
# Eliminar un elemento con pop() que retorna el valor eliminado:
profesion_eliminada = persona.pop("profesion")
print("Profesión eliminada:", profesion_eliminada)
print("Tras eliminar 'profesion':", persona)
# Otra forma: usar del para eliminar una clave
del persona["ciudad"]
print("Tras eliminar 'ciudad':", persona)

# =====================================================
# 5. RECORRER DICCIONARIOS
# =====================================================
# Recorrer las claves:
print("Recorrida de claves:")
for clave in persona:
    print(clave, ":", persona[clave])

# Recorrer clave y valor utilizando items():
print("Recorrida con items():")
for clave, valor in persona.items():
    print(f"{clave} -> {valor}")

# =====================================================
# 6. MÉTODOS ÚTILES
# =====================================================
# Obtener las claves, valores o ambos en forma de lista:
claves = list(persona.keys())
valores = list(persona.values())
print("Claves:", claves)
print("Valores:", valores)

# Actualizar diccionario con otro:
datos_extra = {"correo": "alberto@example.com", "edad": 32}  # Nota: 'edad' se actualizará
persona.update(datos_extra)
print("Diccionario tras update:", persona)

# =====================================================
# 7. COMPRENSIÓN DE DICCIONARIOS
# =====================================================
# Crear un diccionario usando una comprensión: por ejemplo, generar cuadrados de números.
cuadrados = {x: x ** 2 for x in range(1, 6)}
print("Diccionario de cuadrados:", cuadrados)

# =====================================================
# 8. MINI TAREA
# =====================================================

# Ejercicio 1: Crear un diccionario a partir de una entrada del usuario.
# Se pide una cadena en la que cada par nombre:edad esté separado por comas.
# Ejemplo de entrada: "Juan:25, María:30, Pedro:22"
entrada = input("Introduce nombres y edades (ej: Juan:25, María:30, Pedro:22): ")
elementos = entrada.split(",")  # Separa en pares
diccionario_personas = {}
for elemento in elementos:
    par = elemento.split(":")
    nombre = par[0].strip()
    edad = int(par[1].strip())
    diccionario_personas[nombre] = edad
print("Diccionario de personas:", diccionario_personas)

# Ejercicio 2: Dado un diccionario de productos y precios, mostrar los productos con precio mayor a un valor definido.
productos = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 250,
    "Impresora": 150
}

valor_limite = 50  # Puedes modificar este valor o solicitarlo al usuario.
print(f"Productos con precio mayor a {valor_limite}:")
for producto, precio in productos.items():
    if precio > valor_limite:
        print(f"{producto} -> ${precio}")