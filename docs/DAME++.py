import copy
import time
import random

board = [
    [' ', 'O', ' ', 'O', ' ', 'O', ' ','O'],
    ['O', ' ', 'O', ' ', 'O', ' ', 'O',' '],
    [' ', 'O', ' ', 'O', ' ', 'O', ' ','O'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
    ['X', ' ', 'X', ' ', 'X', ' ', 'X',' '],
    [' ', 'X', ' ', 'X', ' ', 'X', ' ','X'],
    ['X', ' ', 'X', ' ', 'X', ' ', 'X',' '],
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
w=[]
#


def printboard(board):
    print('  1   2   3   4   5   6   7   8')
    print('---------------------------------')
    for i in range(8):
        print('I ', end='')
        for j in range(8):
            print(board[i][j], end='')
            print(' I ', end='')
        print(i + 1)
        print('---------------------------------')

def schlagenmoeglichX(y,x,boar):
    r=False
    if y-2>-1 and x-2>-1:
        if boar[y-2][x-2]==' 'and boar[y-1][x-1]=='O':
            r=True
    if y-2>-1 and x+2<8:
        if boar[y-2][x+2]==' ' and boar[y-1][x+1]=='O':
            r=True
    else:
        r=False
    return r

def schlagenplayer(vy,vx,zy,zx,boardcopy):
    while schlagenmoeglichX(vy,vx,boardcopy):
        try:
            if zy==vy- 2 and zx==vx +2 and boardcopy[vy-1][vx+1]=='O':
                boardcopy[zy][zx]='X'
                boardcopy[vy][vx]=' '
                boardcopy[vy-1][vx+1]=' '
                printboard(boardcopy)
                vx = zx
                vy = zy
                if not schlagenmoeglichX(vy,vx,boardcopy):
                    break
                zx = int(input('zu x: ')) - 1
                zy = int(input('zu y: ')) - 1
                                    
            elif zy==vy- 2 and zx==vx-2 and boardcopy[vy-1][vx-1]=='O':
                boardcopy[zy][zx]='X'
                boardcopy[vy][vx]=' '
                boardcopy[vy-1][vx-1]=' '
                printboard(boardcopy)
                vx = zx
                vy = zy
                if not schlagenmoeglichX(vy,vx,boardcopy):
                    break
                zx = int(input('zu x: ')) - 1
                zy = int(input('zu y: ')) - 1
            else:
                zx = int(input('zu x: ')) - 1
                zy = int(input('zu y: ')) - 1
                schlagenplayer(vy,vx,zy,zx,boardcopy)
                
        except:
            print('EINGABE NICHT KORREKT')
            zx = int(input('zu x: ')) - 1
            zy = int(input('zu y: ')) - 1
            schlagenplayer(vy,vx,zy,zx,boardcopy)
    return boardcopy

def player(playerk, boardk):
    boardcopy=copy.deepcopy(boardk)
    try:
        vx = int(input('von x: ')) - 1
        vy = int(input('von y: ')) - 1
        zx = int(input('zu x: ')) - 1
        zy = int(input('zu y: ')) - 1
    except:
        print('EINGABE NICHT KORREKT')
        player(playerk, boardk)
    try:
        if zy<9 and zy>0 and zx>0 and zx<9 and boardcopy[vy][vx] == playerk and boardcopy[zy][zx]==' ':
            if playerk=='X':
                if zy==vy- 1:
                    if zx==vx +1:
                        boardcopy[zy][zx]='X'
                        boardcopy[vy][vx]=' '
                        return boardcopy
                    elif zx==vx-1:
                        boardcopy[zy][zx]='X'
                        boardcopy[vy][vx]=' '
                        return boardcopy
                elif zy==vy- 2:
                    f=schlagenplayer(vy,vx,zy,zx,boardcopy)
                    return f
                else:
                    print('EINGABE NICHT KORREKT')
                    player(playerk, boardk)
                
        else:
            print('EINGABE NICHT KORREKT')
            player(playerk, boardk)
    except:
        print('EINGABE NICHT KORREKT')
        player(playerk, boardk)

def genchildren(position, playerq):
    children = []
    boardcopy = copy.deepcopy(position)
    y = 0
    for i in range(8):
        x = 0
        for j in range(8):
            if boardcopy[y][x] == playerq:
                if playerq=='X':
                    if y-1>-1 and x-1>-1 and boardcopy[y-1][x-1]==' ':
                        boardcopy[y-1][x-1]='X'
                        boardcopy[y][x]=' '
                        children.append(boardcopy)
                        boardcopy = copy.deepcopy(position)
                    if y-1>-1 and x+ 1<8 and boardcopy[y-1][x+ 1]==' ':
                        boardcopy[y-1][x+ 1]='X'
                        boardcopy[y][x]=' '
                        children.append(boardcopy)
                        boardcopy = copy.deepcopy(position)
                    if y-2>-1 and x-2>-1 and boardcopy[y-1][x-1]=='O' and boardcopy[y-2][x-2]==' ':
                        boardcopy[y-1][x-1]=' '
                        boardcopy[y-2][x-2]='X'
                        boardcopy[y][x]=' '
                        children.append(boardcopy)
                        boardcopy = copy.deepcopy(position)
                    if y-2>-1 and x+ 2<8 and boardcopy[y-1][x+ 1]=='O' and boardcopy[y-2][x+2]==' ':
                        boardcopy[y-1][x+1]=' '
                        boardcopy[y-2][x+2]='X'
                        boardcopy[y][x]=' '
                        children.append(boardcopy)
                        boardcopy = copy.deepcopy(position)
                    else:
                        pass
                elif playerq=='O':
                    if y+ 1<8 and x-1>-1 and  boardcopy[y+ 1][x-1]==' ':
                        boardcopy[y+1][x-1]='O'
                        boardcopy[y][x]=' '
                        children.append(boardcopy)
                        boardcopy = copy.deepcopy(position)
                    if y+ 1<8 and x+ 1<8 and boardcopy[y+ 1][x+ 1]==' ':
                        boardcopy[y+ 1][x+ 1]='O'
                        boardcopy[y][x]=' '
                        children.append(boardcopy)
                        boardcopy = copy.deepcopy(position)
                    if y+ 2<8 and x-2>-1 and  boardcopy[y+ 1][x-1]=='X' and boardcopy[y+2][x-2]==' ':
                        boardcopy[y+1][x-1]=' '
                        boardcopy[y+2][x-2]='O'
                        boardcopy[y][x]=' '
                        children.append(boardcopy)
                        boardcopy = copy.deepcopy(position)
                    if y+ 2<8 and x+ 2<8 and boardcopy[y+ 1][x+ 1]=='X' and boardcopy[y+2][x+2]==' ':
                        boardcopy[y+1][x+1]=' '
                        boardcopy[y+2][x+2]='O'
                        boardcopy[y][x]=' '
                        children.append(boardcopy)
                        boardcopy = copy.deepcopy(position)
                    else:
                        pass
                else:
                    pass
            x = x + 1
        y = y + 1
    #
    global minimaxc
    minimaxc = minimaxc + 1
    #
    return children

def evaluatepos(pos):
    eval=0
    for sl in range(len(pos)):
        for o in range(pos[sl].count('X')):
            eval=eval+1
        for o in range(pos[sl].count('O')):
            eval=eval-1
    return eval

def gameover(pos):
    evalX=0
    evalO=0
    for sl in range(len(pos)):
        for o in range(pos[sl].count('X')):
            evalX=evalX+1
    for sl in range(len(pos)):
        for o in range(pos[sl].count('O')):
            evalO=evalO+1
    if evalO==0:
        return True
    if evalX==0:
        return True
    else:
        return False

def gewonnen(pos,otherplayer):
    eval=0
    for sl in range(len(pos)):
        for o in range(pos[sl].count(otherplayer)):
            eval=eval+1
    if eval==0:
        return True
    else:
        return False
    


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

    f=evaluatepos(pos)
    if gewonnen(position, 'O') == True:
        return f
    elif gewonnen(position, 'X') == True:
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
        scores.append(minimax(firstgenchild, 1, True, -1000000000000, 100000000000000))
        if (time.time() - start) > maxtime:
            break
    #
    print(scores)
    #
    for y in range(len(scores)):
        if scores[y]==(min(scores)):
            moves.append(copy.deepcopy(nextmoves[y]))
    move.extend(copy.deepcopy(random.choice(moves)))


def play():
    global turn
    while not gameover(board) and not gewonnen(board, 'O') and not gewonnen(board, 'X'):
        turn =turn+1
        print(turn)
        printboard(board)
        w.clear()
        w=copy.deepcopy(player('X',board))
        board.clear()
        board.extend(w)
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
    if gewonnen(board, 'X'):
        print(':( VERLOREN')
    elif gewonnen(board, 'O'):
        print(':) GEWONNEN')
    else:
        print(':l UNENTSCHIEDEN')


play()



#print(schlagenmoeglichX(5,2,board))
#printboard(board)
#printboard(player('X',board))
############
#printboard(board)
#for t in genchildren(board,'O'):
    #printboard(t)
#print(gewonnen('O',board))
