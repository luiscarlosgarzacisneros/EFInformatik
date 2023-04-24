import copy
import time
import random

sfb=['T','L','X','Q','K','B',' ']
sfbnls=['T','L','X','Q','K','B']
sfs=['t','l','x','q','k','b',' ']
sfsnls=['t','l','x','q','k','b']


board = [
    ['T', 'L', 'X', 'Q', 'K', 'X', 'L','T'],
    ['B', 'B', 'B', 'B', 'B', 'B', 'B','B'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', 'T', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
    ['b', 'b', 'b', 'b', 'b', 'b', 'b','b'],
    ['t', 'l', 'x', 'q', 'k', 'x', 'l','t'],
]
#
e=[]
minimaxc = 0
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
                    pass
                if boardcopy[y][x]=='k':
                    for h in gcKk(y,x,boardcopy,'k'):
                        children.append(h)
                if boardcopy[y][x]=='t':
                    for h in gcTt(y,x,boardcopy,"t"):
                        children.append(h)
                if boardcopy[y][x]=='x':
                    pass
                if boardcopy[y][x]=='q':
                    pass
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
                    pass
                if boardcopy[y][x]=='K':
                    for h in gcKk(y,x,boardcopy,'K'):
                        children.append(h)
                if boardcopy[y][x]=='T':
                    for h in gcTt(y,x,boardcopy,'T'):
                        children.append(h)
                if boardcopy[y][x]=='X':
                    pass
                if boardcopy[y][x]=='Q':
                    pass
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

for t in genchildren(board,'K'):
    printboard(t)


def test():
    for i in range(9):
        printboard(board)
        player(board)

    printboard(board)


#genchildren k,q,b,t,x,l: genchildrenk(y,x,pos,playert): return childrenk
#for h in genchildrenk(y,x,boardcopy,'K'):
#   children.append(h)