
# PROGRAMACIÓN I - Práctico 6: Estructuras de datos complejas
# Alumno: Calcatelli Renzo.
# > Objetivo:
# Dominar el uso de estructuras de datos complejas en Python para
# almacenar, organizar y manipular datos de manera eficiente, aplicando
# buenas prácticas y optimizando el rendimiento de las aplicaciones.



# 1. Dado el diccionario precios_frutas

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

# Añadir las siguientes frutas con sus respectivos precios:

# - Naranja = 1200
# - Manzana = 1500
# - Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadir nuevas frutas

precios_frutas.update({
    'Naranja': 1200,
    'Manzana': 1500,
    'Pera': 2300
})

print(precios_frutas)

# 2. Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# - Banana = 1330
# - Manzana = 1700
# - Melón = 2800

# Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

# 3. Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.

lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

# 4. Escribí un programa que permita almacenar y consultar números telefónicos.
# - Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# - Luego, pedí un nombre y mostrale el número asociado, si existe.

agenda = {}
for i in range(5):
    nombre = input(f"Ingrese nombre del contacto {i+1}: ")
    numero = input(f"Ingrese número de {nombre}: ")
    agenda[nombre] = numero

consulta = input("Ingrese nombre a consultar: ")
print(f"Teléfono: {agenda.get(consulta, 'No encontrado')}")

# 5. Solicita al usuario una frase e imprime:
# - Las palabras únicas (usando un set).
# - Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase: ")
palabras = frase.split()

# Palabras únicas
unicas = set(palabras)
print("Palabras únicas:", unicas)

# Conteo de palabras
conteo = {}
for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1
print("Conteo de palabras:", conteo)

# 6. Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.

alumnos = {}
for i in range(3):
    nombre = input(f"Ingrese nombre del alumno {i+1}: ")
    notas = tuple(float(input(f"Ingrese nota {j+1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas)/len(notas)
    print(f"{nombre}: promedio {promedio:.2f}")

# 7. Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# - Mostrá los que aprobaron ambos parciales.
# - Mostrá los que aprobaron solo uno de los dos.
# - Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial1 = {101, 102, 105, 107, 110}
parcial2 = {102, 103, 105, 108, 110}

# Aprobaron ambos
ambos = parcial1 & parcial2
print("Aprobaron ambos:", ambos)

# Aprobaron solo uno
solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno:", solo_uno)

# Aprobaron al menos uno
al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos uno:", al_menos_uno)

# 8. Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# - Consultar el stock de un producto ingresado.
# - Agregar unidades al stock si el producto ya existe.
# - Agregar un nuevo producto si no existe.

inventario = {'Lápiz': 50, 'Cuaderno': 30, 'Goma': 20}

while True:
    producto = input("Producto (o 'salir' para terminar): ")
    if producto.lower() == 'salir':
        break

    if producto in inventario:
        print(f"Stock actual: {inventario[producto]}")
        accion = input("¿Agregar unidades? (s/n): ")
        if accion.lower() == 's':
            unidades = int(input("Unidades a agregar: "))
            inventario[producto] += unidades
    else:
        print("Producto no encontrado")
        agregar = input("¿Agregar nuevo producto? (s/n): ")
        if agregar.lower() == 's':
            stock = int(input("Stock inicial: "))
            inventario[producto] = stock

print("Inventario final:", inventario)

# 9. Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.

agenda = {
    ('Lunes', '09:00'): 'Reunión equipo',
    ('Martes', '14:00'): 'Clase de programación'
}

dia = input("Día a consultar: ")
hora = input("Hora a consultar: ")

evento = agenda.get((dia, hora), "No hay eventos programados")
print(f"Evento: {evento}")

# 10. Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# - Las capitales sean las claves.
# - Los países sean los valores.

paises = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago'
}

capitales = {capital: pais for pais, capital in paises.items()}
print("Diccionario invertido:", capitales)
