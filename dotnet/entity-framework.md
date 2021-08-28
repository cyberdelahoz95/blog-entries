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

 - Estamos utilizando la dependencia **System.ComponentModel.DataAnnotations.Schema** la cual nos permite agregar anotaciones que facilitan el mapping que EF realiza al interpretar nuestra clase. No siempre las anotaciones son necesarias, por ejemplo, por convención EF realizará mapping de los fields de la tabla en la base de datos, que tengan el mismo nombre que nuestras propiedades en la clase.
 - En este caso, debido a que los nombres de los campos en la base de datos no son exactamente iguales a nuestras propiedades, nos valemos de data annotations para configurar el comportamiento deseado. En este caso, la anotación Column nos ayuda con ese propósito. La anotación Table, hace lo propio al indicar que esta clase contendrá la representación de registros de la tabla products.
 - 

<!--stackedit_data:
eyJoaXN0b3J5IjpbOTYxMTI4NzY5LDE0MjE2ODMwNTQsLTE0Nz
UzNjg4NjksNjE2OTU2NTkzXX0=
-->