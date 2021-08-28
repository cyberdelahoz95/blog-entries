# Conexión a base de datos a través de Entity Framework
Entity framework es una capa de acceso a datos que se utiliza en aplicaciones .Net para facilitar el uso de base de datos en nuestras aplicaciones.
Existe una gran variedad de módulos o paquetes .Net que utilizan los estándares de Entity Framework para implementar una capa de acceso a diferentes motores de base de datos.
En este breve post, utilizaremos una implementación de una capa de acceso al motor PostgreSql.
## Instalación de paquete
la forma más sencilla de instalar el paquete en nuestro proyecto es usando la instrucción

    dotnet add package Npgsql.EntityFrameworkCore.PostgreSQL --version 5.0.7

Por supuesto, en este caso usamos la versión 5.0.7, sin embargo, ten en cuenta que probablemente al leer este post, ya exista una versión más reciente y sólo es cuestión de cambiarla en el comando.

Podrás verificar que se instaló correctamente si revisas el archivo .csproj de tu proyecto y deberás encontrar una línea similar a esta.
```xml
<PackageReference  Include="Npgsql.EntityFrameworkCore.PostgreSQL"  Version="5.0.7" />
```
## Creación de clases schema
Las clases schema, nos sirven para indicarle a EF cómo hará el mapeo o por decirlo así, la traducción de los datos d

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIzOTY2NzE1MSw2MTY5NTY1OTNdfQ==
-->