"""
PROGRAMA: PLAYLIST EN PYTHON USANDO LISTAS

Este programa permite gestionar una playlist de música, con las siguientes acciones:
- Agregar canciones a la playlist.
- Eliminar canciones de la playlist.
- Mostrar la playlist actual.

Métodos utilizados:
- Lista (`list`) para almacenar las canciones.
- Entrada del usuario con `input()`.
- Uso de bucles (`while`) para interactuar con el usuario.
- Métodos de listas (`append()`, `remove()`, `enumerate()`).
"""

# Inicializar la playlist como una lista vacía
playlist = []

print("🎵 Bienvenido a tu Playlist 🎵")
print("Opciones disponibles:")
print("1. Agregar canción")
print("2. Eliminar canción")
print("3. Mostrar playlist")
print("4. Salir")

while True:
    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        cancion = input("Ingresa el nombre de la canción a agregar: ")
        playlist.append(cancion)
        print(f"✅ '{cancion}' fue añadida a la playlist.")

    elif opcion == "2":
        if not playlist:
            print("❌ La playlist está vacía, no hay canciones para eliminar.")
        else:
            print("📜 Canciones en la playlist:")
            for i, song in enumerate(playlist, start=1):
                print(f"{i}. {song}")
            try:
                indice = int(input("Ingresa el número de la canción a eliminar: ")) - 1
                if 0 <= indice < len(playlist):
                    eliminada = playlist.pop(indice)
                    print(f"🗑 '{eliminada}' fue eliminada de la playlist.")
                else:
                    print("❌ Número inválido.")
            except ValueError:
                print("❌ Ingresa un número válido.")

    elif opcion == "3":
        if playlist:
            print("\n🎶 Tu Playlist Actual 🎶")
            for i, song in enumerate(playlist, start=1):
                print(f"{i}. {song}")
        else:
            print("📭 La playlist está vacía.")

    elif opcion == "4":
        print("👋 ¡Gracias por usar tu playlist en Python! Hasta pronto.")
        break

    else:
        print("❌ Opción no válida. Elige entre 1 y 4.")