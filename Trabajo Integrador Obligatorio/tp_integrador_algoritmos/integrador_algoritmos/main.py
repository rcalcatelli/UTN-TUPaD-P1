import timeit
import random
import matplotlib.pyplot as plt
from src.algoritmos_ordenamiento import (
    ordenamiento_seleccion,
    ordenamiento_insercion,
    ordenamiento_burbuja,
    quicksort,
    mergesort
)
from src.algoritmos_busqueda import busqueda_lineal, busqueda_binaria
from src.utilidades import mezclar

def mostrar_grafico_tiempos(tiempos, titulo):
    # Crear figura y eje
    plt.figure(figsize=(12, 6))
    
    # Crear gráfico de barras
    algoritmos = list(tiempos.keys())
    tiempos_valores = list(tiempos.values())
    
    # Crear barras con colores diferentes
    barras = plt.bar(algoritmos, tiempos_valores)
    
    # Personalizar colores
    for i, barra in enumerate(barras):
        barra.set_color(plt.cm.viridis(i/len(algoritmos)))
    
    # Agregar etiquetas y título
    plt.title(titulo, pad=20, fontsize=14, fontweight='bold')
    plt.xlabel('Algoritmos', labelpad=10)
    plt.ylabel('Tiempo (segundos)', labelpad=10)
    
    # Rotar etiquetas del eje x
    plt.xticks(rotation=45, ha='right')
    
    # Agregar valores sobre las barras
    for i, v in enumerate(tiempos_valores):
        plt.text(i, v, f'{v:.4f}s', ha='center', va='bottom')
    
    # Agregar grid
    plt.grid(True, linestyle='--', alpha=0.3)
    
    # Ajustar layout
    plt.tight_layout()
    
    # Mostrar gráfico
    plt.show()

def mostrar_grafico_tiempos_ordenamiento(datos_tiempos):
    plt.figure(figsize=(10, 6))
    
    for nombre_algoritmo, tiempos in datos_tiempos.items():
        tamaños_lista = sorted(tiempos.keys())
        tiempos_algoritmo = [tiempos[tamaño] for tamaño in tamaños_lista]
        plt.plot(tamaños_lista, tiempos_algoritmo, marker='o', linestyle='-', label=nombre_algoritmo)
        
    plt.title('Rendimiento de Algoritmos de Ordenamiento (Listas Aleatorias)')
    plt.xlabel('Tamaño de la Lista (n)')
    plt.ylabel('Tiempo de Ejecución (segundos)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def mostrar_grafico_tiempos_busqueda(datos_tiempos):
    plt.figure(figsize=(10, 6))
    
    for nombre_algoritmo, tiempos in datos_tiempos.items():
        tamaños_lista = sorted(tiempos.keys())
        tiempos_algoritmo = [tiempos[tamaño] for tamaño in tamaños_lista]
        plt.plot(tamaños_lista, tiempos_algoritmo, marker='o', linestyle='-', label=nombre_algoritmo)
        
    plt.title('Rendimiento de Algoritmos de Búsqueda (Listas Aleatorias)')
    plt.xlabel('Tamaño de la Lista (n)')
    plt.ylabel('Tiempo de Ejecución (segundos)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def ejecutar_algoritmos_ordenamiento_multi_size(tamaños_lista, min_val, max_val):
    algoritmos = [
        ("Bubble Sort", ordenamiento_burbuja),
        ("Selection Sort", ordenamiento_seleccion),
        ("Insertion Sort", ordenamiento_insercion),
        ("Quick Sort", quicksort),
        ("Merge Sort", mergesort)
    ]
    
    datos_tiempos = {nombre: {} for nombre, _ in algoritmos}
    
    print("\n=== COMPARANDO TIEMPOS DE ORDENAMIENTO PARA DIFERENTES TAMAÑOS ===")
    
    for n in tamaños_lista:
        print(f"Generando lista de tamaño {n}...")
        lista_original = [random.randint(min_val, max_val) for _ in range(n)]
        
        for nombre, funcion in algoritmos:
            copia = lista_original.copy()
            
            inicio = timeit.default_timer()
            resultado = funcion(copia)
            fin = timeit.default_timer()
            
            tiempo = fin - inicio
            datos_tiempos[nombre][n] = tiempo
            
            # Opcional: verificar orden para cada tamaño (puede ser lento)
            # correcto = "OK" if resultado == sorted(lista_original) else "ERROR"
            # print(f"  {nombre} (Tamaño {n}): {tiempo:.6f} segundos ({correcto})")
        print(f"Comparación para tamaño {n} completa.")
        
    return datos_tiempos

def ejecutar_algoritmos_busqueda_multi_size(tamaños_lista, min_val, max_val):
    algoritmos = [
        ("Búsqueda Lineal", busqueda_lineal),
        ("Búsqueda Binaria", busqueda_binaria)
    ]
    
    datos_tiempos = {nombre: {} for nombre, _ in algoritmos}
    
    print("\n=== COMPARANDO TIEMPOS DE BÚSQUEDA PARA DIFERENTES TAMAÑOS ===")
    
    for n in tamaños_lista:
        print(f"Generando lista de tamaño {n}...")
        # Para búsqueda binaria, la lista debe estar ordenada
        lista_original = [random.randint(min_val, max_val) for _ in range(n)]
        lista_ordenada = sorted(lista_original)
        
        # Seleccionar un objetivo que esté en la lista para obtener tiempos representativos
        objetivo = random.choice(lista_original) if lista_original else None
        
        if objetivo is not None:
            # Ejecutar Búsqueda Lineal
            nombre, funcion = algoritmos[0]
            inicio = timeit.default_timer()
            funcion(lista_original, objetivo)
            fin = timeit.default_timer()
            datos_tiempos[nombre][n] = fin - inicio
            
            # Ejecutar Búsqueda Binaria
            nombre, funcion = algoritmos[1]
            inicio = timeit.default_timer()
            funcion(lista_ordenada, objetivo)
            fin = timeit.default_timer()
            datos_tiempos[nombre][n] = fin - inicio
            
            print(f"Comparación de búsqueda para tamaño {n} completa.")
        else:
            print(f"Lista de tamaño {n} vacía, omitiendo búsqueda.")
            # Añadir 0 o None para mantener la estructura si es necesario
            # datos_tiempos["Búsqueda Lineal"][n] = 0
            # datos_tiempos["Búsqueda Binaria"][n] = 0
        
    return datos_tiempos

def ejecutar_algoritmos_busqueda_single_size(lista_original, lista_ordenada):
    # Función original de comparación de búsqueda para un solo tamaño
    objetivo = lista_original[-1]
    print(f"\nBuscando: {objetivo}")
    
    print("\n=== TIEMPOS DE BÚSQUEDA ===")
    
    # Búsqueda lineal
    inicio = timeit.default_timer()
    posicion_lineal = busqueda_lineal(lista_original, objetivo)
    tiempo_lineal = timeit.default_timer() - inicio
    print(f"Búsqueda lineal: {tiempo_lineal:.6f} segundos → Posición: {posicion_lineal}")
    
    # Búsqueda binaria
    inicio = timeit.default_timer()
    posicion_binaria = busqueda_binaria(lista_ordenada, objetivo)
    tiempo_binario = timeit.default_timer() - inicio
    print(f"Búsqueda binaria: {tiempo_binario:.6f} segundos → Posición: {posicion_binaria}")
    
    if tiempo_binario > 0:
        mejora = tiempo_lineal / tiempo_binario
        print(f"Búsqueda binaria fue {mejora:.1f}x más rápida que la lineal")
    
    # Esta función no retorna tiempos para graficado multi-size, solo imprime
    # return {"Búsqueda Lineal": tiempo_lineal, "Búsqueda Binaria": tiempo_binario}

def mostrar_menu():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Ejecutar y comparar algoritmos de ordenamiento (para gráfico)")
    print("2. Ejecutar algoritmos de búsqueda (tamaño base)")
    print("3. Ejecutar ambos (ordenamiento para gráfico + búsqueda tamaño base)")
    print("4. Mostrar gráfico de tiempos de ordenamiento")
    print("5. Ejecutar y comparar algoritmos de búsqueda (para gráfico)")
    print("6. Mostrar gráfico de tiempos de búsqueda")
    print("7. Salir")
    return input("Seleccione una opción (1-7): ")

def main():
    print("=== COMPARADOR DE ALGORITMOS ===")
    
    # Configuración por defecto
    n_busqueda_single = 10000 # Tamaño de lista base para busqueda opción 2
    min_val = 1
    max_val = 1000000
    
    # Tamaños de lista para el gráfico de ordenamiento
    tamaños_grafico_ordenamiento = [100, 500, 1000, 2000, 5000, 10000]
    
    # Tamaños de lista para el gráfico de búsqueda (pueden ser más grandes)
    tamaños_grafico_busqueda = [10000, 50000, 100000, 500000, 1000000]
    
    # Variables para almacenar los tiempos para los gráficos
    datos_tiempos_ordenamiento_grafico = {}
    datos_tiempos_busqueda_grafico = {}
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            # Ejecutar algoritmos de ordenamiento para recopilar datos de grafico
            datos_tiempos_ordenamiento_grafico = ejecutar_algoritmos_ordenamiento_multi_size(tamaños_grafico_ordenamiento, min_val, max_val)
            print("\nDatos de ordenamiento recopilados para gráfico listos.")
            
        elif opcion == "2":
            # Ejecutar algoritmos de búsqueda para tamaño base
            lista_original_single = [random.randint(min_val, max_val) for _ in range(n_busqueda_single)]
            lista_ordenada_single = sorted(lista_original_single)
            ejecutar_algoritmos_busqueda_single_size(lista_original_single, lista_ordenada_single)
            print("\nComparación de búsqueda para tamaño base completa.")
            
        elif opcion == "3":
            # Ejecutar ambos (ordenamiento para gráfico + búsqueda tamaño base)
            datos_tiempos_ordenamiento_grafico = ejecutar_algoritmos_ordenamiento_multi_size(tamaños_grafico_ordenamiento, min_val, max_val)
            print("\nDatos de ordenamiento recopilados para gráfico listos.")
            
            lista_original_single = [random.randint(min_val, max_val) for _ in range(n_busqueda_single)]
            lista_ordenada_single = sorted(lista_original_single)
            ejecutar_algoritmos_busqueda_single_size(lista_original_single, lista_ordenada_single)
            print("\nComparación de búsqueda para tamaño base completa.")
            
        elif opcion == "4":
            # Mostrar gráfico de tiempos de ordenamiento
            if datos_tiempos_ordenamiento_grafico:
                mostrar_grafico_tiempos_ordenamiento(datos_tiempos_ordenamiento_grafico)
            else:
                print("\nPrimero debe ejecutar los algoritmos de ordenamiento para el gráfico (opción 1 o 3)")
                
        elif opcion == "5":
            # Ejecutar algoritmos de búsqueda para recopilar datos de grafico
            datos_tiempos_busqueda_grafico = ejecutar_algoritmos_busqueda_multi_size(tamaños_grafico_busqueda, min_val, max_val)
            print("\nDatos de búsqueda recopilados para gráfico listos.")
            
        elif opcion == "6":
            # Mostrar gráfico de tiempos de búsqueda
            if datos_tiempos_busqueda_grafico:
                mostrar_grafico_tiempos_busqueda(datos_tiempos_busqueda_grafico)
            else:
                print("\nPrimero debe ejecutar los algoritmos de búsqueda para el gráfico (opción 5)")
            
        elif opcion == "7":
            print("\n¡Gracias por usar el comparador de algoritmos!")
            break
            
        else:
            print("\nOpción no válida. Por favor, seleccione una opción del 1 al 7.")

if __name__ == "__main__":
    main() 