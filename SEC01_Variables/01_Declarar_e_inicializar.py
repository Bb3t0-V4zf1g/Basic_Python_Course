"""
    En python, una variable es un espacio en memoria que se utiliza para almacenar datos.
    Se puede pensar en una variable como una etiqueta que se le asigna a un valor.

    En python, no es necesario declarar el tipo de variable, ya que el intérprete lo infiere automáticamente.

    No como en otros lenguajes como Java o C, donde se debe declarar el tipo de variable antes de usarla. Por ejemplo:
    int numero = 10;
    float decimal = 10.5;
    Cuadrado cua1 = new Cuadrado(23);

    Basta con poner el nombre de la variable, el signo igual y el valor que se le quiere asignar.
"""

# Declarar e inicializar una variable
nombre = "Juan"

# En python es necesario declara e inicializar la variable en la misma línea
num1 = 30

saludo = "Hola, soy Daniel"

"""
    Para confirmar el valor que tiene una variable, se puede usar la función print() para imprimir el valor de la variable en la consola.
    
    La función print() es una función incorporada en python que se utiliza para mostrar información en la consola.
    Es muy útil para depurar el código y verificar que las variables tienen los valores esperados.
    
    Para ejecutar tu archivo de python, puedes usar el comando "python nombre_del_archivo.py" en la terminal.
    Pero si estas fuera de la carpeta donde se encuentra el archivo, debes usar la ruta completa del archivo o
    navegar a la carpeta donde se encuentra el archivo usando el comando "cd nombre_de_la_carpeta".
    
    Si es que estas usando un IDE como PyCharm, puedes ejecutar el archivo directamente desde el IDE.
    En este caso, puedes hacer clic derecho en el archivo y seleccionar "Run 'nombre_del_archivo'" o
    en el boton de "Run", que tiene símbolo de un triángulo verde.
"""

# Imprimir el valor de la variable
print(nombre) # Juan

# También puede agregar texto a la variable
print("Hola, soy " + nombre) # "Hola, soy Juan"
print("Hola, soy {}".format(nombre)) # "Hola, soy Juan"
print(f"Hola, soy {nombre}") # "Hola, soy Juan"
#Luego veremos la concatenación de cadenas y el uso de f-strings

print("Mi numero es: " + str(num1)) # "Mi numero es: 30"

"""
    str() es una función incorporada en python que se utiliza para convertir un valor a una cadena de texto.
    Ya que nuestra variable num1 es un entero, debemos convertirlo a una cadena para poder concatenarlo con el texto.
    texto + texto, no es posible un texto + numero, ya que son tipos de datos diferentes.
"""

# Declarar e inicializar varias variables en una sola línea

nombre_1, nombre_2, nombre_3 = "Juan", "Pedro", "Maria"
nombre_hombre, edad, altura = "Leo", 30, 1.75

print(nombre_1) # Juan
print(nombre_2) # Pedro
print(nombre_3) # Maria
print(nombre_hombre) # Leo
print(edad) # 30
print(altura) # 1.75

# EJERCICIO

# Declara e inicializa las siguientes variables: tenis - "Nike", balon - "Adidas", camiseta - "Puma", pantalon - "Levis"

...

# Declara e inicializa las siguientes variables en una sola línea: nickname - "Leo", edad - 30, altura - 1.55, familia - "Padre, Madre, Hermano"

...

# Imprime el valor de las variables, trata de usar la menor cantidad de print() posibles