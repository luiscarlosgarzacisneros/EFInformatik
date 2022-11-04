import zufallsworte as zufall

wort = zufall.zufallswoerter

# Variablen
gesucht = 'test'

gefunden = []
falsch_geraten = []


def eingabe():
    buchstabe = input('Buchstabe? ')

    return buchstabe.lower()


def auswerten(buchstabe):

    if buchstabe in gesucht:
        gefunden.append(buchstabe)
    else:
        falsch_geraten.append(buchstabe)


def show():
    print('Falsche Buchstaben:', falsch_geraten)
    for buchstabe in gesucht:
        if buchstabe in gefunden:
            print(buchstabe, end=' ')
        else:
            print('_', end=' ')
    print('')


def gewonnen():
    pass


def game_over():
    if len(falsch_geraten) > 10:
        True


def play():
    while not game_over():
        show()
        inp = eingabe()
        auswerten(inp)
    if game_over() == True:
        print('Verloren)')


play()
