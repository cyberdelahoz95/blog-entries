Convertiremos mediante simulación de Montecarlo la obtención de pi (solución determinística) en una solución estocástica.

Inicialmente se parte del conocimiento de las fórmulas matemáticas del área de un cuadrado y de un círculo.

Recordemos que el área de un cuadrado es base por altura y el área de un círculo es pi por radio al cuadrado.

Consideremos un circulo que cabe exactamente dentro de un cuadrado con base y altura de 2.
Entonces podemos concluir que el radio del círculo es de 1 y a el área del cuadrado es de 4, además podemos concluir que el área del círculo es igual a pi.

En definitiva, si sabemos cuánto es el área del círculo en este problema, sabremos el valor de pi.

Para resolver este problema de forma no determinista simularemos que se lanzan o avientan muchas agujas y veremos cuántas caen fuera y cuántas dentro del círculo.
Este acercamiento nos permite tener la proporción de agujas afuera del círculo y dentro del círculo y por ende la proporción de las áreas del círculo y el cuadrado.

Agujas en cuadrado = agujas fuera del círculo

Agujas en círculo / agujas en cuadrado = área circulo / área cuadrado

Área circulo = (4 \* agujas circulo) = agujas cuadrado.

Suponiendo que el centro del círculo y del cuadrado están en la coordenada 0,0
Los alfileres deberán caer dentro del rango de -1 y 1 para x y -1 & 1 para y (recordemos que el radio del círculo es 1).

Pero, ¿cómo sabemos que una aguja cayó adentro o afuera del círculo?
Usaremos el teorema de Pitágoras.
Calcularemos las hipotenusas que se forman de los triángulos, producto de los valores para y & x de las coordenadas de las agujas que se obtengan aleatoriamente.

Hipotenusas mayores a 1, significará que el alfiler o aguja cayó por fuera del círculo, hipotenusas menores o iguales a 1 son alfileres o agujas que caen dentro del círculo.

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
