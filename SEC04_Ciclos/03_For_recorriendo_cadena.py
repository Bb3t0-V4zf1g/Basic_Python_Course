"""
    RECORRIDO DE UNA CADENA CON FOR EN PYTHON

    En Python, se puede recorrer una cadena de texto con un bucle for,
    iterando sobre cada carácter de la cadena.

    Sintaxis básica:

    for caracter in cadena:
        # Código dentro del bucle

    Ejemplo:

    palabra = "Python"
    for letra in palabra:
        print(letra)  # Muestra cada letra en una línea
"""

# Ejemplo 1: Recorrer una palabra e imprimir cada letra
palabra = input("Ingresa una palabra: ")
for letra in palabra:
    print(letra)

# Ejemplo 2: Contar cuántas veces aparece una letra en una cadena
frase = input("Ingresa una frase: ")
letra_buscar = input("Ingresa una letra para contar: ")
contador = 0

for letra in frase:
    if letra == letra_buscar:
        contador += 1

print(f"La letra '{letra_buscar}' aparece {contador} veces en la frase.")

# Ejemplo 3: Mostrar los caracteres en mayúsculas
texto = input("Ingresa un texto: ")
for caracter in texto:
    print(caracter.upper())

# Ejemplo 4: Filtrar y mostrar solo las vocales de una cadena
texto = input("Ingresa una oración: ")
vocales = "aeiouAEIOU"

for caracter in texto:
    if caracter in vocales:
        print(caracter)

# MINITAREA
"""
1) Pedir al usuario una palabra y mostrar cada letra con su índice.
2) Solicitar una oración y contar cuántas vocales contiene.
3) Pedir una cadena y generar una nueva sin espacios.
4) Invertir una palabra recorriéndola con for y mostrarla al usuario.
"""

print("Has aprendido cómo recorrer una cadena con for. Completa la mini tarea para reforzar tu conocimiento.")