# Union Find 


**Union-Find**, también conocido como **Disjoint Set Union (DSU)** o **Estructura de Conjuntos Disjuntos**, es una estructura de datos que maneja un conjunto de elementos particionados en un número de subconjuntos disjuntos (sin intersección). Esta estructura es especialmente útil para problemas relacionados con la detección de ciclos en un grafo, la determinación de componentes conectados, o para modelar la unión y la búsqueda de conjuntos disjuntos.

### Principales operaciones en Union-Find:
1. **Find**: Determina a cuál conjunto pertenece un elemento específico. También puede ser utilizado para encontrar el "representante" o "raíz" de un conjunto.
2. **Union**: Une dos conjuntos distintos en uno solo.

### Optimización con Path Compression y Union by Rank:
- **Path Compression**: Durante la operación `find`, se comprime el camino para que los nodos apunten directamente a la raíz del conjunto, lo que acelera futuras operaciones `find`.
- **Union by Rank**: Durante la operación `union`, el conjunto con menor altura (o rango) se une al conjunto con mayor altura, lo que ayuda a mantener el árbol más plano y las operaciones más eficientes.

### Implementación en Python:

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # Inicialmente, cada nodo es su propio padre
        self.rank = [1] * n  # Rango de cada conjunto es 1 inicialmente

    def find(self, node):
        if self.parent[node] != node:
            # Path Compression: Hace que cada nodo apunte directamente a la raíz
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            # Union by Rank: El árbol con menor rango se une al árbol con mayor rango
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

# Ejemplo de uso de Union-Find
uf = UnionFind(10)  # Crea 10 conjuntos (0 a 9)

# Unir algunos conjuntos
uf.union(1, 2)
uf.union(3, 4)
uf.union(2, 4)

# Verificar si dos elementos están en el mismo conjunto
print(uf.find(1) == uf.find(3))  # Salida: True
print(uf.find(1) == uf.find(5))  # Salida: False
```

### Explicación del código:

- **Inicialización**: `parent` almacena el padre de cada nodo. Al principio, cada nodo es su propio padre. `rank` almacena el rango de cada conjunto, que se utiliza para optimizar la operación `union`.
- **Find**: La función `find` realiza la compresión de camino para hacer que todos los nodos en el camino apunten directamente a la raíz del conjunto, lo que mejora la eficiencia.
- **Union**: La función `union` combina dos conjuntos utilizando la técnica de `Union by Rank` para minimizar la altura del árbol resultante, lo que también mejora la eficiencia de futuras operaciones.

### Aplicaciones comunes:
- Detección de ciclos en grafos.
- Algoritmo de Kruskal para encontrar el árbol de expansión mínima.
- Determinación de componentes conectados en un grafo.