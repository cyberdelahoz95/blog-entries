En recientes versiones de C# se agregó un feature llamado records, ¿qué son y para qué sirven?

Los records entran a formar parte de la familia de tipos de datos personalizados de la familia de C#. De esta familia hacen parte, la hermana mayor class, luego los struct. Los records son tipos de datos complejos creados para cumplir principalmente 2 objetivos.

1. Enfocarse en modelar datos.
2. Evitar la igualdad referencial.

3. Enfocarse en modelar datos.
   Normalmente usamos clases para modelar tanto datos como para describir el comportamiento del objeto que estamos modelando, esto lo hacemos a través de métodos. Sin embargo, los records pasan a ser un tipo de dato que se enfoca sólo en modelar datos, tal vez busquemos mapear una tabla de configuraciones globales que no tienen ninguna implicación en la lógica del negocio, esto abre la posibilidad para usar records.

EJEMPLO DEFINICIÓN DE UN RECOR

2. Evitar la igualdad referencial.
