import time
import copy

def medir_tiempo_ejecucion(algoritmo_func, datos):
    
    # Mide el tiempo de ejecución de una función de algoritmo.
    # Hace una copia de los datos para no modificar la lista original.
    
    # Se hace una copia profunda de los datos para evitar modificar la lista original
    datos_copia = copy.deepcopy(datos)
    
    # Se toma el tiempo antes de ejecutar el algoritmo
    inicio = time.perf_counter()  # Preciso para medir tiempos cortos
    
    # Se ejecuta el algoritmo con la copia de los datos
    algoritmo_func(datos_copia)
    
    # Se toma el tiempo después de ejecutar el algoritmo
    fin = time.perf_counter()
    
    # Se retorna la diferencia de tiempo (duración de la ejecución)
    return fin - inicio  # Tiempo en segundos