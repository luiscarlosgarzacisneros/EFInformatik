import copy
import time
import random
import math

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
     
#

def play():
    global turn
    while not verloren2(board, -1,-2) and not verloren2(board, 1,2):
        turn =turn+1
        print(turn)
        printboard(board)
        player(board)
        printboard(board)
        if not verloren2(board, -1,-2) and not verloren2(board, 1,2):
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
    if verloren2(board, 1,2):
        print(':( VERLOREN')
    elif verloren2(board, -1,-2):
        print(':) GEWONNEN')

#
e=[]
es=[]
esw=[]
ds=[]

def eingabeschlagen(pos,vy,vx):
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
   
#

def minimax(position, depth, maxplayer, alpha, beta):
    # X:maxplayer,spieler O:minplayer,computer
    # Spieler
    # alpha: best maxpl, beta: best minpl
    if maxplayer:
        player = 1
    else:
        player = -1

    # return
    if verloren1(position, -1,-2) == True:
        return evaluatepos(position,-1)
    elif verloren1(position, 1,2) == True:
        return evaluatepos(position,-1)
    elif depth == d:
        return evaluatepos(position,-1)
    children=genchildren(position, player)
    if children == [] and player==1:
        return -8888
    elif children == [] and player==-1:
        return +8888
    #
    if maxplayer:
        maxvalue = -100000000000
        for child in children:
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
        for child in children:
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

#

def keinezugmoeglichkeiten(pos,player):
    if genchildren(pos,player)==[]:
        return True
    else:
        return False

def verloren1(pos,playerf1, playerf2):
    eval=0
    for sl in range(len(pos)):
        for o in range(pos[sl].count(playerf1)):
            eval=eval+1
        for p in range(pos[sl].count(playerf2)):
            eval=eval+1
    if eval==0:
        return True
    else:
        return False

def verloren2(pos,playerf1, playerf2):
    eval=0
    for sl in range(len(pos)):
        for o in range(pos[sl].count(playerf1)):
            eval=eval+1
        for p in range(pos[sl].count(playerf2)):
            eval=eval+1
    if eval==0:
        return True
    elif keinezugmoeglichkeiten(pos,playerf1):
        return True
    else:
        return False

#

childrens=[]
childrensWM=[]

def genchildren(position, player):
    children1=[]
    children2=[]
    boardcopy = copy.deepcopy(position)
    for y in range(8):
        for x in range(8):
            if player==1:
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
                    for h in genchildrenschlagen(y,x,boardcopy,1,True):
                        children1.append(h)
                #
                elif boardcopy[y][x] == 2:
                    for r in genchildrenWM(y,x,boardcopy,2):
                        children1.append(r)
            elif player==-1:
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
                    for h in genchildrenschlagen(y,x,boardcopy,-1,True):
                        children1.append(h)
                #
                elif boardcopy[y][x] == -2:
                    for r in genchildrenWM(y,x,boardcopy,-2):
                        children1.append(r)
    #
    global minimaxc
    minimaxc = minimaxc + 1
    #
    children1.extend(children2)
    #
    return children1

def genchildrenschlagen(y,x,position,player,new):
    global childrens
    if new:
        childrens=[]
    boardcopy = copy.deepcopy(position)
    if player==1:
        if y-2>-1 and x-2>-1 and  boardcopy[y-2][x-2]==0:
            if boardcopy[y-1][x-1]<0:
                boardcopy[y-1][x-1]=0
                boardcopy[y-2][x-2]=1
                boardcopy[y][x]=0
                if y-2==0:
                    boardcopy[y-2][x-2]=2
                childrens.append(copy.deepcopy(boardcopy))
                genchildrenschlagen(y-2,x-2,boardcopy,player,False)
                boardcopy = copy.deepcopy(position)
        if y-2>-1 and x+ 2<8 and  boardcopy[y-2][x+2]==0:
            if boardcopy[y-1][x+ 1]<0:
                boardcopy[y-1][x+1]=0
                boardcopy[y-2][x+2]=1
                boardcopy[y][x]=0
                if y-2==0:
                    boardcopy[y-2][x+2]=2
                childrens.append(copy.deepcopy(boardcopy))
                genchildrenschlagen(y-2,x+2,boardcopy,player,False)
                boardcopy = copy.deepcopy(position)
    elif player==-1:
        if y+ 2<8 and x-2>-1 and boardcopy[y+2][x-2]==0:
            if boardcopy[y+ 1][x-1]>0:
                boardcopy[y+1][x-1]=0
                boardcopy[y+2][x-2]=-1
                boardcopy[y][x]=0
                if y+2==7:
                    boardcopy[y+2][x-2]=-2
                childrens.append(copy.deepcopy(boardcopy))
                genchildrenschlagen(y+2,x-2,boardcopy,player,False)
                boardcopy = copy.deepcopy(position)
        if y+ 2<8 and x+ 2<8 and boardcopy[y+2][x+2]==0:
            if boardcopy[y+ 1][x+ 1]>0:
                boardcopy[y+1][x+1]=0
                boardcopy[y+2][x+2]=-1
                boardcopy[y][x]=0
                if y+2==7:
                    boardcopy[y+2][x+2]=-2
                childrens.append(copy.deepcopy(boardcopy))
                genchildrenschlagen(y+2,x+2,boardcopy,player,False)
                boardcopy = copy.deepcopy(position)
    childrens.reverse()
    return childrens

def genchildrenWM(y,x,pos,player):
    childrenWM1=[]
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
                    childrenWM1.append(boardcopy)
                    for r in genchildrenschlagenWM(y+2+o,x+2+o,boardcopy,-2,True):
                        childrenWM1.append(r)
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
                    childrenWM1.append(boardcopy)
                    for r in genchildrenschlagenWM(y+2+o,x-2-o,boardcopy,-2,True):
                        childrenWM1.append(r)
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
                    childrenWM1.append(boardcopy)
                    for r in genchildrenschlagenWM(y-2-o,x-2-o,boardcopy,-2,True):
                        childrenWM1.append(r)
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
                    if not x+2+o>7:               
                        schlagen=True
            if boardcopy[y-1-o][x+1+o]==0:
                boardcopy[y-1-o][x+1+o]=-2
                boardcopy[y][x]=0               
                childrenWM2.append(boardcopy)
                boardcopy=copy.deepcopy(pos)
            if schlagen:
                if boardcopy[y-2-o][x+2+o]==0:
                    boardcopy[y-2-o][x+2+o]=-2
                    boardcopy[y][x]=0
                    boardcopy[y-1-o][x+1+o]=0
                    childrenWM1.append(boardcopy)
                    for r in genchildrenschlagenWM(y-2-o,x+2+o,boardcopy,-2,True):
                        childrenWM1.append(r)
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
                    childrenWM1.append(boardcopy)
                    for r in genchildrenschlagenWM(y+2+o,x+2+o,boardcopy,2,True):
                        childrenWM1.append(r)
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
                    childrenWM1.append(boardcopy)
                    for r in genchildrenschlagenWM(y+2+o,x-2-o,boardcopy,2,True):
                        childrenWM1.append(r)
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
                    childrenWM1.append(boardcopy)
                    for r in genchildrenschlagenWM(y-2-o,x-2-o,boardcopy,2,True):
                        childrenWM1.append(r)
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
                    childrenWM1.append(boardcopy)
                    for r in genchildrenschlagenWM(y-2-o,x+2+o,boardcopy,2,True):
                        childrenWM1.append(r)
                    boardcopy=copy.deepcopy(pos)
                    schlagen=False
                    break
                else:
                    break
    childrenWM1.extend(childrenWM2)
    return childrenWM1

def genchildrenschlagenWM(y,x,pos,player,new):
    global childrensWM
    if new:
        childrensWM=[]
    #
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
                    genchildrenschlagenWM(y+2+o,x+2+o,boardcopy,-2,False)
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
                    genchildrenschlagenWM(y-2-o,x+2+o,boardcopy,-2,False)
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
                    genchildrenschlagenWM(y-2-o,x-2-o,boardcopy,-2,False)
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
                    genchildrenschlagenWM(y+2+o,x-2-o,boardcopy,-2,False)
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
                    genchildrenschlagenWM(y+2+o,x+2+o,boardcopy,2,False)
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
                    genchildrenschlagenWM(y-2-o,x+2+o,boardcopy,2,False)
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
                    genchildrenschlagenWM(y-2-o,x-2-o,boardcopy,2,False)
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
                    genchildrenschlagenWM(y+2+o,x-2-o,boardcopy,2,False)
                    boardcopy=copy.deepcopy(pos)
                    break
                else:
                    break
    childrensWM.reverse()
    return childrensWM

#

def evaluatepos(pos,player):
    eval=0
    if player==1:
        anz_X=0
        anz_O=0
        anz_W=0
        anz_M=0
        for sl in range(len(pos)):
            for o in range(pos[sl].count(1)):
                eval=eval+9
                anz_X+=1
            for o in range(pos[sl].count(-1)):
                eval=eval-1
                anz_O+=1
            for o in range(pos[sl].count(2)):
                eval=eval+49
                anz_W+=1
            for o in range(pos[sl].count(-2)):
                eval=eval-51
                anz_M+=1
        if anz_X==0 and anz_W==0:
            eval=eval-8888
        elif anz_O and anz_M==0:
            eval=eval+8888
        return eval
    elif player==-1:
        anz_X=0
        anz_O=0
        anz_W=0
        anz_M=0
        for sl in range(len(pos)):
            for o in range(pos[sl].count(1)):
                eval=eval-11
                anz_X+=1
            for o in range(pos[sl].count(-1)):
                eval=eval+9
                anz_O+=1
            for o in range(pos[sl].count(2)):
                eval=eval-51
                anz_W+=1
            for o in range(pos[sl].count(-2)):
                eval=eval+49
                anz_M+=1
        if anz_X==0 and anz_W==0:
            eval=eval+8888
        elif anz_O and anz_M==0:
            eval=eval-8888
        return eval

#

play()

#wenn klar gewonnen dann d -2 odr so