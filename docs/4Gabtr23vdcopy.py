import copy
import time
import random

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
d = 5
nextmoves = []
scores = []
move = []
moves=[]
bestscores=[]
maxtime = 20
turn=0
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
#
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

def inarow(board, player, otherplayer):
    score=0
    # horizontal
    for q in range(4):
        for w in range(6):
            empty=0
            other=0
            filled=0
            #
            if board[w][q] == player:
                filled=filled+ 1
            if board[w][q + 1] == player:
                filled=filled+ 1
            if board[w][q + 2] == player:
                filled=filled+ 1
            if board[w][q + 3] == player:
                filled=filled+ 1
            #
            if board[w][q] == ' ':
                empty=empty+ 1
            if board[w][q + 1] == ' ':
                empty=empty+ 1
            if board[w][q + 2] == ' ':
                empty=empty+ 1
            if board[w][q + 3] == ' ':
                empty=empty+ 1
            #
            if board[w][q] == otherplayer:
                other=other+ 1
            if board[w][q + 1] == otherplayer:
                other=other+ 1
            if board[w][q + 2] == otherplayer:
                other=other+ 1
            if board[w][q + 3] == otherplayer:
                other=other+ 1
            #
            if other==0:
                if filled==4:
                    score=score+10000
                if filled==3:
                    score=score+100
                if filled==2:
                    score=score+3
            elif filled==0:
                if other==4:
                    score=score-10000
                if other==3:
                    score=score-100
                if other==2:
                    score=score-3
    # vertikal
    for q in range(7):
        for w in range(3):
            empty=0
            other=0
            filled=0
            #
            if board[w][q] == player:
                filled=filled+ 1
            if board[w + 1][q] == player:
                filled=filled+ 1
            if board[w + 2][q] == player:
                filled=filled+ 1
            if board[w + 3][q] == player:
                filled=filled+ 1
            #
            if board[w][q] == ' ':
                empty=empty+ 1
            if board[w + 1][q] == ' ':
                empty=empty+ 1
            if board[w + 2][q] == ' ':
                empty=empty+ 1
            if board[w + 3][q] == ' ':
                empty=empty+ 1
            #
            if board[w][q] == otherplayer:
                other=other+ 1
            if board[w + 1][q] == otherplayer:
                other=other+ 1
            if board[w + 2][q] == otherplayer:
                other=other+ 1
            if board[w + 3][q] == otherplayer:
                other=other+ 1
            #
            if other==0:
                if filled==4:
                    score=score+10000
                if filled==3:
                    score=score+50
                if filled==2:
                    score=score+1
            elif filled==0:
                if other==4:
                    score=score-10000
                if other==3:
                    score=score-50
                if other==2:
                    score=score-1
    # diagonal1
    for q in range(4):
        for w in range(3):
            empty=0
            other=0
            filled=0
            #
            if board[w][q] == player:
                filled=filled+ 1
            if board[w + 1][q + 1] == player:
                filled=filled+ 1
            if board[w + 2][q + 2] == player:
                filled=filled+ 1
            if board[w + 3][q + 3] == player:
                filled=filled+ 1
            #
            if board[w][q] == ' ':
                empty=empty+ 1
            if board[w + 1][q + 1] == ' ':
                empty=empty+ 1
            if board[w + 2][q + 2] == ' ':
                empty=empty+ 1
            if board[w + 3][q + 3] == ' ':
                empty=empty+ 1
            #
            if board[w][q] == otherplayer:
                other=other+ 1
            if board[w + 1][q + 1] == otherplayer:
                other=other+ 1
            if board[w + 2][q + 2] == otherplayer:
                other=other+ 1
            if board[w + 3][q + 3] == otherplayer:
                other=other+ 1
            #
            if other==0:
                if filled==4:
                    score=score+10000
                if filled==3:
                    score=score+100
                if filled==2:
                    score=score+3
            elif filled==0:
                if other==4:
                    score=score-10000
                if other==3:
                    score=score-100
                if other==2:
                    score=score-3
    # diagonal2
    for q in range(4):
        for w in range(3):
            empty=0
            other=0
            filled=0
            #
            if board[w][q + 3] == player:
                filled=filled+ 1
            if board[w + 1][q + 2] == player:
                filled=filled+ 1
            if board[w + 2][q + 1] == player:
                filled=filled+ 1
            if board[w + 3][q] == player:
                filled=filled+ 1
            #
            if board[w][q + 3] == ' ':
                empty=empty+ 1
            if board[w + 1][q + 2] == ' ':
                empty=empty+ 1
            if board[w + 2][q + 1] == ' ':
                empty=empty+ 1
            if board[w + 3][q] == ' ':
                empty=empty+ 1
            #
            if board[w][q + 3] == otherplayer:
                other=other+ 1
            if board[w + 1][q + 2] == otherplayer:
                other=other+ 1
            if board[w + 2][q + 1] == otherplayer:
                other=other+ 1
            if board[w + 3][q] == otherplayer:
                other=other+ 1
            #
            if other==0:
                if filled==4:
                    score=score+10000
                if filled==3:
                    score=score+100
                if filled==2:
                    score=score+3
            elif filled==0:
                if other==4:
                    score=score-10000
                if other==3:
                    score=score-100
                if other==2:
                    score=score-3
    return score
#
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
#
def minimax(position, depth, maxplayer, alpha, beta):
    # X:maxplayer,spieler O:minplayer,computer
    # Spieler
    # alpha: best maxpl, beta: best minpl
    if maxplayer:
        playerj = 'X'
    else:
        playerj = 'O'

    # return
    pos =copy.deepcopy(position)

    f=inarow(pos,'X','O')
    if gewonnen(position, 'O') == True or gewonnen(position, 'X') == True:
        return f
    elif depth == d:
        return f
    elif genchildren(position, playerj) == []:
        return f
    #
    if maxplayer:
        maxvalue = -100000000000
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
        minvalue = 1000000000000
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
#
def minimaxer(boa):
    global minimaxc
    minimaxc = 0
    nextmoves.clear()
    scores.clear()
    move.clear()
    moves.clear()
    start = time.time()
    for firstgenchild in genchildren(boa, 'O'):
        nextmoves.append(copy.deepcopy(firstgenchild))
        scores.append(minimax(firstgenchild, 1, True, -10000000000000000000, 1000000000000000000000))
        if (time.time() - start) > maxtime:
            break
    #
    print(scores)
    #
    for y in range(len(scores)):
        if scores[y]==(min(scores)):
            moves.append(copy.deepcopy(nextmoves[y]))
    move.extend(copy.deepcopy(random.choice(moves)))
#
def gameover(boar):
    isover = True
    for q in range(6):
        if boar[q].count(' ') > 0:
            isover = False
    return isover

def play():
    global turn
    while not gameover(board) and not gewonnen(board, 'O') and not gewonnen(board, 'X'):
        turn =turn+1
        print(turn)
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
    print(turn)
    printboard(board)
    print('GAME OVER')
    if gewonnen(board, 'O'):
        print(':( VERLOREN')
    elif gewonnen(board, 'X'):
        print(':) GEWONNEN')
    else:
        print(':l UNENTSCHIEDEN')


play()
