import copy

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


def player():
    x = int(input('x: ')) - 1
    y = int(input('y: ')) - 1
    if board[y][x] == ' ':
        board[y][x] = 'X'


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


d = 3
minimaxc = 0
bestmove = []
value = 0


def minimax(position, depth, maxplayer):
    global value
    global minimaxc
    minimaxc = minimaxc + 1
    # X:maxplayer,spieler O:minplayer,computer
    if gewonnen(position, 'O'):
        return -1
    elif gewonnen(position, 'X'):
        return 1
    elif depth == d:
        return 0
    elif position.count(' ') == 0:
        return 0
    else:
        pass

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
    #

    if maxplayer:
        maxvalue = -10
        for child in children:
            value = minimax(child, depth + 1, False)
            if value > maxvalue:
                maxvalue = value
        return maxvalue

    if not maxplayer:
        minvalue = 10
        for child in children:
            value = minimax(child, depth + 1, True)
            if value < minvalue:
                minvalue = value
        return minvalue


firstgenchildren = []
scores = []


def minimaxer(startpos):
    firstgenchildren.clear()
    scores.clear()
    boardc = copy.deepcopy(startpos)
    y = 0
    for i in range(3):
        x = 0
        for j in range(3):
            if boardc[x][y] == ' ':
                boardc[x][y] = str('O')
                firstgenchildren.append(boardc)
                boardc = copy.deepcopy(startpos)
            else:
                pass
            x = x + 1
        y = y + 1

    for firstgenchild in firstgenchildren:
        score = int(minimax(firstgenchild, 1, False))
        scores.append(copy.deepcopy(score))
        score = 0


def newboard():
    indx = scores.index(min(scores))
    bestmove = copy.deepcopy(firstgenchildren[indx])
    board.clear()
    board.extend(copy.deepcopy(bestmove))
    bestmove.clear()


def printf():
    for b in firstgenchildren:
        print('  1   2   3')
        print('-------------')
        for i in range(3):
            print('I ', end='')
            for j in range(3):
                print(b[i][j], end='')
                print(' I ', end='')
            print(i + 1)
            print('-------------')
        print(minimax(b, 0, False))
        print(evaluatepos(b))


def play():
    while True:
        printboard()
        player()
        minimaxer(board)
        newboard()
        print(minimaxc)
        #
        # printf()
        # print(len(firstgenchildren))
        # print(scores)
        # print(scores.index(min(scores)))
        #


play()
