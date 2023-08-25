import copy
import random
import time
import math

board = [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,2,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]
        ]

#--------------------nicht fertig

def gorcXO(y,x,boardc,player):
    childrenXO=[]
    if player==1:
        #normal
        if y-1>-1 and x-1>-1 and boardc[y-1][x-1]==0:
            childrenXO.append(1)
        if y-1>-1 and x+ 1<8 and boardc[y-1][x+1]==0:
            childrenXO.append(2)
        #schlagen
        if y-2>-1 and x-2>-1 and  boardc[y-2][x-2]==0:
            if boardc[y-1][x-1]<0:
                #schlagen
                pass
        if y-2>-1 and x+ 2<8 and  boardc[y-2][x+2]==0:
            if boardc[y-1][x+1]<0:
                #schlagen
                pass
    elif player==-1:
        #normal
        if y+1<8 and x-1>-1 and  boardc[y+1][x-1]==0:
            childrenXO.append(1)
        if y+1<8 and x+ 1<8 and boardc[y+1][x+1]==0:
            childrenXO.append(2)
        #schlagen
        if y+2<8 and x-2>-1 and boardc[y+2][x-2]==0:
            if boardc[y+1][x-1]>0:
                #schlagen
                pass
        if y+2<8 and x+ 2<8 and boardc[y+2][x+2]==0:
            if boardc[y+1][x+1]>0:
                #schlagen
                pass
    #
    if childrenXO==[]:
        return []
    else:
        n=random.choice(childrenXO)
        if player==1:
            if n==1:
                boardc[y][x]=0
                if y-1==0:
                    boardc[y-1][x-1]=2
                else:
                    boardc[y-1][x-1]=1
                return boardc
            elif n==2:
                boardc[y][x]=0
                if y-1==0:
                    boardc[y-1][x+1]=2
                else:
                    boardc[y-1][x+1]=1
                return boardc
            else: #schlagen
               pass
        elif player==-1:
            if n==1:
                boardc[y][x]=0
                if y+1==7:
                    boardc[y-1][x-1]=-2
                else:
                    boardc[y+1][x-1]=-1
                return boardc
            elif n==2:
                boardc[y][x]=0
                if y+1==7:
                    boardc[y-1][x+1]=-2
                else:
                    boardc[y+1][x+1]=-1
                return boardc
            else: #schlagen
                pass
    
def generate_one_random_child(position, player):#pick rand piece, then pick rand move
    boardcopy = copy.deepcopy(position)
    #
    piecesy=[]
    piecesx=[]
    if player==1:
        for y in range(8):
            for x in range(8):
                if boardcopy[y][x]==1:
                    piecesy.append(y)
                    piecesx.append(x)
                elif boardcopy[y][x]==2:
                    for i in range(5):
                        piecesy.append(y)
                        piecesx.append(x)
    elif player==-1:
        for y in range(8):
            for x in range(8):
                if boardcopy[y][x]==-1:
                    piecesy.append(y)
                    piecesx.append(x)
                elif boardcopy[y][x]==-2:
                    for i in range(5):
                        piecesy.append(y)
                        piecesx.append(x)
    #
    if piecesx==[]:
        return []
    #
    while True:
        child=[]
        n = random.randint(0, len(piecesy) - 1)
        y = piecesy[n]
        x = piecesx[n]
        #
        if player==1:
            if boardcopy[y][x]==1:
                child=gorcXO(y,x,position,1)
            elif boardcopy[y][x]==2:
                child=gorcWM(y,x,position,2)
        elif player==-1:
            if boardcopy[y][x]==-1:
                child=gorcXO(y,x,position,-1)
            elif boardcopy[y][x]==-2:
                child=gorcWM(y,x,position,-2)
        #
        if child!=[]: 
            break
    #
    return child

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

ne=[]
while True:
    ne=generate_one_random_child(board, 1)
    if ne!=[]:
        break
printboard(ne)