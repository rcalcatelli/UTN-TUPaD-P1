# Algoritmos de Ordenamiento y Búsqueda

Este proyecto implementa y compara diferentes algoritmos de ordenamiento y búsqueda, permitiendo analizar su rendimiento en términos de tiempo de ejecución mediante una interfaz de consola interactiva.

## 🚀 Características

- Implementación de múltiples algoritmos de ordenamiento:
  - Selection Sort
  - Insertion Sort
  - Bubble Sort
  - Quicksort
  - Mergesort
- Implementación de algoritmos de búsqueda:
  - Búsqueda Lineal
  - Búsqueda Binaria
- Menú interactivo para seleccionar operaciones
- Comparación de tiempos de ejecución en consola
- Generación de listas aleatorias para pruebas
- **No requiere dependencias externas**

## 📁 Estructura del Proyecto

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

````

## ⚙️ Requisitos

- Python 3.8 o superior  
- No se necesitan librerías externas

## 🧪 Instalación y Ejecución

```bash
# 1. Clonar o descargar el repositorio
git clone https://github.com/rcalcatelli/UTN-TUPaD-P1

# 2. Navegar al directorio
cd integrador_algoritmos

# 3. Ejecutar el programa principal
python main.py
````

## 📌 Uso

El programa presenta un menú interactivo con las siguientes opciones:

1. **Ejecutar algoritmos de ordenamiento**

   * Muestra los tiempos de ejecución de cada algoritmo
   * Indica el más rápido y más lento
   * Verifica que el ordenamiento sea correcto

2. **Ejecutar algoritmos de búsqueda**

   * Compara búsqueda lineal vs binaria
   * Muestra tiempos de ejecución
   * Indica la posición del elemento si fue encontrado

3. **Ejecutar ambos**

   * Realiza todas las comparaciones anteriores

4. **Salir**

   * Finaliza el programa

---

## 🔍 Algoritmos Implementados

### 📦 Ordenamiento

| Algoritmo      | Complejidad  | Estabilidad | Comentarios                                 |
| -------------- | ------------ | ----------- | ------------------------------------------- |
| Selection Sort | O(n²)        | ❌           | Simple, in-place, poco eficiente            |
| Insertion Sort | O(n²)        | ✅           | Bueno para listas pequeñas o casi ordenadas |
| Bubble Sort    | O(n²)        | ✅           | Educativo, ineficiente para listas grandes  |
| Quicksort      | O(n log n)\* | ❌           | Muy rápido, no estable, in-place            |
| Mergesort      | O(n log n)   | ✅           | Estable, eficiente, requiere memoria extra  |

### 🔎 Búsqueda

| Algoritmo        | Complejidad | Requiere Ordenamiento | Uso recomendado                   |
| ---------------- | ----------- | --------------------- | --------------------------------- |
| Búsqueda Lineal  | O(n)        | No                    | Listas pequeñas o desordenadas    |
| Búsqueda Binaria | O(log n)    | Sí                    | Listas ordenadas, alta eficiencia |

---

## ⚙️ Configuración por Defecto

* Tamaño de la lista: **10,000** elementos
* Rango de valores aleatorios: **1 a 1,000,000**

---

## 📌 Notas de Implementación

* Código en **Python puro**
* Estructurado por módulos para facilitar su mantenimiento
* Utiliza solo módulos de la biblioteca estándar
* Incluye comentarios explicativos en el código fuente

---

## 👥 Autores

Trabajo realizado para la materia **Programación I** - UTN (Universidad Tecnológica Nacional)  
Autores: **Renzo Calcatelli** y **Hugo Albertini**






