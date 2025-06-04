def merge_sort(lista):
    
    # Caso base: si la lista tiene 0 o 1 elemento, ya está ordenada
    if len(lista) <= 1:
        return lista

    # Dividir la lista en dos mitades
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]

    # Ordenar recursivamente cada mitad
    izquierda_ordenada = merge_sort(izquierda)
    derecha_ordenada = merge_sort(derecha)

    # Mezclar las dos mitades ordenadas
    return _merge(izquierda_ordenada, derecha_ordenada)

def _merge(izquierda, derecha):
    # Función auxiliar para mezclar dos listas ordenadas.
    resultado = []  # Lista donde se almacenará el resultado final
    i = j = 0  # Índices para recorrer las listas izquierda y derecha

    # Comparar elementos de ambas listas y agregarlos en orden
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Agregar los elementos restantes de la lista izquierda (si hay)
    resultado.extend(izquierda[i:])
    # Agregar los elementos restantes de la lista derecha (si hay)
    resultado.extend(derecha[j:])
    return resultado

if __name__ == "__main__":
    print("Test Merge Sort:")
    lista = [38, 27, 43, 3, 9, 82, 10]
    print("Lista original:", lista)
    print("Lista ordenada:", merge_sort(lista))
    print("Caso lista vacía:", merge_sort([]))
    print("Caso un solo elemento:", merge_sort([7]))