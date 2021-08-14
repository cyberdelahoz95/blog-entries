# Manejo de Errores en python

La manera de leer los Traceback al presentarse un error, es leer de abajo hacia arriba. Por lo general, la última línea es la excepción que se presentó, posteriormente de abajo hacia arriba la segunda línea contiene, el archivo, la línea de código y el módulo en el que se presentó el error.

Cabe señalar que, si en la función en la que se presentó el error, no hay un manejador de excepciones, python eleva, es decir transfiere el error a la función desde la cual se llamo a la función en la que se presentó el error. Este proceso ocurre iterativamente hasta que suceda la primera de 2 cosas, o se encuentra un manejador de excepciones o se llega hasta la función main y por ende se corta la ejecución del programa, razón por la cual en python la primera línea de arriba hacia a abajo dice "most recent call last", dando a entender que el origen del error se encuentra hasta el final del Traceback.

## Manejo de excepciones

**try, except**

```python
try:
    palindrome(1)
except TypeError:
    print("Sólo se puede ingresar cadenas de texto")
```
En el bloque anterior, python ejecutará el bloque de código dentro de la instrucción try y sólo si se presenta una excepción del tipo TypeError se ejecutará lo que se encuentra dentro del except. Cabe señalar que si se presenta una excepción de otro tipo, no se ejecutará el código dentro de except.

**raise**
esta función nos permite elevar una excepción el tipo que nos parezca más conveniente y luego dejar que el manejador de errores except, haga lo propio con el tipo de error que hemos elevado.

```python
try:
    # otro código
    raise ValueError("Descripción del error")
except ValueError as err:
    print(err)
    # más código
```

**finally**
Es una instrucción que se ejecuta al final de un try y de un except, la ejecución dentro de finally es indistinta de que ocurra un error o no.

```python
try:
    f = open("archivo.txt")
    # otro código
finally:
    f.close()
```

**assert statement**
Permiten manejar flujos de código a través de encapsularlos en aserciones, es decir, expresiones que esperamos que sean verdaderas para continuar con ejecución y en caso contrario, lanzamos una excepción.

```python
def palindrome (string):
    assert len(string) > 0, "No se puede ingresar una cadena vacía"
    return string == string [::-1]

print(palindrome(""))
```

Resultar en

```
AssertError: No se puede ingresar una cadena vacía
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTM2NDk0MTU0M119
-->