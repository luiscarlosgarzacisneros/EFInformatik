


import copy
import time
import random

board = [
    [' ', 'O', ' ', 'O', ' ', 'O', ' ','O'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', 'O', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
    [' ', ' ', ' ', 'O', ' ', ' ', ' ',' '],
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

def xy():
    try:
        vx = int(input('von x: ')) - 1
        vy = int(input('von y: ')) - 1
        zx = int(input('zu x: ')) - 1
        zy = int(input('zu y: ')) - 1
        return player('X',board,vy,vx,zy,zx)
    except:
        print('EINGABE NICHT KORREKT')
        xy()



def schlagenplayer(playerk, boardk, vx,vy,zx,zy):
    
    print('ok')
    if zx< 9 and zy<9 and zx> 0 and zy>0:
        print('yes')
        boardcopy=copy.deepcopy(boardk)
        if zx==vx +2 and copy.deepcopy(boardcopy)[vy+1][vx+1]=='O':
            print('kr')
            boardcopy[zy][zx]='X'
            boardcopy[vy][vx]=' '
            boardcopy[vy-1][vx+1]=' '
            nvy=zy
            nvx=zx
            nzx=int(input('zu x: ')) - 1
            nzy=int(input('zu y: ')) - 1
            printboard(boardcopy)
            schlagenplayer('X',copy.deepcopy(boardcopy),nvx,nvy,nzx,nzy)

        if zx==vx-2 and copy.deepcopy(boardcopy)[vy-1][vx-1]=='O':
            print('kr')
            boardcopy[zy][zx]='X'
            boardcopy[vy][vx]=' '
            boardcopy[vy-1][vx-1]=' '
            vy=zy
            vx=zx

            printboard(boardcopy)
            schlagenplayer('X',copy.deepcopy(boardcopy),vx,vy,zx,zy)
            
        
        return copy.deepcopy(boardcopy)


def player(playerk, boardk, vy,vx,zy,zx):
    boardcopy=copy.deepcopy(boardk)
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
                    schlagenplayer(playerk, boardk, vx,vy,zx,zy)

                else:
                    print('EINGABE NICHT KORREKT')
                    player(playerk, boardk)
        else:
            print('EINGABE NICHT KORREKT')
            player(playerk, boardk)
    except:
        print('EINGABE NICHT KORREKT')
        player(playerk, boardk)



def schlagen(pos, playert,r):
    boardcopy=copy.deepcopy(pos)
    #am anfang=0
    if playert=='O':
        y = 0
        for i in range(8):
            x = 0
            for j in range(8):
                if y+2<8 and x+2<8 and boardcopy[y][x]=='O' and boardcopy[y+2][x+2]==' ' and boardcopy[y+1][x+1]=='X':
                    r=r+1
                    boardcopy[y][x]=' '
                    boardcopy[y+2][x+2]='O'
                    boardcopy[y+1][x+1]=' '
                    rets.append(copy.deepcopy(boardcopy))
                    rs.append(copy.deepcopy(r))
                    schlagen(boardcopy, playert,r)
                    boardcopy=copy.deepcopy(pos)
                    r=0

                if y+2<8 and x-2<8 and boardcopy[y][x]=='O' and boardcopy[y+2][x-2]==' ' and boardcopy[y+1][x-1]=='X':
                    r=r+1
                    boardcopy[y][x]=' '
                    boardcopy[y+2][x-2]='O'
                    boardcopy[y+1][x-1]=' '
                    rets.append(copy.deepcopy(boardcopy))
                    rs.append(copy.deepcopy(r))
                    schlagen(boardcopy, playert,r)
                    boardcopy=copy.deepcopy(pos)
                    r=0

                x = x + 1
            y = y + 1
        #
    elif playert=='X':
        y = 0
        for i in range(8):
            x = 0
            for j in range(8):
                if y-2<8 and x+2<8 and boardcopy[y][x]=='X' and boardcopy[y-2][x+2]==' ' and boardcopy[y-1][x+1]=='O':
                    r=r+1
                    boardcopy[y][x]=' '
                    boardcopy[y-2][x+2]='X' 
                    boardcopy[y-1][x+1]=' '
                    rets.append(copy.deepcopy(boardcopy))
                    rs.append(copy.deepcopy(r))
                    schlagen(boardcopy, playert,r)
                    boardcopy=copy.deepcopy(pos)
                    r=0
                    
                if y-2<8 and x-2<8 and boardcopy[y][x]=='X' and boardcopy[y-2][x-2]==' ' and boardcopy[y-1][x-1]=='O':
                    r=r+1
                    boardcopy[y][x]=' '
                    boardcopy[y-2][x-2]='X'
                    boardcopy[y-1][x-1]=' '
                    rets.append(copy.deepcopy(boardcopy))
                    rs.append(copy.deepcopy(r))
                    schlagen(boardcopy, playert,r)
                    boardcopy=copy.deepcopy(pos)
                    r=0
                    
                x = x + 1
            y = y + 1
        #



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

#printboard(board)
#for t in genchildren(board,'O'):
    #printboard(t)
#xy()
#printboard(board)

#schlagen(board,'X',0)

#for t in range(len(rets)):
    #printboard(rets[t])
    #print(rs[t])

printboard(board)
print(xy())

########################
# genchildren mit schlagen, falls schlagen, keine anderen children.
#clear rs and ret