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
Como podemos notar en el archivo docker-compose anterior, en vez de insertar los valores de manera estática
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTU0MTY3NzY2MCwxODgwNzUwNTQsLTY1MD
U2NTkwMV19
-->