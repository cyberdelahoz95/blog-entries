# Algoritmos de agrupamiento

Estos algoritmos buscan agrupar elementos de un arreglo, busca características similares en los elementos e intenta agruparlos basandose en dichas características.
Lógicamente, estos algoritmos son especialmente de utilidad en los casos en los que no es sencillo un agrupamiento de los datos, tal vez por la gran cantidad de los mismos, porque son muy variables entre sí o porque sus características similares no son tan evidentes.
Por ejemplo, en redes sociales se utiliza este tipo de algoritmos para agrupar personas que aparentemente son muy diferentes, tal vez ni se conocen y se arman nichos a los que puede interesarle el mismo tipo de cosas, De esa manera se les envía publicidad que puede motivarlos a comprar. 
En escenarios con grandes cantidades de datos, los algoritmos de agrupamiento también nos permiten tener una idea de la forma en la que los datos en conjunto están estructurados.
## Agrupamiento jerárquico
Toma los puntos (elemanto, datos) más cercanos, los agrupa en un cluster. Posteriormente toma este cluster y ubica el punto más cercano a dicho cluster. Finalmente, crea un cluster nuevo formado por el cluster del paso anterior junto con el punto más cercano encontrado en este último paso. Este algoritmo se repite hasta que ya queda un sólo "supercluster" que incorpora a todos los puntos o datos.
El resultado de este algoritmo es un dendograma. Esta gráfica señala o describe la relación de cada individuo, dato o elemente, con respecto al grupo o supercluster como tal.

### Aspectos que se tienen en cuenta en el agrupamiento jerárquico

 - Se parte del supuesto de que todos los puntos con los que se inicia, corresponden a un dato único e individual. En otras palabras, **el punto de inicio es un set de datos sin clusterizar o agrupar.**
 - Se debe determinar la forma en la que se calculará la distancia entre los puntos. (euclidiana, de Manhattan, etc.) El tipo de proyecto o lo que se quiere encontrar, determinará el tipo de cáculo para la distancia que se utilizará.
 - Qué tipo de criterio se usará para enlazar los puntos. Es decir, a partir de la segunda iteración, deberemos calcular la distancia del cluster que formamos en el primer paso al siguiente punto más cercano. Sin embargo, si notamos bien, un cluster es un grupo de datos, gráficamente sería un grupo de coordenadas cartesianas, entonces nos preguntamos, de este grupo de coordenadas, ¿cuál será la que usarémos como punto de referencia a partir del cual calcular la distancia? a eso nos referimos al decir, "'¿qué tipo de criterio se usará para enlazar los puntos?". Para responder esta pregunta, tenemos 3 opciones de criterio.
	 - Single Linkage, consiste en tomar los puntos más cercanos.
	 - Complete Linkage, consiste en tomar los puntos más lejanos
	 - Average Linkage, consiste en encontrar una coordenada promedio y usar esta coordanda como punto referencia para el cluster, en otras palabras el punto punto representativo a partir del cual se calculará la distancia.

## Agrupamiento K means
Este proceso está bajo el contexto de aprendizaje no supervisado. En el agrupamiento K means, se tiene un set de datos del que se desea conocer cómo los features vectores se correlacionan entre sí. Este ejercicio permite entre otra cosas, encontrar grupos de personas con intereses similares, automatizar el control de calidad de granos de café, etc.

El proceso consiste en seleccionar el número de grupos en los que se desea agrupar el dataset. En general, ese valor (k) es arbitrario, sin embargo, para una mayor precisión y efectividad del algoritmo, se recomienda seleccionar este número basado en la intuición que viene de entender con claridad la lógica del negocio.
Por cada k, se seleccionan k puntos del dataset que serán los centroides iniciales. Esta selección de centroides, es arbitraria y sirve nada más que, como punto de partida inicial de la ejecución del algoritmo. Se asume que, cada centroide corresponde a un grupo diferente....
Con el valor de k, es decir,  numero de grupos en los que se agrupará y los k centroides elegidos al azar, se inicia un proceso iterativo. 

 1. Se calcula la distancia de cada punto del dataset a los centroides seleccionados.
<!--stackedit_data:
eyJoaXN0b3J5IjpbOTQ0NzM5NzQyLC01NzAxMzA4ODMsOTQyNj
Q5OTA2LDczNzYzNDgzMV19
-->