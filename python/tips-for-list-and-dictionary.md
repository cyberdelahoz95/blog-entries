# Tips de uso de list y diccionarios en python

## Lists y Dict anidados
Debido a que en python todo es un objeto, es posible realizar listas anidades o listas que contienen diccionarios e incluso se puede crear diccionarios que contienen listas.

```python
my_list_containing_dictionaries = [
    {"firstname":"Pedro", "lastname":"Perez"},
    {"firstname":"Pablo", "lastname":"Marmol"},
    {"firstname":"Joe", "lastname":"Doe"},
    {"firstname":"Juan", "lastname":"Garcia"},
]

my_dictionary_containing_lists = {
    "natural_numbers":[1,2,3,4,5,6],
    "floating_numbers":[1.1,2.3,3.5,4.1,5.7,6.9],
}
```
## List comprehensions
Proceso para llenar una lista con los números del 1 al 100 elevados al cuadrado si no son divisibles exactamente entre 3.
Antes

```python
square = []
# range va hasta el 101 porque el segundo argumento de la function range no es inclusivo en el conteo
for i in range(1,101):
    if i % 3 != 0:
        square.append(i**2)
```

Después, con list comprehensions

```python
square = [i**2 for i in range(1,101) if i%3 != 0]
```
Forma general
[element for element in iterable if condition]

## Dictionary comprehensions

```python
my_dict = {i:i**3 for i in range(1,101) if i % 3 !- 0}
```

Forma general
{key:value for element in iterable if condition}
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0Mjc0NDMxNThdfQ==
-->