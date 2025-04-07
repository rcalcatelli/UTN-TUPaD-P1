#Práctico 3: Estructuras condicionales


### 1. Mayor de edad

# Solicita la edad al usuario
edad = int(input("Ingrese su edad: "))

# Condición: si la edad es mayor a 18, se considera mayor de edad
if edad > 18:
    print("Es mayor de edad")
# No hay "else" porque no se pide hacer nada si no se cumple la condición


### 2. Nota aprobada o desaprobada

nota = int(input("Ingrese su nota: "))

# Condición: si la nota es mayor o igual a 6, el usuario aprueba
if nota >= 6:
    print("Aprobado")
# Si no se cumple la condición anterior, entra en el else y está desaprobado
else:
    print("Desaprobado")


### 3. Número par

numero = int(input("Ingrese un número par: "))

# El operador % (módulo) devuelve el resto de la división
# Si el resto de dividir el número por 2 es 0, entonces es par
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    # Si el número no es par, se informa al usuario
    print("Por favor, ingrese un número par")


### 4. Categoría según edad

edad = int(input("Ingrese su edad: "))

# Se evalúan las condiciones en orden para categorizar por edad
if edad < 12:
    print("Niño/a")
elif edad < 18:
    # Solo entra acá si edad es >= 12 y < 18
    print("Adolescente")
elif edad < 30:
    # Solo entra si edad es >= 18 y < 30
    print("Adulto/a joven")
else:
    # Si ninguna condición anterior se cumple, es mayor o igual a 30
    print("Adulto/a")



### 5. Validación de contraseña

contraseña = input("Ingrese una contraseña: ")

# La función len() devuelve la cantidad de caracteres del string
# Se verifica si la longitud está dentro del rango permitido (inclusive)
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    # Si no se cumple la condición anterior, la contraseña no es válida
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


### 6. Sesgo de distribución

import random
from statistics import mean, median, mode

# Genera una lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcula los tres parámetros estadísticos
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

# Se imprimen los valores calculados para analizarlos
print(f"Media: {media}, Mediana: {mediana}, Moda: {moda}")

# Se analiza la relación entre media, mediana y moda para determinar el sesgo
if media > mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana < moda:
    print("Sesgo negativo o a la izquierda")
else:
    # Si los tres valores son iguales (o no cumplen las relaciones anteriores), no hay sesgo
    print("Sin sesgo")


### 7. Vocal al final

frase = input("Ingrese una frase o palabra: ")

# Se verifica si el último carácter es una vocal (en minúscula, usando .lower() para evitar errores)
if frase[-1].lower() in "aeiou":
    # Si termina en vocal, se agrega un signo de exclamación
    frase += "!"

# Se imprime la frase modificada o igual, según la condición
print(frase)


### 8. Transformar nombre

nombre = input("Ingrese su nombre: ")
opcion = int(input("Elija una opción (1-mayúsculas, 2-minúsculas, 3-capitalizar): "))

# Se evalúa qué transformación aplicar según la opción elegida
if opcion == 1:
    print(nombre.upper())  # Transforma todo en mayúsculas
elif opcion == 2:
    print(nombre.lower())  # Transforma todo en minúsculas
elif opcion == 3:
    print(nombre.title())  # Capitaliza la primera letra de cada palabra
else:
    # Si no se eligió ninguna opción válida, se informa al usuario
    print("Opción inválida")


### 9. Clasificación de terremoto

magnitud = float(input("Ingrese la magnitud del terremoto: "))

# Se compara la magnitud usando rangos definidos por la escala de Richter
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    # Si es mayor o igual que 7
    print("Extremo (puede causar graves daños a gran escala)")


### 10. Estación del año según hemisferio y fecha

# Se pide al usuario que ingrese el hemisferio, mes y día
hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = int(input("Ingrese el número de mes (1-12): "))
dia = int(input("Ingrese el día: "))

# Se analiza el periodo según mes y día para determinar la estación
if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
    # Entre el 21/12 y el 20/3 inclusive
    estacion = "Invierno" if hemisferio == "N" else "Verano"
elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
    # Entre el 21/3 y el 20/6 inclusive
    estacion = "Primavera" if hemisferio == "N" else "Otoño"
elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
    # Entre el 21/6 y el 20/9 inclusive
    estacion = "Verano" if hemisferio == "N" else "Invierno"
elif (mes == 9 and dia >= 21) or (10 <= mes <= 11) or (mes == 12 and dia <= 20):
    # Entre el 21/9 y el 20/12 inclusive
    estacion = "Otoño" if hemisferio == "N" else "Primavera"
else:
    estacion = "Dato inválido"  # Por si se ingresa una fecha incorrecta

# Se imprime el resultado final
print(f"La estación es: {estacion}")


