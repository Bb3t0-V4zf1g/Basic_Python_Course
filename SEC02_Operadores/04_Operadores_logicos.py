"""
    OPERADORES LÓGICOS

    and  Devuelve True si AMBAS expresiones son True
    or   Devuelve True si AL MENOS UNA expresión es True
    not  Invierte el valor lógico
"""

# Ejemplos
a = True
b = False
print(a and b)  # False
print(a or b)   # True
print(not a)    # False

c, d, e = True, False, True
print(c and d or e)  # True
print(c or d and e)  # True
print(not c and d)   # False

# Combinando comparaciones
d = 10
print(d > 5 and d < 20)  # True
print(d < 5 or d % 2 == 0) # True

# Ejercicio
# 1) Pedir al usuario edad y si tiene carnet (sí/no).
#    Mostrar si puede conducir: edad>=18 AND carnet=='sí'.
# 2) Pedir dos condiciones (True/False) y mostrar si ambas no se cumplen (usar not, or).
