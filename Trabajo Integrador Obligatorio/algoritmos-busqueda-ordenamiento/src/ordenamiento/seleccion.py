def selection_sort(lista):
    # Implementa el algoritmo Selection Sort.
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

if __name__ == "__main__":
    print("Test Selection Sort:")
    lista = [64, 25, 12, 22, 11]
    print("Lista original:", lista)
    print("Lista ordenada:", selection_sort(lista.copy()))
    print("Caso lista vacía:", selection_sort([]))
    print("Caso un solo elemento:", selection_sort([7]))