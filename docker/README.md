# Tips para desarrollo y despliegue con contenedores de Docker

## Variables de entorno
Una buena práctica, no sólo en Docker sino en cualquier escenario, es el uso de variables de entorno y de esa manera evitar ingresar valores quemados (hard code) al código.
En el caso de Docker, podemos usar con facilidad variables de entorno de la siguiente manera.
```yaml
version: "3"
services:
	cms_app:
		image: strapi/strapi
		environment:
			DATABASE_CLIENT: ${DATABASE_CLIENT}
			DATABASE_NAME: ${POSTGRES_DB}
			DATABASE_HOST: ${DATABASE_HOST}
			DATABASE_PORT: ${DATABASE_PORT}
			DATABASE_USERNAME: ${DATABASE_USERNAME}
			DATABASE_PASSWORD: ${DATABASE_PASSWORD}
		volumes:
		- "${CMS_APP_PATH}:/srv/app"
		ports:
		- "1337:1337"
```
Como podemos notar en el archivo docker-compose anterior, en vez de insertar los valores de manera estática, utilizamos la forma **${VARIABLE_DE_ENTORNO}**
Las variables de entorno pueden estar definidas de manera directa en el sistema operativo, también pueden ser inyectadas a través de un administrador, este es el caso de las instancias de AWS. Localmente y para fines de desarrollo, podemos utilizar un archivo .env en el que definamos nuestras variables.
```
DATABASE_CLIENT=postgres
DATABASE_HOST=container_db
DATABASE_PORT=5432
DATABASE_USERNAME=my-user
DATABASE_PASSWORD=p4ssw0rd
```
## Comunicar contenedores definidos en diferentes archivo docker-compose
En algunas ocasiones, no tenemos toda nuestra infraestructura definida en un sólo archivo docker-compose, esto es especialmente cierto en fase de desarrollo y estamos comunicando aplicaciones totalmente diferentes.
Para poder establecer un canal de comunicación, creamos una red en el primer archivo docker-compose que ejecutemos.
```yaml
version: "3"
services:
	cms_app:
		image: strapi/strapi
		...
		ports: - "1337:1337"
		depends_on:
			- cms_db
		networks:
			- local_net
	cms_db:
		image: postgres
		...
		networks:
		- local_net

networks:
	local_net:
		name: multiple_containers_net 
```
Ahora tenemos la red creata disponible para ser "consumida" desde otros proyectos docker-compose de la siguiente manera.

```yaml
version: "3.8"
services:
	adminer:
		image: adminer
		...
		networks:
			- adminer_local_net
networks:
	adminer_local_net:
		external:
		name: multiple_containers_net
```
También es posible enlazarnos desde contenedores creados de manera directa con comandos de Docker, para lo cual usamos el subcomando network al ejecutar docker run.

    --network="multiple_containers_net"

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTYxOTY4NjExLDE4OTY3NjYzNjgsNzk4MT
M1Mjg0LDY3MzExMjg1NCwxODgwNzUwNTQsLTY1MDU2NTkwMV19

-->