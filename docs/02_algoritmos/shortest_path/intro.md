# Shortest Path

Para aprender a resolver problemas de programación relacionados con el camino más corto ("shortest path"), deberemos cubrir los siguientes conceptos y técnicas algorítmicas.

1. **Estructuras de Datos Básicas**:
    - **Grafos**: Los conceptos: 
        - nodos (o vértices) y 
        - aristas, y las representaciones comunes de grafos, 
        - listas de adyacencia y 
        - matrices de adyacencia.
    - **Colas de Prioridad**: Necesarias para implementar algoritmos como Dijkstra.

2. **Algoritmos Clásicos**:
    - **Búsqueda en Amplitud (BFS)**: Bread First Search es útil para encontrar el camino más corto en un grafo no ponderado.
    - **Dijkstra**: Algoritmo para encontrar el camino más corto desde un solo nodo a todos los demás en un grafo con aristas no negativas.
    - **Bellman-Ford**: Permite encontrar caminos más cortos en grafos con aristas negativas.
    - **Floyd-Warshall**: Un algoritmo para encontrar caminos más cortos entre todos los pares de nodos en un grafo.
    - **A***: Algoritmo de búsqueda informada que utiliza heurísticas para encontrar el camino más corto de manera eficiente, especialmente en grafos grandes.

3. **Conceptos Avanzados**:
    - **Algoritmo de Johnson**: Combina Bellman-Ford y Dijkstra para resolver el problema de caminos más cortos entre todos los pares en grafos con aristas negativas.
    - **Teoría de Caminos Mínimos**: Incluye técnicas como el Shortest Path Faster Algorithm (SPFA), que es una optimización del Bellman-Ford.

4. **Casos Especiales**:
    - grafos dirigidos, 
    - no dirigidos, 
    - con ciclos y 
    - sin ciclos.




