import pytest
from src.busqueda.lineal import busqueda_lineal
from src.busqueda.binaria import busqueda_binaria
from src.busqueda.hash_table import HashTable
from src.busqueda.busqueda_hash import busqueda_por_hash
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

# Prueba: insertar y buscar elementos en una tabla hash
def test_hash_table_insertar_y_buscar():
    ht = HashTable(10)
    ht.insertar("manzana", 5)
    ht.insertar("banana", 10)
    ht.insertar("naranja", 15)
    assert ht.buscar("manzana") == 5
    assert ht.buscar("banana") == 10
    assert ht.buscar("naranja") == 15
    assert ht.buscar("uva") is None

# Prueba: actualizar y eliminar elementos en una tabla hash
def test_hash_table_actualizar_y_eliminar():
    ht = HashTable(10)
    ht.insertar("clave1", 100)
    assert ht.buscar("clave1") == 100
    ht.insertar("clave1", 200) # Actualizar valor existente
    assert ht.buscar("clave1") == 200
    assert ht.eliminar("clave1") is True
    assert ht.buscar("clave1") is None
    assert ht.eliminar("clave_no_existente") is False

# Prueba: buscar usando función de búsqueda por hash
def test_busqueda_por_hash():
    ht = HashTable(100)
    test_data = generar_lista_aleatoria(50)
    for i, val in enumerate(test_data):
        ht.insertar(f"key_{i}", val)

    # Buscar un elemento que sabemos que existe
    idx_existente = random.randint(0, 49)
    key_existente = f"key_{idx_existente}"
    assert busqueda_por_hash(ht, key_existente) == test_data[idx_existente]

    # Buscar un elemento que no existe
    assert busqueda_por_hash(ht, "key_no_existe") is None