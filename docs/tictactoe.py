import copy

# boards--------------
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]
board2 = [
    ['U', 'U', 'U'],
    ['U', 'U', 'U'],
    [' ', ' ', ' '],
]
# --------------------


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


def gewonnen(board, xoro):
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


def evaluatepos(board):
    # board ist hier wieder das ausgawählte Spielfeld
    if gewonnen(board, 'X') == True:
        return 100
    elif gewonnen(board, 'O') == True:
        return -100
    else:
        return 0


d = 3
minimaxc = 0
bestmove = []
value = 0


def minimax(position, depth, maxplayer):
    global value
    global minimaxc
    minimaxc = minimaxc + 1
    # X:maxplayer,spieler O:minplayer,computer
    if depth == d or gewonnen(position, 'X') == True or gewonnen(position, 'O') == True:
        return evaluatepos(position)

    # ----
    boardcopy = copy.deepcopy(position)
    children = []
    # -----

    # Spieler
    if maxplayer:
        player = 'X'
    else:
        player = 'O'

    # children generieren
    y = 0
    for i in range(3):
        x = 0
        for j in range(3):
            if boardcopy[x][y] == ' ':
                boardcopy[x][y] = str(player)
                children.append(boardcopy)
                boardcopy = copy.deepcopy(position)
            else:
                pass
            x = x + 1
        y = y + 1

    if maxplayer:
        maxvalue = -100
        for child in children:
            value = minimax(child, depth + 1, False)
            maxvalue = max(value, maxvalue)
        return maxvalue

    if not maxplayer:
        minvalue = 100
        for child in children:
            value = minimax(child, depth + 1, True)
            minvalue = min(value, minvalue)
        return minvalue


# ------------------------------------
minimax(board, 0, True)
print(bestmove)
print(minimax(board, 0, True))

# try returnin list with [value][bestmove]
