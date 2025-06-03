# Objetivo: Comprender el uso de recursividad en problemas matemáticos simples.

# Ejercicios

# 1. Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Mostrar factoriales desde 1 hasta n
n = int(input("Ingrese un número: "))
for i in range(1, n + 1):
    print(f"Factorial de {i}: {factorial(i)}")

# 2. Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.

def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)

# Mostrar serie completa
n = int(input("Ingrese la posición máxima: "))
for i in range(n + 1):
    print(f"Posición {i}: {fibonacci(i)}")

# 3. Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un algoritmo general.

def potencia(base, exp):
    if exp == 0:
        return 1
    else:
        return base * potencia(base, exp - 1)

# Prueba
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(f"{base}^{exponente} = {potencia(base, exponente)}")

# 4. Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Prueba
num = int(input("Ingrese un número decimal: "))
print(f"Binario: {decimal_a_binario(num)}")

# 5. Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
# > Requisitos: La solución debe ser recursiva.No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# Prueba
texto = input("Ingrese una palabra: ").lower()
print(f"¿Es palíndromo? {es_palindromo(texto)}")

# 6. Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)

# Prueba
numero = int(input("Ingrese un número: "))
print(f"Suma de dígitos: {suma_digitos(numero)}")

# 7. Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

# Prueba
bloques = int(input("Bloques en base: "))
print(f"Total de bloques: {contar_bloques(bloques)}")

# 8. Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    if numero < 10:
        return 1 if numero == digito else 0
    else:
        ultimo = numero % 10
        resto = numero // 10
        return (1 if ultimo == digito else 0) + contar_digito(resto, digito)

# Prueba
num = int(input("Número: "))
d = int(input("Dígito a buscar (0-9): "))
print(f"El dígito aparece {contar_digito(num, d)} veces")