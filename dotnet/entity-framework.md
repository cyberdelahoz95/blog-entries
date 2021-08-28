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
Las clases schema, nos sirven para indicarle a EF cómo hará el mapeo o por decirlo así, la traducción de los datos de una tabla a un objeto en nuestra lógica del backend. Generalmente estás clases siguen muy de cerca la estructura de campo de la tabla que representan en la base de datos.
Por ejemplo, si en la base de datos tenemos una tabla que se llama **products** que contiene los registros de productos vendidos en una tienda, muy probablemente tendremos una clase schema con un nombre similar y la siguiente definición
```c#
using  System;
using  System.ComponentModel.DataAnnotations.Schema;

namespace  my_project.Models
{
	[Table("products")]
	public  class  Product
	{
		[Column("id")]
		public  int Id { get; set; }

		[Column("title")]
		public  string Title { get; set; }

		[Column("description")]
		public  string Description { get; set; }

		[Column("price")]
		public  int Price { get; set; }
	}
}
```
Podemos notar varios detalles, 

 - Estamo

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExNDY1NTgzMTgsNjE2OTU2NTkzXX0=
-->