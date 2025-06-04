def quicksort(lista):

    # Implementación recursiva de quicksort

    # Caso base: si la lista tiene 1 o ningún elemento, ya está ordenada
    if len(lista) <= 1:
        return lista

    # Elegir el elemento pivote (el del medio)
    pivote = lista[len(lista) // 2]

    # Crear sublistas:
    # izquierda: elementos menores al pivote
    izquierda = [x for x in lista if x < pivote]
    # medio: elementos iguales al pivote
    medio = [x for x in lista if x == pivote]
    # derecha: elementos mayores al pivote
    derecha = [x for x in lista if x > pivote]

    # Ordenar recursivamente las sublistas y combinarlas
    return quicksort(izquierda) + medio + quicksort(derecha)

# Ejemplo de uso
if __name__ == "__main__":
    print("Test Quick Sort:")
    lista = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", lista)
    print("Lista ordenada:", quicksort(lista))
    print("Caso lista vacía:", quicksort([]))
    print("Caso un solo elemento:", quicksort([7]))