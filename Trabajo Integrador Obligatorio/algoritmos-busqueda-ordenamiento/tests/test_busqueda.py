import pytest
from src.busqueda.lineal import busqueda_lineal
from src.busqueda.binaria import busqueda_binaria
from src.utils.generador_datos import generar_lista_aleatoria, generar_lista_ordenada

# Prueba: buscar un elemento existente con búsqueda lineal
def test_busqueda_lineal_elemento_encontrado():
    lista = [10, 20, 30, 40, 50]
    assert busqueda_lineal(lista, 30) == 2
    assert busqueda_lineal(lista, 10) == 0
    assert busqueda_lineal(lista, 50) == 4

# Prueba: buscar un elemento inexistente con búsqueda lineal
def test_busqueda_lineal_elemento_no_encontrado():
    lista = [10, 20, 30, 40, 50]
    assert busqueda_lineal(lista, 25) == -1
    assert busqueda_lineal([], 100) == -1

# Prueba: buscar un elemento existente con búsqueda binaria
def test_busqueda_binaria_elemento_encontrado():
    lista_ordenada = [10, 20, 30, 40, 50]
    assert busqueda_binaria(lista_ordenada, 30) == 2
    assert busqueda_binaria(lista_ordenada, 10) == 0
    assert busqueda_binaria(lista_ordenada, 50) == 4

# Prueba: buscar un elemento inexistente con búsqueda binaria
def test_busqueda_binaria_elemento_no_encontrado():
    lista_ordenada = [10, 20, 30, 40, 50]
    assert busqueda_binaria(lista_ordenada, 25) == -1
    assert busqueda_binaria([], 100) == -1