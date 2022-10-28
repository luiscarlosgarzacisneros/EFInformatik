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
    return False


def game_over():
    pass


def play():
    while not game_over():

        buchstabe = eingabe()
        auswerten(buchstabe)
        print(buchstabe)
        show()
    if gewonnen():
        print('...')
    else:
        print('...')


play()
