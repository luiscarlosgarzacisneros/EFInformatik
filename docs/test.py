import copy
import time
import random

board = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', ' ', ' ', 'W', ' ',' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', 'M', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', ' ', 'O', ' ', ' ',' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
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
childrens=[]
e=[]
es=[]
esw=[]
ds=[]
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
        if boar[y-2][x-2]==' ':
            if boar[y-1][x-1]=='O' or boar[y-1][x-1]=='M':
                r=True
    if y-2>-1 and x+2<8:
        if boar[y-2][x+2]==' ':
            if boar[y-1][x+1]=='O' or boar[y-1][x+1]=='M':
                r=True
    return r

def eingabe(pos):
    e.clear()
    korrekt=False
    try:
        vx = int(input('von x: ')) - 1
        vy = int(input('von y: ')) - 1
        zx = int(input('zu x: ')) - 1
        zy = int(input('zu y: ')) - 1
    except:
        print('EINGABE NICHT KORREKT')
        return False
    #
    if vy<8 and vy>-1 and vx<8 and vx>-1 and zy<8 and zy>-1 and zx<8 and zx>-1:
        if zy==vy-1 and zx==vx-1 and pos[vy][vx]=='X' and pos[zy][zx]==' ':
            korrekt=True
        if zy==vy-1 and zx==vx+1 and pos[vy][vx]=='X' and pos[zy][zx]==' ':
            korrekt=True
        #
        if zy==vy-2 and zx==vx-2 and pos[vy][vx]=='X' and pos[zy][zx]==' ':
            if pos[vy-1][vx-1]=='O' or pos[vy-1][vx-1]=='M':
                korrekt=True
        if zy==vy-2 and zx==vx+2 and pos[vy][vx]=='X' and pos[zy][zx]==' ':
            if pos[vy-1][vx+1]=='O' or pos[vy-1][vx+1]=='M':
                korrekt=True
        #
        ds.clear()
        if pos[vy][vx]=='W':
            schlagen=False
            for i in range(7):
                if vy-1-i<0 or vx-1-i<0:
                    break
                if pos[vy-1-i][vx-1-i]=='X':
                    break
                elif pos[vy-1-i][vx-1-i]=='W':
                    break
                if pos[vy-1-i][vx-1-i]=='O':
                    schlagen=True
                elif pos[vy-1-i][vx-1-i]=='M':
                    schlagen=True
                if pos[vy-1-i][vx-1-i]==' ' and vy-1-i==zy and vx-1-i==zx:
                    korrekt=True
                    break
                if schlagen:
                    if vy-2-i==zy and vx-2-i==zx and pos[vy-2-i][vx-2-i]==' ':
                        korrekt=True
                        ds.append(vy-1-i)
                        ds.append(vx-1-i)
                        break
                    break
        if pos[vy][vx]=='W':
            schlagen=False
            for i in range(7):
                if vy+1+i>7 or vx+1+i>7:
                    break
                if pos[vy+1+i][vx+1+i]=='X':
                    break
                elif pos[vy+1+i][vx+1+i]=='W':
                    break
                if pos[vy+1+i][vx+1+i]=='O':
                    schlagen=True
                elif pos[vy+1+i][vx+1+i]=='M':
                    schlagen=True
                if pos[vy+1+i][vx+1+i]==' ' and vy+1+i==zy and vx+1+i==zx:
                    korrekt=True
                    break
                if schlagen:
                    if vy+2+i==zy and vx+2+i==zx and pos[vy+2+i][vx+2+i]==' ':
                        korrekt=True
                        ds.append(vy+1+i)
                        ds.append(vx+1+i)
                        break
                    break
        if pos[vy][vx]=='W':
            schlagen=False
            for i in range(7):
                if vy+1+i>7 or vx-1-i<0:
                    break
                if pos[vy+1+i][vx-1-i]=='X':
                    break
                elif pos[vy+1+i][vx-1-i]=='W':
                    break
                if pos[vy+1+i][vx-1-i]=='O':
                    schlagen=True
                elif pos[vy+1+i][vx-1-i]=='M':
                    schlagen=True
                if pos[vy+1+i][vx-1-i]==' ' and vy+1+i==zy and vx-1-i==zx:
                    korrekt=True
                    break
                if schlagen:
                    if vy+2+i==zy and vx-2-i==zx and pos[vy+2+i][vx-2-i]==' ':
                        korrekt=True
                        ds.append(vy+1+i)
                        ds.append(vx-1-i)
                        break
                    break
        if pos[vy][vx]=='W':
            schlagen=False
            for i in range(7):
                if vy-1-i<0 or vx+1+i>7:
                    break
                if pos[vy-1-i][vx+1+i]=='X':
                    break
                elif pos[vy-1-i][vx+1+i]=='W':
                    break
                if pos[vy-1-i][vx+1+i]=='O':
                    schlagen=True
                elif pos[vy-1-i][vx+1+i]=='M':
                    schlagen=True
                if pos[vy-1-i][vx+1+i]==' ' and vy-1-i==zy and vx+1+i==zx:
                    korrekt=True
                    break
                if schlagen:
                    if vy-2-i==zy and vx+2+i==zx and pos[vy-2-i][vx+2+i]==' ':
                        korrekt=True
                        ds.append(vy-1-i)
                        ds.append(vx+1+i)
                        break
                    break
                
            #
                
    if korrekt:
        e.append(vy)
        e.append(vx)
        e.append(zy)
        e.append(zx)
        return True
    else:
        print('EINGABE NICHT KORREKT')
        return False

def eingabeschlagen(pos, vy,vx):
    es.clear()
    korrekt=False
    try:
        zx = int(input('zu x: ')) - 1
        zy = int(input('zu y: ')) - 1
    except:
        print('EINGABE NICHT KORREKT')
        return False
    #
    if zx==vx and zy==vy:
        korrekt=True
    #
    if zy<8 and zy>-1 and zx<8 and zx>-1:
        #
        if zy==vy-2 and zx==vx-2 and pos[vy][vx]=='X' and pos[zy][zx]==' ':
            if pos[vy-1][vx-1]=='O' or pos[vy-1][vx-1]=='M':
                korrekt=True
        if zy==vy-2 and zx==vx+2 and pos[vy][vx]=='X' and pos[zy][zx]==' ':
            if pos[vy-1][vx+1]=='O' or pos[vy-1][vx+1]=='M':
                korrekt=True
    if korrekt:
        es.append(zy)
        es.append(zx)
        return True
    else:
        print('EINGABE NICHT KORREKT')
        return False

def playerschlagen(vy,vx,zy,zx,pos):
    if schlagenmoeglichX(vy,vx,pos):
        if zx==vx and vy==zy:
            pass
        if zy==vy-2 and zx==vx-2 and pos[vy][vx]=='X' and pos[zy][zx]==' ':
            if pos[vy-1][vx-1]=='O' or pos[vy-1][vx-1]=='M':
                pos[vy][vx]=' '
                pos[zy][zx]='X'
                if zy==0:
                    pos[zy][zx]='W'
                pos[vy-1][vx-1]=' '
                printboard(pos)
                #
                vy = zy
                vx = zx
                if schlagenmoeglichX(vy,vx,pos):
                    while True:
                        if eingabeschlagen(pos,vy,vx)==True:
                            break
                        else:
                            continue
                    zy = es[0]
                    zx = es[1]
                    playerschlagen(vy,vx,zy,zx,pos)

        if zy==vy-2 and zx==vx+2 and pos[vy][vx]=='X' and pos[zy][zx]==' ':
            if pos[vy-1][vx+1]=='O' or pos[vy-1][vx+1]=='M':
                pos[vy][vx]=' '
                pos[zy][zx]='X'
                if zy==0:
                    pos[zy][zx]='W'
                pos[vy-1][vx+1]=' '
                printboard(pos)
                #
                vy = zy
                vx = zx
                if schlagenmoeglichX(vy,vx,pos):
                    while True:
                        if eingabeschlagen(pos,vy,vx)==True:
                            break
                        else:
                            continue
                    zy = es[0]
                    zx = es[1]
                    playerschlagen(vy,vx,zy,zx,pos)
        
def player(pos):
    while True:
        if eingabe(pos)==True:
            break
        else:
            continue
    #
    vy = e[0]
    vx = e[1]
    zy = e[2]
    zx = e[3]
    #
    if zy==vy-1 and zx==vx-1 and pos[vy][vx]=='X' and pos[zy][zx]==' ':
        pos[vy][vx]=' '
        pos[zy][zx]='X'
        if zy==0:
            pos[zy][zx]='W'
    elif zy==vy-1 and zx==vx+1 and pos[vy][vx]=='X' and pos[zy][zx]==' ':
        pos[vy][vx]=' '
        pos[zy][zx]='X'
        if zy==0:
            pos[zy][zx]='W'
    #schlagen.
    elif zy==vy-2 and zx==vx-2 and pos[vy][vx]=='X' and pos[zy][zx]==' ':
        if pos[vy-1][vx-1]=='O'or pos[vy-1][vx-1]=='M':
            playerschlagen(vy,vx,zy,zx,pos)
            if zy==0:
                pos[zy][zx]='W'
    elif zy==vy-2 and zx==vx+2 and pos[vy][vx]=='X' and pos[zy][zx]==' ':
        if pos[vy-1][vx+1]=='O'or pos[vy-1][vx+1]=='M':
            playerschlagen(vy,vx,zy,zx,pos)
            if zy==0:
                pos[zy][zx]='W'
    #W
    if pos[vy][vx]=='W':
        try:
            if pos[ds[0]][ds[1]]=='O' or pos[ds[0]][ds[1]]=='M':
                pos[vy][vx]=' '
                pos[zy][zx]='W'
                pos[ds[0]][ds[1]]=' '
                if schlagenmoeglichW(zy,zx,pos):
                    playerschlagenW(zy,zx,pos)
        except:
            pos[vy][vx]=' '
            pos[zy][zx]='W'

def genchildrenschlagen(y,x,position,playerq):
    boardcopy = copy.deepcopy(position)
    if playerq=='X':
        if y-2>-1 and x-2>-1 and  boardcopy[y-2][x-2]==' ':
            if boardcopy[y-1][x-1]=='O' or boardcopy[y-1][x-1]=='M':
                boardcopy[y-1][x-1]=' '
                boardcopy[y-2][x-2]='X'
                boardcopy[y][x]=' '
                if y-2==0:
                    boardcopy[y-2][x-2]='W'
                childrens.append(copy.deepcopy(boardcopy))
                genchildrenschlagen(y-2,x-2,boardcopy,playerq)
                boardcopy = copy.deepcopy(position)
        if y-2>-1 and x+ 2<8 and  boardcopy[y-2][x+2]==' ':
            if boardcopy[y-1][x+ 1]=='O' or boardcopy[y-1][x+ 1]=='M':
                boardcopy[y-1][x+1]=' '
                boardcopy[y-2][x+2]='X'
                boardcopy[y][x]=' '
                if y-2==0:
                    boardcopy[y-2][x+2]='W'
                childrens.append(copy.deepcopy(boardcopy))
                genchildrenschlagen(y-2,x+2,boardcopy,playerq)
                boardcopy = copy.deepcopy(position)
        else:
            pass
    elif playerq=='O':
        if y+ 2<8 and x-2>-1 and boardcopy[y+2][x-2]==' ':
            if boardcopy[y+ 1][x-1]=='X' or boardcopy[y+ 1][x-1]=='W':
                boardcopy[y+1][x-1]=' '
                boardcopy[y+2][x-2]='O'
                boardcopy[y][x]=' '
                if y+2==7:
                    boardcopy[y+2][x-2]='M'
                childrens.append(copy.deepcopy(boardcopy))
                genchildrenschlagen(y+2,x-2,boardcopy,playerq)
                boardcopy = copy.deepcopy(position)
        if y+ 2<8 and x+ 2<8 and boardcopy[y+2][x+2]==' ':
            if boardcopy[y+ 1][x+ 1]=='X' or boardcopy[y+ 1][x+ 1]=='W':
                boardcopy[y+1][x+1]=' '
                boardcopy[y+2][x+2]='O'
                boardcopy[y][x]=' '
                if y+2==7:
                    boardcopy[y+2][x+2]='M'
                childrens.append(copy.deepcopy(boardcopy))
                genchildrenschlagen(y+2,x+2,boardcopy,playerq)
                boardcopy = copy.deepcopy(position)
        else:
            pass
    return childrens

def genchildren(position, playerq):
    children = []
    boardcopy = copy.deepcopy(position)
    y = 0
    for i in range(8):
        x = 0
        for j in range(8):
            if playerq=='X':
                if boardcopy[y][x] == 'X':
                    if y-1>-1 and x-1>-1 and boardcopy[y-1][x-1]==' ':
                        boardcopy[y-1][x-1]='X'
                        boardcopy[y][x]=' '
                        if y-1==0:
                            boardcopy[y-1][x-1]='W'
                        children.append(boardcopy)
                        boardcopy = copy.deepcopy(position)
                    if y-1>-1 and x+ 1<8 and boardcopy[y-1][x+ 1]==' ':
                        boardcopy[y-1][x+ 1]='X'
                        boardcopy[y][x]=' '
                        if y-1==0:
                            boardcopy[y-1][x+1]='W'
                        children.append(boardcopy)
                        boardcopy = copy.deepcopy(position)
                    else:
                        pass
                    childrens.clear()
                    for h in genchildrenschlagen(y,x,boardcopy,'X'):
                        children.append(h)
                elif boardcopy[y][x] == 'W':
                    for r in genchildrenWM(y,x,boardcopy,'W'):
                        children.append(r)
            elif playerq=='O':
                if boardcopy[y][x] == 'O':
                    if y+ 1<8 and x-1>-1 and  boardcopy[y+ 1][x-1]==' ':
                        boardcopy[y+1][x-1]='O'
                        boardcopy[y][x]=' '
                        if y+1==7:
                            boardcopy[y+1][x-1]='M'
                        children.append(boardcopy)
                        boardcopy = copy.deepcopy(position)
                    if y+ 1<8 and x+ 1<8 and boardcopy[y+ 1][x+ 1]==' ':
                        boardcopy[y+ 1][x+ 1]='O'
                        boardcopy[y][x]=' '
                        if y+1==7:
                            boardcopy[y+1][x+1]='M'
                        children.append(boardcopy)
                        boardcopy = copy.deepcopy(position)
                    else:
                        pass
                    childrens.clear()
                    for h in genchildrenschlagen(y,x,boardcopy,'O'):
                        children.append(h)
                elif boardcopy[y][x] == 'M':
                    for r in genchildrenWM(y,x,boardcopy,'M'):
                        children.append(r)
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
        for o in range(pos[sl].count('W')):
            eval=eval+5
        for o in range(pos[sl].count('M')):
            eval=eval-5
    return eval

def gameover(pos):
    evalX=0
    evalO=0
    for sl in range(len(pos)):
        for o in range(pos[sl].count('X')):
            evalX=evalX+1
        for o in range(pos[sl].count('W')):
            evalX=evalX+1
    for sl in range(len(pos)):
        for o in range(pos[sl].count('O')):
            evalO=evalO+1
        for o in range(pos[sl].count('M')):
            evalO=evalO+1
    if evalO==0:
        return True
    if evalX==0:
        return True
    else:
        return False

def verloren(pos,otherplayer1, otherplayer2):
    eval=0
    for sl in range(len(pos)):
        for o in range(pos[sl].count(otherplayer1)):
            eval=eval+1
        for p in range(pos[sl].count(otherplayer2)):
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
    if verloren(position, 'O','M') == True:
        return f
    elif verloren(position, 'X','W') == True:
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
    while not gameover(board) and not verloren(board, 'O','M') and not verloren(board, 'X','W'):
        turn =turn+1
        print(turn)
        printboard(board)
        player(board)
        printboard(board)
        if not gameover(board) and not verloren(board, 'O','M') and not verloren(board, 'X','W'):
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
    if verloren(board, 'X','W'):
        print(':( VERLOREN')
    elif verloren(board, 'O','M'):
        print(':) GEWONNEN')
    else:
        print(':l UNENTSCHIEDEN')

def damewerden(player,pos):
    if player=='O':
        for i in range(len(pos[0])):
            if pos[7][i]=='O':
                pos[7][i]='M'
    if player=='X':
        for i in range(len(pos[0])):
            if pos[0][i]=='X':
                pos[0][i]='W'

def schlagenmoeglichW(y,x,boar):
    moeglich=False
    for i in range(7):
        if y+2+i>7 or x+2+i>7:
            break
        if boar[y+1+i][x+1+i]=='X' or boar[y+1+i][x+1+i]=='W':
            break
        if boar[y+1+i][x+1+i]=='O' or boar[y+1+i][x+1+i]=='M':
            if boar[y+2+i][x+2+i]==' ':
                moeglich=True
                break
            else:
                break
    if not moeglich:
        for i in range(7):
            if y-2-i<0 or x+2+i>7:
                break
            if boar[y-1-i][x+1+i]=='X' or boar[y-1-i][x+1+i]=='W':
                break
            if boar[y-1-i][x+1+i]=='O' or boar[y-1-i][x+1+i]=='M':
                if boar[y-2-i][x+2+i]==' ':
                    moeglich=True
                    break
                else:
                    break
    if not moeglich:
        for i in range(7):
            if y-2-i<0 or x-2-i<0:
                break
            if boar[y-1-i][x-1-i]=='X' or boar[y-1-i][x-1-i]=='W':
                break
            if boar[y-1-i][x-1-i]=='O' or boar[y-1-i][x-1-i]=='M':
                if boar[y-2-i][x-2-i]==' ':
                    moeglich=True
                    break
                else:
                    break
    if not moeglich:
        for i in range(7):
            if y+2+i>7 or x-2-i<0:
                break
            if boar[y+1+i][x-1-i]=='X' or boar[y+1+i][x-1-i]=='W':
                break
            if boar[y+1+i][x-1-i]=='O' or boar[y+1+i][x-1-i]=='M':
                if boar[y+2+i][x-2-i]==' ':
                    moeglich=True
                    break
                else:
                    break
    return moeglich

def eingabeschlagenW(vy,vx,pos):
    esw.clear()
    korrekt=False
    try:
        zx = int(input('zu x: ')) - 1
        zy = int(input('zu y: ')) - 1
    except:
        print('EINGABE NICHT KORREKT')
        return False
    #
    if zx==vx and zy==vy:
        korrekt=True
    #
    if zy<8 and zy>-1 and zx<8 and zx>-1:
        #
        for i in range(7):
            if vy+2+i>7 or vx+2+i>7:
                break
            if pos[vy+1+i][vx+1+i]=='X' or pos[vy+1+i][vx+1+i]=='W':
                break
            if pos[vy+1+i][vx+1+i]=='O' or pos[vy+1+i][vx+1+i]=='M':
                if pos[vy+2+i][vx+2+i]==' ' and vy+2+i==zy and vx+2+i==zx:
                    oy=vy+1+i
                    ox=vx+1+i
                    korrekt=True
                    break
        if not korrekt:
            for i in range(7):
                if vy+2+i>7 or vx-2-i<0:
                    break
                if pos[vy+1+i][vx-1-i]=='X' or pos[vy+1+i][vx-1-i]=='W':
                    break
                if pos[vy+1+i][vx-1-i]=='O' or pos[vy+1+i][vx-1-i]=='M':
                    if pos[vy+2+i][vx-2-i]==' ' and vy+2+i==zy and vx-2-i==zx:
                        oy=vy+1+i
                        ox=vx-1-i
                        korrekt=True
                        break
        if not korrekt:
            for i in range(7):
                if vy-2-i<0 or vx-2-i<0:
                    break
                if pos[vy-1-i][vx-1-i]=='X' or pos[vy-1-i][vx-1-i]=='W':
                    break
                if pos[vy-1-i][vx-1-i]=='O' or pos[vy-1-i][vx-1-i]=='M':
                    if pos[vy-2-i][vx-2-i]==' ' and vy-2-i==zy and vx-2-i==zx:
                        oy=vy-1-i
                        ox=vx-1-i
                        korrekt=True
                        break
        if not korrekt:
            for i in range(7):
                if vy-2-i<0 or vx+2+i>7:
                    break
                if pos[vy-1-i][vx+1+i]=='X' or pos[vy-1-i][vx+1+i]=='W':
                    break
                if pos[vy-1-i][vx+1+i]=='O' or pos[vy-1-i][vx+1+i]=='M':
                    if pos[vy-2-i][vx+2+i]==' ' and vy-2-i==zy and vx+2+i==zx:
                        oy=vy-1-i
                        ox=vx+1+i
                        korrekt=True
                        break
        #
    if korrekt:
        esw.append(zy)
        esw.append(zx)
        esw.append(oy)
        esw.append(ox)
        return True
    else:
        print('EINGABE NICHT KORREKT')
        return False

def playerschlagenW(vy,vx,pos):
    if schlagenmoeglichW(vy,vx,pos):
        printboard(pos)
        while True:
            if eingabeschlagenW(vy,vx,pos)==True:
                break
            else:
                continue
        if vx==esw[1] and esw[0]==vy:
            pass
        else:
            zy=esw[0]
            zx=esw[1]
            oy=esw[2]
            ox=esw[3]
            pos[zy][zx]='W'
            pos[vy][vx]=' '
            pos[oy][ox]=' '
            playerschlagenW(zy,zx,pos)

def genchildrenWM(y,x,pos,player):
    childrenWM=[]
    boardcopy=copy.deepcopy(pos)
    schlagen=False
    if player=='M':
        for o in range(7):
            if y+1+o>7 or x+1+o>7:
                break
            if boardcopy[y+1+o][x+1+o]=='O' or boardcopy[y+1+o][x+1+o]=='M':
                break
            if boardcopy[y+1+o][x+1+o]=='X' or boardcopy[y+1+o][x+1+o]=='W':
                schlagen=True
            if boardcopy[y+1+o][x+1+o]==' ':
                boardcopy[y+1+o][x+1+o]='M'
                boardcopy[y][x]=' '
                childrenWM.append(boardcopy)
                boardcopy=copy.deepcopy(pos)
            if schlagen:
                if boardcopy[y+2+o][x+2+o]==' ':
                    boardcopy[y+2+o][x+2+o]='M'
                    boardcopy[y][x]=' '
                    boardcopy[y+1+o][x+1+o]=' '
                    childrenWM.append(boardcopy)
                    for r in genchildrenschlagenWM(y+2+o,x+2+o,boardcopy,'M'):
                        childrenWM.append(r)
                    boardcopy=copy.deepcopy(pos)
                    break
        for o in range(7):
            if y+1+o>7 or x-1-o<0:
                break
            if boardcopy[y+1+o][x-1-o]=='O' or boardcopy[y+1+o][x-1-o]=='M':
                break
            if boardcopy[y+1+o][x-1-o]=='X' or boardcopy[y+1+o][x-1-o]=='W':
                schlagen=True
            if boardcopy[y+1+o][x-1-o]==' ':
                boardcopy[y+1+o][x-1-o]='M'
                boardcopy[y][x]=' '
                childrenWM.append(boardcopy)
                boardcopy=copy.deepcopy(pos)
            if schlagen:
                if boardcopy[y+2+o][x-2-o]==' ':
                    boardcopy[y+2+o][x-2-o]='M'
                    boardcopy[y][x]=' '
                    boardcopy[y+1+o][x-1-o]=' '
                    childrenWM.append(boardcopy)
                    for r in genchildrenschlagenWM(y+2+o,x-2-o,boardcopy,'M'):
                        childrenWM.append(r)
                    boardcopy=copy.deepcopy(pos)
                    break
        for o in range(7):
            if y-1-o<0 or x-1-o<0:
                break
            if boardcopy[y-1-o][x-1-o]=='O' or boardcopy[y-1-o][x-1-o]=='M':
                break
            if boardcopy[y-1-o][x-1-o]=='X' or boardcopy[y-1-o][x-1-o]=='W':
                schlagen=True
            if boardcopy[y-1-o][x-1-o]==' ':
                boardcopy[y-1-o][x-1-o]='M'
                boardcopy[y][x]=' '
                childrenWM.append(boardcopy)
                boardcopy=copy.deepcopy(pos)
            if schlagen:
                if boardcopy[y-2-o][x-2-o]==' ':
                    boardcopy[y-2-o][x-2-o]='M'
                    boardcopy[y][x]=' '
                    boardcopy[y-1-o][x-1-o]=' '
                    childrenWM.append(boardcopy)
                    for r in genchildrenschlagenWM(y-2-o,x-2-o,boardcopy,'M'):
                        childrenWM.append(r)
                    boardcopy=copy.deepcopy(pos)
                    break
        for o in range(7):
            if y-1-o<0 or x+1+o>7:
                break
            if boardcopy[y-1-o][x+1+o]=='O' or boardcopy[y-1-o][x+1+o]=='M':
                break
            if boardcopy[y-1-o][x+1+o]=='X' or boardcopy[y-1-o][x+1+o]=='W':
                schlagen=True
            if boardcopy[y-1-o][x+1+o]==' ':
                boardcopy[y-1-o][x+1+o]='M'
                boardcopy[y][x]=' '
                childrenWM.append(boardcopy)
                boardcopy=copy.deepcopy(pos)
            if schlagen:
                if boardcopy[y-2-o][x+2+o]==' ':
                    boardcopy[y-2-o][x+2+o]='M'
                    boardcopy[y][x]=' '
                    boardcopy[y-1-o][x+1+o]=' '
                    childrenWM.append(boardcopy)
                    for r in genchildrenschlagenWM(y-2-o,x+2+o,boardcopy,'M'):
                        childrenWM.append(r)
                    boardcopy=copy.deepcopy(pos)
                    break
    elif player=='W':
        for o in range(7):
            if y+1+o>7 or x+1+o>7:
                break
            if boardcopy[y+1+o][x+1+o]=='X' or boardcopy[y+1+o][x+1+o]=='W':
                break
            if boardcopy[y+1+o][x+1+o]=='O' or boardcopy[y+1+o][x+1+o]=='M':
                schlagen=True
            if boardcopy[y+1+o][x+1+o]==' ':
                boardcopy[y+1+o][x+1+o]='W'
                boardcopy[y][x]=' '
                childrenWM.append(boardcopy)
                boardcopy=copy.deepcopy(pos)
            if schlagen:
                if boardcopy[y+2+o][x+2+o]==' ':
                    boardcopy[y+2+o][x+2+o]='W'
                    boardcopy[y][x]=' '
                    boardcopy[y+1+o][x+1+o]=' '
                    childrenWM.append(boardcopy)
                    for r in genchildrenschlagenWM(y+2+o,x+2+o,boardcopy,'W'):
                        childrenWM.append(r)
                    boardcopy=copy.deepcopy(pos)
                    break
        for o in range(7):
            if y+1+o>7 or x-1-o<0:
                break
            if boardcopy[y+1+o][x-1-o]=='X' or boardcopy[y+1+o][x-1-o]=='W':
                break
            if boardcopy[y+1+o][x-1-o]=='O' or boardcopy[y+1+o][x-1-o]=='M':
                schlagen=True
            if boardcopy[y+1+o][x-1-o]==' ':
                boardcopy[y+1+o][x-1-o]='W'
                boardcopy[y][x]=' '
                childrenWM.append(boardcopy)
                boardcopy=copy.deepcopy(pos)
            if schlagen:
                if boardcopy[y+2+o][x-2-o]==' ':
                    boardcopy[y+2+o][x-2-o]='W'
                    boardcopy[y][x]=' '
                    boardcopy[y+1+o][x-1-o]=' '
                    childrenWM.append(boardcopy)
                    for r in genchildrenschlagenWM(y+2+o,x-2-o,boardcopy,'W'):
                        childrenWM.append(r)
                    boardcopy=copy.deepcopy(pos)
                    break
        for o in range(7):
            if y-1-o<0 or x-1-o<0:
                break
            if boardcopy[y-1-o][x-1-o]=='X' or boardcopy[y-1-o][x-1-o]=='W':
                break
            if boardcopy[y-1-o][x-1-o]=='O' or boardcopy[y-1-o][x-1-o]=='M':
                schlagen=True
            if boardcopy[y-1-o][x-1-o]==' ':
                boardcopy[y-1-o][x-1-o]='W'
                boardcopy[y][x]=' '
                childrenWM.append(boardcopy)
                boardcopy=copy.deepcopy(pos)
            if schlagen:
                if boardcopy[y-2-o][x-2-o]==' ':
                    boardcopy[y-2-o][x-2-o]='W'
                    boardcopy[y][x]=' '
                    boardcopy[y-1-o][x-1-o]=' '
                    childrenWM.append(boardcopy)
                    for r in genchildrenschlagenWM(y-2-o,x-2-o,boardcopy,'W'):
                        childrenWM.append(r)
                    boardcopy=copy.deepcopy(pos)
                    break
        for o in range(7):
            if y-1-o<0 or x+1+o>7:
                break
            if boardcopy[y-1-o][x+1+o]=='X' or boardcopy[y-1-o][x+1+o]=='W':
                break
            if boardcopy[y-1-o][x+1+o]=='O' or boardcopy[y-1-o][x+1+o]=='M':
                schlagen=True
            if boardcopy[y-1-o][x+1+o]==' ':
                boardcopy[y-1-o][x+1+o]='W'
                boardcopy[y][x]=' '
                childrenWM.append(boardcopy)
                boardcopy=copy.deepcopy(pos)
            if schlagen:
                if boardcopy[y-2-o][x+2+o]==' ':
                    boardcopy[y-2-o][x+2+o]='W'
                    boardcopy[y][x]=' '
                    boardcopy[y-1-o][x+1+o]=' '
                    childrenWM.append(boardcopy)
                    for r in genchildrenschlagenWM(y-2-o,x+2+o,boardcopy,'W'):
                        childrenWM.append(r)
                    boardcopy=copy.deepcopy(pos)
                    break
    return childrenWM

def genchildrenschlagenWM(y,x,pos,player):
    childrensWM=[]
    boardcopy=copy.deepcopy(pos)
    if player=='M':
        for o in range(7):
            if y+2+o>7 or x+2+o>7:
                break
            if boardcopy[y+1+o][x+1+o]=='O' or boardcopy[y+1+o][x+1+o]=='M':
                break
            if boardcopy[y+1+o][x+1+o]=='X' or boardcopy[y+1+o][x+1+o]=='W':
                if boardcopy[y+2+o][x+2+o]==' ':
                    boardcopy[y+2+o][x+2+o]='M'
                    boardcopy[y+1+o][x+1+o]=' '
                    boardcopy[y][x]=' '
                    childrensWM.append(boardcopy)
                    genchildrenschlagenWM(y+2+o,x+2+o,boardcopy,'M')
                    boardcopy=copy.deepcopy(pos)
                    break
        for o in range(7):
            if y-2-o<0 or x+2+o>7:
                break
            if boardcopy[y-1-o][x+1+o]=='O' or boardcopy[y-1-o][x+1+o]=='M':
                break
            if boardcopy[y-1-o][x+1+o]=='X' or boardcopy[y-1-o][x+1+o]=='W':
                if boardcopy[y-2-o][x+2+o]==' ':
                    boardcopy[y-2-o][x+2+o]='M'
                    boardcopy[y-1-o][x+1+o]=' '
                    boardcopy[y][x]=' '
                    childrensWM.append(boardcopy)
                    genchildrenschlagenWM(y-2-o,x+2+o,boardcopy,'M')
                    boardcopy=copy.deepcopy(pos)
                    break
        for o in range(7):
            if y-2-o<0 or x-2-o<0:
                break
            if boardcopy[y-1-o][x-1-o]=='O' or boardcopy[y-1-o][x-1-o]=='M':
                break
            if boardcopy[y-1-o][x-1-o]=='X' or boardcopy[y-1-o][x-1-o]=='W':
                if boardcopy[y-2-o][x-2-o]==' ':
                    boardcopy[y-2-o][x-2-o]='M'
                    boardcopy[y-1-o][x-1-o]=' '
                    boardcopy[y][x]=' '
                    childrensWM.append(boardcopy)
                    genchildrenschlagenWM(y-2-o,x-2-o,boardcopy,'M')
                    boardcopy=copy.deepcopy(pos)
                    break
        for o in range(7):
            if y+2+o>8 or x-2-o<0:
                break
            if boardcopy[y+1+o][x-1-o]=='O' or boardcopy[y+1+o][x-1-o]=='M':
                break
            if boardcopy[y+1+o][x-1-o]=='X' or boardcopy[y+1+o][x-1-o]=='W':
                if boardcopy[y+2+o][x-2-o]==' ':
                    boardcopy[y+2+o][x-2-o]='M'
                    boardcopy[y+1+o][x-1-o]=' '
                    boardcopy[y][x]=' '
                    childrensWM.append(boardcopy)
                    genchildrenschlagenWM(y+2+o,x-2-o,boardcopy,'M')
                    boardcopy=copy.deepcopy(pos)
                    break
    if player=='W':
        for o in range(7):
            if y+2+o>7 or x+2+o>7:
                break
            if boardcopy[y+1+o][x+1+o]=='X' or boardcopy[y+1+o][x+1+o]=='W':
                break
            if boardcopy[y+1+o][x+1+o]=='O' or boardcopy[y+1+o][x+1+o]=='M':
                if boardcopy[y+2+o][x+2+o]==' ':
                    boardcopy[y+2+o][x+2+o]='W'
                    boardcopy[y+1+o][x+1+o]=' '
                    boardcopy[y][x]=' '
                    childrensWM.append(boardcopy)
                    genchildrenschlagenWM(y+2+o,x+2+o,boardcopy,'W')
                    boardcopy=copy.deepcopy(pos)
                    break
        for o in range(7):
            if y-2-o<0 or x+2+o>7:
                break
            if boardcopy[y-1-o][x+1+o]=='X' or boardcopy[y-1-o][x+1+o]=='W':
                break
            if boardcopy[y-1-o][x+1+o]=='O' or boardcopy[y-1-o][x+1+o]=='M':
                if boardcopy[y-2-o][x+2+o]==' ':
                    boardcopy[y-2-o][x+2+o]='W'
                    boardcopy[y-1-o][x+1+o]=' '
                    boardcopy[y][x]=' '
                    childrensWM.append(boardcopy)
                    genchildrenschlagenWM(y-2-o,x+2+o,boardcopy,'W')
                    boardcopy=copy.deepcopy(pos)
                    break
        for o in range(7):
            if y-2-o<0 or x-2-o<0:
                break
            if boardcopy[y-1-o][x-1-o]=='X' or boardcopy[y-1-o][x-1-o]=='W':
                break
            if boardcopy[y-1-o][x-1-o]=='O' or boardcopy[y-1-o][x-1-o]=='M':
                if boardcopy[y-2-o][x-2-o]==' ':
                    boardcopy[y-2-o][x-2-o]='W'
                    boardcopy[y-1-o][x-1-o]=' '
                    boardcopy[y][x]=' '
                    childrensWM.append(boardcopy)
                    genchildrenschlagenWM(y-2-o,x-2-o,boardcopy,'W')
                    boardcopy=copy.deepcopy(pos)
                    break
        for o in range(7):
            if y+2+o>8 or x-2-o<0:
                break
            if boardcopy[y+1+o][x-1-o]=='X' or boardcopy[y+1+o][x-1-o]=='W':
                break
            if boardcopy[y+1+o][x-1-o]=='O' or boardcopy[y+1+o][x-1-o]=='M':
                if boardcopy[y+2+o][x-2-o]==' ':
                    boardcopy[y+2+o][x-2-o]='W'
                    boardcopy[y+1+o][x-1-o]=' '
                    boardcopy[y][x]=' '
                    childrensWM.append(boardcopy)
                    genchildrenschlagenWM(y+2+o,x-2-o,boardcopy,'W')
                    boardcopy=copy.deepcopy(pos)
                    break
    return childrensWM

for i in genchildrenWM(1,5,board,'W'):
    printboard(i)

#yes: minimaxer,minimax,printboard,schlagenmoeglichX, genchildren, genchildrenschlagen, evaluatepos, verloren, gameovereingabe, eingabeschlagen, player, playerschlagen,
#no: damegenchildren, genchildrenschlagendame, positionsmatrix, 

