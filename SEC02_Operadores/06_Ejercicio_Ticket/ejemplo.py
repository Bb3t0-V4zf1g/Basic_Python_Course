"""
    GENERADOR DE TICKETS EN PYTHON

    Este programa genera un ticket con un identificador único y detalles ingresados por el usuario.

    Métodos utilizados:
    - Entrada del usuario (`input()`)
    - Uso de fechas (`datetime`)
    - Concatenación de cadenas (`+`)
"""

import datetime

# Solicitar datos al usuario
nombre = input("Ingresa tu nombre: ")
evento = input("Nombre del evento: ")
fecha_evento = input("Fecha del evento (dd/mm/aaaa): ")

# Generar número de ticket basado en la fecha actual
fecha_actual = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
ticket_id = "TICKET-" + fecha_actual

# Mostrar ticket
print("\n===== TICKET GENERADO =====")
print("Nombre:", nombre)
print("Evento:", evento)
print("Fecha del evento:", fecha_evento)
print("Número de ticket:", ticket_id)
print("===========================\n")

# MINITAREA
"""
1) Agregar un costo al ticket y calcular un descuento si el usuario es estudiante.
2) Incluir una validación para evitar fechas inválidas.
3) Generar un código de verificación basado en la primera letra del nombre y un número aleatorio.
4) Crear una opción para imprimir múltiples tickets para diferentes eventos.
"""

print("Has aprendido a generar tickets en Python. Completa la mini tarea para reforzar tu conocimiento.")