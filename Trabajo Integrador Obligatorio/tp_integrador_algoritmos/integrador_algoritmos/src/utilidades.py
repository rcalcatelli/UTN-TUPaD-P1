def mezclar(izquierda, derecha):
    """
    Mezcla dos listas ordenadas en una sola lista ordenada.
    Args:
        izquierda (list): Primera lista ordenada.
        derecha (list): Segunda lista ordenada.
    Returns:
        list: Nueva lista ordenada que contiene todos los elementos de ambas listas.
    """
    resultado = []
    i = j = 0
    
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    
    resultado += izquierda[i:]
    resultado += derecha[j:]
    return resultado 