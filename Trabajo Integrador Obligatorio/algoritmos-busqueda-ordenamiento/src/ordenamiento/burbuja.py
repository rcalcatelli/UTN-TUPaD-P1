def bubble_sort(lista):
    
    # Ordena una lista de elementos utilizando el algoritmo de ordenamiento Burbuja (Bubble Sort).

    # Este algoritmo compara elementos adyacentes y los intercambia si están en el orden incorrecto.
    # El proceso se repite hasta que la lista está completamente ordenada.
    # Incluye una optimización: si en una pasada no se realiza ningún intercambio, la función termina antes.

    # Parámetros:
    #     lista (list): Lista de elementos comparables a ordenar.

    # Retorna:
    #     list: La misma lista de entrada, pero ordenada de menor a mayor.

    # Ejemplo de uso:
    n = len(lista)
    for i in range(n):
        intercambiado = False # Optimización: si no hay intercambios, la lista ya está ordenada
        for j in range(0, n - i - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambiado = True
        if not intercambiado:
            break
    return lista

if __name__ == "__main__":
    print("Test Bubble Sort:")
    lista = [5, 1, 4, 2, 8]
    print("Lista original:", lista)
    print("Lista ordenada:", bubble_sort(lista.copy()))
    print("Caso lista vacía:", bubble_sort([]))
    print("Caso un solo elemento:", bubble_sort([7]))