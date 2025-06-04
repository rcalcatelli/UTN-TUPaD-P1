def busqueda_lineal(lista, elemento):
    
    # Implementa el algoritmo de búsqueda lineal.
    # Recorre la lista elemento por elemento hasta encontrar la coincidencia.
    
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i  # Retorna el índice del elemento
    return -1 # Retorna -1 si el elemento no se encuentra

if __name__ == "__main__":
    print("Test Búsqueda Lineal:")
    lista = [5, 3, 8, 1, 9]
    print("Lista:", lista)
    print("Buscar 8:", busqueda_lineal(lista, 8))
    print("Buscar 2 (no está):", busqueda_lineal(lista, 2))
    print("Caso lista vacía:", busqueda_lineal([], 1))
    print("Caso un solo elemento (existe):", busqueda_lineal([7], 7))
    print("Caso un solo elemento (no existe):", busqueda_lineal([7], 3))