import copy
import time
import random

board = [
    [' ', 'O', ' ', 'O', ' ', 'O', ' ','O'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
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

def xy():
    try:
        vx = int(input('von x: ')) - 1
        vy = int(input('von y: ')) - 1
        zx = int(input('zu x: ')) - 1
        zy = int(input('zu y: ')) - 1
        player('X',board,vy,vx,zy,zx)
    except:
        print('EINGABE NICHT KORREKT')
        xy()

def player(playerk, boardk, vy,vx,zy,zx):
    try:
        if zy<9 and zy>0 and zx>0 and zx<9 and boardk[vy][vx] == playerk:
            if playerk=='X':
                if zy==vy- 1:
                    if zx==vx +1:
                        boardk[zy][zx]='X'
                        boardk[vy][vx]=' '
                    elif zx==vx-1:
                        boardk[zy][zx]='X'
                        boardk[vy][vx]=' '
                    else:
                        print('EINGABE NICHT KORREKT')
                        player(playerk, boardk)
                else:
                    print('EINGABE NICHT KORREKT')
                    player(playerk, boardk)
            elif playerk=='O':
                if zy==vy+ 1:
                    print('ok')
                    if zx==vx+ 1:
                        boardk[zy][zx]='O'
                        boardk[vy][vx]=' '
                    elif zx==vx-1:
                        boardk[zy][zx]='O'
                        boardk[vy][vx]=' '
                    else:
                        print('EINGABE NICHT KORREKT')
                        player(playerk, boardk)
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

printboard(board)
for t in genchildren(board,'O'):
    printboard(t)