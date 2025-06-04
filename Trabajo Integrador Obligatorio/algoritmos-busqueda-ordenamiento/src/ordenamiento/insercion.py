def insertion_sort(lista):
    # Recorre la lista desde el segundo elemento hasta el final
    for i in range(1, len(lista)):
        key = lista[i]  # Guarda el elemento actual que se va a insertar
        j = i - 1
        # Mueve los elementos mayores que key una posición hacia adelante
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        # Inserta el elemento en la posición correcta
        lista[j + 1] = key
    return lista  # Devuelve la lista ordenada

if __name__ == "__main__":
    print("Test Insertion Sort:")
    lista = [12, 11, 13, 5, 6]
    print("Lista original:", lista)
    print("Lista ordenada:", insertion_sort(lista.copy()))
    print("Caso lista vacía:", insertion_sort([]))
    print("Caso un solo elemento:", insertion_sort([7]))