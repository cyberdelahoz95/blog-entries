Lambda o funciones anónimas

```python
palindrome = lambda string: string == string[::-1]

print(palindrome('ana'))
```

Funciones de orden superior
Son funciones que reciben como parámetro funciones que han de ser ejecutadas dentro de la función contenedora.
Un buen ejemplo de las funciones de orden superior, es la función filter, map y reduce

```python
my_list = [1,4,5,6,9,13,21]

odd = list( filter(lambda x: x%2 != 0, my_list) )

print(odd)
```

```python
my_list = [1,4,5,6,9,13,21]

squares = list( map(lambda x: x**2, my_list) )

print(squares)
```

```python
from functools import reduce

my_list = [1,4,5,6,9,13,21]

reduced = reduce(lambda a, b: a * b, my_list)

print(reduced)
```
