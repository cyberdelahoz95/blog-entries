# Manejo básico de archivos en python
En python, la manipulación de archivos viene dada en los siguientes tipos de manipulación.

 - **r** Solo lectura
-   **r+**  Lectura y escritura
-   **w**  Solo escritura. Sobre escribe el archivo si existe. Crea el archivo si no existe
-   **w+**  Escritura y lectura. Sobre escribe el archivo si existe. Crea el archivo si no existe
-   **a**  Añadido (agregar contenido). Crea el archivo si éste no existe
-   **a+**  Añadido (agregar contenido) y lectura. Crea el archivo si éste no existe.

La estructura o formato de la instrucción en python para manigular archivos, se presenta de la siguiente manera

    with  open(<ruta>, <modo_de_manipulación>) as <nombre> :

<!--stackedit_data:
eyJoaXN0b3J5IjpbNjgwNjYwMTg1XX0=
-->