"""
SISTEMA DE DESCUENTOS EN PYTHON

Este programa permite calcular el precio final de una compra aplicando descuentos según:
  - Nivel de membresía:
      • Premium: 40% de descuento
      • VIP Oro: 30% de descuento
      • VIP Plata: 20% de descuento
      • VIP Bronce: 10% de descuento
      • Sin membresía o entrada no válida: 0% de descuento
  - Descuento adicional del 5% si el usuario es estudiante.

Además, el programa permite ingresar varios productos y calcular el precio total con descuento.

Métodos utilizados:
- Entrada del usuario con `input()`
- Uso de condicionales (`if-elif-else`)
- Operaciones matemáticas (`*`, `-`)
- Validaciones de datos para evitar errores
"""

# =====================================================
# INGRESO DE PRODUCTOS
# =====================================================
print("Bienvenido al Sistema de Descuentos")
print("Ingresa el precio de cada producto. Escribe 'fin' cuando ya no desees agregar más productos.")

productos = []
while True:
    entrada = input("Precio del producto: ")
    if entrada.lower() == "fin":
        break
    try:
        precio = float(entrada)
        if precio < 0:
            print("El precio no puede ser negativo. Intenta nuevamente.")
        else:
            productos.append(precio)
    except ValueError:
        print("Por favor ingresa un valor numérico válido o 'fin' para terminar.")

if not productos:
    print("No se ingresaron productos. Finalizando programa.")
    exit()

total_original = sum(productos)
print(f"\nTotal de la compra sin descuento: ${total_original:.2f}")

# =====================================================
# SELECCIÓN DE MEMBRESÍA
# =====================================================
print("\nNiveles de membresía disponibles:")
print("  - Premium (40% de descuento)")
print("  - Oro (30% de descuento)")
print("  - Plata (20% de descuento)")
print("  - Bronce (10% de descuento)")
print("  - Ninguna (sin descuento)")

membresia = input("Ingresa tu nivel de membresía: ").lower()
descuentos = {
    "premium": 0.40,
    "oro": 0.30,
    "plata": 0.20,
    "bronce": 0.10,
    "ninguna": 0.00
}

descuento_membresia = descuentos.get(membresia, 0)
if membresia not in descuentos:
    print("Nivel de membresía no reconocido. Se aplicará sin descuento por membresía.")

# =====================================================
# DESCUENTO POR ESTUDIANTE
# =====================================================
es_estudiante = input("¿Eres estudiante? (si/no): ").lower()
descuento_estudiante = 0.05 if es_estudiante in ["si", "sí"] else 0.00

# =====================================================
# CÁLCULO DEL DESCUENTO TOTAL
# =====================================================
monto_descuento_membresia = total_original * descuento_membresia
precio_despues_membresia = total_original - monto_descuento_membresia

monto_descuento_estudiante = precio_despues_membresia * descuento_estudiante
precio_final = precio_despues_membresia - monto_descuento_estudiante

# =====================================================
# MOSTRAR RESULTADOS
# =====================================================
print("\n--- Resumen de Descuentos ---")
print(f"Total original: ${total_original:.2f}")
print(f"Descuento por membresía ({descuento_membresia*100:.0f}%): -${monto_descuento_membresia:.2f}")
print(f"Subtotal después de membresía: ${precio_despues_membresia:.2f}")
print(f"Descuento extra por estudiante ({descuento_estudiante*100:.0f}%): -${monto_descuento_estudiante:.2f}")
print