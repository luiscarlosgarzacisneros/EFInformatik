import copy
import time

board = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
]
#
minimaxc = 0
d = 6
nextmoves = []
scores = []
move = []
maxtime = 15
#


def printboard(board):
    print('  1   2   3   4   5   6   7')
    print('-----------------------------')
    for i in range(6):
        print('I ', end='')
        for j in range(7):
            print(board[i][j], end='')
            print(' I ', end='')
        print('')
        print('-----------------------------')


def fall(board, y, x, player):
    if y <= 4:
        if board[y + 1][x] == ' ':
            board[y + 1][x] = player
            board[y][x] = ' '
            y = y + 1
            fall(board, y, x, player)
        else:
            pass


def player():
    try:
        x = int(input('x: ')) - 1
        if board[0][x] == ' ':
            board[0][x] = 'X'
            fall(board, 0, x, 'X')
        else:
            print('FELD BESETZT')
            player()
    except:
        print('EINGABE NICHT KORREKT')
        player()


def gewonnen(board, player):
    gew = False
    # horizontal
    for q in range(4):
        for w in range(6):
            if board[w][q] == player and board[w][q + 1] == player and board[w][q + 2] == player and board[w][q + 3] == player:
                gew = True
    # vertikal
    for q in range(7):
        for w in range(3):
            if board[w][q] == player and board[w + 1][q] == player and board[w + 2][q] == player and board[w + 3][q] == player:
                gew = True
    # diagonal1
    for q in range(4):
        for w in range(3):
            if board[w][q] == player and board[w + 1][q + 1] == player and board[w + 2][q + 2] == player and board[w + 3][q + 3] == player:
                gew = True
    # diagonal2
    for q in range(4):
        for w in range(3):
            if board[w][q + 3] == player and board[w + 1][q + 2] == player and board[w + 2][q + 1] == player and board[w + 3][q] == player:
                gew = True
    return gew


def genchildren(position, playerk):
    children = []
    boardcopy = copy.deepcopy(position)
    for x in range(7):
        if boardcopy[0][x] == ' ':
            boardcopy[0][x] = str(playerk)
            fall(boardcopy, 0, x, playerk)
            children.append(boardcopy)
            boardcopy = copy.deepcopy(position)
    #
    global minimaxc
    minimaxc = minimaxc + 1
    #
    return children


def minimax(position, depth, maxplayer, alpha, beta):
    # X:maxplayer,spieler O:minplayer,computer
    # Spieler
    # alpha: best maxpl, beta: best minpl
    if maxplayer:
        playerj = 'X'
    else:
        playerj = 'O'

    # return
    if gewonnen(position, 'O') == True:
        return -1
    elif gewonnen(position, 'X') == True:
        return 1
    elif depth == d:
        return 0
    elif genchildren(position, playerj) == []:
        return 0

    #
    if maxplayer:
        maxvalue = -10
        for child in genchildren(position, playerj):
            value = minimax(child, depth + 1, False, alpha, beta)
            if value > maxvalue:
                maxvalue = value
            # pruning
            if value > alpha:
                alpha = value
            if beta <= alpha:
                break
        return maxvalue
    #
    if not maxplayer:
        minvalue = 10
        for child in genchildren(position, playerj):
            value = minimax(child, depth + 1, True, alpha, beta)
            if value < minvalue:
                minvalue = value
            # pruning
            if value < beta:
                beta = value
            if beta <= alpha:
                break
        return minvalue


def minimaxer(boa):
    global minimaxc
    minimaxc = 0
    nextmoves.clear()
    scores.clear()
    move.clear()
    start = time.time()
    for firstgenchild in genchildren(boa, 'O'):
        nextmoves.append(copy.deepcopy(firstgenchild))
        scores.append(minimax(firstgenchild, 1, True, -2, 2))
        if (time.time() - start) > maxtime:
            break
    #
    move.extend(copy.deepcopy(nextmoves[scores.index(min(scores))]))


def gameover(boar):
    isover = True
    for q in range(6):
        if boar[q].count(' ') > 0:
            isover = False
    return isover


def play():
    while not gameover(board) and not gewonnen(board, 'O') and not gewonnen(board, 'X'):
        printboard(board)
        player()
        if not gameover(board) and not gewonnen(board, 'O') and not gewonnen(board, 'X'):
            start = time.time()
            minimaxer(board)
            end = time.time()
            board.clear()
            board.extend(copy.deepcopy(move))
            print(end - start)
            print(minimaxc)
    printboard(board)
    print('GAME OVER')
    if gewonnen(board, 'O'):
        print(':( VERLOREN')
    elif gewonnen(board, 'X'):
        print(':) GEWONNEN')
    else:
        print(':l UNENTSCHIEDEN')


play()

# funktioniert vielleicht
# spiel randomizieren
# OO_O, OOO auch reward
#tyrytryrtytryryt