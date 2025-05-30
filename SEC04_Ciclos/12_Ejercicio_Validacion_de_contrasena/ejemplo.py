"""
PROGRAMA: VALIDACIÓN DE CONTRASEÑAS EN PYTHON

Este programa verifica si una contraseña cumple con los siguientes requisitos:
✅ Longitud mínima de 8 caracteres.
✅ Debe contener al menos una letra mayúscula.
✅ Debe contener al menos una letra minúscula.
✅ Debe contener al menos un número.
✅ Debe contener al menos un carácter especial (!, @, #, $, etc.).

Métodos utilizados:
- Uso de cadenas y bucles para recorrer caracteres.
- Condicionales (`if-elif-else`) para validar condiciones de seguridad.
- Expresiones regulares (`re.match`) para detectar caracteres específicos.
"""

import re  # Importar el módulo de expresiones regulares


def validar_contraseña(contraseña):
    """
    Evalúa si una contraseña es segura cumpliendo criterios mínimos.

    Parámetro:
      contraseña (str): La contraseña a validar.

    Retorna:
      str: Mensaje indicando si es válida o qué falta para cumplir los requisitos.
    """
    if len(contraseña) < 8:
        return "❌ La contraseña debe tener al menos 8 caracteres."

    if not re.search(r'[A-Z]', contraseña):
        return "❌ La contraseña debe contener al menos una letra mayúscula."

    if not re.search(r'[a-z]', contraseña):
        return "❌ La contraseña debe contener al menos una letra minúscula."

    if not re.search(r'\d', contraseña):
        return "❌ La contraseña debe contener al menos un número."

    if not re.search(r'[!@#$%^&*()_+=<>?/]', contraseña):
        return "❌ La contraseña debe contener al menos un carácter especial (!, @, #, $, etc.)."

    return "✅ La contraseña es segura."


# Solicitar la contraseña al usuario
contraseña = input("Ingresa tu contraseña: ")
print(validar_contraseña(contraseña))