"""
SISTEMA MULTIFUNCIONAL EN PYTHON

Este archivo integra diversas funcionalidades, incluyendo:
1. Sistema de descuentos basado en membresía.
2. Detección de mayor de edad con validaciones.
3. Comparación de números para identificar el mayor.
4. Evaluación de calificaciones en formato numérico y de letra.

Cada sección está modularizada en funciones para mejorar la reutilización del código.

Métodos utilizados:
- Definición de funciones con `def`
- Entrada del usuario con `input()`
- Conversión de datos con `float()` y `int()`
- Uso de condicionales (`if-elif-else`)
- Validaciones para evitar datos incorrectos
"""

# =====================================================
# 1. SISTEMA DE DESCUENTOS
# =====================================================
def calcular_precio_final(precio_original, membresia, es_estudiante):
    """Aplica descuentos según membresía y estado de estudiante."""
    descuentos = {
        "premium": 0.40,
        "oro": 0.30,
        "plata": 0.20,
        "bronce": 0.10,
        "ninguna": 0.00
    }

    descuento_membresia = descuentos.get(membresia.lower(), 0)
    descuento_estudiante = 0.05 if es_estudiante.lower() in ["si", "sí"] else 0

    precio_con_membresia = precio_original * (1 - descuento_membresia)
    precio_final = precio_con_membresia * (1 - descuento_estudiante)

    return precio_final

precio = float(input("Ingresa el precio del producto: "))
membresia = input("Ingresa tu nivel de membresía: ")
es_estudiante = input("¿Eres estudiante? (si/no): ")
precio_final = calcular_precio_final(precio, membresia, es_estudiante)

print(f"Precio final con descuentos: ${precio_final:.2f}")


# =====================================================
# 2. DETECCIÓN DE MAYOR DE EDAD
# =====================================================
def verificar_mayoria_edad(edad):
    """Evalúa si el usuario es mayor de edad y cuántos años faltan."""
    if edad < 0:
        return "Error: La edad no puede ser negativa."
    elif edad >= 18:
        return "Eres mayor de edad."
    else:
        return f"Eres menor de edad. Te faltan {18 - edad} años para ser mayor."

edad_usuario = int(input("Ingresa tu edad: "))
print(verificar_mayoria_edad(edad_usuario))


# =====================================================
# 3. COMPARACIÓN DE NÚMEROS
# =====================================================
def obtener_mayor(num1, num2):
    """Compara dos números y determina cuál es mayor."""
    if num1 > num2:
        return f"El número mayor es: {num1}"
    elif num2 > num1:
        return f"El número mayor es: {num2}"
    else:
        return "Ambos números son iguales."

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
print(obtener_mayor(num1, num2))


# =====================================================
# 4. EVALUACIÓN DE CALIFICACIONES
# =====================================================
def obtener_calificacion(nota):
    """Convierte una nota numérica en su equivalente en letra."""
    if nota < 0 or nota > 100:
        return "Error: La nota debe estar entre 0 y 100."
    elif nota >= 90:
        return "A"
    elif nota >= 80:
        return "B"
    elif nota >= 70:
        return "C"
    elif nota >= 60:
        return "D"
    else:
        return "F"

def obtener_mensaje(nota):
    """Determina un mensaje motivador basado en la calificación."""
    if nota >= 90:
        return "¡Excelente trabajo!"
    elif nota >= 80:
        return "Muy bien, sigue esforzándote."
    elif nota >= 70:
        return "Buen desempeño, pero hay margen de mejora."
    elif nota >= 60:
        return "Necesitas esforzarte más."
    else:
        return "Es recomendable estudiar más y pedir ayuda."

nota = float(input("Ingresa tu calificación (0-100): "))
calificacion = obtener_calificacion(nota)
mensaje = obtener_mensaje(nota)

print(f"Calificación: {calificacion} - {mensaje}")

# =====================================================
# MINI TAREA
# =====================================================
"""
Extiende el código con las siguientes mejoras:
1) **Validar entradas numéricas** en todas las secciones para evitar errores.
2) **Agregar cálculo de promedio** para múltiples calificaciones antes de determinar la calificación final.
3) **Permitir ingresar nombres en el sistema de descuentos** y mostrar un recibo completo con detalles.
4) **Implementar una versión de comparación de números con una lista completa de valores.**
"""