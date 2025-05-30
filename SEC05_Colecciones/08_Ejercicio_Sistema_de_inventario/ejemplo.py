"""
PROGRAMA: SISTEMA DE INVENTARIO EN PYTHON USANDO LISTAS

Este programa permite gestionar un inventario de productos con las siguientes acciones:
📦 Agregar productos al inventario.
🗑 Eliminar productos del inventario.
📋 Mostrar el inventario actual.

Métodos utilizados:
- Uso de listas (`list`) para almacenar los productos.
- Entrada del usuario con `input()`.
- Uso de bucles (`while`) para interactuar con el usuario.
- Métodos de listas (`append()`, `pop()`, `enumerate()`).
"""

# Inicializar el inventario como una lista vacía
inventario = []

print("\n📦 Bienvenido al Sistema de Inventario 📦")
print("Opciones disponibles:")
print("1. Agregar producto")
print("2. Eliminar producto")
print("3. Mostrar inventario")
print("4. Salir")

while True:
    opcion = input("\nElige una opción (1-4): ")

    if opcion == "1":
        producto = input("📝 Ingresa el nombre del producto a agregar: ")
        inventario.append(producto)
        print(f"✅ '{producto}' ha sido añadido al inventario.")

    elif opcion == "2":
        if not inventario:
            print("❌ No hay productos en el inventario para eliminar.")
        else:
            print("\n📜 Productos en el inventario:")
            for i, item in enumerate(inventario, start=1):
                print(f"{i}. {item}")
            try:
                indice = int(input("\nIngresa el número del producto a eliminar: ")) - 1
                if 0 <= indice < len(inventario):
                    eliminado = inventario.pop(indice)
                    print(f"🗑 '{eliminado}' ha sido eliminado del inventario.")
                else:
                    print("❌ Número inválido.")
            except ValueError:
                print("❌ Ingresa un número válido.")

    elif opcion == "3":
        if inventario:
            print("\n📋 Inventario Actual 📋")
            for i, item in enumerate(inventario, start=1):
                print(f"{i}. {item}")
        else:
            print("📭 No hay productos en el inventario.")

    elif opcion == "4":
        print("\n👋 Gracias por usar el Sistema de Inventario. ¡Hasta pronto!")
        break

    else:
        print("❌ Opción no válida. Elige entre 1 y 4.")