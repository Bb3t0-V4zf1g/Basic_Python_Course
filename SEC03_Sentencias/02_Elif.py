"""
    SENTENCIA IF-ELIF-ELSE EN PYTHON

    La sentencia if-elif-else permite evaluar múltiples condiciones en orden.

    Estructura básica:

    if condición1:
        # Código si condición1 es verdadera
    elif condición2:
        # Código si condición2 es verdadera
    else:
        # Código si ninguna condición anterior se cumple

    Ejemplo básico:

    temperatura = 20
    if temperatura > 30:
        print("Hace mucho calor.")
    elif temperatura > 20:
        print("Hace un clima agradable.")
    else:
        print("Hace frío.")
"""

# Ejemplo 1: Clasificación de edades
edad = int(input("Ingresa tu edad: "))

if edad < 12:
    print("Eres un niño.")
elif edad < 18:
    print("Eres un adolescente.")
else:
    print("Eres un adulto.")

# Ejemplo 2: Evaluación de notas
nota = int(input("Ingresa tu calificación (0-100): "))

if nota >= 90:
    print("Tu calificación es excelente.")
elif nota >= 70:
    print("Aprobaste con buena nota.")
elif nota >= 60:
    print("Aprobaste, pero puedes mejorar.")
else:
    print("Reprobaste el curso.")

# Ejemplo 3: Clasificación de temperatura
temperatura = int(input("Ingresa la temperatura en grados Celsius: "))

if temperatura >= 35:
    print("Hace mucho calor.")
elif temperatura >= 20:
    print("El clima es templado.")
elif temperatura >= 10:
    print("Hace frío.")
else:
    print("Hace mucho frío.")

# MINITAREA
"""
1) Pedir al usuario un número y clasificarlo como positivo, negativo o cero.
2) Solicitar la hora del día (0-23) y mostrar si es madrugada, mañana, tarde o noche.
3) Pedir un número y mostrar si es múltiplo de 2, 3 o ninguno.
4) Crear un programa que clasifique una película según su calificación (G, PG, PG-13, R).
"""

print("Has aprendido sobre la sentencia if-elif-else. Completa la mini tarea para reforzar tu conocimiento.")