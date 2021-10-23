# Algoritmos de clasificación
Los algoritmos de clasificación son una técnica de aprendizaje supervisado que se aplica en ML para asignarle una etiqueta a un dato dependiendo de su ubicación en un plano de coordenadas.
A diferencia de la clusterización o agrupamiento, en la clasificación es importante que conozcamos las etiquetas que el algoritmo asignará a los datos bajo evaluación.

##   Clasificadores lineales
Estos tipos de clasificadores se distinguen porque dividen el conjunto de datos con una línea (que puede ser multidimensional dependiendo de la cantidad de  _features_  que hemos utilizado para definir a nuestros datos). Esto genera áreas dentro de nuestro espacio de búsqueda para que cuando coloquemos un nuevo dato podamos clasificarlo fácilmente.

## K nearest neighbors
En este algorito se parte del supuesto de que ya se cuenta con un conjunto de datos clasificados, podemos pensar en un plano de coordenadas con un conjunto de datos ubicados en él y dadas las ubicaciones de los mismos, ya sabemos a qué clase pertenecen.
Al recibir un valor o data point del cual no conocemos su etiqueta o clase, determinamos sus K vecinos más cercanos y de acuerdo a su cercanía con dichos vecinos, el data point se le asignará una clase o etiqueta.
En este algoritmo el valor de K corresponde al número de vecinos necesarios para que un vector o data point se le asigna la clase o etiqueta correspondiente a esos vecinos.
Si un data point no llega exactamente a tener K vecinos, entonces se le asigna la clase a la que pertenecen la mayor cantidad de vecinos más cercanos.
Por ejemplo, si K es igual a 5, con 3 vecinos de una clase es suficiente para que se le asigne dicha clase al data point entrante.
Este algoritmo es computacionalmente costoso, por lo tanto no se recomienda utilizar toda la población de datos para su ejecución, en vez de eso, se puede utilizar una muestra representativa.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3NjQwNDUwNzEsLTE3MTU2OTQxMjYsLT
EzNjg2Nzk5NzEsLTU5MDcwMDI4MCwxNTUxODQ1NDg2LDEwOTE0
NTczODIsLTIwODg3NDY2MTJdfQ==
-->