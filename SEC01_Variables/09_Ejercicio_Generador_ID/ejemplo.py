"""
    GENERADOR DE ID EN PYTHON

    Un identificador único es útil para asignar un valor único a usuarios, productos,
    registros, etc.

    Métodos comunes:
    - Números aleatorios (`random.randint()`)
    - UUID (`uuid.uuid4()`)
    - Combinaciones de fecha y hora (`datetime`)
    - Codificación de información (usuario + número aleatorio)

    Ejemplo:

    import uuid
    id_unico = uuid.uuid4()
    print("ID generado:", id_unico)
"""

import random
import uuid
import datetime

# Ejemplo 1: Generador de ID aleatorio basado en números
id_numerico = random.randint(1000, 9999)
print("ID numérico:", id_numerico)

# Ejemplo 2: Generador de ID usando UUID
id_unico = uuid.uuid4()
print("ID único con UUID:", id_unico)

# Ejemplo 3: Generador de ID con fecha y hora
fecha_actual = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
id_fecha = f"USR-{fecha_actual}"
print("ID basado en fecha:", id_fecha)

# Ejemplo 4: Generador de ID combinando usuario y aleatorio
usuario = input("Ingresa tu nombre de usuario: ")
id_usuario = f"{usuario}-{random.randint(1000, 9999)}"
print("ID de usuario:", id_usuario)

# MINITAREA
"""
1) Crear un generador de ID que combine el nombre del usuario con su año de nacimiento y un número aleatorio.
2) Generar un identificador basado en la fecha exacta (incluyendo milisegundos).
3) Crear un sistema que genere IDs aleatorios sin repetir (lista de IDs únicos).
4) Hacer un programa que genere un ID seguro utilizando hash (`hashlib.sha256()`).
"""

print("Has aprendido a generar identificadores en Python. Completa la mini tarea para reforzar tu conocimiento.")