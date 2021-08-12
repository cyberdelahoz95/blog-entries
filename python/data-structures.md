# Estructuras de datos en Python

## Listas

En su forma básica, agrupa objetos al incluirlos dentro de corchetes []

    mi_lista = [1,2,'tres']

Se accede al elemento de una lista mediante el número índice del elemento deseado.
mi_lista[0]

Se añaden elementos a la lista mediante el método append
mi_lista.append(4)

Se eliminan elementos mediante el método pop, se incluye como parámetro, el índice del elemento que se desea eliminar
mi_lista.pop(1)

Se puede recorrer una lista mediante la instrucción for
for mi_elemento in mi_lista: # comando dentro del ciclo

Finalmente, las listas en python permiten el uso de slices "::"

Las listas se pueden sumar o combinar al usar el operador +
mi_lista1 + mi_lista2

Tuplas
Se declara una tupla con el comando
mi_tupla = ()
Es una lista inmutable, no es posible agregar ni remover elemento de la lista una vez ha sido inicializada.
Su característica principal es que al ser inmutable, operarlo es mucho más rápido.

Diccionarios
Se declara un diccionario con la instrucción
mi_dicc = {}

Un diccionario es una estructura de datos del tipo llave valor.
mi_dicc = {
'llave1':1,
'llave2':2,
'llave3':3
}

Se acceden a un elemento a través de la llave.
mi_dicc['llave1']

Se recorre de la siguiente manera

for pair in mi_dicc.keys(): # pair tendrá el valor de las keys
for pair in mi_dicc.values(): # pair tendrá el valor de los values
for key, value for dicc.items()
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwNTc5NTIwMDBdfQ==
-->