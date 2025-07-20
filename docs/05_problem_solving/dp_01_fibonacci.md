# Secuencia de Fibonacci


El patrón de la secuencia de Fibonacci es útil cuando **la solución de un problema depende de las soluciones de instancias más pequeñas del mismo problema.**

Sabremosq ue habra que usar esta técnica si existe una relación recursiva, que se asemeje a la secuencia de Fibonacci:

$$ F(n) = F(n-1) + F(n-2)$$

Veamos un par de problemas cuya solución es similar a la de fibonacci.

- Fibonacci Number
- Min Cost Climbing Stairs

## Fibonacci Number

Los números de Fibonacci, comúnmente denotados por $f(n)$, forman una secuencia, llamada secuencia de Fibonacci, tal que cada número es la suma de los dos anteriores, comenzando por 0 y 1. Es decir,

$$ f(0) = 0$$

$$ f(1) = 1 $$

$$ f(n) = f(n - 1) + f(n - 2),\mbox{ para }n > 1.$$

Dado un entero positivo $n$, calcula $f(n)$.



```python linenums="1" title="Solución Recursiva"
class Solution:
    def fib(n: int) -> int:
        if n==0
            return 0
        if n == 1:
            return 1
        return fib(n-1) + fib(n-2)
```
