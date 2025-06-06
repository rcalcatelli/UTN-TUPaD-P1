def busqueda_lineal(lista, objetivo):
    # Recorre cada elemento de la lista
    for i in range(len(lista)):
        # Si el elemento actual es igual al objetivo
        if lista[i] == objetivo:
            # Devuelve el índice donde se encontró el objetivo
            return i
    # Si no se encuentra el objetivo, devuelve -1
    return -1

def busqueda_binaria(lista, objetivo):
    """
    Realiza una búsqueda binaria en una lista ordenada para encontrar la posición de un elemento objetivo.
    Parámetros:
        lista (list): Lista de elementos ordenados donde se realizará la búsqueda.
        objetivo: Elemento que se desea encontrar en la lista.
    Retorna:
        int: Índice del elemento objetivo si se encuentra en la lista; de lo contrario, -1.
    """
    izquierda = 0  # Índice inicial de la lista
    derecha = len(lista) - 1  # Índice final de la lista
    
    # Mientras el índice izquierdo no supere al derecho
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2  # Calcula el índice del medio
        # Si el elemento en el medio es el objetivo
        if lista[medio] == objetivo:
            return medio  # Devuelve el índice del objetivo
        # Si el elemento en el medio es menor que el objetivo
        elif lista[medio] < objetivo:
            izquierda = medio + 1  # Busca en la mitad derecha
        else:
            derecha = medio - 1  # Busca en la mitad izquierda
    # Si no se encuentra el objetivo, devuelve -1
    return -1 