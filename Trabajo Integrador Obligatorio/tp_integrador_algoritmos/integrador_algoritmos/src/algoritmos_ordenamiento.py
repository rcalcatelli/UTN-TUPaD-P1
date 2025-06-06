from .utilidades import mezclar

# Ordenamiento por selección: busca el menor elemento y lo coloca al principio
def ordenamiento_seleccion(lista):
    n = len(lista)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        # Intercambia el elemento actual con el menor encontrado
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    return lista

# Ordenamiento por inserción: inserta cada elemento en su lugar correcto
def ordenamiento_insercion(lista):
    n = len(lista)
    for i in range(1, n):
        valor_actual = lista[i]
        j = i - 1
        # Desplaza los elementos mayores hacia la derecha
        while j >= 0 and valor_actual < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        # Inserta el valor en la posición correcta
        lista[j + 1] = valor_actual
    return lista

# Ordenamiento burbuja: compara elementos adyacentes y los intercambia si están desordenados
def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(0, n - 1):
            if lista[j] > lista[j + 1]:
                # Intercambia si están en el orden incorrecto
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Quicksort: divide la lista usando un pivote y ordena recursivamente
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista.pop()  # Toma el último elemento como pivote
    menores = []
    mayores = []
    for x in lista:
        if x <= pivote:
            menores.append(x)
        else:
            mayores.append(x)
    # Ordena recursivamente las sublistas y las une
    return quicksort(menores) + [pivote] + quicksort(mayores)

# Mergesort: divide la lista en mitades, las ordena y luego las mezcla
def mergesort(lista):
    if len(lista) <= 1:
        return lista
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]
    izquierda = mergesort(izquierda)
    derecha = mergesort(derecha)
    # Mezcla las dos mitades ordenadas
    return mezclar(izquierda, derecha)
