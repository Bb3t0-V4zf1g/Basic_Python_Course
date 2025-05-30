"""
PROGRAMA: CAJERO AUTOMÁTICO EN PYTHON

Este programa simula un cajero automático, permitiendo:
- Consultar saldo.
- Depositar dinero.
- Retirar dinero (con validación de saldo disponible).

Métodos utilizados:
- Uso de variables para manejar el saldo.
- Entrada del usuario con `input()`.
- Conversión de datos con `float()`.
- Condicionales (`if-elif-else`) para determinar la acción elegida.
- Validaciones para evitar retiros mayores al saldo disponible.
"""

# Saldo inicial del usuario
saldo = 1000.00  # Puedes cambiar este valor según la cuenta simulada

print("Bienvenido al Cajero Automático")
print("Opciones disponibles:")
print("1. Consultar saldo")
print("2. Depositar dinero")
print("3. Retirar dinero")
print("4. Salir")

while True:
    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        print(f"Tu saldo actual es: ${saldo:.2f}")

    elif opcion == "2":
        try:
            deposito = float(input("Ingresa la cantidad a depositar: "))
            if deposito <= 0:
                print("Error: Debes ingresar un monto positivo.")
            else:
                saldo += deposito
                print(f"Depósito exitoso. Tu nuevo saldo es: ${saldo:.2f}")
        except ValueError:
            print("Error: Ingresa una cantidad válida.")

    elif opcion == "3":
        try:
            retiro = float(input("Ingresa la cantidad a retirar: "))
            if retiro <= 0:
                print("Error: Debes ingresar un monto positivo.")
            elif retiro > saldo:
                print("Fondos insuficientes. No puedes retirar más dinero del que tienes.")
            else:
                saldo -= retiro
                print(f"Retiro exitoso. Tu nuevo saldo es: ${saldo:.2f}")
        except ValueError:
            print("Error: Ingresa una cantidad válida.")

    elif opcion == "4":
        print("Gracias por utilizar el cajero automático. ¡Hasta pronto!")
        break

    else:
        print("Opción no válida. Por favor, elige una opción entre 1 y 4.")