def fonction(k):
    return k**3 - 5


def regulafalsi():
    x = int(input('x:'))
    y = int(input('y:'))

    while abs(x - y) > 1e-10:
        zéro = ((-(fonction(x))) * (y - x) / (fonction(y) - (fonction(x)))) + x

        print(zéro)
        print(fonction(zéro))

        if fonction(x) > 0 and fonction(zéro) > 0 and fonction(y) < 0:
            x = zéro
            y = y
        elif fonction(x) > 0 and fonction(zéro) < 0 and fonction(y) < 0:
            x = x
            y = zéro
        elif fonction(x) < 0 and fonction(zéro) < 0 and fonction(y) > 0:
            x = zéro
            y = y
        elif fonction(x) < 0 and fonction(zéro) > 0 and fonction(y) > 0:
            x = x
            y = zéro


regulafalsi()
#x<0, y>0
