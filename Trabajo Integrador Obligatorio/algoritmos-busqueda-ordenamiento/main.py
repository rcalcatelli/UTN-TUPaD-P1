# Importa funciones y clases de los módulos de búsqueda
from src.busqueda.lineal import busqueda_lineal
from src.busqueda.binaria import busqueda_binaria

# Importa funciones de los módulos de ordenamiento
from src.ordenamiento.burbuja import bubble_sort
from src.ordenamiento.seleccion import selection_sort
from src.ordenamiento.insercion import insertion_sort
from src.ordenamiento.quicksort import quicksort
from src.ordenamiento.mergesort import merge_sort

# Importa utilidades para generar datos, medir tiempo y graficar
from src.utils.generador_datos import (
    generar_lista_aleatoria,
    generar_lista_ordenada,
    generar_lista_inversa
    # puedes añadir casi_ordenada si la usas
)
from src.utils.medidor_tiempo import medir_tiempo_ejecucion
import matplotlib.pyplot as plt

import copy
import random
import sys

def ejecutar_experimentos_ordenamiento():
    """
    Ejecuta experimentos para comparar el rendimiento de los algoritmos de ordenamiento.
    """
    # Diccionario con los algoritmos de ordenamiento a probar
    algoritmos_ordenamiento = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Quick Sort": quicksort,
        "Merge Sort": merge_sort
    }

    # Tamaños de listas pequeños para algoritmos lentos (O(n^2))
    tamanos_n_pequenos = [10, 50, 100, 200, 500, 1000, 2000]
    # Tamaños grandes para algoritmos rápidos (O(n log n))
    tamanos_n_grandes = [1000, 5000, 10000, 50000, 100000]

    # Experimento con listas aleatorias
    print("--- Experimento de Ordenamiento: Listas Aleatorias ---")
    resultados_aleatorios = {nombre: [] for nombre in algoritmos_ordenamiento.keys()}
    
    # Pruebas para algoritmos O(N^2)
    for n in tamanos_n_pequenos:
        lista_original = generar_lista_aleatoria(n)
        print(f"Probando con N = {n}")
        for nombre, alg_func in algoritmos_ordenamiento.items():
            # Salta algoritmos lentos para listas grandes
            if "Sort" in nombre and n > 2000 and (nombre == "Bubble Sort" or nombre == "Selection Sort" or nombre == "Insertion Sort"):
                print(f"  Saltando {nombre} para N={n} (demasiado lento)")
                continue
            
            # Ejecuta el algoritmo 3 veces y promedia el tiempo
            tiempos = []
            for _ in range(3):
                tiempo = medir_tiempo_ejecucion(alg_func, lista_original)
                tiempos.append(tiempo)
            promedio_tiempo = sum(tiempos) / len(tiempos)
            
            resultados_aleatorios[nombre].append((n, promedio_tiempo))
            print(f"  {nombre}: {promedio_tiempo:.6f} segundos")
    
    # Grafica los resultados de ordenamiento con listas aleatorias
    graficar_rendimiento(resultados_aleatorios,
        "Rendimiento de Algoritmos de Ordenamiento (Listas Aleatorias)",
        "Tamaño de la Lista (n)", "Tiempo de Ejecución (segundos)")

    # Experimento con listas ya ordenadas
    print("\n--- Experimento de Ordenamiento: Listas Ordenadas ---")
    resultados_ordenados = {nombre: [] for nombre in algoritmos_ordenamiento.keys()}
    for n in tamanos_n_pequenos:
        lista_original = generar_lista_ordenada(n)
        print(f"Probando con N = {n}")
        for nombre, alg_func in algoritmos_ordenamiento.items():
            tiempos = []
            for _ in range(3):
                tiempo = medir_tiempo_ejecucion(alg_func, lista_original)
                tiempos.append(tiempo)
            promedio_tiempo = sum(tiempos) / len(tiempos)
            
            resultados_ordenados[nombre].append((n, promedio_tiempo))
            print(f"  {nombre}: {promedio_tiempo:.6f} segundos")
            
    # Grafica los resultados de ordenamiento con listas ordenadas
    graficar_rendimiento(resultados_ordenados,
        "Rendimiento de Algoritmos de Ordenamiento (Listas Ordenadas)",
        "Tamaño de la Lista (n)", "Tiempo de Ejecución (segundos)")

    # Puedes añadir experimentos para listas inversas y casi ordenadas de manera similar

def ejecutar_experimentos_busqueda():
    """
    Ejecuta experimentos para comparar el rendimiento de los algoritmos de búsqueda.
    """
    tamanos_n = [1000, 10000, 50000, 100000, 500000, 1000000]
    algoritmos_busqueda = {
        "Búsqueda Lineal": busqueda_lineal,
        "Búsqueda Binaria": busqueda_binaria,
    }
    print("--- Experimento de Búsqueda: Listas Aleatorias (Lineal) y Ordenadas (Binaria) ---")
    resultados_busqueda = {nombre: [] for nombre in algoritmos_busqueda.keys()}
    for n in tamanos_n:
        lista_lineal = generar_lista_aleatoria(n)
        elemento_lineal = random.choice(lista_lineal)
        lista_binaria = generar_lista_ordenada(n)
        elemento_binaria = random.choice(lista_binaria)
        print(f"Probando con N = {n}")
        tiempo_lineal = medir_tiempo_ejecucion(lambda l: busqueda_lineal(l, elemento_lineal), lista_lineal)
        resultados_busqueda["Búsqueda Lineal"].append((n, tiempo_lineal))
        print(f"  Búsqueda Lineal: {tiempo_lineal:.6f} segundos")
        tiempo_binaria = medir_tiempo_ejecucion(lambda l: busqueda_binaria(l, elemento_binaria), lista_binaria)
        resultados_busqueda["Búsqueda Binaria"].append((n, tiempo_binaria))
        print(f"  Búsqueda Binaria: {tiempo_binaria:.6f} segundos")
    graficar_rendimiento(resultados_busqueda,
                         "Rendimiento de Algoritmos de Búsqueda",
                         "Tamaño de la Lista (n)", "Tiempo de Ejecución (segundos)")

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Probar algoritmos de ordenamiento")
        print("2. Probar algoritmos de búsqueda")
        print("3. Ejecutar experimentos de rendimiento (ordenamiento)")
        print("4. Ejecutar experimentos de rendimiento (búsqueda)")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            probar_ordenamiento()
        elif opcion == "2":
            probar_busqueda()
        elif opcion == "3":
            ejecutar_experimentos_ordenamiento()
        elif opcion == "4":
            ejecutar_experimentos_busqueda()
        elif opcion == "5":
            print("¡Hasta luego!")
            sys.exit(0)
        else:
            print("Opción no válida. Intente de nuevo.")


def probar_ordenamiento():
    print("\n--- Prueba de Algoritmos de Ordenamiento ---")
    algoritmos = {
        "1": ("Bubble Sort", bubble_sort),
        "2": ("Selection Sort", selection_sort),
        "3": ("Insertion Sort", insertion_sort),
        "4": ("Quick Sort", quicksort),
        "5": ("Merge Sort", merge_sort)
    }
    for k, v in algoritmos.items():
        print(f"{k}. {v[0]}")
    opcion = input("Seleccione un algoritmo: ")
    if opcion not in algoritmos:
        print("Opción no válida.")
        return
    lista = input("Ingrese una lista de números separados por coma (ej: 5,3,8,1): ")
    try:
        lista = [int(x.strip()) for x in lista.split(",") if x.strip() != ""]
    except Exception:
        print("Entrada inválida.")
        return
    if not lista:
        print("\nCaso lista vacía:")
        print("Lista vacía ordenada:", algoritmos[opcion][1]([]))
        elemento = input("Ingrese el número a buscar en la lista vacía: ")
        try:
            elemento = int(elemento)
        except Exception:
            print("Elemento inválido.")
            return
        print(f"Posición de {elemento} en lista vacía: No encontrado")
        return
    elemento = input("Ingrese el número a buscar en la lista: ")
    try:
        elemento = int(elemento)
    except Exception:
        print("Elemento inválido.")
        return
    print(f"\nLista original: {lista}")
    tiempo_orden = medir_tiempo_ejecucion(algoritmos[opcion][1], lista)
    resultado = algoritmos[opcion][1](lista.copy())
    print(f"Lista ordenada: {resultado}")
    print(f"Tiempo de ordenamiento: {tiempo_orden:.6f} segundos")
    pos_original = busqueda_lineal(lista, elemento)
    tiempo_busq_orig = medir_tiempo_ejecucion(lambda l: busqueda_lineal(l, elemento), lista)
    print(f"Posición de {elemento} en la lista original: {pos_original if pos_original != -1 else 'No encontrado'} (Tiempo: {tiempo_busq_orig:.6f} s)")
    pos_ordenada = busqueda_lineal(resultado, elemento)
    tiempo_busq_ord = medir_tiempo_ejecucion(lambda l: busqueda_lineal(l, elemento), resultado)
    print(f"Posición de {elemento} en la lista ordenada: {pos_ordenada if pos_ordenada != -1 else 'No encontrado'} (Tiempo: {tiempo_busq_ord:.6f} s)")


def probar_busqueda():
    print("\n--- Prueba de Algoritmos de Búsqueda ---")
    algoritmos = {
        "1": ("Búsqueda Lineal", busqueda_lineal),
        "2": ("Búsqueda Binaria", busqueda_binaria)
    }
    for k, v in algoritmos.items():
        print(f"{k}. {v[0]}")
    opcion = input("Seleccione un algoritmo: ")
    if opcion not in algoritmos:
        print("Opción no válida.")
        return
    lista = input("Ingrese una lista de números separados por coma (ej: 5,3,8,1): ")
    try:
        lista = [int(x.strip()) for x in lista.split(",") if x.strip() != ""]
    except Exception:
        print("Entrada inválida.")
        return
    if not lista:
        print("\nCaso lista vacía:")
        elemento = input("Ingrese el elemento a buscar en la lista vacía: ")
        try:
            elemento = int(elemento)
        except Exception:
            print("Elemento inválido.")
            return
        print(f"Posición de {elemento} en lista vacía: No encontrado")
        return
    elemento = input("Ingrese el elemento a buscar: ")
    try:
        elemento = int(elemento)
    except Exception:
        print("Elemento inválido.")
        return
    print(f"\nLista original: {lista}")
    lista_ordenada = sorted(lista)
    print(f"Lista ordenada: {lista_ordenada}")
    if opcion == "1":  # Búsqueda lineal
        import time
        inicio = time.perf_counter()
        resultado_orig = busqueda_lineal(lista, elemento)
        fin = time.perf_counter()
        print(f"Resultado de búsqueda lineal en lista original: {resultado_orig if resultado_orig != -1 else 'No encontrado'} (Tiempo: {fin-inicio:.6f} s)")
        inicio = time.perf_counter()
        resultado_ord = busqueda_lineal(lista_ordenada, elemento)
        fin = time.perf_counter()
        print(f"Resultado de búsqueda lineal en lista ordenada: {resultado_ord if resultado_ord != -1 else 'No encontrado'} (Tiempo: {fin-inicio:.6f} s)")
    elif opcion == "2":  # Búsqueda binaria
        import time
        inicio = time.perf_counter()
        resultado_ord = busqueda_binaria(lista_ordenada, elemento)
        fin = time.perf_counter()
        print(f"Resultado de búsqueda binaria en lista ordenada: {resultado_ord if resultado_ord != -1 else 'No encontrado'} (Tiempo: {fin-inicio:.6f} s)")
        inicio = time.perf_counter()
        resultado_orig = busqueda_binaria(lista, elemento)
        fin = time.perf_counter()
        print(f"Resultado de búsqueda binaria en lista original: {resultado_orig if resultado_orig != -1 else 'No encontrado'} (Tiempo: {fin-inicio:.6f} s)")


def graficar_rendimiento(resultados, titulo, xlabel, ylabel):
    for nombre, datos in resultados.items():
        x = [n for n, _ in datos]
        y = [t for _, t in datos]
        plt.plot(x, y, label=nombre)
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    menu()
