# Hash Table

Una hash table (tabla hash en español) es una estructura de datos que se utiliza para almacenar pares clave-valor, donde las claves son únicas. Es extremadamente eficiente para operaciones de búsqueda, inserción y eliminación, ya que en promedio estas operaciones se realizan en tiempo constante $O(1)$.

Hay dos tipos de tablas hash:

- Hash set: Es una implementación de una estructura de datos set que no  permite elementos repetidos.
- Hash map: Es una implementación de  una estructura de datos map, es decir, pares (llave, valor).


## Cómo funciona una hash table

**Función hash**: Una función hash toma una clave y la convierte en un índice numérico, que corresponde a una posición en un array donde se almacenará el valor asociado. La calidad de la función hash es crucial para el rendimiento de la tabla hash, ya que debe distribuir las claves de manera uniforme para evitar colisiones.

**Colisiones**: Ocurren cuando dos claves diferentes producen el mismo índice. Hay varias formas de manejar colisiones:

**Encadenamiento (Chaining)**: Cada posición del array apunta a una lista enlazada de todos los pares clave-valor que tienen el mismo índice.

**Dirección abierta (Open Addressing)**: Si ocurre una colisión, se busca la siguiente posición disponible en el array para almacenar el nuevo par clave-valor.
Operaciones comunes:

**Inserción**: La clave se convierte en un índice usando la función hash y el valor se almacena en la posición correspondiente.

**Búsqueda**: La clave se convierte en un índice y se accede directamente a la posición del array para obtener el valor.

**Eliminación**: Similar a la búsqueda, pero se elimina el par clave-valor de la posición correspondiente.

## Ventajas y desventajas

- Ventajas:
    - Operaciones rápidas en tiempo promedio O(1).
    - Sencilla de implementar y útil para búsquedas rápidas.
- Desventajas:
    - Puede haber colisiones, lo que puede afectar el rendimiento.
    - Requiere una buena función hash para evitar agrupaciones (clusters) de datos en ciertas posiciones.
    - El tamaño del array (o el número de posiciones disponibles) debe ser cuidadosamente gestionado para evitar desperdicio de espacio o excesivas colisiones.

