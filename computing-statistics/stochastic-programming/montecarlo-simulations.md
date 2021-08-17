Son simulaciones que utilizan la aleatoriedad para predecir el resultado de un problema.

Permiten transformar un problema determinístico en uno no determinístico.

```python
import random
import collections

# baraja es una pareja palo valor
PALOS = ['E', 'C', 'D', 'T']
VALORES = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))

    return barajas


def obtener_mano(barajas, tamano_mano):
    # sample retorna una muestra sin repetirlas posteriormente
    mano = random.sample(barajas, tamano_mano)
    return mano


def main(tamano_mano, intentos):
    barajas = crear_baraja()
    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)

    pares = 0

    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])

        counter = dict(collections.Counter(valores))
        for val in counter.values():
            if val == 2:  # 2 porque es par, si queremos tercia es 3
                pares += 1
                break

    probabilidad_par = pares / intentos
    print("probabilidad de obtener un par")
    print(probabilidad_par)


if __name__ == '__main__':
    barajas = crear_baraja()
    mano = obtener_mano(barajas, 5)
    tamano_mano = int(input("De cuantas barajas sera la mano? "))
    intentos = int(input("Cuantos intentos para calcular la probabilidad "))

    main(tamano_mano, intentos)
```

> Written with [StackEdit](https://stackedit.io/).

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTkzMDQzMzYzM119
-->
