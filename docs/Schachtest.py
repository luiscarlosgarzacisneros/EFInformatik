import copy
import time
import random

sfb=['T','L','X','Q','K','B',' ']
sfbnls=['T','L','X','Q','K','B']
sfs=['t','l','x','q','k','b',' ']
sfsnls=['t','l','x','q','k','b']
#
board = [
    ['T', 'L', 'X', 'Q', 'K', 'X', 'L','T'],
    ['B', 'B', 'B', 'B', 'B', 'B', 'B','B'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
    ['b', 'b', 'b', 'b', 'b', 'b', 'b','b'],
    ['t', 'l', 'x', 'q', 'k', 'x', 'l','t'],
]
#
ek=[
    [-3, -4, -4, -5, -5, -4, -4,-3],
    [-3, -4, -4, -5, -5, -4, -4,-3],
    [-3, -4, -4, -5, -5, -4, -4,-3],
    [-3, -4, -4, -5, -5, -4, -4,-3],
    [-2, -3, -3, -4, -4, -3, -3,-2],
    [-1, -2, -2, -2, -2, -2, -2,-1],
    [2, 2, 0, 0, 0, 0, 2,2],
    [2, 3, 1, 0, 0, 1, 3,2],
]
eK=[
    [2, 3, 1, 0, 0, 1, 3,2],
    [2, 2, 0, 0, 0, 0, 2,2],
    [-1, -2, -2, -2, -2, -2, -2,-1],
    [-2, -3, -3, -4, -4, -3, -3,-2],
    [-3, -4, -4, -5, -5, -4, -4,-3],
    [-3, -4, -4, -5, -5, -4, -4,-3],
    [-3, -4, -4, -5, -5, -4, -4,-3],
    [-3, -4, -4, -5, -5, -4, -4,-3],
]
eq=[

]
eQ=[]
eb=[]
eB=[]
ex=[]
eX=[]
et=[]
eT=[]
#
e=[]
minimaxc = 0
d = 4
nextmoves = []
scores = []
move = []
moves=[]
bestscores=[]
maxtime = 200000
turn=0
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
        #b
        if pos[vy][vx]=='b':
            #2nachv
            if vy==6 and pos[zy][zx]==' ' and pos[vy-1][vx]==' ' and vx==zx and zy==vy-2:
                korrekt=True
            #1nachv normal bew
            if pos[zy][zx]==' ' and vx==zx and zy==vy-1:
                korrekt=True
            #schlagen
            if pos[zy][zx] in sfbnls and zy==vy-1 and vx-1==zx:
                korrekt=True
            if pos[zy][zx] in sfbnls and zy==vy-1 and vx+1==zx:
                korrekt=True
        #k
        if pos[vy][vx]=='k':
            #vertikal
            if pos[zy][zx] in sfb and vx-1==zx and zy==vy:
                korrekt=True
            if pos[zy][zx] in sfb and vx+1==zx and zy==vy:
                korrekt=True
            #horizontal
            if pos[zy][zx] in sfb and vx==zx and zy==vy-1:
                korrekt=True
            if pos[zy][zx] in sfb and vx==zx and zy==vy+1:
                korrekt=True
            #diagonal
            if pos[zy][zx] in sfb and vx-1==zx and zy==vy-1:
                korrekt=True
            if pos[zy][zx] in sfb and vx+1==zx and zy==vy-1:
                korrekt=True
            if pos[zy][zx] in sfb and vx+1==zx and zy==vy+1:
                korrekt=True
            if pos[zy][zx] in sfb and vx-1==zx and zy==vy+1:
                korrekt=True
        #t 
        if pos[vy][vx]=='t':
            #vertikal
            if pos[zy][zx] in sfb and vx==zx:
                #nach unten
                if vy<zy:
                    pathclear=True
                    f=1
                    while True:
                        if vy+f==zy:
                            break
                        if pos[vy+f][vx]!=' ':
                            pathclear=False
                            break
                        f=f+1
                    if pathclear:
                        korrekt=True
                #nach oben
                if vy>zy:
                    pathclear=True
                    f=1
                    while True:
                        if vy-f==zy:
                            break
                        if pos[vy-f][vx]!=' ':
                            pathclear=False
                            break
                        f=f+1
                    if pathclear:
                        korrekt=True
            #horizontal
            if pos[zy][zx] in sfb and vy==zy:
                #nach rechts
                if vx<zx:
                    pathclear=True
                    f=1
                    while True:
                        if vx+f==zx:
                            break
                        if pos[vy][vx+f]!=' ':
                            pathclear=False
                            break
                        f=f+1
                    if pathclear:
                        korrekt=True
                #nach links
                if vx>zx:
                    pathclear=True
                    f=1
                    while True:
                        if vx-f==zx:
                            break
                        if pos[vy][vx-f]!=' ':
                            pathclear=False
                            break
                        f=f+1
                    if pathclear:
                        korrekt=True
        #x
        if pos[vy][vx]=='x' and pos[zy][zx] in sfb:
            pathclear=False
            for u in range(8):
                if zy>vy and zx>vx:
                    if vx+u+1==zx and vy+u+1==zy:
                        pathclear=True
                        break
                    if pos[vy+u+1][vx+u+1]!=' ':
                        break
                if zy<vy and zx>vx:
                    if vx+u+1==zx and vy-u-1==zy:
                        pathclear=True
                        break
                    if pos[vy-u-1][vx+u+1]!=' ':
                        break
                if zy>vy and zx<vx:
                    if vx-u-1==zx and vy+u+1==zy:
                        pathclear=True
                        break
                    if pos[vy+u+1][vx-1-u]!=' ':
                        break
                if zy<vy and zx<vx:
                    if vx-1-u==zx and vy-u-1==zy:
                        pathclear=True
                        break
                    if pos[vy-u-1][vx-u-1]!=' ':
                        break
            if pathclear:
                korrekt=True
        #q
        if pos[vy][vx]=='q' and pos[zy][zx] in sfb:
            pathcleart=False
            for u in range(8):
                if zy>vy and zx>vx:
                    if vx+u+1==zx and vy+u+1==zy:
                        pathcleart=True
                        break
                    if pos[vy+u+1][vx+u+1]!=' ':
                        break
                if zy<vy and zx>vx:
                    if vx+u+1==zx and vy-u-1==zy:
                        pathcleart=True
                        break
                    if pos[vy-u-1][vx+u+1]!=' ':
                        break
                if zy>vy and zx<vx:
                    if vx-u-1==zx and vy+u+1==zy:
                        pathcleart=True
                        break
                    if pos[vy+u+1][vx-1-u]!=' ':
                        break
                if zy<vy and zx<vx:
                    if vx-1-u==zx and vy-u-1==zy:
                        pathcleart=True
                        break
                    if pos[vy-u-1][vx-u-1]!=' ':
                        break
            if pathcleart:
                korrekt=True
            #vertikal
            if pos[zy][zx] in sfb and vx==zx:
                #nach unten
                if vy<zy:
                    pathclearl=True
                    f=1
                    while True:
                        if vy+f==zy:
                            break
                        if pos[vy+f][vx]!=' ':
                            pathclearl=False
                            break
                        f=f+1
                    if pathclearl:
                        korrekt=True
                #nach oben
                if vy>zy:
                    pathclearl=True
                    f=1
                    while True:
                        if vy-f==zy:
                            break
                        if pos[vy-f][vx]!=' ':
                            pathclearl=False
                            break
                        f=f+1
                    if pathclearl:
                        korrekt=True
            #horizontal
            if pos[zy][zx] in sfb and vy==zy:
                #nach rechts
                if vx<zx:
                    pathclearl=True
                    f=1
                    while True:
                        if vx+f==zx:
                            break
                        if pos[vy][vx+f]!=' ':
                            pathclearl=False
                            break
                        f=f+1
                    if pathclearl:
                        korrekt=True
                #nach links
                if vx>zx:
                    pathclearl=True
                    f=1
                    while True:
                        if vx-f==zx:
                            break
                        if pos[vy][vx-f]!=' ':
                            pathclearl=False
                            break
                        f=f+1
                    if pathclearl:
                        korrekt=True
        #l
        if pos[vy][vx]=='l' and pos[zy][zx] in sfb:
            if zy==vy-2 and zx==vx+1:
                korrekt=True
            if zy==vy-2 and zx==vx-1:
                korrekt=True
            if zy==vy+2 and zx==vx+1:
                korrekt=True
            if zy==vy+2 and zx==vx-1:
                korrekt=True
            if zy==vy+1 and zx==vx+2:
                korrekt=True
            if zy==vy-1 and zx==vx+2:
                korrekt=True
            if zy==vy+1 and zx==vx-2:
                korrekt=True
            if zy==vy-1 and zx==vx-2:
                korrekt=True

    if korrekt:
        e.append(vy)
        e.append(vx)
        e.append(zy)
        e.append(zx)
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
    pos[zy][zx]=pos[vy][vx]
    pos[vy][vx]=' '

def genchildren(position, playerk):
    children = []
    boardcopy = copy.deepcopy(position)
    #
    if playerk=='k':
        y = 0
        for i in range(8):
            x = 0
            for j in range(8):
                if boardcopy[y][x]=='b':
                    for h in gcBb(y,x,boardcopy,'b'):
                        children.append(h)
                if boardcopy[y][x]=='k':
                    for h in gcKk(y,x,boardcopy,'k'):
                        children.append(h)
                if boardcopy[y][x]=='t':
                    for h in gcTt(y,x,boardcopy,"t"):
                        children.append(h)
                if boardcopy[y][x]=='x':
                    for h in gcXx(y,x,boardcopy,"x"):
                        children.append(h)
                if boardcopy[y][x]=='q':
                    for h in gcQq(y,x,boardcopy,"q"):
                        children.append(h)
                if boardcopy[y][x]=='l':
                    for h in gcLl(y,x,boardcopy,'l'):
                        children.append(h)

                x = x + 1
            y = y + 1
    if playerk=='K':
        y = 0
        for i in range(8):
            x = 0
            for j in range(8):
                if boardcopy[y][x]=='B':
                    for h in gcBb(y,x,boardcopy,'B'):
                        children.append(h)
                if boardcopy[y][x]=='K':
                    for h in gcKk(y,x,boardcopy,'K'):
                        children.append(h)
                if boardcopy[y][x]=='T':
                    for h in gcTt(y,x,boardcopy,'T'):
                        children.append(h)
                if boardcopy[y][x]=='X':
                    for h in gcXx(y,x,boardcopy,"X"):
                        children.append(h)
                if boardcopy[y][x]=='Q':
                    for h in gcQq(y,x,boardcopy,"Q"):
                        children.append(h)
                if boardcopy[y][x]=='L':
                    for h in gcLl(y,x,boardcopy,'L'):
                        children.append(h)

                x = x + 1
            y = y + 1
    #
    global minimaxc
    minimaxc = minimaxc + 1
    #
    return children

def gcKk(y,x,pos,player):
    boardc=copy.deepcopy(pos)
    childrenK= []
    if player=='K':
        if y+1<8 and x+1<8:
            if boardc[y+1][x+1] in sfs:
                boardc[y][x]=' '
                boardc[y+1][x+1]='K'
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
        if y+1<8 and x-1>-1:
            if boardc[y+1][x-1] in sfs:
                boardc[y][x]=' '
                boardc[y+1][x-1]='K'
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
        if y-1>-1 and x+1<8:
            if boardc[y-1][x+1] in sfs:
                boardc[y][x]=' '
                boardc[y-1][x+1]='K'
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
        if y-1>-1 and x+1<8:
            if boardc[y-1][x-1] in sfs:
                boardc[y][x]=' '
                boardc[y-1][x-1]='K'
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
        if x+1<8:
            if boardc[y][x+1] in sfs:
                boardc[y][x]=' '
                boardc[y][x+1]='K'
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
        if x-1>-1:
            if boardc[y][x-1] in sfs:
                boardc[y][x]=' '
                boardc[y][x-1]='K'
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
        if y+1<8:
            if boardc[y+1][x] in sfs:
                boardc[y][x]=' '
                boardc[y+1][x]='K'
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
        if y-1>-1:
            if boardc[y-1][x] in sfs:
                boardc[y][x]=' '
                boardc[y-1][x]='K'
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
    if player=='k':
        if y+1<8 and x+1<8:
            if boardc[y+1][x+1] in sfb:
                boardc[y][x]=' '
                boardc[y+1][x+1]='k'
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
        if y+1<8 and x-1>-1:
            if boardc[y+1][x-1] in sfb:
                boardc[y][x]=' '
                boardc[y+1][x-1]='k'
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
        if y-1>-1 and x+1<8:
            if boardc[y-1][x+1] in sfb:
                boardc[y][x]=' '
                boardc[y-1][x+1]='k'
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
        if y-1>-1 and x+1<8:
            if boardc[y-1][x-1] in sfb:
                boardc[y][x]=' '
                boardc[y-1][x-1]='k'
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
        if x+1<8:
            if boardc[y][x+1] in sfb:
                boardc[y][x]=' '
                boardc[y][x+1]='k'
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
        if x-1>-1:
            if boardc[y][x-1] in sfb:
                boardc[y][x]=' '
                boardc[y][x-1]='k'
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
        if y+1<8:
            if boardc[y+1][x] in sfb:
                boardc[y][x]=' '
                boardc[y+1][x]='k'
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
        if y-1>-1:
            if boardc[y-1][x] in sfb:
                boardc[y][x]=' '
                boardc[y-1][x]='k'
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
    return childrenK

def gcLl(y,x,pos,player):
    boardc=copy.deepcopy(pos)
    childrenL= []
    if player=='L':
        if y-2>-1 and x+1<8:
            if boardc[y-2][x+1] in sfs:
                boardc[y][x]=' '
                boardc[y-2][x+1]='L'
                childrenL.append(boardc)
                boardc=copy.deepcopy(pos)
        if y-2>-1 and x-1>-1:
            if boardc[y-2][x-1] in sfs:
                boardc[y][x]=' '
                boardc[y-2][x-1]='L'
                childrenL.append(boardc)
                boardc=copy.deepcopy(pos)
        if y+2<8 and x+1<8:
            if boardc[y+2][x+1] in sfs:
                boardc[y][x]=' '
                boardc[y+2][x+1]='L'
                childrenL.append(boardc)
                boardc=copy.deepcopy(pos)
        if y+2<8 and x-1>-1:
            if boardc[y+2][x-1] in sfs:
                boardc[y][x]=' '
                boardc[y+2][x-1]='L'
                childrenL.append(boardc)
                boardc=copy.deepcopy(pos)
        if y+1<8 and x+2<8:
            if boardc[y+1][x+2] in sfs:
                boardc[y][x]=' '
                boardc[y+1][x+2]='L'
                childrenL.append(boardc)
                boardc=copy.deepcopy(pos)
        if y-1>-1 and x+2<8:
            if boardc[y-1][x+2] in sfs:
                boardc[y][x]=' '
                boardc[y-1][x+2]='L'
                childrenL.append(boardc)
                boardc=copy.deepcopy(pos)
        if y+1<8 and x-2>-1:
            if boardc[y+1][x-2] in sfs:
                boardc[y][x]=' '
                boardc[y+1][x-2]='L'
                childrenL.append(boardc)
                boardc=copy.deepcopy(pos)
        if y-1>-1 and x-2>-1:
            if boardc[y-1][x-2] in sfs:
                boardc[y][x]=' '
                boardc[y-1][x-2]='L'
                childrenL.append(boardc)
                boardc=copy.deepcopy(pos)
    if player=='l':
        if y-2>-1 and x+1<8:
            if boardc[y-2][x+1] in sfb:
                boardc[y][x]=' '
                boardc[y-2][x+1]='l'
                childrenL.append(boardc)
                boardc=copy.deepcopy(pos)
        if y-2>-1 and x-1>-1:
            if boardc[y-2][x-1] in sfb:
                boardc[y][x]=' '
                boardc[y-2][x-1]='l'
                childrenL.append(boardc)
                boardc=copy.deepcopy(pos)
        if y+2<8 and x+1<8:
            if boardc[y+2][x+1] in sfb:
                boardc[y][x]=' '
                boardc[y+2][x+1]='l'
                childrenL.append(boardc)
                boardc=copy.deepcopy(pos)
        if y+2<8 and x-1>-1:
            if boardc[y+2][x-1] in sfb:
                boardc[y][x]=' '
                boardc[y+2][x-1]='l'
                childrenL.append(boardc)
                boardc=copy.deepcopy(pos)
        if y+1<8 and x+2<8:
            if boardc[y+1][x+2] in sfb:
                boardc[y][x]=' '
                boardc[y+1][x+2]='l'
                childrenL.append(boardc)
                boardc=copy.deepcopy(pos)
        if y-1>-1 and x+2<8:
            if boardc[y-1][x+2] in sfb:
                boardc[y][x]=' '
                boardc[y-1][x+2]='l'
                childrenL.append(boardc)
                boardc=copy.deepcopy(pos)
        if y+1<8 and x-2>-1:
            if boardc[y+1][x-2] in sfb:
                boardc[y][x]=' '
                boardc[y+1][x-2]='l'
                childrenL.append(boardc)
                boardc=copy.deepcopy(pos)
        if y-1>-1 and x-2>-1:
            if boardc[y-1][x-2] in sfb:
                boardc[y][x]=' '
                boardc[y-1][x-2]='l'
                childrenL.append(boardc)
                boardc=copy.deepcopy(pos)

    return childrenL

def gcTt(y,x,pos,player):
    boardc=copy.deepcopy(pos)
    childrenT= []
    if player=='T':
        for i in range(7):
            if x+i+1<8:
                if boardc[y][x+i+1] in sfs:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=' '
                    boardc[y][x+i+1]='T'
                    childrenT.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y][x+i+1]!=' ':
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y+i+1<8:
                if boardc[y+i+1][x] in sfs:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=' '
                    boardc[y+i+1][x]='T'
                    childrenT.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y+i+1][x]!=' ':
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if x-i-1>-1:
                if boardc[y][x-i-1] in sfs:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=' '
                    boardc[y][x-i-1]='T'
                    childrenT.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y][x-i-1]!=' ':
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1:
                if boardc[y-i-1][x] in sfs:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=' '
                    boardc[y-i-1][x]='T'
                    childrenT.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y-i-1][x]!=" ":
                        break
                else:
                    break
            else:
                break
    if player=='t':
        for i in range(7):
            if x+i+1<8:
                if boardc[y][x+i+1] in sfb:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=' '
                    boardc[y][x+i+1]='t'
                    childrenT.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y][x+i+1]!=' ':
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y+i+1<8:
                if boardc[y+i+1][x] in sfb:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=' '
                    boardc[y+i+1][x]='t'
                    childrenT.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y+i+1][x]!=' ':
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if x-i-1>-1:
                if boardc[y][x-i-1] in sfb:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=' '
                    boardc[y][x-i-1]='t'
                    childrenT.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y][x-i-1]!=' ':
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1:
                if boardc[y-i-1][x] in sfb:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=' '
                    boardc[y-i-1][x]='t'
                    childrenT.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y-i-1][x]!=" ":
                        break
                else:
                    break
            else:
                break
    return childrenT

def gcXx(y,x,pos,player):
    boardc=copy.deepcopy(pos)
    childrenX= []
    if player=="X":
        for i in range(7):
            if x+i+1<8 and y+i+1<8:
                if boardc[y+i+1][x+i+1] in sfs:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=' '
                    boardc[y+i+1][x+i+1]='X'
                    childrenX.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y+i+1][x+i+1]!=' ':
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1 and x-i-1>-1:
                if boardc[y-i-1][x-i-1] in sfs:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=' '
                    boardc[y-i-1][x-i-1]='X'
                    childrenX.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y-i-1][x-i-1]!=' ':
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y+i+1<8 and x-i-1>-1:
                if boardc[y+i+1][x-i-1] in sfs:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=' '
                    boardc[y+i+1][x-i-1]='X'
                    childrenX.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y+i+1][x-i-1]!=' ':
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1 and x+i+1<8:
                if boardc[y-i-1][x+i+1] in sfs:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=' '
                    boardc[y-i-1][x+i+1]='X'
                    childrenX.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y-i-1][x+i+1]!=' ':
                        break
                else:
                    break
            else:
                break
    if player=="x":
        for i in range(7):
            if x+i+1<8 and y+i+1<8:
                if boardc[y+i+1][x+i+1] in sfb:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=' '
                    boardc[y+i+1][x+i+1]='x'
                    childrenX.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y+i+1][x+i+1]!=' ':
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1 and x-i-1>-1:
                if boardc[y-i-1][x-i-1] in sfb:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=' '
                    boardc[y-i-1][x-i-1]='x'
                    childrenX.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y-i-1][x-i-1]!=' ':
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y+i+1<8 and x-i-1>-1:
                if boardc[y+i+1][x-i-1] in sfb:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=' '
                    boardc[y+i+1][x-i-1]='x'
                    childrenX.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y+i+1][x-i-1]!=' ':
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1 and x+i+1<8:
                if boardc[y-i-1][x+i+1] in sfb:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=' '
                    boardc[y-i-1][x+i+1]='x'
                    childrenX.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y-i-1][x+i+1]!=' ':
                        break
                else:
                    break
            else:
                break
    return childrenX

def gcQq(y,x,pos,player):
    boardc=copy.deepcopy(pos)
    childrenQ= []
    if player=='Q':
        for i in range(7):
            if x+i+1<8:
                if boardc[y][x+i+1] in sfs:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=' '
                    boardc[y][x+i+1]='Q'
                    childrenQ.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y][x+i+1]!=' ':
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y+i+1<8:
                if boardc[y+i+1][x] in sfs:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=' '
                    boardc[y+i+1][x]='Q'
                    childrenQ.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y+i+1][x]!=' ':
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if x-i-1>-1:
                if boardc[y][x-i-1] in sfs:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=' '
                    boardc[y][x-i-1]='Q'
                    childrenQ.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y][x-i-1]!=' ':
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1:
                if boardc[y-i-1][x] in sfs:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=' '
                    boardc[y-i-1][x]='Q'
                    childrenQ.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y-i-1][x]!=" ":
                        break
                else:
                    break
            else:
                break
    if player=='q':
        for i in range(7):
            if x+i+1<8:
                if boardc[y][x+i+1] in sfb:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=' '
                    boardc[y][x+i+1]='q'
                    childrenQ.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y][x+i+1]!=' ':
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y+i+1<8:
                if boardc[y+i+1][x] in sfb:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=' '
                    boardc[y+i+1][x]='q'
                    childrenQ.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y+i+1][x]!=' ':
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if x-i-1>-1:
                if boardc[y][x-i-1] in sfb:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=' '
                    boardc[y][x-i-1]='q'
                    childrenQ.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y][x-i-1]!=' ':
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1:
                if boardc[y-i-1][x] in sfb:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=' '
                    boardc[y-i-1][x]='q'
                    childrenQ.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y-i-1][x]!=" ":
                        break
                else:
                    break
            else:
                break
    if player=="Q":
        for i in range(7):
            if x+i+1<8 and y+i+1<8:
                if boardc[y+i+1][x+i+1] in sfs:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=' '
                    boardc[y+i+1][x+i+1]='Q'
                    childrenQ.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y+i+1][x+i+1]!=' ':
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1 and x-i-1>-1:
                if boardc[y-i-1][x-i-1] in sfs:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=' '
                    boardc[y-i-1][x-i-1]='Q'
                    childrenQ.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y-i-1][x-i-1]!=' ':
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y+i+1<8 and x-i-1>-1:
                if boardc[y+i+1][x-i-1] in sfs:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=' '
                    boardc[y+i+1][x-i-1]='Q'
                    childrenQ.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y+i+1][x-i-1]!=' ':
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1 and x+i+1<8:
                if boardc[y-i-1][x+i+1] in sfs:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=' '
                    boardc[y-i-1][x+i+1]='Q'
                    childrenQ.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y-i-1][x+i+1]!=' ':
                        break
                else:
                    break
            else:
                break
    if player=="q":
        for i in range(7):
            if x+i+1<8 and y+i+1<8:
                if boardc[y+i+1][x+i+1] in sfb:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=' '
                    boardc[y+i+1][x+i+1]='q'
                    childrenQ.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y+i+1][x+i+1]!=' ':
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1 and x-i-1>-1:
                if boardc[y-i-1][x-i-1] in sfb:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=' '
                    boardc[y-i-1][x-i-1]='q'
                    childrenQ.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y-i-1][x-i-1]!=' ':
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y+i+1<8 and x-i-1>-1:
                if boardc[y+i+1][x-i-1] in sfb:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=' '
                    boardc[y+i+1][x-i-1]='q'
                    childrenQ.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y+i+1][x-i-1]!=' ':
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1 and x+i+1<8:
                if boardc[y-i-1][x+i+1] in sfb:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=' '
                    boardc[y-i-1][x+i+1]='q'
                    childrenQ.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y-i-1][x+i+1]!=' ':
                        break
                else:
                    break
            else:
                break
    return childrenQ

def gcBb(y,x,pos,player):
    boardc=copy.deepcopy(pos)
    childrenB= []
    if player=="B":
        if y==1 and boardc[y+2][x]==' ' and boardc[y+1][x]==' ':
            boardc[y][x]=' '
            boardc[y+2][x]='B'
            childrenB.append(boardc)
            boardc=copy.deepcopy(pos)
        if y+1<8:
            if boardc[y+1][x]==' ':
                boardc[y][x]=' '
                boardc[y+1][x]='B'
                if y+1==7:
                    boardc[y+1][x]='Q'
                childrenB.append(boardc)
                boardc=copy.deepcopy(pos)
        if x-1>-1 and y+1<8:
            if boardc[y+1][x-1] in sfsnls:
                boardc[y][x]=' '
                boardc[y+1][x-1]='B'
                if y+1==7:
                    boardc[y+1][x-1]='Q'
                childrenB.append(boardc)
                boardc=copy.deepcopy(pos)
        if x+1<8 and y+1<8:
            if boardc[y+1][x+1] in sfsnls:
                boardc[y][x]=' '
                boardc[y+1][x+1]='B'
                if y+1==7:
                    boardc[y+1][x+1]='Q'
                childrenB.append(boardc)
                boardc=copy.deepcopy(pos)
    if player=="b":
        if y==6 and boardc[y-2][x]==' ' and boardc[y-1][x]==' ':
            boardc[y][x]=' '
            boardc[y-2][x]='b'
            childrenB.append(boardc)
            boardc=copy.deepcopy(pos)
        if y-1>-1:
            if boardc[y-1][x]==' ':
                boardc[y][x]=' '
                boardc[y-1][x]='b'
                if y-1==0:
                    boardc[y-1][x]='q'
                childrenB.append(boardc)
                boardc=copy.deepcopy(pos)
        if x-1>-1 and y-1>-1:
            if boardc[y-1][x-1] in sfbnls:
                boardc[y][x]=' '
                boardc[y-1][x-1]='b'
                if y-1==0:
                    boardc[y-1][x-1]='q'
                childrenB.append(boardc)
                boardc=copy.deepcopy(pos)
        if x+1<8 and y-1>-1:
            if boardc[y-1][x+1] in sfbnls:
                boardc[y][x]=' '
                boardc[y-1][x+1]='b'
                if y-1==0:
                    boardc[y-1][x+1]='q'
                childrenB.append(boardc)
                boardc=copy.deepcopy(pos)
    return childrenB

def verloren(pos,player):
    eval=False
    for p in range(8):
        for o in range(8):
            if pos[p][o]==player:
                eval=True
    if eval:
        return False
    else:
        return True

def evaluatepos(pos):
    val=0
    for p in range(8):
        for o in range(8):
            if pos[p][o]=='K':
                val=val-1000
            if pos[p][o]=='Q':
                val=val-90
            if pos[p][o]=='T':
                val=val-50
            if pos[p][o]=='L':
                val=val-30
            if pos[p][o]=='X':
                val=val-30
            if pos[p][o]=='B':
                val=val-10
            #
            if pos[p][o]=='k':
                val=val+1000
            if pos[p][o]=='q':
                val=val+90
            if pos[p][o]=='t':
                val=val+50
            if pos[p][o]=='l':
                val=val+30
            if pos[p][o]=='x':
                val=val+30
            if pos[p][o]=='b':
                val=val+10
    return val

def minimax(position, depth, maxplayer, alpha, beta):
    # X:maxplayer,spieler O:minplayer,computer
    # Spieler
    # alpha: best maxpl, beta: best minpl
    if maxplayer:
        playerj = 'k'
    else:
        playerj = 'K'

    # return
    pos =copy.deepcopy(position)
    f=evaluatepos(pos)
    if verloren(position, 'K') == True:
        return f
    elif verloren(position, 'k') == True:
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
    for firstgenchild in genchildren(boa, 'K'):
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
    while not verloren(board, 'K') and not verloren(board, 'k'):
        turn =turn+1
        print(turn)
        printboard(board)
        player(board)
        printboard(board)
        if not verloren(board, 'K') and not verloren(board, 'k'):
            start = time.time()
            minimaxer(board)
            end = time.time()
            board.clear()
            board.extend(copy.deepcopy(move))
            print(end - start)
            print(minimaxc)
            print(evaluatepos(board))
    print(turn)
    printboard(board)
    print('GAME OVER')
    if verloren(board, 'k'):
        print(':( VERLOREN')
    elif verloren(board, 'K'):
        print(':) GEWONNEN')


play()


#wenn evalpos hoeher wird: minimax stoppen