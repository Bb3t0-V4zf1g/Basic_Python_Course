"""
PROGRAMA: BOLETÍN INFORMATIVO EN PYTHON USANDO LISTAS

Este programa permite gestionar un boletín informativo con opciones para:
📌 Agregar noticias al boletín.
📌 Eliminar noticias del boletín.
📌 Mostrar el boletín actualizado.

Métodos utilizados:
- Uso de listas (`list`) para almacenar las noticias.
- Entrada del usuario con `input()`.
- Uso de bucles (`while`) para interactuar con el usuario.
- Métodos de listas (`append()`, `pop()`, `enumerate()`).
"""

# Inicializar el boletín como una lista vacía
boletin = []

print("\n📰 Bienvenido al Boletín Informativo 📰")
print("Opciones disponibles:")
print("1. Agregar noticia")
print("2. Eliminar noticia")
print("3. Mostrar boletín")
print("4. Salir")

while True:
    opcion = input("\nElige una opción (1-4): ")

    if opcion == "1":
        noticia = input("📝 Ingresa la noticia a agregar: ")
        boletin.append(noticia)
        print(f"✅ La noticia ha sido añadida al boletín.")

    elif opcion == "2":
        if not boletin:
            print("❌ No hay noticias en el boletín para eliminar.")
        else:
            print("\n📜 Noticias en el boletín:")
            for i, item in enumerate(boletin, start=1):
                print(f"{i}. {item}")
            try:
                indice = int(input("\nIngresa el número de la noticia a eliminar: ")) - 1
                if 0 <= indice < len(boletin):
                    eliminada = boletin.pop(indice)
                    print(f"🗑 La noticia '{eliminada}' ha sido eliminada del boletín.")
                else:
                    print("❌ Número inválido.")
            except ValueError:
                print("❌ Ingresa un número válido.")

    elif opcion == "3":
        if boletin:
            print("\n📢 Boletín Informativo 📢")
            for i, item in enumerate(boletin, start=1):
                print(f"{i}. {item}")
        else:
            print("📭 No hay noticias en el boletín.")

    elif opcion == "4":
        print("\n👋 Gracias por utilizar el Boletín Informativo. ¡Hasta pronto!")
        break

    else:
        print("❌ Opción no válida. Elige entre 1 y 4.")