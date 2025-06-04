import random

def generar_lista_aleatoria(n):
    # Crea una lista de n números aleatorios entre 0 y n*10
    return [random.randint(0, n * 10) for _ in range(n)]

def generar_lista_ordenada(n):

    # Crea una lista ordenada de 0 a n-1
    return list(range(n))

def generar_lista_inversa(n):
    # Crea una lista ordenada de n-1 a 0
    return list(range(n - 1, -1, -1))

def generar_lista_casi_ordenada(n, intercambios_max=5):
    # Crea una lista ordenada de 0 a n-1
    lista = list(range(n))
    # Realiza una cantidad limitada de intercambios aleatorios para desordenar un poco la lista
    for _ in range(intercambios_max):
        idx1, idx2 = random.sample(range(n), 2)  # Elige dos índices distintos al azar
        lista[idx1], lista[idx2] = lista[idx2], lista[idx1]  # Intercambia los valores
    return lista