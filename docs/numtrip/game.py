
board = [
        [88, 88, 666, 88, 88],
        [88, 222222, 8, 2, 1],
        [4, 69, 88, 4, 2],
        [2, 88, 1111, 44444, 1],
        [2, 4, 444, 444, 4]
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
            anzleer = 6 - int(len(str(board[zeile][spalte])))
            print('I', end='')
            for g in range(anzleer):
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
        board[zeile - 1][spalte - 1] = ' '
    else:
        print('Fehlerhafte Eingabe')
        print(fehler)


spielen = True


def play():
    while spielen == True:
        board1()
        feldlöschen()


play()
