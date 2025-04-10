# Ejercicio 1: Imprimir números del 0 al 100
for i in range(101):
    print(i)

# Ejercicio 2: Contar dígitos de un número
numero = "12345"  # Valor de prueba para evitar input()
print("Cantidad de dígitos:", len(numero))

# Ejercicio 3: Sumar números entre dos valores (excluidos)
inicio = 1  # Valor de prueba
fin = 5     # Valor de prueba
suma = 0
for i in range(inicio + 1, fin):
    suma += i
print("La suma es:", suma)

# Ejercicio 4: Sumar números hasta ingresar 0
numeros = [3, 5, -2, 0]  # Lista de prueba
total = 0
index = 0
while numeros[index] != 0:
    total += numeros[index]
    index += 1
print("Total acumulado:", total)

# Ejercicio 5: Adivinar número aleatorio entre 0 y 9
import random
numero_secreto = 4  # Valor fijo para prueba
aintentos = [1, 2, 4]  # Intentos de prueba
intentos_realizados = 0
for intento in aintentos:
    intentos_realizados += 1
    if intento == numero_secreto:
        break
print(f"¡Correcto! Lo adivinaste en {intentos_realizados} intentos.")

# Ejercicio 6: Imprimir números pares de 100 a 0
to_print = [i for i in range(100, -1, -2)]
print("\nNúmeros pares de 100 a 0:")
for i in to_print:
    print(i)

# Ejercicio 7: Sumar del 0 hasta un número ingresado
fin = 10  # Valor de prueba
suma = 0
for i in range(fin + 1):
    suma += i
print("La suma total es:", suma)

# Ejercicio 8: Contar pares, impares, positivos y negativos
pares = impares = positivos = negativos = 0
numeros = [1, 2, -3, -4, 0, 5, 6, -7, 8, 9]  # Lista de prueba (usar 100 para test real)
for num in numeros:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
print("\nPares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

# Ejercicio 9: Calcular media de 100 números
numeros = [1, 2, 3, 4, 5]  # Lista de prueba (usar 100 para test real)
suma = sum(numeros)
cantidad = len(numeros)
media = suma / cantidad
print("La media es:", media)

# Ejercicio 10: Invertir número ingresado
numero = "547"  # Valor de prueba
numero_invertido = numero[::-1]
print("Número invertido:", numero_invertido)
