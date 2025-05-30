# En este curso combinamos dos estructuras fundamentales:
# - Listas: Colecciones ordenadas y mutables.
# - Diccionarios: Colecciones de pares clave:valor.
#
# Esta combinación es muy útil para representar conjuntos de datos complejos;
# por ejemplo, una lista de registros (cada uno representado como un diccionario)
# o un diccionario cuyos valores sean listas de elementos relacionados.

# =====================================================
# 1. LISTA DE DICCIONARIOS
# =====================================================
# Imagina que tenemos una lista de estudiantes, donde cada estudiante se
# representa mediante un diccionario con información como nombre, edad y grado.
estudiantes = [
    {"nombre": "Alberto", "edad": 20, "grado": "A"},
    {"nombre": "Mariana", "edad": 22, "grado": "B"},
    {"nombre": "Juan", "edad": 19, "grado": "A"},
    {"nombre": "Sofía", "edad": 21, "grado": "C"}
]

print("Lista de estudiantes:")
for estudiante in estudiantes:
    print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Grado: {estudiante['grado']}")

# Ejemplo de modificación:
# Actualizamos el grado del estudiante "Mariana"
for estudiante in estudiantes:
    if estudiante["nombre"] == "Mariana":
        estudiante["grado"] = "A"
print("\nTras actualizar el grado de Mariana:")
for estudiante in estudiantes:
    print(estudiante)


# =====================================================
# 2. DICCIONARIO CON LISTAS COMO VALORES
# =====================================================
# Otra forma de combinar estas estructuras es tener un diccionario donde
# cada clave esté asociada a una lista de elementos. Por ejemplo, una clasificación
# de productos por categoría.
productos_por_categoria = {
    "Electrónica": ["Laptop", "Smartphone", "Tablet"],
    "Hogar": ["Sofá", "Mesa", "Silla"],
    "Ropa": ["Camiseta", "Pantalón", "Zapatos"]
}

print("\nProductos por categoría:")
for categoria, productos in productos_por_categoria.items():
    print(f"{categoria}:")
    # Recorremos la lista de productos de cada categoría
    for producto in productos:
        print(f"  - {producto}")

# Podemos añadir un nuevo producto a una categoría existente:
productos_por_categoria["Electrónica"].append("Auriculares")
print("\nTras añadir 'Auriculares' a Electrónica:")
print(productos_por_categoria["Electrónica"])


# =====================================================
# 3. ACCESO Y MODIFICACIÓN COMPLEJA
# =====================================================
# Es común combinar búsquedas y modificaciones en estructuras anidadas.
# Ejemplo: Filtrar estudiantes que están en el grado "A" y crear un diccionario
# que agrupe sus nombres y edades.

estudiantes_grado_A = {"nombres": [], "edades": []}
for estudiante in estudiantes:
    if estudiante["grado"] == "A":
        estudiantes_grado_A["nombres"].append(estudiante["nombre"])
        estudiantes_grado_A["edades"].append(estudiante["edad"])

print("\nEstudiantes en el grado \"A\":")
print(estudiantes_grado_A)


# =====================================================
# 4. COMBINAR DICCIONARIOS Y LISTAS CON COMPRENSIÓN
# =====================================================
# Podemos usar comprensiones para generar nuevas estructuras.
# Ejemplo: Dado un diccionario de productos y sus precios,
# generar una lista de diccionarios solo con productos caros (precio > 100).

productos_precios = {
    "Laptop": 1200,
    "Mouse": 25,
    "Teclado": 45,
    "Monitor": 250,
    "Impresora": 150
}

productos_caros = [
    {"producto": prod, "precio": precio}
    for prod, precio in productos_precios.items() if precio > 100
]

print("\nProductos con precio mayor a 100:")
for item in productos_caros:
    print(item)


# =====================================================
# 5. MINI TAREA
# =====================================================
# Practica lo aprendido con los siguientes ejercicios:
#
# Ejercicio 1: Solicita al usuario ingresar varios registros de personas
# en el formato "nombre:edad:ciudad" separados por comas (ej: "Juan:25:Madrid, Ana:30:Barcelona").
# Convierte la entrada en una lista de diccionarios con claves "nombre", "edad" y "ciudad"
# y muestra la lista resultante.
#
# Ejercicio 2: Crea un diccionario donde las claves sean nombres de cursos y
# los valores sean listas de alumnos inscritos. Recorre el diccionario y
# muestra, para cada curso, el número de alumnos inscritos.
#
# Ejercicio 3 (opcional): A partir de la lista de diccionarios de estudiantes,
# crea un diccionario agrupado por grados, donde cada clave sea un grado y
# su valor sea una lista con los nombres de los estudiantes que pertenecen a ese grado.

# Ejercicio 1: Creación de una lista de diccionarios a partir de una entrada.
entrada_registros = input("\nIntroduce registros de personas (ej: Juan:25:Madrid, Ana:30:Barcelona): ")
# Separa por comas para obtener cada registro
registros = entrada_registros.split(",")
lista_personas = []
for registro in registros:
    try:
        nombre, edad, ciudad = registro.split(":")
        persona = {
            "nombre": nombre.strip(),
            "edad": int(edad.strip()),
            "ciudad": ciudad.strip()
        }
        lista_personas.append(persona)
    except ValueError:
        print(f"Formato incorrecto en: {registro}")
print("Lista de personas ingresadas:")
for persona in lista_personas:
    print(persona)

# Ejercicio 2: Diccionario de cursos con alumnos inscritos.
cursos = {
    "Python": ["Alberto", "Mariana", "Juan"],
    "JavaScript": ["Sofía", "Carlos"],
    "Bases de Datos": ["Ana", "Luis", "Mariana", "Juan"]
}
print("\nCantidad de alumnos por curso:")
for curso, alumnos in cursos.items():
    print(f"{curso}: {len(alumnos)} alumno(s)")

# Ejercicio 3: Agrupar estudiantes por grado (utilizando la lista 'estudiantes' definida anteriormente).
estudiantes_por_grado = {}
for estudiante in estudiantes:
    grado = estudiante["grado"]
    nombre = estudiante["nombre"]
    if grado not in estudiantes_por_grado:
        estudiantes_por_grado[grado] = []
    estudiantes_por_grado[grado].append(nombre)
print("\nEstudiantes agrupados por grado:")
for grado, nombres in estudiantes_por_grado.items():
    print(f"Grado {grado}: {nombres}")