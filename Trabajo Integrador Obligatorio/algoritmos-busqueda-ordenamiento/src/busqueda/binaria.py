def busqueda_binaria(lista, elemento):
    # Implementación iterativa de búsqueda binaria
    # Devuelve el índice del elemento si se encuentra, -1 si no
    izquierda, derecha = 0, len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        valor_medio = lista[medio]
        
        if valor_medio == elemento:
            return medio
        elif valor_medio < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    return -1

# Ejemplo de uso
if __name__ == "__main__":
    print("Test Búsqueda Binaria:")
    lista = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    print("Lista:", lista)
    print("Buscar 23:", busqueda_binaria(lista, 23))
    print("Buscar 100 (no está):", busqueda_binaria(lista, 100))
    print("Caso lista vacía:", busqueda_binaria([], 1))
    print("Caso un solo elemento (existe):", busqueda_binaria([7], 7))
    print("Caso un solo elemento (no existe):", busqueda_binaria([7], 3))