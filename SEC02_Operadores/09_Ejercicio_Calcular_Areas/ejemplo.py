"""
    CÁLCULO DE ÁREA EN PYTHON SIN FUNCIONES

    Este programa calcula el área de diferentes figuras geométricas según los datos ingresados por el usuario.

    Métodos utilizados:
    - Entrada del usuario (`input()`)
    - Operaciones matemáticas (`*`, `/`)
    - Condicionales (`if-elif-else`)
"""

# Selección de figura
print("Elige una figura para calcular su área:")
print("1. Cuadrado")
print("2. Rectángulo")
print("3. Triángulo")
print("4. Círculo")

opcion = input("Ingresa el número de la figura: ")

# Cálculo del área según la figura seleccionada
if opcion == "1":  # Cuadrado
    lado = float(input("Ingresa la longitud del lado: "))
    area = lado * lado
    print("El área del cuadrado es:", area)

elif opcion == "2":  # Rectángulo
    base = float(input("Ingresa la base: "))
    altura = float(input("Ingresa la altura: "))
    area = base * altura
    print("El área del rectángulo es:", area)

elif opcion == "3":  # Triángulo
    base = float(input("Ingresa la base: "))
    altura = float(input("Ingresa la altura: "))
    area = (base * altura) / 2
    print("El área del triángulo es:", area)

elif opcion == "4":  # Círculo
    radio = float(input("Ingresa el radio: "))
    area = 3.1416 * (radio ** 2)
    print("El área del círculo es:", area)

else:
    print("Opción inválida.")

# MINITAREA
"""
1) Modificar el código para permitir calcular el área de un trapecio.
2) Agregar validaciones para evitar entradas incorrectas o vacías.
3) Permitir calcular varias áreas sin necesidad de reiniciar el programa.
4) Agregar opciones para elegir la unidad de medida (cm², m², etc.).
"""

print("Has aprendido a calcular áreas en Python sin usar funciones. Completa la mini tarea para reforzar tu conocimiento.")