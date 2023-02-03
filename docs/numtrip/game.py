import random

züge = 1
gewonnen = False
spielen = True

board = []
numbers = [1, 2, 4, 8]


def generateboard():
    # board wird zufällig generiert. zeile wird generiert mit 5 spalten und an board appended
    list = []
    for j in range(5):
        for i in range(5):
            list.append(int(random.choice(numbers)))
        board.append(list)
        list = []


def board1():
    # board wird ausgegeben
    zeile = 0
    spalte = 0
    zahlrechts = 1

    print("    1      2      3      4      5")
    for i in range(5):
        print("+------+------+------+------+------+")

        print("I      I      I      I      I      I")

        # Zeile mit board Element
        # Die Zahl sollte in der Mitte der Zelle sein, nicht Rechtsbündig
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

        print("I      I      I      I      I      I")
    print("+------+------+------+------+------+")


def floodfill(x, y, wert):
    # füllt Nachbarszellen mit dem gleichen Wert mit ' '
    if x + 1 < 5:
        if board[x + 1][y] == wert:
            board[x + 1][y] = ' '
            floodfill(x + 1, y, wert)
    if x - 1 > -1:
        if board[x - 1][y] == wert:
            board[x - 1][y] = ' '
            floodfill(x - 1, y, wert)
    if y + 1 < 5:
        if board[x][y + 1] == wert:
            board[x][y + 1] = ' '
            floodfill(x, y + 1, wert)
    if y - 1 > -1:
        if board[x][y - 1] == wert:
            board[x][y - 1] = ' '
            floodfill(x, y - 1, wert)

# mehr einzelne Definitionen. 
# Definition passender benennen.

def eingabe():
    global züge
    global gewonnen

    # ausgewähltes feld
    zeile = input('zeile: ')
    spalte = input('spalte: ')

    eingabe_zeile = True
    eingabe_spalte = True

    # eingabeüberprüfung
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
        zeilex = int(zeile) - 1
        spaltex = int(spalte) - 1
        # wenn eingabe richtig
        züge = züge + 1
        ausgewähltezahl = board[zeilex][spaltex]

        # hat das ausgewählte feld einen Nachbarn mit der gleichen zahl
        o = False
        if zeilex + 1 < 5:
            if int(board[zeilex + 1][spaltex]) == int(board[zeilex][spaltex]):
                o = True
        if zeilex - 1 > -1:
            if int(board[zeilex - 1][spaltex]) == int(board[zeilex][spaltex]):
                o = True
        if spaltex + 1 < 5:
            if int(board[zeilex][spaltex + 1]) == int(board[zeilex][spaltex]):
                o = True
        if spaltex - 1 > -1:
            if int(board[zeilex][spaltex - 1]) == int(board[zeilex][spaltex]):
                o = True

        # Wenn ja, dann wird dieses Feld gelöscht & floodfill von da aus gemacht. Wenn nein dann kann man diese Feld nicht auswähen:X
        if o == True:
            floodfill(zeilex, spaltex, board[zeilex][spaltex])
            # Wenn die Eingabe korrekt war wird das ausgewählte Feld mal 2 gerechnet
            board[int(zeilex)][int(spaltex)] = str(int(ausgewähltezahl) * 2)
        else:
            print('X')

        # Felder oberhalb eines ' ' Feldes gehen 1 nah unten. Alle Felder werden überprüft
        spalte = 0
        zeile = 0
        for i in range(5):
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

            # wenn ein Feld oben leer ist, wird es mit einer zufälligen Zahl (1,2 oder 4) gefüllt.
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

        # hat man eine bestimmte Zahl erreicht, dann hat man gewonnen
        for i in range(5):
            if board[zeilex][spaltex] == '1024':
                gewonnen = True
            if zeilex < 4:
                zeilex = zeilex + 1

    # Fehler wird gezeigt wenn Eingabe fehlerhaft
    else:
        print('Fehlerhafte Eingabe')
        print(fehler)

# Es wird überprüft, ob ein Feld ein Nachbarsfeld der gleichen Zahl hat. Wenn nein hat der spieler verloren.

# Die ganzen try-except sind hier nicht nögtig. 1. Wegen dem 'past', 2. wird es bei z.B. bei Eingaben, oder Dateien benutzt.

def verloren():
    global spielen
    verloren = True
    x = 0
    y = 0
    a = board[x][y]
    for i in range(5):
        x = 0
        for j in range(5):
            a = board[x][y]
            if x > 1:
                if board[x - 1][y] == a:
                    verloren = False
            if x < 1:
                if board[x + 1][y] == a:
                    verloren = False
            if y > 1:
                if board[x][y - 1] == a:
                    verloren = False
            if y < 1:
                if board[x][y + 1] == a:
                    verloren = False
            x = x + 1
        y = y + 1
    if verloren == True:
        print('game over')
        spielen = False
        board1()

# Spielablauf: Feld zeigen, Felder werden gelöscht und wieder aufgefüllt, man schaut ob man verloren oder gewonnen hat, Zug:x


def play():
    global gewonnen
    while spielen == True:
        board1()
        eingabe()
        verloren()
        print(f'zug:{züge}')
        if gewonnen == True:
            print('gewonnen')
            board1()
            break


generateboard()
play()


# mind python3, um spielen zu können
