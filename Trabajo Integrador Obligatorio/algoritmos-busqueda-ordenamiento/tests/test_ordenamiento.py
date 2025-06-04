import pytest
# Importa las funciones de ordenamiento desde sus respectivos módulos
from src.ordenamiento.burbuja import bubble_sort
from src.ordenamiento.seleccion import selection_sort
from src.ordenamiento.insercion import insertion_sort
from src.ordenamiento.quicksort import quick_sort
from src.ordenamiento.mergesort import merge_sort

# Importa funciones para generar listas de prueba
from src.utils.generador_datos import generar_lista_aleatoria, generar_lista_ordenada, generar_lista_inversa

# Prueba todos los algoritmos de ordenamiento con listas aleatorias
@pytest.mark.parametrize("algoritmo", [
    bubble_sort,
    selection_sort,
    insertion_sort,
    quick_sort,
    merge_sort,
])
def test_ordenamiento_listas_aleatorias(algoritmo):
    lista = generar_lista_aleatoria(100)  # Genera una lista aleatoria de 100 elementos
    lista_ordenada = sorted(lista)        # Ordena la lista usando la función built-in
    assert algoritmo(list(lista)) == lista_ordenada  # Verifica que el algoritmo ordena correctamente

# Prueba todos los algoritmos con listas ya ordenadas
@pytest.mark.parametrize("algoritmo", [
    bubble_sort,
    selection_sort,
    insertion_sort,
    quick_sort,
    merge_sort,
])
def test_ordenamiento_listas_ordenadas(algoritmo):
    lista = generar_lista_ordenada(50)    # Genera una lista ordenada de 50 elementos
    lista_ordenada = sorted(lista)
    assert algoritmo(list(lista)) == lista_ordenada

# Prueba todos los algoritmos con listas en orden inverso
@pytest.mark.parametrize("algoritmo", [
    bubble_sort,
    selection_sort,
    insertion_sort,
    quick_sort,
    merge_sort,
])
def test_ordenamiento_listas_inversas(algoritmo):
    lista = generar_lista_inversa(75)     # Genera una lista en orden inverso de 75 elementos
    lista_ordenada = sorted(lista)
    assert algoritmo(list(lista)) == lista_ordenada

# Prueba los algoritmos con una lista vacía
def test_ordenamiento_lista_vacia():
    assert bubble_sort([]) == []
    assert quick_sort([]) == []
    assert selection_sort([]) == []
    assert insertion_sort([]) == []
    assert merge_sort([]) == []

# Prueba los algoritmos con una lista de un solo elemento
def test_ordenamiento_lista_un_elemento():
    assert bubble_sort([5]) == [5]
    assert quick_sort([10]) == [10]
    assert selection_sort([7]) == [7]
    assert insertion_sort([3]) == [3]
    assert merge_sort([8]) == [8]