# Stack

LIFO implies that the element that is inserted last, comes out first and FILO implies that the element that is inserted first, comes out last.


Un Stack o pila es una estructura de datos lineal  que funciona bajo LIFO(Last In First Out), esto es el último elemento insertado es el primero en salir, o visto
desde otro punto de vista el primero en ser insertado es el último en salir.


## Operaciones

- Push: Agrega un elemento al top de la pila.
- Pop: Remueve el elemento en el top de la pila.
- Peek: Retorna el valor del elemento en el top de la pila.
- IsEmpty: Verifica que la pila esta vacia.
- IsFull: Verifica que la pila esta llena.



## Monotonic Stack

Una **pila monotonica** es una estructura de datos especial usada para resolución de problemas donde el orden importa o ayuda. Las **pilas monoticas** mantienen los elementos en la pila
en order creciente o decreciente.

Tenemos basicamente dos tipos de monotonic stack ( y ligeras variantes)

- Monotonic Increasing Stack
- Monotonic Decreasing Stack

### Monotonic Increasing Stack

Para construir una pila monotonica

- Initilizamos un stack vacio
- Iteramos los elementos y para cada elemento:
    - Mientras el stack no sea vacio y la cima(top) del stack sea mayor que el elemento actual:
        - Removemos(pop) el elemento del stack
    - Insertamos(push) el elemento en el stack
- Al final de la iteracion el stack contiene los elementos en orden monotonicamente creciente.



### Monotonic Decreasing Stack




