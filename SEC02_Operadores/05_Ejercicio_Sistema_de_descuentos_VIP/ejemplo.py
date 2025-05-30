"""
    SISTEMA DE DESCUENTOS VIP EN PYTHON

    Este programa calcula el descuento aplicado a una compra según el nivel de membresía del usuario.

    Tipos de membresía:
    - VIP Oro: 30% de descuento
    - VIP Plata: 20% de descuento
    - VIP Bronce: 10% de descuento
    - Sin membresía: No aplica descuento

    Métodos utilizados:
    - Condicionales (`if-elif-else`)
    - Operaciones matemáticas (`*`, `-`)
    - Entrada del usuario con `input()`
"""

# Solicitar datos al usuario
precio_original = float(input("Ingresa el precio del producto: "))
membresia = input("Ingresa tu nivel de membresía (Oro, Plata, Bronce, Ninguna): ").lower()

# Aplicar descuento según la membresía
if membresia == "oro":
    descuento = precio_original * 0.3
elif membresia == "plata":
    descuento = precio_original * 0.2
elif membresia == "bronce":
    descuento = precio_original * 0.1
else:
    descuento = 0

precio_final = precio_original - descuento

# Mostrar resultados
print("Precio original:", precio_original)
print("Descuento aplicado:", descuento)
print("Precio final a pagar:", precio_final)

# MINITAREA
"""
1) Modificar el programa para agregar una membresía Premium con 40% de descuento.
2) Hacer que el sistema pregunte si el usuario es estudiante y aplicar un descuento extra del 5%.
3) Incluir validaciones para evitar entradas incorrectas de membresía.
4) Pedir al usuario varios productos y calcular el precio total con descuento.
"""

print("Has aprendido a crear un sistema de descuentos VIP en Python. Completa la mini tarea para reforzar tu conocimiento.")