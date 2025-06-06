# Algoritmos de Ordenamiento y Búsqueda

Este proyecto implementa y compara diferentes algoritmos de ordenamiento y búsqueda, permitiendo analizar su rendimiento en términos de tiempo de ejecución mediante una interfaz de consola interactiva.

## Características

- Implementación de múltiples algoritmos de ordenamiento:
  - Selection Sort
  - Insertion Sort
  - Bubble Sort
  - Quicksort
  - Mergesort

- Implementación de algoritmos de búsqueda:
  - Búsqueda Lineal
  - Búsqueda Binaria

- Menú interactivo para seleccionar las operaciones a realizar
- Comparación de tiempos de ejecución en consola
- Generación de listas aleatorias para pruebas
- No requiere dependencias externas

## Estructura del Proyecto

```
integrador_algoritmos/
│
├── src/
│   ├── algoritmos_ordenamiento.py  # Implementaciones de algoritmos de ordenamiento
│   ├── algoritmos_busqueda.py      # Implementaciones de algoritmos de búsqueda
│   └── utilidades.py               # Funciones auxiliares
│
├── main.py                         # Programa principal con menú interactivo
└── README.md                       # Este archivo
```

## Requisitos

- Python 3.8 o superior (no se requieren dependencias externas)

## Instalación

1. Clonar o descargar el repositorio
2. Navegar al directorio del proyecto
3. Ejecutar el programa principal:
```bash
python main.py
```

## Uso

El programa presenta un menú interactivo con las siguientes opciones:

1. **Ejecutar algoritmos de ordenamiento**
   - Muestra los tiempos de ejecución de cada algoritmo
   - Indica el algoritmo más rápido y más lento
   - Verifica la correctitud del ordenamiento

2. **Ejecutar algoritmos de búsqueda**
   - Compara búsqueda lineal vs binaria
   - Muestra los tiempos de ejecución
   - Indica la posición del elemento encontrado

3. **Ejecutar ambos**
   - Realiza todas las comparaciones anteriores

4. **Salir**
   - Finaliza el programa

## Algoritmos Implementados

### Algoritmos de Ordenamiento

1. **Selection Sort (Ordenamiento por Selección)**
   - Complejidad: O(n²)
   - Características: Simple, in-place, no estable
   - Uso: Listas pequeñas, cuando la memoria es limitada

2. **Insertion Sort (Ordenamiento por Inserción)**
   - Complejidad: O(n²)
   - Características: Eficiente para listas pequeñas, estable
   - Uso: Listas casi ordenadas, pequeñas

3. **Bubble Sort (Ordenamiento Burbuja)**
   - Complejidad: O(n²)
   - Características: Simple, in-place, estable
   - Uso: Propósitos educativos, listas muy pequeñas

4. **Quicksort**
   - Complejidad: O(n log n) promedio
   - Características: Eficiente en la práctica, in-place
   - Uso: Caso general, listas grandes

5. **Mergesort**
   - Complejidad: O(n log n)
   - Características: Estable, requiere espacio adicional
   - Uso: Cuando se necesita estabilidad, listas grandes

### Algoritmos de Búsqueda

1. **Búsqueda Lineal**
   - Complejidad: O(n)
   - Características: Simple, funciona en listas no ordenadas
   - Uso: Listas pequeñas o no ordenadas

2. **Búsqueda Binaria**
   - Complejidad: O(log n)
   - Características: Requiere lista ordenada, muy eficiente
   - Uso: Listas ordenadas de cualquier tamaño

## Configuración

El programa utiliza los siguientes parámetros por defecto:
- Tamaño de lista: 10,000 elementos
- Rango de valores: 1 a 1,000,000

## Notas de Implementación

- Todos los algoritmos están implementados en Python puro
- Se utilizan módulos de la biblioteca estándar de Python
- No se requieren dependencias externas
- El código está organizado en módulos para mejor mantenimiento
- Se incluyen comentarios explicativos en el código

## Autores

Albertini Hugo - Calcatelli Renzo
- Materia: Programación I
- Comisión: M2025-1
- Universidad: UTN
- Año: 2025

## Contribución

Si deseas contribuir al proyecto:

1. Haz un fork del repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request