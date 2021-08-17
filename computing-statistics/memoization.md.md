# Programación Dinámica

Técnica para optimizar problemas que tienen la característica de contar con una **subestructura óptima**.

Básicamente estamos optimizando problemas mediante una optimización de los problemas mas pequeños que componen el problema más grande en cuestión.

Se necesita tener problemas empalmados para poder utilizar programación dinámica. Esto quiere decir que la solución óptima se obtiene al resolver el mismo problema en varias ocasiones.

Un buen ejemplo de la optimización siguiendo la descripción anterior es la **memoización**.

## Memoización

Memoización es guardar el resultado de operaciones previas para que en el futuro sea simplemente consultar en la memoria el resultado previamente guardado y de esa manera ahorrar en tiempo de ejecución.

Ejemplo:

Número de Fibonacci

    F(n) = F(n-1) + F(n-2)

 
Al implementar fibonacci siguiendo el proceso estricto de la formula, se obtiene un algoritmo ineficiente porque el crecimiento computacional (complejidad) es exponencial.

Sin embargo, para poder obtener una respuesta favorable y correcta, es obligatorio realizar el mismo proceso repetitivo.

Entonces, debido a que es un problema que se soluciona realizando una tarea de forma repetitiva, es posible aplicar dynamic programming para optimizar el resultado, se aplica al utilizar memoización en nuestra solución.

```python
mport sys

def fibonacci_recursive(n):

if n == 0 or n == 1:

return 1

return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_with_memo(n, memo={}):

if n == 0 or n == 1:

return 1

try:

return memo[n]

except KeyError:

resultado = fibonacci_with_memo(n - 1, memo) + fibonacci_with_memo(n - 2, memo)

memo[n] = resultado

return resultado

if __name__ == "__main__":

sys.setrecursionlimit(10002)

n = int(input("Escoger número: "))

result = fibonacci_with_memo(n)

print(result)

```


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4NjM5NDk2OF19
-->