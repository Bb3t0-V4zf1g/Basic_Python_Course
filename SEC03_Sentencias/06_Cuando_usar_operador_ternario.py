"""
    CUÁNDO USAR EL OPERADOR TERNARIO EN PYTHON

    El operador ternario es útil cuando se necesita una expresión concisa
    para evaluar una condición y devolver un valor en una sola línea.

    ✅ CUÁNDO USARLO:
    - Cuando la condición es sencilla y clara.
    - Cuando solo se necesita asignar un valor o imprimir un resultado.
    - Para mejorar la legibilidad en casos simples.

    ❌ CUÁNDO EVITARLO:
    - Cuando hay múltiples condiciones.
    - Cuando la expresión es demasiado larga o compleja.
    - Cuando afecta la claridad del código.

    Sintaxis:
    resultado = valor_si_verdadero if condición else valor_si_falso
"""

# Ejemplo 1: Asignación de estado según edad
edad = int(input("Ingresa tu edad: "))
estado = "Adulto" if edad >= 18 else "Menor de edad"
print("Estado:", estado)

# Ejemplo 2: Verificación de número par o impar
numero = int(input("Ingresa un número: "))
tipo = "Par" if numero % 2 == 0 else "Impar"
print("El número es:", tipo)

# Ejemplo 3: Selección de mensaje según temperatura
temperatura = int(input("Ingresa la temperatura en grados Celsius: "))
mensaje = "Clima cálido" if temperatura > 25 else "Clima frío"
print("Mensaje:", mensaje)

# Ejemplo 4: Comparación entre dos valores
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
mayor = a if a > b else b
print("El número mayor es:", mayor)

# MINITAREA
"""
1) Pedir un número y mostrar si es múltiplo de 10 o no usando el operador ternario.
2) Solicitar un nombre y determinar si contiene la letra "a".
3) Pedir una edad y determinar si el usuario puede votar (mayor o igual a 18).
4) Pedir dos números y determinar cuál es el menor.
"""

print("Has aprendido cuándo usar el operador ternario en Python. Completa la mini tarea para reforzar tu conocimiento.")