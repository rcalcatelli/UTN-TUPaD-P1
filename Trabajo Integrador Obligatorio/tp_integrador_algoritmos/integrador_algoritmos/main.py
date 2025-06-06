# Importamos las librerías necesarias
import timeit  # timeit: para medir el tiempo de ejecución de los algoritmos
import random  # random: para generar números aleatorios
from src.algoritmos_ordenamiento import ( # Para importar los algoritmos de ordenamiento
    ordenamiento_seleccion, 
    ordenamiento_insercion,
    ordenamiento_burbuja,
    quicksort,
    mergesort
)
from src.algoritmos_busqueda import busqueda_lineal, busqueda_binaria # Para importar los algoritmos de búsqueda
from src.utilidades import mezclar # Para importar la función mezclar

# Ejecuta y mide el tiempo de varios algoritmos de ordenamiento
def ejecutar_algoritmos_ordenamiento(lista_original):
    algoritmos = [
        ("Selection Sort", ordenamiento_seleccion),
        ("Insertion Sort", ordenamiento_insercion),
        ("Bubble Sort", ordenamiento_burbuja),
        ("Quicksort", quicksort),
        ("Mergesort", mergesort)
    ]
    
    tiempos = {}
    lista_ordenada = sorted(lista_original)  # Lista ordenada de referencia
    
    print("\n=== TIEMPOS DE ORDENAMIENTO ===")
    for nombre, funcion in algoritmos:
        copia = lista_original.copy()  # Copia para no modificar la original
        
        inicio = timeit.default_timer()
        resultado = funcion(copia)  # Ejecuta el algoritmo
        fin = timeit.default_timer()
        
        correcto = "OK" if resultado == lista_ordenada else "ERROR"  # Verifica si ordenó bien
        tiempo = fin - inicio
        tiempos[nombre] = tiempo # Guarda el tiempo de ejecución en el diccionario
        
        print(f"{nombre}: {tiempo:.6f} segundos ({correcto})") 
    
    return tiempos

# Ejecuta y mide el tiempo de búsqueda lineal y binaria
def ejecutar_algoritmos_busqueda(lista_original, lista_ordenada):
    objetivo = random.choice(lista_original)  # Selecciona un elemento aleatorio de la lista
    print(f"\nBuscando: {objetivo}")
    
    print("\n=== TIEMPOS DE BÚSQUEDA ===")
    
    # Búsqueda lineal
    inicio = timeit.default_timer() 
    posicion_lineal = busqueda_lineal(lista_original, objetivo) # Busca el objetivo en la lista original
    tiempo_lineal = timeit.default_timer() - inicio
    print(f"Búsqueda lineal: {tiempo_lineal:.6f} segundos → Posición de lista original: {posicion_lineal}")
    
    # Búsqueda binaria
    inicio = timeit.default_timer()
    posicion_binaria = busqueda_binaria(lista_ordenada, objetivo) # Busca el objetivo en la lista ordenada
    tiempo_binario = timeit.default_timer() - inicio
    print(f"Búsqueda binaria: {tiempo_binario:.6f} segundos → Posición de lista ordenada: {posicion_binaria}")
    
    # Compara la velocidad de ambas búsquedas
    if tiempo_binario > 0:
        mejora = tiempo_lineal / tiempo_binario
        print(f"Búsqueda binaria fue {mejora:.1f}x más rápida que la lineal")

# Muestra el menú principal y pide una opción al usuario
def mostrar_menu():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Ejecutar algoritmos de ordenamiento")
    print("2. Ejecutar algoritmos de búsqueda")
    print("3. Ejecutar ambos")
    print("4. Salir")
    return input("Seleccione una opción (1-4): ")

# Función principal del programa
def main():
    print("=== COMPARADOR DE ALGORITMOS ===")
    
    # Parámetros de la lista a generar
    n = 10000
    min_val = 1
    max_val = 1000000
    
    # Genera una lista aleatoria de n elementos
    lista_original = [random.randint(min_val, max_val) for _ in range(n)]
    print(f"Lista generada con {n} elementos!")
    lista_ordenada = sorted(lista_original)
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            # Ejecuta solo los algoritmos de ordenamiento
            tiempos = ejecutar_algoritmos_ordenamiento(lista_original)
            
            # Encuentra el algoritmo más rápido y más lento
            mejor_orden = None
            peor_orden = None
            mejor_tiempo = float('inf')
            peor_tiempo = float('-inf')
            
            for algoritmo, tiempo in tiempos.items():
                if tiempo < mejor_tiempo:
                    mejor_tiempo = tiempo
                    mejor_orden = algoritmo
                if tiempo > peor_tiempo:
                    peor_tiempo = tiempo
                    peor_orden = algoritmo
            
            print(f"\nAlgoritmo más rápido: {mejor_orden}")
            print(f"Algoritmo más lento: {peor_orden}")
            
        elif opcion == "2":
            # Ejecuta solo los algoritmos de búsqueda
            ejecutar_algoritmos_busqueda(lista_original, lista_ordenada)
            
        elif opcion == "3":
            # Ejecuta ambos tipos de algoritmos
            tiempos = ejecutar_algoritmos_ordenamiento(lista_original)
            
            # Encuentra el algoritmo más rápido y más lento
            mejor_orden = None
            peor_orden = None
            mejor_tiempo = float('inf')
            peor_tiempo = float('-inf')
            
            for algoritmo, tiempo in tiempos.items(): # Itera sobre los algoritmos y sus tiempos
                if tiempo < mejor_tiempo:
                    mejor_tiempo = tiempo
                    mejor_orden = algoritmo
                if tiempo > peor_tiempo:
                    peor_tiempo = tiempo
                    peor_orden = algoritmo
            
            print(f"\nAlgoritmo más rápido: {mejor_orden}")
            print(f"Algoritmo más lento: {peor_orden}")
            ejecutar_algoritmos_busqueda(lista_original, lista_ordenada)
            
        elif opcion == "4":
            # Sale del programa
            print("\n¡Gracias por usar el comparador de algoritmos!")
            break
            
        else:
            print("\nOpción no válida. Por favor, seleccione una opción del 1 al 4.")

# Punto de entrada del programa
if __name__ == "__main__":
    main() 