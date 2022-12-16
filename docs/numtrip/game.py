

import random

board = [
        [2, 2, 2, 4, 2],
        [2, 2, 2, 4, 2],
        [2, 2, 2, 4, 2],
        [2, 2, 2, 2, 4],
        [2, 2, 2, 2, 2]
        ]


def board1():
    artzeile = 3
    zeile = 0
    spalte = 0
    zahlrechts = 1

    print("    1      2      3      4      5")
    for i in range(5):
        print("+------+------+------+------+------+")
        artzeile = 0

        print("I      I      I      I      I      I")
        artzeile = artzeile + 1

        for o in range(5):
            print('I', end='')
            for g in range(6 - int(len(str(board[zeile][spalte])))):
                print(' ', end='')
            print(board[zeile][spalte], end='')

            spalte = spalte + 1

        print('I  ', end='')
        print(zahlrechts)
        zahlrechts = zahlrechts + 1
        zeile = zeile + 1
        spalte = 0
        artzeile = artzeile + 1

        print("I      I      I      I      I      I")
        artzeile = artzeile + 1
    print("+------+------+------+------+------+")


def feldlöschen():

    zeile = input('zeile: ')
    spalte = input('spalte: ')

    zeilex = int(zeile) - 1
    spaltex = int(spalte) - 1

    eingabe_zeile = True
    eingabe_spalte = True

    if not zeile.isnumeric():
        eingabe_zeile = False
        fehler = 'eingabe muss eine zahl sein'
    if not spalte.isnumeric():
        eingabe_spalte = False
        fehler = 'eingabe muss eine (ganze) zahl sein'

    if zeile.isnumeric():
        zeile = int(zeile)

        if zeile < 1:
            eingabe_zeile = False
            fehler = 'zahl muss grösser als 1 sein'
        if zeile > 5:
            eingabe_zeile = False
            fehler = 'zahl muss kleiner als 5 sein'

    if spalte.isnumeric():
        spalte = int(spalte)

        if spalte < 1:
            eingabe_spalte = False
            fehler = 'zahl muss grösser als 1 sein'
        if spalte > 5:
            eingabe_spalte = False
            fehler = 'zahl muss kleiner als 5 sein'

    if eingabe_zeile and eingabe_spalte == True:
        ausgewähltezahl = board[zeile - 1][spalte - 1]
        o = False
        if zeile < 5:
            if int(board[zeile][spalte - 1]) == int(board[zeile - 1][spalte - 1]):
                o = True
        if zeile > -1:
            if int(board[zeile - 2][spalte - 1]) == int(board[zeile - 1][spalte - 1]):
                o = True
        if spalte < 5:
            if int(board[zeile - 1][spalte]) == int(board[zeile - 1][spalte - 1]):
                o = True
        if spalte > -1:
            if int(board[zeile - 1][spalte - 2]) == int(board[zeile - 1][spalte - 1]):
                o = True

        if o == True:
            board[zeile - 1][spalte - 1] = ' '
        else:
            print('X')

        spalte = 1
        zeile = 1

        for i in range(8):
            for i in range(5):
                for i in range(5):
                    if board[zeile - 1][spalte - 1] == ' ':
                        feld1 = 0
                        feld2 = 0
                        feld3 = 0
                        feld4 = 0

                        if zeile < 4.1:
                            feld1 = board[zeile][spalte - 1]
                        if zeile - 2 > -1:
                            feld2 = board[zeile - 2][spalte - 1]
                        if spalte < 4.1:
                            feld3 = board[zeile - 1][spalte]
                        if spalte - 2 > -1:
                            feld4 = board[zeile - 1][spalte - 2]

                        if feld1 == ausgewähltezahl:
                            board[zeile][spalte - 1] = ' '
                        if feld2 == ausgewähltezahl:
                            board[zeile - 2][spalte - 1] = ' '
                        if feld3 == ausgewähltezahl:
                            board[zeile - 1][spalte] = ' '
                        if feld4 == ausgewähltezahl:
                            board[zeile - 1][spalte - 2] = ' '
                    spalte = spalte + 1
                spalte = 1
                zeile = zeile + 1
            zeile = 1

        if o == True:
            board[int(zeilex)][int(spaltex)] = str(int(ausgewähltezahl) * 2)

        spalte = 0
        zeile = 0
        for i in range(100):
            for i in range(5):
                for i in range(5):
                    if zeile + 1 < 5:
                        if board[zeile + 1][spalte] == ' ':
                            board[zeile + 1][spalte] = board[zeile][spalte]
                            board[zeile][spalte] = ' '
                        zeile = zeile + 1
                zeile = 0
                spalte = spalte + 1
            spalte = 0

            numbers = [1, 2, 4]
            if board[0][0] == ' ':
                board[0][0] = str(random.choice(numbers))
            if board[0][1] == ' ':
                board[0][1] = str(random.choice(numbers))
            if board[0][2] == ' ':
                board[0][2] = str(random.choice(numbers))
            if board[0][3] == ' ':
                board[0][3] = str(random.choice(numbers))
            if board[0][4] == ' ':
                board[0][4] = str(random.choice(numbers))

    else:
        print('Fehlerhafte Eingabe')
        print(fehler)


spielen = True


def play():
    while spielen == True:
        board1()
        feldlöschen()


play()
