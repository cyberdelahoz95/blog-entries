# Programación Dinámica

Técnica para optimizar problemas que tienen la característica de contar con una **subestructura óptima**.

Básicamente estamos optimizando problemas mediante una optimización de los problemas mas pequeños que componen el problema más grande en cuestión.

Se necesita tener problemas empalmados para poder utilizar programación dinámica. Esto quiere decir que la solución óptima se obtiene al resolver el mismo problema en varias ocasiones.

Un buen ejemplo de la optimización siguiendo la descripción anterior es la **memoización**.

## Memoización

Memoización es guardar el resultado de operaciones previas para que en el futuro sea simplemente consultar en la memoria el resultado previamente guardado y de esa manera ahorrar en tiempo de ejecución.

Ejemplo:

Número de Fibonacci

    F(n) = F(n-1) + F(n-2)

 
Al implementar fibonacci siguiendo el proceso estricto de la formula, se obtiene un algoritmo ineficiente porque el crecimiento computacional (complejidad) es exponencial.

Sin embargo, para poder obtener una respuesta favorable y correcta, es obligatorio realizar el mismo proceso repetitivo.

Entonces, debido a que es un problema que se soluciona realizando una tarea de forma repetitiva, es posible aplicar dynamic programming para optimizar el resultado, se aplica al utilizar memoización en nuestra solución.

```python
def fibo_dinamico(n, memo={}):
	step =  0
	if n ==  0:
		step +=  1
		print(f'.........Caso base - Fibo({n}) = {0}')
		return 0
	elif n ==  1:
		step += 1
		print(f'.........Caso base - Fibo({n}) = {0}')
		return  1
	try:
		print(f'..Consultando en dic_memo Fibo({n})')
		return memo[n]
	except KeyError:
		print(f'....No existe Fibo({n}) en el diccionario')
		print(f'......Calculando Fibo({n})')
		resultado =  fibo_dinamico(n-1, memo) +  fibo_dinamico(n-2, memo)
		memo[n] = resultado
	print(f'.........Se guardo Fibo({n})={resultado} en el diccionario')
return resultado

  

if  __name__  ==  '__main__':

n =  5

num_fibo_n =  fibo_dinamico(n)

print('*'*40)

print(f'El numero Fibo({n}) = {num_fibo_n}')

```


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY2MjkwMDEwM119
-->