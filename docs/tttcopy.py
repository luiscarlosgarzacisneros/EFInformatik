board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]


def printboard():
    print('  1   2   3')
    print('-------------')
    for i in range(3):
        print('I ', end='')
        for j in range(3):
            print(board[i][j], end='')
            print(' I ', end='')
        print(i + 1)
        print('-------------')


def player():
    x = int(input('x: ')) - 1
    y = int(input('y: ')) - 1
    board[y][x] = 'X'


def gameover(board):
    # horizontal
    if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
        return True
    elif board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
        return True
    elif board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
        return True
    # vertikal
    elif board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
        return True
    elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
        return True
    elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
        return True
    # diagonal
    elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        return True
    elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        return True
    else:
        return False


def play():
    round = 1
    while gameover(board) == False:
        printboard()
        player()
        round = round + 1
        print(round)
    printboard()
    print('GAME OVER')
    print(gameover(board))


play()
