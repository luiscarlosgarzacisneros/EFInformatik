

def board1():
    artzeile = 3
    print("    1      2      3      4      5")
    for i in range(5):
        print("+------+------+------+------+------+")
        artzeile = 0

        print("I      I      I      I      I      I")
        artzeile = artzeile + 1

        print("I   2  I   2  I   2  I   2  I   2  I  1")
        artzeile = artzeile + 1

        print("I      I      I      I      I      I")
        artzeile = artzeile + 1
    print("+------+------+------+------+------+")


board = [
    [2, 4, 1, 8, 8],
    [4, 2, 8, 2, 1],
    [4, 4, 8, 4, 2],
    [2, 8, 1, 4, 1],
    [2, 4, 4, 4, 4]
]

zeilnummer = 1

print('  1 2 3 4 5 ')


for zeile in board:
    print(" ", end="")
    for zelle in zeile:
        print(' -', end='')

    print(' ')
    print(zeilnummer, end="")
    zeilnummer = zeilnummer + 1
    for zelle in zeile:
        print(f'|{zelle}', end='')
    print('|')

for zelle in board[0]:
    print(' -', end='')
print(' ')

board1()
