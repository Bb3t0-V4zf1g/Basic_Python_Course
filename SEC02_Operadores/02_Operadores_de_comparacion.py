"""
    OPERADORES DE COMPARACIÓN

    ==  Igual que
    !=  Distinto de
    >   Mayor que
    <   Menor que
    >=  Mayor o igual
    <=  Menor o igual
"""

# Ejemplos
a = 5
b = 8
print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True
print(a >= 5)   # True
print(b <= 10)  # True

# Comparación de cadenas
txt1 = "Python"
txt2 = "python"
print(txt1 == txt2)        # False (case-sensitive)
print(txt1.lower() == txt2) # True

# EJERCICIOS:
# 1) Pedir dos números al usuario y mostrar si el primero es múltiplo del segundo.
#    Pista: usar el operador módulo % y el ==.
# 2) Pedir una contraseña y verificar si coincide con este "Password1234".
# 3) Pedir un número y verificar si es par o impar.
#    Pista: usar el operador módulo % y el ==.
# 4) Pedir un número y verificar si es positivo, negativo o cero.
# 5) Pedir un número y verificar si está entre 1 y 10 (inclusive).
