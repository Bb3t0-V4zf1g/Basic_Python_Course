"""
    SISTEMA DE AUTENTICACIÓN EN PYTHON

    Este programa solicita al usuario sus credenciales y verifica si son correctas.

    Métodos utilizados:
    - Entrada del usuario (`input()`)
    - Condicionales (`if-else`)
"""

# Credenciales predefinidas
usuario_correcto = "admin"
contraseña_correcta = "password123"

# Solicitar datos al usuario
usuario = input("Ingresa tu nombre de usuario: ")
contraseña = input("Ingresa tu contraseña: ")

# Verificar autenticación
if usuario == usuario_correcto and contraseña == contraseña_correcta:
    print("Acceso concedido.")
else:
    print("Acceso denegado.")

# MINITAREA
"""
1) Agregar intentos máximos para evitar múltiples intentos de acceso.
2) Permitir cambiar la contraseña después de una autenticación exitosa.
3) Implementar una autenticación con preguntas de seguridad en caso de fallo.
4) Validar que el usuario ingrese datos y no deje los campos vacíos.
"""

print("Has aprendido a crear un sistema de autenticación en Python. Completa la mini tarea para reforzar tu conocimiento.")