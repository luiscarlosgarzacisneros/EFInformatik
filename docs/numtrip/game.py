
board = [
        [2, 4, 666, 88, 8],
        [4, 222222, 8, 2, 1],
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
            if len(str(board[zeile][spalte])) == 1:
                print('I   ', end='')
                print(board[zeile][spalte], end='')
                print('  ', end='')

            if len(str(board[zeile][spalte])) == 2:
                print('I  ', end='')
                print(board[zeile][spalte], end='')
                print('  ', end='')

            if len(str(board[zeile][spalte])) == 3:
                print('I  ', end='')
                print(board[zeile][spalte], end='')
                print(' ', end='')

            if len(str(board[zeile][spalte])) == 4:
                print('I ', end='')
                print(board[zeile][spalte], end='')
                print(' ', end='')

            if len(str(board[zeile][spalte])) == 5:
                print('I ', end='')
                print(board[zeile][spalte], end='')
                print('', end='')

            if len(str(board[zeile][spalte])) == 6:
                print('I', end='')
                print(board[zeile][spalte], end='')
                print('', end='')

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
    zeile = int(zeile)
    spalte = int(spalte)

    board[zeile - 1][spalte - 1] = ' '


spielen = True


def play():
    while spielen == True:
        board1()
        feldlöschen()


play()
