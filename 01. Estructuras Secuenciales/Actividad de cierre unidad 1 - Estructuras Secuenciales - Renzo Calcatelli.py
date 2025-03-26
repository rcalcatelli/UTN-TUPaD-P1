# Actividad de cierre unidad 1 - Estructuras Secuenciales - Renzo Calcatelli

### 1) Programa que imprime "Hola Mundo!"

# Imprime el mensaje "Hola Mundo!" en la consola
print("Hola Mundo!")

### 2) Programa que pide el nombre del usuario y lo saluda

# Solicita al usuario que ingrese su nombre
nombre = input("¿Cuál es tu nombre? ")
# Imprime un saludo utilizando el nombre ingresado
print(f"Hola {nombre}!")

### 3) Programa que pide nombre, apellido, edad y lugar de residencia

# Solicita al usuario su nombre, apellido, edad y lugar de residencia
nombre = input("¿Cuál es tu nombre? ")
apellido = input("¿Cuál es tu apellido? ")
edad = input("¿Cuántos años tienes? ")
residencia = input("¿Dónde vives? ")
# Imprime una oración con los datos ingresados
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

### 4) Programa que pide el radio de un círculo y calcula área y perímetro

import math  # Importa la librería math para usar funciones matemáticas

# Solicita al usuario que ingrese el radio del círculo
radio = float(input("Introduce el radio del círculo: "))
# Calcula el área del círculo usando la fórmula A = π * r^2
area = math.pi * (radio ** 2)
# Calcula el perímetro del círculo usando la fórmula P = 2 * π * r
perimetro = 2 * math.pi * radio
# Imprime el área y el perímetro calculados
print(f"Área: {area}, Perímetro: {perimetro}")

### 6) Programa que imprime la tabla de multiplicar de un número

# Solicita al usuario que ingrese un número
numero = int(input("Introduce un número: "))
# Imprime la tabla de multiplicar del número del 1 al 10
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

### 7) Programa que suma, divide, multiplica y resta dos números enteros

# Solicita al usuario que ingrese dos números enteros distintos de 0
num1 = int(input("Introduce el primer número (distinto de 0): "))
num2 = int(input("Introduce el segundo número (distinto de 0): "))

# Realiza las operaciones matemáticas
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

# Imprime los resultados de las operaciones
print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division}")

### 8) Programa que calcula el índice de masa corporal (IMC)

# Solicita al usuario que ingrese su peso en kilogramos
peso = float(input("Introduce tu peso en kg: "))
# Solicita al usuario que ingrese su altura en metros
altura = float(input("Introduce tu altura en metros: "))
# Calcula el índice de masa corporal usando la fórmula IMC = peso / (altura^2)
imc = peso / (altura ** 2)
# Imprime el índice de masa corporal calculado
print(f"Tu índice de masa corporal es: {imc}")

### 9) Programa que convierte grados Celsius a Fahrenheit

# Solicita al usuario que ingrese una temperatura en grados Celsius
celsius = float(input("Introduce la temperatura en grados Celsius: "))
# Convierte la temperatura a grados Fahrenheit usando la fórmula F = (9/5) * C + 32
fahrenheit = (9/5) * celsius + 32
# Imprime la temperatura en grados Fahrenheit
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")

### 10) Programa que calcula el promedio de tres números

# Solicita al usuario que ingrese tres números
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))
# Calcula el promedio de los tres números
promedio = (num1 + num2 + num3) / 3
# Imprime el promedio calculado
print(f"El promedio es: {promedio}")
