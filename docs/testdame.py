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
board2 = [
    [' ', ' ', ' ', 'O', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', 'O', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', 'O', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', 'O', ' ', 'O', ' ',' '],
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
childrens=[]
e=[]
es=[]
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
        if zy==vy-1 and zx==vx-1 and pos[vy][vx]=='X' and pos[zy][zx]==' ':
            korrekt=True
        if zy==vy-1 and zx==vx+1 and pos[vy][vx]=='X' and pos[zy][zx]==' ':
            korrekt=True
        #
        if zy==vy-2 and zx==vx-2 and pos[vy][vx]=='X' and pos[zy][zx]==' ' and pos[vy-1][vx-1]=='O':
            korrekt=True
        if zy==vy-2 and zx==vx+2 and pos[vy][vx]=='X' and pos[zy][zx]==' ' and pos[vy-1][vx+1]=='O':
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
    if zy<8 and zy>-1 and zx<8 and zx>-1:
        #
        if zy==vy-2 and zx==vx-2 and pos[vy][vx]=='X' and pos[zy][zx]==' ' and pos[vy-1][vx-1]=='O':
            korrekt=True
        if zy==vy-2 and zx==vx+2 and pos[vy][vx]=='X' and pos[zy][zx]==' ' and pos[vy-1][vx+1]=='O':
            korrekt=True
    if korrekt:
        es.append(zy)
        es.append(zx)
        return True
    else:
        print('EINGABE NICHT KORREKT')
        return False

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

def playerschlagen(vy,vx,zy,zx,pos):
    while schlagenmoeglichX(vy,vx,pos):
        if zy==vy-2 and zx==vx-2 and pos[vy][vx]=='X' and pos[zy][zx]==' ' and pos[vy-1][vx-1]=='O':
            pos[vy][vx]=' '
            pos[zy][zx]='X'
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
        elif zy==vy-2 and zx==vx+2 and pos[vy][vx]=='X' and pos[zy][zx]==' ' and pos[vy-1][vx+1]=='O':
            pos[vy][vx]=' '
            pos[zy][zx]='X'
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
    if zy==vy-1 and zx==vx+1 and pos[vy][vx]=='X' and pos[zy][zx]==' ':
        pos[vy][vx]=' '
        pos[zy][zx]='X'
    #schlagen
    if zy==vy-2 and zx==vx-2 and pos[vy][vx]=='X' and pos[zy][zx]==' ' and pos[vy-1][vx-1]=='O':
        playerschlagen(vy,vx,zy,zx,pos)
    if zy==vy-2 and zx==vx+2 and pos[vy][vx]=='X' and pos[zy][zx]==' ' and pos[vy-1][vx+1]=='O':
        playerschlagen(vy,vx,zy,zx,pos)

printboard(board2)
player(board2)
printboard(board2)