## 📊 Resultados de Pruebas

### 1. Pruebas de Algoritmos de Ordenamiento

- **Pruebas manuales:**  
  Cada algoritmo fue probado con:
  - Listas de ejemplo (desordenadas)
  - Listas vacías
  - Listas de un solo elemento  
  ✅ Todos devolvieron la lista correctamente ordenada, sin errores ni excepciones.

- **Pruebas interactivas:**  
  El menú permite:
  - Ingresar cualquier lista de números.
  - Ver la lista original y la lista ordenada.
  - Medir el tiempo de ordenamiento.
  - Buscar la posición de un elemento antes y después de ordenar.
  - Probar el comportamiento con lista vacía (devuelve lista vacía y no encuentra el elemento).

- **Resultados esperados:**  
  - Los algoritmos O(n²) (burbuja, selección, inserción) son mucho más lentos en listas grandes.
  - Los algoritmos O(n log n) (quicksort, mergesort) son eficientes incluso con listas grandes.

---

### 2. Pruebas de Algoritmos de Búsqueda

- **Pruebas manuales:**  
  Se probó la búsqueda lineal y binaria con:
  - Listas de ejemplo
  - Listas vacías
  - Listas de un solo elemento  
  ✅ Ambos algoritmos retornan correctamente la posición del elemento si existe, o "No encontrado" si no está.

- **Pruebas interactivas:**  
  El menú permite:
  - Ver la lista original y la lista ordenada.
  - Buscar un elemento en ambas listas (cuando aplica).
  - Medir el tiempo de búsqueda en cada caso.
  - Comprobar que la búsqueda binaria solo funciona correctamente en listas ordenadas.

- **Resultados esperados:**  
  - La búsqueda lineal funciona en cualquier lista.
  - La búsqueda binaria solo es válida en listas ordenadas.
  - En listas vacías, ningún algoritmo encuentra el elemento.

---

### 3. Pruebas de Rendimiento y Gráficos

- Se ejecutaron los experimentos de rendimiento desde el menú.
- Se generaron gráficos comparativos de tiempo de ejecución para cada algoritmo.
- Los resultados visuales confirman la diferencia de eficiencia entre algoritmos O(n²) y O(n log n) en ordenamiento, y entre los distintos métodos de búsqueda.

---

### 4. Limpieza y Organización

- Se eliminaron archivos temporales, vacíos y carpetas innecesarias para dejar el proyecto limpio y profesional.

---

### **Conclusión**

Todos los algoritmos funcionan correctamente en los casos normales y en los casos límite (listas vacías, un solo elemento, elemento no encontrado).  
El menú interactivo y los gráficos permiten comparar fácilmente el rendimiento y el funcionamiento de cada algoritmo.

---
