# Estructura de procedimiento para solucionar un problema con Data Science

 - **Problema:** Se plantea una hipótesis y **a través de datos estadísticos presentes**, se valida si la hipótesis representa un problema real o no. En caso de que se valida la veracidad del problema, se pasa al siguiente paso.
 - **Solución:** Se actúa para entender el problema (causas, motivaciones, etc.), además, se actúa para encontrar posibles soluciones al problema. Todo este actuar se efectúa basado en tecnología (ciencia de datos). Finalmente, se definen acciones basadas en datos, que impacten la lógica del negocio. Se puede decir que **la solución tiene que ver con entender el presente de la empresa y predecir el comportamiento futuro**.
 - **Alcance:** Queremos utilizar el método para solucionar el problema, en otro ámbitos de la empresa, tal vez ámbitos geográficos o de las áreas de la empresa. Para poder lograr este objetivo, la solución debe permitir parametrizar o adaptar su ejecución a los diferentes ambientes en los que se desea aplicar.
## Cómo se estructura un caso de negocio para implementar DS

Una hipótesis debe surgir de un problema o potencial problema que se esté percibiendo. A partir de la hipótesis, estructuramos el caso de negocio de la siguiente manera:

 - **Qué:** ¿Qué problema se tiene?, aquí planteamos un problema puntual, por ejemplo: "¿por qué están cayendo las ventas? ¿Por qué está tomando más tiempo el proceso de producción? ¿puedo hacer que la máquina se dañe con menos frecuencia?"
 
 - **Por qué:** ¿Por qué se tiene el problema? en otras palabras, se pretende entender las posibles motivaciones o causas del problema. Esto se logra categorizando los datos, y hacerlo de tal manera que se tenga un número finito y lo más reducido posible de categorías. Por ejemplo, si estoy investigando las posibles causas para que una máquina se dañe, algunas causas o motivaciones pueden ser:
 -- Pieza dañada
 -- Mala configuración
 -- Mala praxis por parte del operario
 -- Fallo eléctrico
 
 - **Cómo:** ¿cómo diseñamos un mecanismo para validar la hipótesis y obtener una solución? En esta fase se ejecutan diferentes **mecanismos de análisis de datos**

### Mecanismos de análisis de datos

 - **Análisis Cuantitativo:** se realizan mediciones y pasamos a categorizar o clasificar la información, esto se logra mediante queries de SQL. Idealmente este proceso se hace lo más dinámico posible (queries parametrizable, por ejemplo, por mes o año).
 - **Análisis Cualitativo:** se intenta clusterizar o agrupar por motivos o casusas del problema. En general se busca desglosar cualitativamente, los factores o variables determinantes en la búsqueda de la solución. Para cada cluster, se profundiza en la obtención de dichos factores previamente mencionados, por ejemplo, un factor determinante pude ser la geolocalización. En otras palabras, para cada grupo se desagregan los registros y es identifican los motivos más sobresalientes. También se trata de identificar palabras relevantes. Cabe mencionar que este análisis no siempre se puede aplicar al caso de negocio.
 - **Minería de datos:** Es un tipo de exploración de datos que se enfoca en detección de datos a través de la revisión de mensajes de texto disponibles en los diferentes canales de comunicación de la empresa. Fuentes de texto para realizar minería Canales de redes sociales Facturas y otros documentos.
 - **Fusión cuantitativa y cualitativa:** En esta actividad se comparan los resultados de cada análisis (cuantitativa y cualitativa). La comparación se realiza al agregar los datos de ambos análisis en una matriz. Pasamos a considerar a partir de esta matriz, qué podemos percibir y obtenemos conclusiones de ello.
 - **Detección de factores determinantes:** Con los pasos anteriores, buscamos los factores determinantes que representan causas o motivaciones para el aparecimiento del problema planteado 

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5NzY0Njk2NDksNDQ5MjAxNzQwLC0xNT
UwMTE4MTk3LC0xNDk2MTI5MzM0LC0xNjU3MjQ3MzI3LDEwMDE0
MzcxNiw2NDkwMTkwMjQsOTI1NzM4NDQ4LDE3NzA2ODIwMDAsNz
Y1NTQ4Njg2XX0=
-->