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

<!--stackedit_data:
eyJoaXN0b3J5IjpbNjczMTEyODU0LDE4ODA3NTA1NCwtNjUwNT
Y1OTAxXX0=
-->