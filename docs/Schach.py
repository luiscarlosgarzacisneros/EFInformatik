import copy
import time
import random

sfb=['T','L','X','Q','K','B',' ']
sfbnls=['T','L','X','Q','K','B']
sfs=['t','l','x','q','k','b',' ']


board = [
    ['T', 'L', 'X', 'Q', 'K', 'X', 'L','T'],
    ['B', 'B', 'B', 'B', 'B', 'B', 'B','B'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', 'b', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', 't', 'b', ' ', ' ',' '],
    [' ', ' ', ' ', 'B', ' ', ' ', ' ',' '],
    ['b', 'b', 'b', ' ', 'b', 'b', 'b','b'],
    ['t', 'l', 'x', 'q', 'k', 'x', 'l','t'],
]
#
e=[]
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

        #x geht noch nicht!!!!!!!
        if pos[vy][vx]=='x':
            for u in range(8):
                if pos[zy][zx] in sfb and vx+u==zx and vy+u==zy:
                    korrekt=True
                if pos[zy][zx] in sfb and vx-u==zx and vy-u==zy:
                    korrekt=True
                if pos[zy][zx] in sfb and vx-u==zx and vy+u==zy:
                    korrekt=True
                if pos[zy][zx] in sfb and vx+u==zx and vy-u==zy:
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

for i in range(9):
    printboard(board)
    player(board)

printboard(board)


#laeufer ueberspringt figuren!!!!!!!
#turm geht nicht!!!!!!!!!