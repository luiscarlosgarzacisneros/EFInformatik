import copy
import time
import random

board = [
    [' ', 'O', ' ', 'O', ' ', 'O', ' ','O'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', 'O', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', 'O', ' ', ' ', ' ',' '],
    [' ', ' ', 'X', ' ', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', 'O', ' ', ' ', ' ',' '],
    ['X', ' ', 'X', ' ', ' ', ' ', 'X',' '],
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
rs=[]
rets=[]
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
        print('ok1')
        if boar[y-2][x-2]==' 'and boar[y-1][x-1]=='O':
            print('ok2')
            r=True
    if y-2>-1 and x+2<8:
        print('ok3')
        if boar[y-2][x+2]==' ' and boar[y-1][x+1]=='O':
            print('ok4')
            r=True
    else:
        r=True
    return r

def player(playerk, boardk):
    boardcopy=copy.deepcopy(boardk)
    vx = int(input('von x: ')) - 1
    vy = int(input('von y: ')) - 1
    zx = int(input('zu x: ')) - 1
    zy = int(input('zu y: ')) - 1
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
                    else:
                        print('EINGABE NICHT KORREKT')
                        player(playerk, boardk)
                elif zy==vy- 2:
                    nvy=vy
                    nvx=vx
                    while True:
                        if zy==vy- 2:
                            if zx==vx +2 and boardcopy[vy-1][vx+1]=='O':
                                boardcopy[zy][zx]='X'
                                boardcopy[vy][vx]=' '
                                boardcopy[vy-1][vx+1]=' '
                                printboard(boardcopy)
                                vx = zx
                                vy = zy
                                zx = int(input('zu x: ')) - 1
                                zy = int(input('zu y: ')) - 1
                                
                            elif zx==vx-2 and boardcopy[vy-1][vx-1]=='O':
                                boardcopy[zy][zx]='X'
                                boardcopy[vy][vx]=' '
                                boardcopy[vy-1][vx-1]=' '
                                printboard(boardcopy)
                                vx = zx
                                vy = zy
                                zx = int(input('zu x: ')) - 1
                                zy = int(input('zu y: ')) - 1
                        if schlagenmoeglichX(vy,vx,boardcopy)==False:
                            break
                            
                    return(boardcopy)
        else:
            print('EINGABE NICHT KORREKT')
            player(playerk, boardk)
    except:
        print('EINGABE NICHT KORREKT')
        player(playerk, boardk)

print(schlagenmoeglichX(5,2,board))

#printboard(board)
#f=player('X',board)
#board.clear()
#board.extend(f)
#printboard(board)
#print(schlagenmoeglichX(5,2,board))

