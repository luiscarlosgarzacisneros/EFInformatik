import copy
import time
import random

board = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', 'O', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
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
    except:
        print('EINGABE NICHT KORREKT')
        xy()

def player(playerk, boardk):
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


printboard(board)
player('O',board)
printboard(board)