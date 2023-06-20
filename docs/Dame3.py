import copy
import time
import random

board = [
    [0,-1,0,-1,0,-1,0,-1],
    [-1,0,-1,0,-1,0,-1,0],
    [0,-1,0,-1,0,-1,0,-1],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0],
    
]
#
minimaxc = 0
d = 6
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
            if board[i][j]==-1:
                print('O', end='')
            elif board[i][j]==1:
                print('X', end='')
            elif board[i][j]==-2:
                print('M', end='')
            elif board[i][j]==2:
                print('W', end='')
            else:
                print(' ', end='')
            print(' I ', end='')
        print(i + 1)
        print('---------------------------------')

def schlagenmoeglichX(y,x,boar):
    r=False
    if y-2>-1 and x-2>-1:
        if boar[y-2][x-2]==0:
            if boar[y-1][x-1]<0:
                r=True
    if y-2>-1 and x+2<8:
        if boar[y-2][x+2]==0:
            if boar[y-1][x+1]<0:
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
        if zy==vy-1 and zx==vx-1 and pos[vy][vx]==1 and pos[zy][zx]==0:
            korrekt=True
        if not korrekt:
            if zy==vy-1 and zx==vx+1 and pos[vy][vx]==1 and pos[zy][zx]==0:
                korrekt=True
        #
        if not korrekt:
            if zy==vy-2 and zx==vx-2 and pos[vy][vx]==1 and pos[zy][zx]==0:
                if pos[vy-1][vx-1]<0:
                    korrekt=True
        if not korrekt:
            if zy==vy-2 and zx==vx+2 and pos[vy][vx]==1 and pos[zy][zx]==0:
                if pos[vy-1][vx+1]<0:
                    korrekt=True
        #
        ds.clear()
        if pos[vy][vx]==2:
            schlagen=False
            for i in range(7):
                if vy-1-i<0 or vx-1-i<0:
                    break
                if pos[vy-1-i][vx-1-i]>0:
                    break
                if pos[vy-1-i][vx-1-i]<0:
                    schlagen=True
                if pos[vy-1-i][vx-1-i]==0 and vy-1-i==zy and vx-1-i==zx:
                    korrekt=True
                    break
                if schlagen:
                    if vy-2-i==zy and vx-2-i==zx and pos[vy-2-i][vx-2-i]==0:
                        korrekt=True
                        ds.append(vy-1-i)
                        ds.append(vx-1-i)
                        break
                    break
        if not korrekt:
            if pos[vy][vx]==2:
                schlagen=False
                for i in range(7):
                    if vy+1+i>7 or vx+1+i>7:
                        break
                    if pos[vy+1+i][vx+1+i]>0:
                        break
                    if pos[vy+1+i][vx+1+i]<0:
                        schlagen=True
                    if pos[vy+1+i][vx+1+i]==0 and vy+1+i==zy and vx+1+i==zx:
                        korrekt=True
                        break
                    if schlagen:
                        if vy+2+i==zy and vx+2+i==zx and pos[vy+2+i][vx+2+i]==0:
                            korrekt=True
                            ds.append(vy+1+i)
                            ds.append(vx+1+i)
                            break
                        break
        if not korrekt:
            if pos[vy][vx]==2:
                schlagen=False
                for i in range(7):
                    if vy+1+i>7 or vx-1-i<0:
                        break
                    if pos[vy+1+i][vx-1-i]>0:
                        break
                    if pos[vy+1+i][vx-1-i]<0:
                        schlagen=True
                    if pos[vy+1+i][vx-1-i]==0 and vy+1+i==zy and vx-1-i==zx:
                        korrekt=True
                        break
                    if schlagen:
                        if vy+2+i==zy and vx-2-i==zx and pos[vy+2+i][vx-2-i]==0:
                            korrekt=True
                            ds.append(vy+1+i)
                            ds.append(vx-1-i)
                            break
                        break
        if not korrekt:
            if pos[vy][vx]==2:
                schlagen=False
                for i in range(7):
                    if vy-1-i<0 or vx+1+i>7:
                        break
                    if pos[vy-1-i][vx+1+i]>0:
                        break
                    if pos[vy-1-i][vx+1+i]<0:
                        schlagen=True
                    if pos[vy-1-i][vx+1+i]==0 and vy-1-i==zy and vx+1+i==zx:
                        korrekt=True
                        break
                    if schlagen:
                        if vy-2-i==zy and vx+2+i==zx and pos[vy-2-i][vx+2+i]==0:
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
        if zy==vy-2 and zx==vx-2 and pos[vy][vx]==1 and pos[zy][zx]==0:
            if pos[vy-1][vx-1]<0:
                korrekt=True
        if zy==vy-2 and zx==vx+2 and pos[vy][vx]==1 and pos[zy][zx]==0:
            if pos[vy-1][vx+1]<0:
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
        if zy==vy-2 and zx==vx-2 and pos[vy][vx]==1 and pos[zy][zx]==0:
            if pos[vy-1][vx-1]<0:
                pos[vy][vx]=0
                pos[zy][zx]=1
                if zy==0:
                    pos[zy][zx]=2
                pos[vy-1][vx-1]=0
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

        if zy==vy-2 and zx==vx+2 and pos[vy][vx]==1 and pos[zy][zx]==0:
            if pos[vy-1][vx+1]<0:
                pos[vy][vx]=0
                pos[zy][zx]=1
                if zy==0:
                    pos[zy][zx]=2
                pos[vy-1][vx+1]=0
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
    if zy==vy-1 and zx==vx-1 and pos[vy][vx]==1 and pos[zy][zx]==0:
        pos[vy][vx]=0
        pos[zy][zx]=1
        if zy==0:
            pos[zy][zx]=2
    elif zy==vy-1 and zx==vx+1 and pos[vy][vx]==1 and pos[zy][zx]==0:
        pos[vy][vx]=0
        pos[zy][zx]=1
        if zy==0:
            pos[zy][zx]=2
    #schlagen.
    elif zy==vy-2 and zx==vx-2 and pos[vy][vx]==1 and pos[zy][zx]==0:
        if pos[vy-1][vx-1]<0:
            playerschlagen(vy,vx,zy,zx,pos)
            if zy==0:
                pos[zy][zx]=2
    elif zy==vy-2 and zx==vx+2 and pos[vy][vx]==1 and pos[zy][zx]==0:
        if pos[vy-1][vx+1]<0:
            playerschlagen(vy,vx,zy,zx,pos)
            if zy==0:
                pos[zy][zx]=2
    #W
    if pos[vy][vx]==2:
        try:
            if pos[ds[0]][ds[1]]<0:
                pos[vy][vx]=0
                pos[zy][zx]=2
                pos[ds[0]][ds[1]]=0
                if schlagenmoeglichW(zy,zx,pos):
                    playerschlagenW(zy,zx,pos)
        except:
            pos[vy][vx]=0
            pos[zy][zx]=2

def genchildrenschlagen(y,x,position,playerq):
    boardcopy = copy.deepcopy(position)
    if playerq==1:
        if y-2>-1 and x-2>-1 and  boardcopy[y-2][x-2]==0:
            if boardcopy[y-1][x-1]<0:
                boardcopy[y-1][x-1]=0
                boardcopy[y-2][x-2]=1
                boardcopy[y][x]=' '
                if y-2==0:
                    boardcopy[y-2][x-2]=2
                childrens.append(copy.deepcopy(boardcopy))
                genchildrenschlagen(y-2,x-2,boardcopy,playerq)
                boardcopy = copy.deepcopy(position)
        if y-2>-1 and x+ 2<8 and  boardcopy[y-2][x+2]==0:
            if boardcopy[y-1][x+ 1]<0:
                boardcopy[y-1][x+1]=0
                boardcopy[y-2][x+2]=1
                boardcopy[y][x]=0
                if y-2==0:
                    boardcopy[y-2][x+2]=2
                childrens.append(copy.deepcopy(boardcopy))
                genchildrenschlagen(y-2,x+2,boardcopy,playerq)
                boardcopy = copy.deepcopy(position)
        else:
            pass
    elif playerq==-1:
        if y+ 2<8 and x-2>-1 and boardcopy[y+2][x-2]==0:
            if boardcopy[y+ 1][x-1]>0:
                boardcopy[y+1][x-1]=0
                boardcopy[y+2][x-2]=-1
                boardcopy[y][x]=0
                if y+2==7:
                    boardcopy[y+2][x-2]=-2
                childrens.append(copy.deepcopy(boardcopy))
                genchildrenschlagen(y+2,x-2,boardcopy,playerq)
                boardcopy = copy.deepcopy(position)
        if y+ 2<8 and x+ 2<8 and boardcopy[y+2][x+2]==0:
            if boardcopy[y+ 1][x+ 1]>0:
                boardcopy[y+1][x+1]=0
                boardcopy[y+2][x+2]=-1
                boardcopy[y][x]=0
                if y+2==7:
                    boardcopy[y+2][x+2]=-2
                childrens.append(copy.deepcopy(boardcopy))
                genchildrenschlagen(y+2,x+2,boardcopy,playerq)
                boardcopy = copy.deepcopy(position)
        else:
            pass
    childrens.reverse()
    return childrens

def genchildren(position, playerq):
    children = []
    children1=[]
    children2=[]
    boardcopy = copy.deepcopy(position)
    y = 0
    for i in range(8):
        x = 0
        for j in range(8):
            if playerq==1:
                if boardcopy[y][x] == 1:
                    if y-1>-1 and x-1>-1 and boardcopy[y-1][x-1]==0:
                        boardcopy[y-1][x-1]=1
                        boardcopy[y][x]=0
                        if y-1==0:
                            boardcopy[y-1][x-1]=2
                            children1.append(boardcopy)
                        children2.append(boardcopy)
                        boardcopy = copy.deepcopy(position)
                    if y-1>-1 and x+ 1<8 and boardcopy[y-1][x+ 1]==0:
                        boardcopy[y-1][x+ 1]=1
                        boardcopy[y][x]=0
                        if y-1==0:
                            boardcopy[y-1][x+1]=2
                            children1.append(boardcopy)
                        children2.append(boardcopy)
                        boardcopy = copy.deepcopy(position)
                    else:
                        pass
                    #
                    childrens.clear()
                    for h in genchildrenschlagen(y,x,boardcopy,1):
                        children1.append(h)
                #
                elif boardcopy[y][x] == 2:
                    for r in genchildrenWM(y,x,boardcopy,2):
                        children1.append(r)
            elif playerq==-1:
                if boardcopy[y][x] == -1:
                    if y+ 1<8 and x-1>-1 and  boardcopy[y+ 1][x-1]==0:
                        boardcopy[y+1][x-1]=-1
                        boardcopy[y][x]=0
                        if y+1==7:
                            boardcopy[y+1][x-1]=-2
                            children1.append(boardcopy)
                        children2.append(boardcopy)
                        boardcopy = copy.deepcopy(position)
                    if y+ 1<8 and x+ 1<8 and boardcopy[y+ 1][x+ 1]==0:
                        boardcopy[y+ 1][x+ 1]=-1
                        boardcopy[y][x]=0
                        if y+1==7:
                            boardcopy[y+1][x+1]=-2
                            children1.append(boardcopy)
                        children2.append(boardcopy)
                        boardcopy = copy.deepcopy(position)
                    else:
                        pass
                    #
                    childrens.clear()
                    for h in genchildrenschlagen(y,x,boardcopy,-1):
                        children1.append(h)
                #
                elif boardcopy[y][x] == -2:
                    for r in genchildrenWM(y,x,boardcopy,-2):
                        children1.append(r)
            x = x + 1
        y = y + 1
    #
    global minimaxc
    minimaxc = minimaxc + 1
    #
    children.extend(children1)
    children.extend(children2)
    #
    return children

def evaluatepos(pos):
    eval=0
    for sl in range(len(pos)):
        for o in range(pos[sl].count(1)):
            eval=eval+1
        for o in range(pos[sl].count(-1)):
            eval=eval-1
        for o in range(pos[sl].count(2)):
            eval=eval+15
        for o in range(pos[sl].count(-2)):
            eval=eval-5
    if verloren(pos,1,2):
        eval=eval-8888
    if verloren(pos,-1,-2):
        eval=eval+8888
    return eval

def gameover(pos):
    evalX=0
    evalO=0
    for sl in range(len(pos)):
        for o in range(pos[sl].count(1)):
            evalX=evalX+1
        for o in range(pos[sl].count(2)):
            evalX=evalX+1
    for sl in range(len(pos)):
        for o in range(pos[sl].count(-1)):
            evalO=evalO+1
        for o in range(pos[sl].count(-2)):
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
        playerj = 1
    else:
        playerj = -1

    # return
    pos =copy.deepcopy(position)
    f=evaluatepos(pos)
    if verloren(position, -1,-2) == True:
        return f
    elif verloren(position, 1,2) == True:
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
    for firstgenchild in genchildren(boa, -1):
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
    while not gameover(board) and not verloren(board, -1,-2) and not verloren(board, 1,2) and not keinezugmoeglichkeiten(board,1) and not keinezugmoeglichkeiten(board,-1):
        turn =turn+1
        print(turn)
        printboard(board)
        player(board)
        printboard(board)
        if not gameover(board) and not verloren(board, -1,-2) and not verloren(board, 1,2) and not keinezugmoeglichkeiten(board,1) and not keinezugmoeglichkeiten(board,-1):
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
    if verloren(board, 1,2):
        print(':( VERLOREN')
    elif verloren(board, -1,-2):
        print(':) GEWONNEN')
    elif keinezugmoeglichkeiten(board,1):
        print(':( VERLOREN')
    elif keinezugmoeglichkeiten(board,-1):
        print(':) GEWONNEN')

def damewerden(player,pos):
    if player==-1:
        for i in range(len(pos[0])):
            if pos[7][i]==-1:
                pos[7][i]=-2
    if player==1:
        for i in range(len(pos[0])):
            if pos[0][i]==1:
                pos[0][i]=2

def schlagenmoeglichW(y,x,boar):
    moeglich=False
    for i in range(7):
        if y+2+i>7 or x+2+i>7:
            break
        if boar[y+1+i][x+1+i]>0:
            break
        if boar[y+1+i][x+1+i]<0:
            if boar[y+2+i][x+2+i]==0:
                moeglich=True
                break
            else:
                break
    if not moeglich:
        for i in range(7):
            if y-2-i<0 or x+2+i>7:
                break
            if boar[y-1-i][x+1+i]>0:
                break
            if boar[y-1-i][x+1+i]<0:
                if boar[y-2-i][x+2+i]==0:
                    moeglich=True
                    break
                else:
                    break
    if not moeglich:
        for i in range(7):
            if y-2-i<0 or x-2-i<0:
                break
            if boar[y-1-i][x-1-i]>0:
                break
            if boar[y-1-i][x-1-i]<0:
                if boar[y-2-i][x-2-i]==0:
                    moeglich=True
                    break
                else:
                    break
    if not moeglich:
        for i in range(7):
            if y+2+i>7 or x-2-i<0:
                break
            if boar[y+1+i][x-1-i]>0:
                break
            if boar[y+1+i][x-1-i]<0:
                if boar[y+2+i][x-2-i]==0:
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
            if pos[vy+1+i][vx+1+i]>0:
                break
            if pos[vy+1+i][vx+1+i]<0:
                if pos[vy+2+i][vx+2+i]==0 and vy+2+i==zy and vx+2+i==zx:
                    oy=vy+1+i
                    ox=vx+1+i
                    korrekt=True
                    break
        if not korrekt:
            for i in range(7):
                if vy+2+i>7 or vx-2-i<0:
                    break
                if pos[vy+1+i][vx-1-i]>0:
                    break
                if pos[vy+1+i][vx-1-i]<0:
                    if pos[vy+2+i][vx-2-i]==0 and vy+2+i==zy and vx-2-i==zx:
                        oy=vy+1+i
                        ox=vx-1-i
                        korrekt=True
                        break
        if not korrekt:
            for i in range(7):
                if vy-2-i<0 or vx-2-i<0:
                    break
                if pos[vy-1-i][vx-1-i]>0:
                    break
                if pos[vy-1-i][vx-1-i]<0:
                    if pos[vy-2-i][vx-2-i]==0 and vy-2-i==zy and vx-2-i==zx:
                        oy=vy-1-i
                        ox=vx-1-i
                        korrekt=True
                        break
        if not korrekt:
            for i in range(7):
                if vy-2-i<0 or vx+2+i>7:
                    break
                if pos[vy-1-i][vx+1+i]>0:
                    break
                if pos[vy-1-i][vx+1+i]<0:
                    if pos[vy-2-i][vx+2+i]==0 and vy-2-i==zy and vx+2+i==zx:
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
            pos[zy][zx]=2
            pos[vy][vx]=0
            pos[oy][ox]=0
            playerschlagenW(zy,zx,pos)

def genchildrenWM(y,x,pos,player):
    childrenWM=[]
    childrenWM2=[]
    boardcopy=copy.deepcopy(pos)
    schlagen=False
    if player==-2:
        for o in range(7):
            schlagen=False
            if y+1+o>7 or x+1+o>7:
                break
            if boardcopy[y+1+o][x+1+o]<0:
                break
            if boardcopy[y+1+o][x+1+o]>0:
                if not y+2+o>7:
                    if not x+2+o>7:
                        schlagen=True
            if boardcopy[y+1+o][x+1+o]==0:
                boardcopy[y+1+o][x+1+o]=-2
                boardcopy[y][x]=0
                childrenWM2.append(boardcopy)
                boardcopy=copy.deepcopy(pos)
            if schlagen:
                if boardcopy[y+2+o][x+2+o]==0:
                    boardcopy[y+2+o][x+2+o]=-2
                    boardcopy[y][x]=0
                    boardcopy[y+1+o][x+1+o]=0
                    childrenWM.append(boardcopy)
                    for r in genchildrenschlagenWM(y+2+o,x+2+o,boardcopy,-2):
                        childrenWM.append(r)
                    boardcopy=copy.deepcopy(pos)
                    schlagen=False
                    break
                else:
                    break
        for o in range(7):
            schlagen=False
            if y+1+o>7 or x-1-o<0:
                break
            if boardcopy[y+1+o][x-1-o]<0:
                break
            if boardcopy[y+1+o][x-1-o]>0:
                if not y+2+o>7:
                    if not x-2-o<0:
                        schlagen=True
            if boardcopy[y+1+o][x-1-o]==0:
                boardcopy[y+1+o][x-1-o]=-2
                boardcopy[y][x]=0
                childrenWM2.append(boardcopy)
                boardcopy=copy.deepcopy(pos)
            if schlagen:
                if boardcopy[y+2+o][x-2-o]==0:
                    boardcopy[y+2+o][x-2-o]=-2
                    boardcopy[y][x]=0
                    boardcopy[y+1+o][x-1-o]=0
                    childrenWM.append(boardcopy)
                    for r in genchildrenschlagenWM(y+2+o,x-2-o,boardcopy,-2):
                        childrenWM.append(r)
                    boardcopy=copy.deepcopy(pos)
                    schlagen=False
                    break
                else:
                    break
        for o in range(7):
            schlagen=False
            if y-1-o<0 or x-1-o<0:
                break
            if boardcopy[y-1-o][x-1-o]<0:
                break
            if boardcopy[y-1-o][x-1-o]>0:
                if y-2-o>-1:
                    if x-2-o>-1: 
                        schlagen=True
            if boardcopy[y-1-o][x-1-o]==0:
                boardcopy[y-1-o][x-1-o]=-2
                boardcopy[y][x]=0
                childrenWM2.append(boardcopy)
                boardcopy=copy.deepcopy(pos)
            if schlagen:
                if boardcopy[y-2-o][x-2-o]==0:
                    boardcopy[y-2-o][x-2-o]=-2
                    boardcopy[y][x]=0
                    boardcopy[y-1-o][x-1-o]=0
                    childrenWM.append(boardcopy)
                    for r in genchildrenschlagenWM(y-2-o,x-2-o,boardcopy,-2):
                        childrenWM.append(r)
                    boardcopy=copy.deepcopy(pos)
                    schlagen=False
                    break
                else:
                    break
        for o in range(7):
            schlagen=False
            if y-1-o<0 or x+1+o>7:
                break
            if boardcopy[y-1-o][x+1+o]<0:
                break
            if boardcopy[y-1-o][x+1+o]>0:
                if y-2-o>-1:
                    if not x+2+o>7:               #????????
                        schlagen=True
            if boardcopy[y-1-o][x+1+o]==0:
                boardcopy[y-1-o][x+1+o]=-2
                boardcopy[y][x]=0               #????????
                childrenWM2.append(boardcopy)
                boardcopy=copy.deepcopy(pos)
            if schlagen:
                if boardcopy[y-2-o][x+2+o]==0:
                    boardcopy[y-2-o][x+2+o]=-2
                    boardcopy[y][x]=0
                    boardcopy[y-1-o][x+1+o]=0
                    childrenWM.append(boardcopy)
                    for r in genchildrenschlagenWM(y-2-o,x+2+o,boardcopy,-2):
                        childrenWM.append(r)
                    boardcopy=copy.deepcopy(pos)
                    schlagen=False
                    break
                else:
                    break
    elif player==2:
        schlagen=False
        for o in range(7):
            if y+1+o>7 or x+1+o>7:
                break
            if boardcopy[y+1+o][x+1+o]>0:
                break
            if boardcopy[y+1+o][x+1+o]<0:
                if not y+2+o>7:
                    if not x+2+o>7:
                        schlagen=True
            if boardcopy[y+1+o][x+1+o]==0:
                boardcopy[y+1+o][x+1+o]=2
                boardcopy[y][x]=0
                childrenWM2.append(boardcopy)
                boardcopy=copy.deepcopy(pos)
            if schlagen:
                if boardcopy[y+2+o][x+2+o]==0:
                    boardcopy[y+2+o][x+2+o]=2
                    boardcopy[y][x]=0
                    boardcopy[y+1+o][x+1+o]=0
                    childrenWM.append(boardcopy)
                    for r in genchildrenschlagenWM(y+2+o,x+2+o,boardcopy,2):
                        childrenWM.append(r)
                    boardcopy=copy.deepcopy(pos)
                    schlagen=False
                    break
                else:
                    break
        for o in range(7):
            schlagen=False
            if y+1+o>7 or x-1-o<0:
                break
            if boardcopy[y+1+o][x-1-o]>0:
                break
            if boardcopy[y+1+o][x-1-o]<0:
                if not y+2+o>7:
                    if not x-2-o<0:
                        schlagen=True
            if boardcopy[y+1+o][x-1-o]==0:
                boardcopy[y+1+o][x-1-o]=2
                boardcopy[y][x]=0
                childrenWM2.append(boardcopy)
                boardcopy=copy.deepcopy(pos)
            if schlagen:
                if boardcopy[y+2+o][x-2-o]==0:
                    boardcopy[y+2+o][x-2-o]=2
                    boardcopy[y][x]=0
                    boardcopy[y+1+o][x-1-o]=0
                    childrenWM.append(boardcopy)
                    for r in genchildrenschlagenWM(y+2+o,x-2-o,boardcopy,2):
                        childrenWM.append(r)
                    boardcopy=copy.deepcopy(pos)
                    schlagen=False
                    break
                else:
                    break
        for o in range(7):
            schlagen=False
            if y-1-o<0 or x-1-o<0:
                break
            if boardcopy[y-1-o][x-1-o]>0:
                break
            if boardcopy[y-1-o][x-1-o]<0:
                if not y-2-o<0:
                    if not x-2-o<0: 
                        schlagen=True
            if boardcopy[y-1-o][x-1-o]==0:
                boardcopy[y-1-o][x-1-o]=2
                boardcopy[y][x]=0
                childrenWM2.append(boardcopy)
                boardcopy=copy.deepcopy(pos)
            if schlagen:
                if boardcopy[y-2-o][x-2-o]==0:
                    boardcopy[y-2-o][x-2-o]=2
                    boardcopy[y][x]=0
                    boardcopy[y-1-o][x-1-o]=0
                    childrenWM.append(boardcopy)
                    for r in genchildrenschlagenWM(y-2-o,x-2-o,boardcopy,2):
                        childrenWM.append(r)
                    boardcopy=copy.deepcopy(pos)
                    schlagen=False
                    break
                else:
                    break
        for o in range(7):
            schlagen=False
            if y-1-o<0 or x+1+o>7:
                break
            if boardcopy[y-1-o][x+1+o]>0:
                break
            if boardcopy[y-1-o][x+1+o]<0:
                if not y-2-o<0:
                    if not x+2+o>7:
                        schlagen=True
            if boardcopy[y-1-o][x+1+o]==0:
                boardcopy[y-1-o][x+1+o]=2
                boardcopy[y][x]=0
                childrenWM2.append(boardcopy)
                boardcopy=copy.deepcopy(pos)
            if schlagen:
                if boardcopy[y-2-o][x+2+o]==0:
                    boardcopy[y-2-o][x+2+o]=2
                    boardcopy[y][x]=0
                    boardcopy[y-1-o][x+1+o]=0
                    childrenWM.append(boardcopy)
                    for r in genchildrenschlagenWM(y-2-o,x+2+o,boardcopy,2):
                        childrenWM.append(r)
                    boardcopy=copy.deepcopy(pos)
                    schlagen=False
                    break
                else:
                    break
    childrenWM.extend(childrenWM2)
    return childrenWM

def genchildrenschlagenWM(y,x,pos,player):
    childrensWM=[]
    boardcopy=copy.deepcopy(pos)
    if player==-2:
        for o in range(7):
            if y+2+o>7 or x+2+o>7:
                break
            if boardcopy[y+1+o][x+1+o]<0:
                break
            if boardcopy[y+1+o][x+1+o]>0:
                if boardcopy[y+2+o][x+2+o]==0:
                    boardcopy[y+2+o][x+2+o]=-2
                    boardcopy[y+1+o][x+1+o]=0
                    boardcopy[y][x]=0
                    childrensWM.append(boardcopy)
                    genchildrenschlagenWM(y+2+o,x+2+o,boardcopy,-2)
                    boardcopy=copy.deepcopy(pos)
                    break
                else:
                    break
        for o in range(7):
            if y-2-o<0 or x+2+o>7:
                break
            if boardcopy[y-1-o][x+1+o]<0:
                break
            if boardcopy[y-1-o][x+1+o]>0:
                if boardcopy[y-2-o][x+2+o]==0:
                    boardcopy[y-2-o][x+2+o]=-2
                    boardcopy[y-1-o][x+1+o]=0
                    boardcopy[y][x]=0
                    childrensWM.append(boardcopy)
                    genchildrenschlagenWM(y-2-o,x+2+o,boardcopy,-2)
                    boardcopy=copy.deepcopy(pos)
                    break
                else:
                    break
        for o in range(7):
            if y-2-o<0 or x-2-o<0:
                break
            if boardcopy[y-1-o][x-1-o]<0:
                break
            if boardcopy[y-1-o][x-1-o]>0:
                if boardcopy[y-2-o][x-2-o]==0:
                    boardcopy[y-2-o][x-2-o]=-2
                    boardcopy[y-1-o][x-1-o]=0
                    boardcopy[y][x]=0
                    childrensWM.append(boardcopy)
                    genchildrenschlagenWM(y-2-o,x-2-o,boardcopy,-2)
                    boardcopy=copy.deepcopy(pos)
                    break
                else:
                    break
        for o in range(7):
            if y+2+o>7 or x-2-o<0:
                break
            if boardcopy[y+1+o][x-1-o]<0:
                break
            if boardcopy[y+1+o][x-1-o]>0:
                if boardcopy[y+2+o][x-2-o]==0:
                    boardcopy[y+2+o][x-2-o]=-2
                    boardcopy[y+1+o][x-1-o]=0
                    boardcopy[y][x]=0
                    childrensWM.append(boardcopy)
                    genchildrenschlagenWM(y+2+o,x-2-o,boardcopy,-2)
                    boardcopy=copy.deepcopy(pos)
                    break
                else:
                    break
    if player==2:
        for o in range(7):
            if y+2+o>7 or x+2+o>7:
                break
            if boardcopy[y+1+o][x+1+o]>0:
                break
            if boardcopy[y+1+o][x+1+o]<0:
                if boardcopy[y+2+o][x+2+o]==0:
                    boardcopy[y+2+o][x+2+o]=2
                    boardcopy[y+1+o][x+1+o]=0
                    boardcopy[y][x]=0
                    childrensWM.append(boardcopy)
                    genchildrenschlagenWM(y+2+o,x+2+o,boardcopy,2)
                    boardcopy=copy.deepcopy(pos)
                    break
                else:
                    break
        for o in range(7):
            if y-2-o<0 or x+2+o>7:
                break
            if boardcopy[y-1-o][x+1+o]>0:
                break
            if boardcopy[y-1-o][x+1+o]<0:
                if boardcopy[y-2-o][x+2+o]==0:
                    boardcopy[y-2-o][x+2+o]=2
                    boardcopy[y-1-o][x+1+o]=0
                    boardcopy[y][x]=0
                    childrensWM.append(boardcopy)
                    genchildrenschlagenWM(y-2-o,x+2+o,boardcopy,2)
                    boardcopy=copy.deepcopy(pos)
                    break
                else:
                    break
        for o in range(7):
            if y-2-o<0 or x-2-o<0:
                break
            if boardcopy[y-1-o][x-1-o]>0:
                break
            if boardcopy[y-1-o][x-1-o]<0:
                if boardcopy[y-2-o][x-2-o]==0:
                    boardcopy[y-2-o][x-2-o]=2
                    boardcopy[y-1-o][x-1-o]=0
                    boardcopy[y][x]=0
                    childrensWM.append(boardcopy)
                    genchildrenschlagenWM(y-2-o,x-2-o,boardcopy,2)
                    boardcopy=copy.deepcopy(pos)
                    break
                else:
                    break
        for o in range(7):
            if y+2+o>7 or x-2-o<0:
                break
            if boardcopy[y+1+o][x-1-o]>0:
                break
            if boardcopy[y+1+o][x-1-o]<0:
                if boardcopy[y+2+o][x-2-o]==0:
                    boardcopy[y+2+o][x-2-o]=2
                    boardcopy[y+1+o][x-1-o]=0
                    boardcopy[y][x]=0
                    childrensWM.append(boardcopy)
                    genchildrenschlagenWM(y+2+o,x-2-o,boardcopy,2)
                    boardcopy=copy.deepcopy(pos)
                    break
                else:
                    break
    childrensWM.reverse()
    return childrensWM

def keinezugmoeglichkeiten(pos,player):
    if genchildren(pos,player)==[]:
        return True
    else:
        return False

play()

#positionsmatrix, genchildrenWM zuerst, depth mit value, endgame verbessern, verloren mehr punkte eval, crash???, keine zugmoeglichkeiten