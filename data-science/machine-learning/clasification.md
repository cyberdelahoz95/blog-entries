# Algoritmos de clasificación
Los algoritmos de clasificación son una técnica de aprendizaje supervisado que se aplica en ML para asignarle una etiqueta a un dato dependiendo de su ubicación en un plano de coordenadas.
A diferencia de la clusterización o agrupamiento, en la clasificación es importante que conozcamos las etiquetas que el algoritmo asignará a los datos bajo evaluación.

## K nearest neighbors
En este algorito se parte del supuesto de que ya se cuenta con un conjunto de datos clasificados, podemos pensar en un plano de coordenadas con un conjunto de datos ubicados en él y dadas las ubicaciones de los mismos, ya sabemos a qué clase pertenecen.
Al recibir un valor o data point del cual no conocemos su etiqueta o clase, determinamos sus vecinos más cercanos y de acuerdo a su cercanía con dichos vecinos, el data point se le asignará una clase o etiqueta.
En este algoritmo el valor de K corresponde al número de vecinos necesarios
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTczNDQ2MTM2OSwtNTkwNzAwMjgwLDE1NT
E4NDU0ODYsMTA5MTQ1NzM4MiwtMjA4ODc0NjYxMl19
-->