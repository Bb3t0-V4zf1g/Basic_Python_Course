"""
    MÉTODOS DE CADENAS

    Las cadenas (`str`) tienen muchos métodos útiles. Aquí algunos de los más usados:
"""

texto = "  Hola Mundo desde Python  "

# upper(): convierte todo a mayúsculas
print(texto.upper())  # "  HOLA MUNDO DESDE PYTHON  "

# lower(): convierte todo a minúsculas
print(texto.lower())  # "  hola mundo desde python  "

# title(): pone mayúscula al inicio de cada palabra
print(texto.title())  # "  Hola Mundo Desde Python  "

# capitalize(): mayúscula solo la primera letra
print(texto.capitalize())  # "  hola mundo desde python  "

# strip(): elimina espacios al inicio y final
print(texto.strip())  # "Hola Mundo desde Python"

# replace(): reemplaza partes del texto
print(texto.replace("Python", "el curso"))  # "  Hola Mundo desde el curso  "

# find(): devuelve la posición donde aparece una palabra
print(texto.find("Mundo"))  # 7

# in: comprueba si existe una palabra en el texto
print("Python" in texto)  # True

# split(): separa el texto en palabras
print(texto.split())  # ['Hola', 'Mundo', 'desde', 'Python']

# count(): cuenta cuántas veces aparece algo
print(texto.count("o"))  # 3

# startswith()/endswith(): si empieza o termina con algo
print(texto.startswith("  Hola"))  # True
print(texto.endswith("Python  "))  # True

# EJERCICIO:
# Escribir una frase y aplicar al menos 4 métodos diferentes

frase = "  Programar en Python es divertido  "

print(frase.upper())
print(frase.strip())
print(frase.replace("divertido", "poderoso"))
print("Python" in frase)
print(frase.count("r"))
