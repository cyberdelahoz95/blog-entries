# Algoritmos de agrupamiento

Estos algoritmos buscan agrupar elementos de un arreglo, busca características similares en los elementos e intenta agruparlos basandose en dichas características.
Lógicamente, estos algoritmos son especialmente de utilidad en los casos en los que no es sencillo un agrupamiento de los datos, tal vez por la gran cantidad de los mismos, porque son muy variables entre sí o porque sus características similares no son tan evidentes.
Por ejemplo, en redes sociales se utiliza este tipo de algoritmos para agrupar personas que aparentemente son muy diferentes, tal vez ni se conocen y se arman nichos a los que puede interesarle el mismo tipo de cosas, De esa manera se les envía publicidad que puede motivarlos a comprar. 
En escenarios con grandes cantidades de datos, los algoritmos de agrupamiento también nos permiten tener una idea de la forma en la que los datos en conjunto están estructurados.
## Agrupamiento jerárquico
Toma los puntos (elemanto, datos) más cercanos, los agrupa en un cluster. Posteriormente toma este cluster y ubica el punto más cercano a dicho cluster. Finalmente, crea un cluster nuevo formado por el cluster del paso anterior junto con el punto más cercano encontrado en este último paso. Este algoritmo se repite hasta que ya queda un sólo "supercluster" que incorpora a todos los puntos o datos.
El resultado de este algoritmo es un dendograma. Esta gráfica señala o describe la relación de cada individuo, dato o elemente, con respecto al grupo o supercluster como tal.

### Aspectos que se tienen en cuenta en el agrup

<!--stackedit_data:
eyJoaXN0b3J5IjpbMjA1Nzc3ODAyNyw3Mzc2MzQ4MzFdfQ==
-->