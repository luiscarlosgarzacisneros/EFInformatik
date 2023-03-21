import copy

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


def gameover(board, xoro):
    # board ist in dieser funktion die ausgewählte matrix, nicht DAS board.
    # horizontal
    if board[0][0] == xoro and board[0][1] == xoro and board[0][2] == xoro:
        return True
    elif board[1][0] == xoro and board[1][1] == xoro and board[1][2] == xoro:
        return True
    elif board[2][0] == xoro and board[2][1] == xoro and board[2][2] == xoro:
        return True
    # vertikal
    elif board[0][0] == xoro and board[1][0] == xoro and board[2][0] == xoro:
        return True
    elif board[0][1] == xoro and board[1][1] == xoro and board[2][1] == xoro:
        return True
    elif board[0][2] == xoro and board[1][2] == xoro and board[2][2] == xoro:
        return True
    # diagonal
    elif board[0][0] == xoro and board[1][1] == xoro and board[2][2] == xoro:
        return True
    elif board[0][2] == xoro and board[1][1] == xoro and board[2][0] == xoro:
        return True
    else:
        return False


def generatechildren(board, xturn):
    # [matrix][alle children]
    xturn = False
    tree = []

    boardcopy = copy.deepcopy(board)
    for s in boardcopy:
        if s == ' ':
            s = 'O'
            tree.append(boardcopy)
        else:
            pass


def evaluatepos(board):
    # board ist hier wieder das ausgawählte Spielfeld
    if gameover(board, 'X') == True:
        return 100
    elif gameover(board, 'O') == True:
        return -100


def minimax(position, depth, maxplayer):
    # X:maxplayer,spieler O:minplayer,computer
    if depth == 0 or gameover(board, 'X') == True or gameover(board, 'O') == True:
        return evaluatepos(positionboard)

    if maxplayer:
        maxvalue = -100
        for child in position:
            value = minimax(child, depth - 1, False)
            maxvalue = max(value, maxvalue)
        return maxvalue

    if not maxplayer:
        minvalue = 100
        for child in position:
            value = minimax(child, depth - 1, True)
            minvalue = min(value, minvalue)
        return minvalue


def play():
    round = 1
    while gameover(board, 'X') == False and gameover(board, 'O') == False:
        gameover(board, 'X')
        gameover(board, 'O')
        printboard()
        player()
        round = round + 1
        print(round)
    printboard()
    print('GAME OVER')


play()
