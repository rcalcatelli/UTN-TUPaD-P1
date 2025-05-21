

# 1. Función que imprime "Hola Mundo!"
def imprimir_hola_mundo():
    print("Hola Mundo!")

# --- Ejecución de la función ---
imprimir_hola_mundo()

# 2. Función que devuelve un saludo personalizado
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# --- Ejecución de la función ---

# Pedir el nombre al usuario para un saludo interactivo
nombre_ingresado = input("¡Hola! ¿Cuál es tu nombre? ")
saludo_interactivo = saludar_usuario(nombre_ingresado)
print(saludo_interactivo) # Esto imprimirá "Hola [nombre que ingresaste]!"

# 3. Función que imprime la información personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# --- Ejecución de la función ---

# Pedir los datos al usuario para una interacción más dinámica
print("\nPor favor, ingresa tu información personal:")
nombre_usuario = input("Nombre: ")
apellido_usuario = input("Apellido: ")
try:
    edad_usuario = int(input("Edad: "))
except ValueError:
    edad_usuario = "una edad inválida" # Manejo básico si el usuario no pone un número
residencia_usuario = input("Residencia: ")

informacion_personal(nombre_usuario, apellido_usuario, edad_usuario, residencia_usuario)
# Esto imprimirá: "Soy [nombre_ingresado] [apellido_ingresado], tengo [edad_ingresada] años y vivo en [residencia_ingresada]."

# 4. Funciones para calcular el área y perímetro de un círculo

import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# --- Ejecución de la función ---

# Pidiendo el radio al usuario
print("-- Calcular el área y perímetro de un círculo --")
try:
    radio_usuario = float(input("Ingrese el radio del círculo: "))
    area_usuario = calcular_area_circulo(radio_usuario)
    perimetro_usuario = calcular_perimetro_circulo(radio_usuario)

    print(f"Para tu círculo con radio de {radio_usuario}:")
    print(f"  Área calculada: {area_usuario:.2f} unidades cuadradas")
    print(f"  Perímetro calculado: {perimetro_usuario:.2f} unidades")
except ValueError:
    print("Parece que no ingresaste un número válido. Inténtalo de nuevo.")

# 5. Función que convierte segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

# --- Ejecución de la función ---

#  Pedir la cantidad de segundos al usuario
print("-- Convertir segundos a horas --")
try:
    segundos_input = int(input("Ingrese una cantidad de segundos: "))
    horas_usuario = segundos_a_horas(segundos_input)
    print(f"Equivale a {segundos_a_horas(segundos):.2f} horas.")
except ValueError:
    print("El número que ingresaste no es entero. Por favor, inténtalo de nuevo.")

# 6. Función que imprime la tabla de multiplicar de un número
def tabla_multiplicar(numero):
    print(f"Tabla del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# --- Ejecución de la función ---

# Pedir al usuario el número para su tabla
print("--- Generador de tabla de multiplicar ---")
try:
    numero_usuario = int(input("Ingresa un número entero para ver su tabla de multiplicar: "))
    tabla_multiplicar(numero_usuario)
except ValueError:
    print("¡Error! Por favor, ingresa un número entero válido.")

# 7. Función que realiza operaciones básicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

# --- Ejecución de la función ---

# Pidiendo los números al usuario
print("--- Ingresa los números para operar ---")
try:
    num_usuario1 = float(input("Ingresa el primer número: "))
    num_usuario2 = float(input("Ingresa el segundo número: "))

    resultados_usuario = operaciones_basicas(num_usuario1, num_usuario2)

    print(f"\nResultados para {num_usuario1} y {num_usuario2}:")
    print(f"  Suma: {resultados_usuario[0]}")
    print(f"  Resta: {resultados_usuario[1]}")
    print(f"  Multiplicación: {resultados_usuario[2]}")
    print(f"  División: {resultados_usuario[3]}") # Se imprimirá el valor o el mensaje de error
except ValueError:
    print("¡Error! Por favor, asegúrate de ingresar solo números.")

# 8. Función que calcula el índice de masa corporal
def calcular_imc(peso, altura):
    if altura <= 0: # Es crucial validar que la altura no sea cero o negativa
        return "Error: La altura debe ser un valor positivo."
    else:
        imc = peso / (altura ** 2)
        return imc

# --- Ejecución de la función ---

# Pedir los datos al usuario
print("--- Calcular IMC ---")
try:
    peso_usuario = float(input("Ingrese su peso en kg: "))
    altura_usuario = float(input("Ingrese su altura en metros: "))

    imc_usuario = calcular_imc(peso_usuario, altura_usuario)

    print(f"\nCon {peso_usuario} kg y {altura_usuario} m:")
    if isinstance(imc_usuario, (int, float)):
        print(f"  Su IMC es: {imc_usuario:.2f}")
    else:
        print(f"  {imc_usuario}") # Si hubo un error en la altura
except ValueError:
    print("¡Error! Asegúrate de ingresar números válidos para peso y altura.")

# 9. Función que convierte grados Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

# --- Ejecución de la función ---

# Pedir la temperatura al usuario
print("--- Convertir temperatura en Celsius ---")
try:
    celsius_usuario = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit_usuario = celsius_a_fahrenheit(celsius_usuario)
    print(f"{celsius_usuario}°C equivalen a {fahrenheit_usuario:.2f}°F.")
except ValueError:
    print("¡Error! Por favor, ingresa un número válido para la temperatura.")

# 10. Función que calcula el promedio de tres números
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# --- Ejecución de la función ---

# Pedir los números al usuario
print("--- Calcular el promedio ---")
try:
    num_usuario1 = float(input("Ingresa el primer número: "))
    num_usuario2 = float(input("Ingresa el segundo número: "))
    num_usuario3 = float(input("Ingresa el tercer número: "))

    promedio_usuario = calcular_promedio(num_usuario1, num_usuario2, num_usuario3)
    print(f"\nEl promedio es: {promedio_usuario:.2f}")
except ValueError:
    print("¡Error! Por favor, ingresa solo números válidos.")