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

## Creación de clase contextual de acceso a datos
Una vez que hayamos instalado nuestro paquete para acceder al motor de base de datos deseado, y posteriormente, implementar nuestros modelos, procedemos a crear una clase que servirá como contexto, podemos pensar en esta clase como el plug o conector que realizará el contacto con la base de datos como tal. Entre otras cosas, esta clase recibe en su constructor, la cadena de conexión y también nos permite declarar propiedades en las que usamos nuestras clases modelo como descriptores de nuestras tablas, veamos un ejemplo para entender mejor este punto.
```c#
using  System;
using  Microsoft.EntityFrameworkCore;

namespace  my_project.Models
{
	public  class  MyContext : DbContext
	{
		public  DbSet<Product> Products { get; set; }

		public  MyContext(DbContextOptions<MyContext> options) : base(options) { }
	}
}
```
Notemos qué:

 - Nuestra clase hereda de DbContext, esta clase padre proviene de EntityFrameworkCore y contiene implementaciones de métodos que se encargan de la conexión a la base de datos, mapear tablas y registros, administrar las conexiones, etc. Es decir, la clase padre DbContext abstrae el trabajo repetitivo relacionado con la base de datos y de esa manera nos enfocamos en nuestra lógica.
 - Notemos la propiedad Products, esta propiedad tiene varios propósitos.
	 - DbSet<Product> es un tipo generic, es decir que para su correcto funcionamiento debemos agregarle como parámetros, una clase modelo, en este caso Product. En caso de que lo queramos, EF nos permite trabajar sobre una base de datos en blanco y EF utilizará lo que hayamos descrito en las clases modelos y a partir de allí crear las tablas. Adicionalmente, al consumir los datos, EF utilizará la clase modelo que pasemos cómo parámetro para crear un objeto de ese tipo por cada registros en la tabla que referenciada en la anotación Table de dicha clase modelo.
	 - Esta propiedad también contiene una serie de métodos que nos permiten manipular los datos y hacer consultas con facilidad. 

## Agregar nuestro servicio de acceso a datos
Con la clase contextual creada, ya está nuestro servicio listo para ponerse a disposición de los controladores que deseen usarlo. Lo ponemos a disposición de los controladores al agregar el servicio en la clase Startup en el archivo Startup.cs
Nos ubicaremos sólo en el método ConfigureServices de dicha clase.
```c#
public  void  ConfigureServices(IServiceCollection  services)
{
	// otros servicios son agregados
	services.AddDbContext<MyContext>(options => options.UseNpgsql(Configuration.GetConnectionString("MyContext")));
}
```
Estamos agregando (AddDbContext) un contexto de base de datos a los servicios disponibles en nuestra aplicación. En este punto podemos notar que es posible agregar varios contextos, en otras palabras, podemos conectarnos a varias bases de datos, incluso diferentes en tipos de motores de db. En este caso, definimos que el contexto es de tipo MyContext.
Posteriormente, 

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTgyNzIyNTM0LDEyMTg4ODUxMjcsMTQyMT
Y4MzA1NCwtMTQ3NTM2ODg2OSw2MTY5NTY1OTNdfQ==
-->