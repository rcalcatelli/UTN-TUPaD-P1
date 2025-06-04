# Marco Teórico: Algoritmos de Búsqueda y Ordenamiento

## 1. Introducción

La programación moderna y la ciencia de datos dependen fundamentalmente de la eficiencia con la que se procesa y organiza la información. En este contexto, los **algoritmos de búsqueda y ordenamiento** se erigen como pilares esenciales, permitiendo localizar datos específicos y estructurar colecciones para su procesamiento eficiente. La elección del algoritmo adecuado no es trivial; puede significar la diferencia entre una aplicación que responde instantáneamente y una que se bloquea con grandes volúmenes de datos.

Este marco teórico explora los fundamentos de estos algoritmos, profundizando en su funcionamiento, sus características y, crucialmente, en el **análisis de su eficiencia** mediante la Notación Big O. En este trabajo nos centraremos en los algoritmos clásicos de búsqueda y ordenamiento más utilizados en la práctica y en la enseñanza universitaria.

---

## 2. Algoritmos de Búsqueda

Los algoritmos de búsqueda tienen como objetivo encontrar uno o más elementos dentro de una estructura de datos. Su eficiencia varía drásticamente según la organización de los datos y el método empleado.

### 2.1. Búsqueda Lineal (Secuencial)

* **Concepto y Funcionamiento:** Es el método de búsqueda más simple. Consiste en recorrer secuencialmente cada elemento de una lista (o arreglo) desde el inicio hasta el final, comparando cada elemento con el valor buscado. Si el elemento se encuentra, la búsqueda termina; de lo contrario, se recorre toda la lista.
* **Análisis de Complejidad:**
    * **Mejor Caso:** $O(1)$ - El elemento buscado es el primero de la lista.
    * **Peor Caso:** $O(n)$ - El elemento buscado es el último de la lista, o no está presente.
    * **Caso Promedio:** $O(n)$ - En promedio, se recorre la mitad de la lista.
* **Complejidad Espacial:** $O(1)$ - Requiere una cantidad constante de memoria adicional.
* **Ventajas y Desventajas:** Es simple de implementar y no requiere que la lista esté ordenada. Sin embargo, es muy ineficiente para listas grandes.

### 2.2. Búsqueda Binaria

* **Concepto y Funcionamiento:** Es un algoritmo de búsqueda mucho más eficiente que la búsqueda lineal, pero requiere que la lista esté **previamente ordenada**. Funciona dividiendo repetidamente por la mitad la porción de la lista donde el elemento podría estar. En cada paso, el algoritmo compara el elemento buscado con el elemento central de la porción actual. Si son iguales, se encuentra el elemento. Si el elemento buscado es menor, la búsqueda continúa en la mitad inferior; si es mayor, en la mitad superior.
* **Análisis de Complejidad:**
    * **Mejor Caso:** $O(1)$ - El elemento buscado es el central de la lista.
    * **Peor Caso y Caso Promedio:** $O(\log n)$ - El número de comparaciones se reduce a la mitad en cada paso.
* **Complejidad Espacial:** $O(1)$ para la versión iterativa, $O(\log n)$ para la versión recursiva (debido a la pila de llamadas).
* **Ventajas y Desventajas:** Extremadamente eficiente para listas grandes y ordenadas. Su principal desventaja es el requisito de que la lista esté ordenada, lo que puede implicar un costo adicional.

---

## 3. Algoritmos de Ordenamiento

Los algoritmos de ordenamiento reorganizan los elementos de una lista (o arreglo) en un orden específico (ascendente o descendente). Son fundamentales para optimizar búsquedas (como la binaria) y facilitar el análisis de datos.

### 3.1. Bubble Sort (Ordenamiento de Burbuja)

* **Concepto y Funcionamiento:** Es uno de los algoritmos de ordenamiento más simples. Recorre repetidamente la lista, comparando pares de elementos adyacentes y los intercambia si están en el orden incorrecto. Este proceso se repite hasta que la lista está ordenada. Los elementos "más pesados" (mayores) "flotan" hacia el final de la lista en cada pasada.
* **Análisis de Complejidad:**
    * **Mejor Caso:** $O(n)$ - La lista ya está ordenada.
    * **Peor Caso y Caso Promedio:** $O(n^2)$ - Requiere múltiples pasadas y comparaciones anidadas.
* **Complejidad Espacial:** $O(1)$ - Ordena la lista "in-place".
* **Estabilidad:** Es un algoritmo **estable**.
* **Ventajas y Desventajas:** Es muy fácil de entender e implementar, pero su ineficiencia lo hace poco práctico para grandes conjuntos de datos.

### 3.2. Selection Sort (Ordenamiento por Selección)

* **Concepto y Funcionamiento:** Divide la lista en dos partes: una sublista ordenada (inicialmente vacía) y una sublista desordenada. En cada iteración, busca el elemento más pequeño (o más grande) en la sublista desordenada y lo intercambia con el primer elemento de la sublista desordenada, extendiendo así la sublista ordenada.
* **Análisis de Complejidad:**
    * **Mejor Caso, Peor Caso y Caso Promedio:** $O(n^2)$ - Siempre realiza un número fijo de comparaciones, independientemente del estado inicial de la lista.
* **Complejidad Espacial:** $O(1)$ - Ordena la lista "in-place".
* **Estabilidad:** Generalmente **no es estable** (a menos que se implemente con cuidado para mantener la estabilidad).
* **Ventajas y Desventajas:** Es simple de implementar y minimiza el número de intercambios. Sin embargo, es ineficiente para listas grandes.

### 3.3. Insertion Sort (Ordenamiento por Inserción)

* **Concepto y Funcionamiento:** También divide la lista en una parte ordenada y una desordenada. En cada iteración, toma el siguiente elemento de la sublista desordenada y lo "inserta" en su posición correcta dentro de la sublista ordenada, desplazando los elementos mayores hacia la derecha.
* **Análisis de Complejidad:**
    * **Mejor Caso:** $O(n)$ - La lista ya está ordenada.
    * **Peor Caso y Caso Promedio:** $O(n^2)$ - Para listas inversamente ordenadas o aleatorias.
* **Complejidad Espacial:** $O(1)$ - Ordena la lista "in-place".
* **Estabilidad:** Es un algoritmo **estable**.
* **Ventajas y Desventajas:** Es eficiente para listas pequeñas o listas que ya están casi ordenadas. Es simple de implementar. Su principal desventaja es su ineficiencia para listas grandes.

### 3.4. Quick Sort (Ordenamiento Rápido)

* **Concepto y Funcionamiento:** Es un algoritmo de "divide y vencerás" muy popular. Elige un elemento de la lista llamado **pivote**. Luego, reorganiza la lista de tal manera que todos los elementos menores que el pivote queden a su izquierda y todos los elementos mayores queden a su derecha. El pivote está ahora en su posición final ordenada. Finalmente, aplica recursivamente los pasos anteriores a las sublistas a ambos lados del pivote.
* **Análisis de Complejidad:**
    * **Mejor Caso y Caso Promedio:** $O(n \log n)$ - Cuando el pivote divide la lista de manera equilibrada.
    * **Peor Caso:** $O(n^2)$ - Cuando el pivote siempre es el elemento más pequeño o más grande (ej. lista ya ordenada y pivote siempre el primero).
* **Complejidad Espacial:** $O(\log n)$ (caso promedio, debido a la recursión) o $O(n)$ (peor caso, para la pila de llamadas).
* **Estabilidad:** Generalmente **no es estable**.
* **Ventajas y Desventajas:** En la práctica, es uno de los algoritmos de ordenamiento más rápidos para la mayoría de los conjuntos de datos. Su rendimiento de peor caso $O(n^2)$ es una desventaja teórica, aunque poco frecuente en la práctica con buenas estrategias de elección de pivote.

### 3.5. Merge Sort (Ordenamiento por Mezcla)

* **Concepto y Funcionamiento:** Es otro algoritmo de "divide y vencerás". Primero, divide la lista en dos mitades recursivamente hasta que cada sublista contiene un solo elemento. Luego, combina (mezcla) las sublistas ordenadas de forma recursiva para producir listas ordenadas más grandes, hasta que se tiene una única lista ordenada. El paso de "mezcla" es una operación clave y eficiente.
* **Análisis de Complejidad:**
    * **Mejor Caso, Peor Caso y Caso Promedio:** $O(n \log n)$ - Consistente para todos los casos debido a su estructura de división y mezcla equilibrada.
* **Complejidad Espacial:** $O(n)$ - Requiere un arreglo auxiliar para el proceso de mezcla.
* **Estabilidad:** Es un algoritmo **estable**.
* **Ventajas y Desventajas:** Ofrece un rendimiento consistente de $O(n \log n)$ en todos los casos y es un algoritmo estable. Su principal desventaja es que requiere espacio adicional $O(n)$, lo que puede ser un problema para grandes volúmenes de datos con memoria limitada.

---

## 4. Análisis de Algoritmos: Eficiencia y Notación Big O

El análisis de algoritmos es el proceso de determinar los recursos (tiempo y espacio) necesarios para ejecutar un algoritmo. Esto nos permite comparar algoritmos y predecir su rendimiento en diferentes escenarios.

### 4.1. Importancia del Análisis de Algoritmos
El análisis de algoritmos es crucial para predecir y comparar el rendimiento de diferentes soluciones para un mismo problema, especialmente a medida que el volumen de datos crece. No se trata de medir el tiempo exacto en segundos (ya que esto varía con el hardware y el software), sino de entender cómo el tiempo o el espacio requerido por un algoritmo escala con el tamaño de la entrada.

### 4.2. La Notación Big O (O Grande)
La Notación Big O es una notación matemática que describe el **comportamiento asintótico** del tiempo o espacio de ejecución de un algoritmo a medida que el tamaño de la entrada ($n$) tiende a infinito. Se enfoca en el **término de mayor crecimiento** de la función de complejidad y omite constantes y términos de orden inferior, ya que estos factores se vuelven insignificantes para grandes valores de $n$.

* **Clases de Complejidad Comunes:**
    * **$O(1)$ - Tiempo Constante:** El tiempo de ejecución no depende del tamaño de la entrada. (Ej: Acceder a un elemento por su índice en un arreglo).
    * **$O(\log n)$ - Tiempo Logarítmico:** El tiempo de ejecución crece muy lentamente. El problema se reduce a la mitad en cada paso. (Ej: Búsqueda Binaria).
    * **$O(n)$ - Tiempo Lineal:** El tiempo de ejecución crece directamente proporcional al tamaño de la entrada. (Ej: Búsqueda Lineal, recorrer una lista).
    * **$O(n \log n)$ - Tiempo Log-Lineal:** Es el mejor rendimiento posible para algoritmos de ordenamiento basados en comparaciones en el peor caso. (Ej: Merge Sort, Quick Sort (promedio)).
    * **$O(n^2)$ - Tiempo Cuadrático:** El tiempo de ejecución crece al cuadrado del tamaño de la entrada. Común en algoritmos con bucles anidados. (Ej: Bubble Sort, Selection Sort, Insertion Sort).
    * **$O(2^n)$ - Tiempo Exponencial:** El tiempo de ejecución se duplica con cada adición a la entrada. Extremadamente ineficiente para entradas grandes. (Ej: Algunos problemas de fuerza bruta).
    * **$O(n!)$ - Tiempo Factorial:** El tiempo de ejecución crece de forma extremadamente rápida. Muy ineficiente. (Ej: Problema del viajante de comercio con fuerza bruta).

### 4.3. Comparación de Algoritmos en la Práctica
Aquí se presenta una tabla comparativa de los algoritmos estudiados, destacando sus complejidades temporales y espaciales, así como su estabilidad.

| Algoritmo             | Funcionamiento Básico                       | Tiempo: Mejor Caso | Tiempo: Promedio | Tiempo: Peor Caso | Espacio   | Estable |
| :-------------------- | :------------------------------------------ | :----------------- | :--------------- | :---------------- | :-------- | :------ |
| **Búsqueda** |                                             |                    |                  |                   |           |         |
| Búsqueda Lineal       | Recorre secuencialmente                     | $O(1)$             | $O(n)$           | $O(n)$            | $O(1)$    | -       |
| Búsqueda Binaria      | Divide la lista ordenada por la mitad       | $O(1)$             | $O(\log n)$      | $O(\log n)$       | $O(1)$    | -       |
| **Ordenamiento** |                                             |                    |                  |                   |           |         |
| Bubble Sort           | Intercambia adyacentes                      | $O(n)$             | $O(n^2)$         | $O(n^2)$          | $O(1)$    | ✅       |
| Insertion Sort        | Inserta elemento en sublista ordenada       | $O(n)$             | $O(n^2)$         | $O(n^2)$          | $O(1)$    | ✅       |
| Selection Sort        | Encuentra mínimo y lo reubica               | $O(n^2)$           | $O(n^2)$         | $O(n^2)$          | $O(1)$    | ❌       |
| Merge Sort            | Divide y mezcla                             | $O(n \log n)$     | $O(n \log n)$   | $O(n \log n)$    | $O(n)$    | ✅       |
| Quick Sort            | Elige pivote y particiona                   | $O(n \log n)$     | $O(n \log n)$   | $O(n^2)$          | $O(\log n)$ | ❌   |

**Notas sobre la tabla:**
* Los valores de **Eficiencia (Big O)** representan el crecimiento del tiempo de ejecución en relación con el tamaño de la entrada ($n$).
* **Espacio** se refiere a la complejidad espacial auxiliar (memoria adicional requerida por el algoritmo).
* **Estable** indica si el algoritmo mantiene el orden relativo de elementos con valores iguales.

---

## 5. Conclusión del Marco Teórico

El estudio de los algoritmos de búsqueda y ordenamiento, junto con el análisis de su eficiencia, es fundamental para cualquier desarrollador. Hemos visto cómo algoritmos con lógicas aparentemente simples pueden tener complejidades muy diferentes, impactando drásticamente el rendimiento con el crecimiento de los datos. La **Notación Big O** proporciona una herramienta poderosa para predecir y comparar el comportamiento de los algoritmos de manera abstracta, permitiéndonos tomar decisiones informadas sobre qué solución aplicar.

En este trabajo nos enfocamos en los métodos más utilizados y enseñados, mostrando sus ventajas, desventajas y aplicaciones prácticas en Python.