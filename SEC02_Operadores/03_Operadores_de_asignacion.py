"""
    OPERADORES DE ASIGNACIÓN

    =   Asignación simple
    +=  Suma y asigna
    -=  Resta y asigna
    *=  Multiplica y asigna
    /=  Divide y asigna
    //= División entera y asigna
    %=  Módulo y asigna
    **= Potencia y asigna

    Estos operadores permiten realizar una operación y asignar el resultado a la misma variable en una sola línea.
    Por ejemplo, en lugar de escribir:

    contador = contador + 1
    se puede escribir:
    contador += 1

    Otro ejemplo:
    valor = valor * 2
    se puede escribir:
    valor *= 2
"""

# Ejemplos
contador = 0
print("Contador inicial:", contador)

contador += 1  # contador = contador + 1
print("Contador:", contador)

valor = 5
valor *= 2     # valor = valor * 2
print("Valor:", valor)

dinero = 100
dinero -= 25   # dinero = dinero - 25
print("Dinero restante:", dinero)

# EJERCICIOS:
# 1) Simular un saldo bancario: iniciar con 1000, luego hacer un retiro de 150,
#    un depósito de 300, y mostrar el saldo final usando operadores compuestos.
## 2) Crear una variable de temperatura en Celsius, convertirla a Fahrenheit
#    usando la fórmula F = C * 9/5 + 32, y mostrar el resultado.
# 3) Crear una variable de edad, sumar 5 años, y mostrar la nueva edad.
# 4) Crear una variable de distancia en kilómetros, convertirla a millas
