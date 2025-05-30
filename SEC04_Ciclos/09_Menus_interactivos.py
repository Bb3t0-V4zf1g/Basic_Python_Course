"""
    MENÚS INTERACTIVOS EN PYTHON

    Un menú interactivo permite al usuario elegir opciones y realizar acciones
    basadas en su selección.

    Uso común:
    - Mejorar la experiencia de usuario en programas de consola.
    - Permitir múltiples operaciones sin reiniciar el programa.
    - Ofrecer navegación intuitiva en aplicaciones CLI.

    Estructura básica:

    while True:
        print("1. Opción A")
        print("2. Opción B")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("Has elegido la opción A.")
        elif opcion == "2":
            print("Has elegido la opción B.")
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
"""

# Ejemplo 1: Menú interactivo con opciones básicas
while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Saludar")
    print("2. Mostrar fecha y hora")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Ingresa tu nombre: ")
        print(f"Hola, {nombre}!")
    elif opcion == "2":
        from datetime import datetime
        print("Fecha y hora actual:", datetime.now())
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intenta de nuevo.")

# Ejemplo 2: Menú de operaciones matemáticas
while True:
    print("\n=== MENÚ DE OPERACIONES ===")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion in ["1", "2", "3"]:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == "1":
            print("Resultado:", num1 + num2)
        elif opcion == "2":
            print("Resultado:", num1 - num2)
        elif opcion == "3":
            print("Resultado:", num1 * num2)
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intenta de nuevo.")

# MINITAREA
"""
1) Crear un menú de conversión de unidades (kilómetros a millas, Celsius a Fahrenheit, etc.).
2) Desarrollar un menú de gestión de tareas donde el usuario pueda agregar, ver y eliminar tareas.
3) Implementar un menú de calculadora con operaciones avanzadas (potencia, raíz cuadrada, módulo).
4) Diseñar un menú de juegos donde el usuario pueda elegir entre diferentes juegos simples.
"""

print("Has aprendido sobre menús interactivos en Python. Completa la mini tarea para reforzar tu conocimiento.")