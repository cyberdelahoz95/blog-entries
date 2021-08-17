Convertiremos mediante simulación de montecarlo la obteción de pi (solución determinística) en una solución estocástica.

Inicialmente se parte del conocimiento de las fórmulas matemáticas del área de un cuadrado y de un círculo.

Recordemos que el area de un cuadrado es base por altura y el área de un circulo es pi por radio al cuadrado.

Consideremos un circulo que cabe exactamente dentro de un cuadrado con base y altura de 2.
Entonces podemos concluir que el radio del circulo es de 1 y al área del cuadrado es de 4, además podemos concluir que el área del circulo es igual a pi.

En definitiva, si sabemos cuánto es el área del circulo en este problema, sabremos el valor de pi.

Para resolver este problema de forma no determinísta simularemos que se lanzan o avientan muchas agujas y veremos cuántas caen fuera y cuántas dentro del circulo.
Este acercamiento nos permite tener la proporción de agujas afuera del círculo y dentro del círculo y por ende la proporción de las áreas del círculo y el cuadrado.

agujas en cuadrado = agujas fuera del circulo

agujas en circulo / agujas en cuadrado = area circulo / area cuadrado

area circulo = (4 \* agujas circulo) = agujas cuadrado.

Suponiendo que el centro del circulo y del cuadrado están en la coordenada 0,0
los alfileres deberán caer dentro del rango de -1 y 1 para x y -1 & 1 para y (recordemos que el radio del circulo es 1).

Pero, como sabemos que una aguja cayó adentro o afuera del circulo?
usaremos el teorema de pitágoras.
calcularemos las hipotenusas que se forman de los triangulos producto de los valores para y & x de las coordenadas de las agujas que se obtengan aleatoriamente.

Hipotenusas mayores a 1, significará que el alfiler o aguja cayó por fuera del circulo, hipotenusas menores o iguales a 1 son alfileres o agujas que caen dentro del circulo.

```python
import math
# incluir estadisticas
from estadisticas import desviacion_estandar, media


def aventar_agujas(numero_de_agujas):
    adentro_del_circulo = 0

    for _ in range(numero_de_agujas):
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])
        distancia_desde_el_centro = math.sqrt(x**2 + y**2)

        if distancia_desde_el_centro <= 1:
            adentro_del_circulo += 1

    return (4 * adentro_del_circulo) / numero_de_agujas


def estimacion(numero_de_agujas, numero_de_intentos):
    estimados = []
    for _ in range(numero_de_intentos):
        estimacion_pi = aventar_agujas(numero_de_agujas)
        estimados.append(estimacion_pi)

    media_estimados = media(estimados)
    sigma = desviacion_estandar(estimados)
    return (media_estimados, sigma)


def estimar_pi(precision, numero_de_intentos):
    numero_de_agujas = 1000
    sigma = precision

    while sigma >= precision/1.96:  # intervalo de confianza
        media, sigma = estimacion(numero_de_agujas, numero_de_intentos)
        numero_de_agujas *= 2

    return media


if __name__ == '__main__':
    estimar_pi(0.01, 1000)
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ3MDEyODc2M119
-->
