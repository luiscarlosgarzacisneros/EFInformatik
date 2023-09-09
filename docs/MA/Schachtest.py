import copy
import time
import random
import math

#-1:B
#-2:L
#-3:X
#-4:T
#-5:Q
#-6:K
#-7:Z not moved towerT
#-8:Y not moved kingK
#-9:F en passant B (just moved 2 forw)

#1:b
#2:l
#3:x
#4:t
#5:q
#6:k
#7:z not moved towert
#8:y not moved kingk
#9:f en passant b (just moved 2 forw)


#

def printboard2(board):
    print('  1   2   3   4   5   6   7   8')
    print('---------------------------------')
    for i in range(8):
        print('I ', end='')
        for j in range(8):
            if board[i][j]==1 or board[i][j]==9:
                print('b', end='')
            elif board[i][j]==2:
                print('l', end='')
            elif board[i][j]==3:
                print('x', end='')
            elif board[i][j]==4 or board[i][j]==7:
                print('t', end='')
            elif board[i][j]==5:
                print('q', end='')
            elif board[i][j]==6 or board[i][j]==8:
                print('k', end='')
            elif board[i][j]==-1 or board[i][j]==-9:
                print('B', end='')
            elif board[i][j]==-2:
                print('L', end='')
            elif board[i][j]==-3:
                print('X', end='')
            elif board[i][j]==-4 or board[i][j]==-7:
                print('T', end='')
            elif board[i][j]==-5:
                print('Q', end='')
            elif board[i][j]==-6 or board[i][j]==-8:
                print('K', end='')
            elif board[i][j]==0:
                print(' ', end='')
            print(' I ', end='')
        print(i + 1)
        print('---------------------------------')

def printboard(board):
    print('  1   2   3   4   5   6   7   8')
    print('---------------------------------')
    for i in range(8):
        print('I ', end='')
        for j in range(8):
            if board[i][j]==1:
                print('b', end='')
            elif board[i][j]==2:
                print('l', end='')
            elif board[i][j]==3:
                print('x', end='')
            elif board[i][j]==4:
                print('t', end='')
            elif board[i][j]==5:
                print('q', end='')
            elif board[i][j]==6:
                print('k', end='')
            elif board[i][j]==-1:
                print('B', end='')
            elif board[i][j]==-2:
                print('L', end='')
            elif board[i][j]==-3:
                print('X', end='')
            elif board[i][j]==-4:
                print('T', end='')
            elif board[i][j]==-5:
                print('Q', end='')
            elif board[i][j]==-6:
                print('K', end='')
            elif board[i][j]==0:
                print(' ', end='')
            #
            elif board[i][j]==9:
                print('f', end='')
            elif board[i][j]==-9:
                print('F', end='')
            #
            elif board[i][j]==7:
                print('z', end='')
            elif board[i][j]==-7:
                print('Z', end='')
            #
            elif board[i][j]==8:
                print('y', end='')
            elif board[i][j]==-8:
                print('Y', end='')
            #
            print(' I ', end='')
        print(i + 1)
        print('---------------------------------')

#

def genchildren(position, playerk):
    children=[]
    #9&-9 zu 1&-1
    if playerk==6:
        for y in range(len(position)):
            for x in range(len(position[y])):
                if position[y][x]==9:
                    position[y][x]=1
    elif playerk==-6:
        for y in range(len(position)):
            for x in range(len(position[y])):
                if position[y][x]==-9:
                    position[y][x]=-1
    #
    if playerk==6:
        for y in range(8):
            for x in range(8):
                if position[y][x]==1:
                    for h in gcBb(y,x,position,1):
                        children.append(h)
                elif position[y][x]==6:
                    for h in gcKk(y,x,position,6):
                        children.append(h)
                elif position[y][x]==4 or position[y][x]==7:
                    for h in gcTtXxQq(y,x,position,4,[0, 0, 1, -1], [1, -1, 0, 0]):
                        children.append(h)
                elif position[y][x]==3:
                    for h in gcTtXxQq(y,x,position,3,[1, -1, -1, 1], [1, 1, -1, -1]):
                        children.append(h)
                elif position[y][x]==5:
                    for h in gcTtXxQq(y,x,position,5,[1, -1, -1, 1, 0, 0, 1, -1], [1, 1, -1, -1, 1, -1, 0, 0]):
                        children.append(h)
                elif position[y][x]==2:
                    for h in gcLl(y,x,position,2):
                        children.append(h)
                elif position[y][x]==8:
                    for h in gcKk(y,x,position,8):
                        children.append(h)
    elif playerk==-6:
        for y in range(8):
            for x in range(8):
                if position[y][x]==-1:
                    for h in gcBb(y,x,position,-1):
                        children.append(h)
                elif position[y][x]==-6:
                    for h in gcKk(y,x,position,-6):
                        children.append(h)
                elif position[y][x]==-4 or position[y][x]==-7:
                    for h in gcTtXxQq(y,x,position,-4,[0, 0, 1, -1], [1, -1, 0, 0]):
                        children.append(h)
                elif position[y][x]==-3:
                    for h in gcTtXxQq(y,x,position,-3,[1, -1, -1, 1], [1, 1, -1, -1]):
                        children.append(h)
                elif position[y][x]==-5:
                    for h in gcTtXxQq(y,x,position,-5,[1, -1, -1, 1, 0, 0, 1, -1], [1, 1, -1, -1, 1, -1, 0, 0]):
                        children.append(h)
                elif position[y][x]==-2:
                    for h in gcLl(y,x,position,-2):
                        children.append(h)
                elif position[y][x]==-8:
                    for h in gcKk(y,x,position,-8):
                        children.append(h)
    #
    return children

def gcTtXxQq(y, x, pos, player, direction_y, direction_x):
    children = []
    #
    if player<0:
        for dir in range(len(direction_y)):
            for step in range(1, 8):
                new_y = y + step * direction_y[dir]
                new_x = x + step * direction_x[dir]
                #
                if -1<new_y<8 and -1<new_x<8:
                    if pos[new_y][new_x]==0:
                        boardc=copy.deepcopy(pos)
                        boardc[y][x]=0
                        boardc[new_y][new_x]=player
                        children.append(boardc)
                    elif pos[new_y][new_x]<0:
                        break
                    elif pos[new_y][new_x]>0:
                        boardc=copy.deepcopy(pos)
                        boardc[y][x]=0
                        boardc[new_y][new_x]=player
                        children.append(boardc)
                        break
                else:
                    break
    elif player>0:
        for dir in range(len(direction_y)):
            for step in range(1, 8):
                new_y = y + step * direction_y[dir]
                new_x = x + step * direction_x[dir]
                #
                if -1<new_y<8 and -1<new_x<8:
                    if pos[new_y][new_x]==0:
                        boardc=copy.deepcopy(pos)
                        boardc[y][x]=0
                        boardc[new_y][new_x]=player
                        children.append(boardc)
                    elif pos[new_y][new_x]>0:
                        break
                    elif pos[new_y][new_x]<0:
                        boardc=copy.deepcopy(pos)
                        boardc[y][x]=0
                        boardc[new_y][new_x]=player
                        children.append(boardc)
                        break
                else:
                    break
    #
    return children

def gcLl(y, x, pos, player):
    boardc = copy.deepcopy(pos)
    childrenL = []
    #
    direction_y = [-2, -2, 2, 2, 1, -1, 1, -1]
    direction_x = [1, -1, 1, -1, 2, 2, -2, -2]
    #
    if player==-2:
        for i in range(8):
            new_y = y + direction_y[i]
            new_x = x + direction_x[i]
            if -1<new_y<8 and -1<new_x<8 and pos[new_y][new_x]>=0:
                boardc = copy.deepcopy(pos)
                boardc[y][x]=0
                boardc[new_y][new_x]=-2
                childrenL.append(boardc)
    #
    elif player==2:
        for i in range(8):
            new_y = y + direction_y[i]
            new_x = x + direction_x[i]
            if -1<new_y<8 and -1<new_x<8 and pos[new_y][new_x]<=0:
                boardc = copy.deepcopy(pos)
                boardc[y][x]=0
                boardc[new_y][new_x]=2
                childrenL.append(boardc)
    #
    return childrenL

def gcKk(y, x, pos, player):
    childrenK = []
    boardc=copy.deepcopy(pos)
    #
    direction_y = [-1, -1, -1, 0, 0, 1, 1, 1]
    direction_x = [-1, 0, 1, -1, 1, -1, 0, 1]
    #
    for i in range(8):
        new_y = y + direction_y[i]
        new_x = x + direction_x[i]
        if -1<new_y<8 and -1<new_x<8:
            if (player==-6 or player==-8) and boardc[new_y][new_x]>=0:
                boardc[y][x]=0
                boardc[new_y][new_x]=-6
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
            elif (player==6 or player==8) and boardc[new_y][new_x]<=0:
                boardc[y][x]=0
                boardc[new_y][new_x]=6
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
    #rochade
    if player==-8:
        if boardc[0][0]==-7 and boardc[0][1]==0 and boardc[0][2]==0 and boardc[0][3]==0:
            boardc[0][2]=-6
            boardc[0][3]=-4
            boardc[0][0]=0
            boardc[0][4]=0
            legal=True
            for child in genchildren(boardc,6):
                if child[0][2]>0 or child[0][3]>0 or child[0][4]>0:
                    legal=False
                    break
            if legal:
                childrenK.append(boardc)
            boardc=copy.deepcopy(pos)
        if boardc[0][7]==-7 and boardc[0][6]==0 and boardc[0][5]==0:
            boardc[0][6]=-6
            boardc[0][5]=-4
            boardc[0][7]=0
            boardc[0][4]=0
            legal=True
            for child in genchildren(boardc,6):
                if child[0][4]>0 or child[0][5]>0 or child[0][6]>0:
                    legal=False
                    break
            if legal:
                childrenK.append(boardc)
            boardc=copy.deepcopy(pos)
    elif player==8:
        if boardc[7][0]==7 and boardc[7][1]==0 and boardc[7][2]==0 and boardc[7][3]==0:
            boardc[7][2]=6
            boardc[7][3]=4
            boardc[7][0]=0
            boardc[7][4]=0
            legal=True
            for child in genchildren(boardc,-6):
                if child[7][2]<0 or child[7][3]<0 or child[7][4]<0:
                    legal=False
                    break
            if legal:
                childrenK.append(boardc)
            boardc=copy.deepcopy(pos)
        if boardc[7][7]==7 and boardc[7][6]==0 and boardc[7][5]==0:
            boardc[7][6]=6
            boardc[7][5]=4
            boardc[7][7]=0
            boardc[7][4]=0
            legal=True
            for child in genchildren(boardc,-6):
                if child[7][4]<0 or child[7][5]<0 or child[7][6]<0:
                    legal=False
                    break
            if legal:
                childrenK.append(boardc)
            boardc=copy.deepcopy(pos)
    return childrenK

def gcBb(y,x,pos,player):
    boardc=copy.deepcopy(pos)
    childrenB= []
    if player==-1:
        if y==1 and boardc[y+2][x]==0 and boardc[y+1][x]==0:
            boardc[y][x]=0
            boardc[y+2][x]=-9
            childrenB.append(boardc)
            boardc=copy.deepcopy(pos)
        if y+1<8:
            if boardc[y+1][x]==0:
                boardc[y][x]=0
                boardc[y+1][x]=-1
                if y+1==7:
                    boardc[y+1][x]=-5
                childrenB.append(boardc)
                boardc=copy.deepcopy(pos)
        if x-1>-1 and y+1<8:
            if boardc[y+1][x-1]>0:
                boardc[y][x]=0
                boardc[y+1][x-1]=-1
                if y+1==7:
                    boardc[y+1][x-1]=-5
                childrenB.append(boardc)
                boardc=copy.deepcopy(pos)
        if x+1<8 and y+1<8:
            if boardc[y+1][x+1]>0:
                boardc[y][x]=0
                boardc[y+1][x+1]=-1
                if y+1==7:
                    boardc[y+1][x+1]=-5
                childrenB.append(boardc)
                boardc=copy.deepcopy(pos)
        #en passant
        if x-1>-1 and y+1<8:
            if boardc[y][x-1]==9 and boardc[y+1][x-1]==0:
                boardc[y][x]=0
                boardc[y+1][x-1]=-1
                boardc[y][x-1]=0
                childrenB.append(boardc)
                boardc=copy.deepcopy(pos)
        if x+1<8 and y+1<8:
            if boardc[y][x+1]==9 and boardc[y+1][x+1]==0:
                boardc[y][x]=0
                boardc[y+1][x+1]=-1
                boardc[y][x+1]=0
                childrenB.append(boardc)
                boardc=copy.deepcopy(pos)

    elif player==1:
        if y==6 and boardc[y-2][x]==0 and boardc[y-1][x]==0:
            boardc[y][x]=0
            boardc[y-2][x]=9
            childrenB.append(boardc)
            boardc=copy.deepcopy(pos)
        if y-1>-1:
            if boardc[y-1][x]==0:
                boardc[y][x]=0
                boardc[y-1][x]=1
                if y-1==0:
                    boardc[y-1][x]=5
                childrenB.append(boardc)
                boardc=copy.deepcopy(pos)
        if x-1>-1 and y-1>-1:
            if boardc[y-1][x-1]<0:
                boardc[y][x]=0
                boardc[y-1][x-1]=1
                if y-1==0:
                    boardc[y-1][x-1]=5
                childrenB.append(boardc)
                boardc=copy.deepcopy(pos)
        if x+1<8 and y-1>-1:
            if boardc[y-1][x+1]<0:
                boardc[y][x]=0
                boardc[y-1][x+1]=1
                if y-1==0:
                    boardc[y-1][x+1]=5
                childrenB.append(boardc)
                boardc=copy.deepcopy(pos)
        #en passant
        if x-1>-1 and y-1>-1:
            if boardc[y][x-1]==-9 and boardc[y-1][x-1]==0:
                boardc[y][x]=0
                boardc[y-1][x-1]=1
                boardc[y][x-1]=0
                childrenB.append(boardc)
                boardc=copy.deepcopy(pos)
        if x+1<8 and y-1>-1:
            if boardc[y][x+1]==-9 and boardc[y-1][x+1]==0:
                boardc[y][x]=0
                boardc[y-1][x+1]=1
                boardc[y][x+1]=0
                childrenB.append(boardc)
                boardc=copy.deepcopy(pos)
    return childrenB

#Gorc

def generate_one_random_child2(position, playerk):#für MCTS Simulation
    #wählt random Spielfigur aus, gen moves für Figur, wählt random move -> not all moves are equal, schneller
    boardcopy = copy.deepcopy(position)
    #
    #9&-9 zu 1&-1
    if playerk==6:
        for y in range(len(boardcopy)):
            for x in range(len(boardcopy[y])):
                if boardcopy[y][x]==9:
                    boardcopy[y][x]=1
    elif playerk==-6:
        for y in range(len(boardcopy)):
            for x in range(len(boardcopy[y])):
                if boardcopy[y][x]==-9:
                    boardcopy[y][x]=-1
    #
    piecesy=[]
    piecesx=[]
    if playerk==6:
        for y in range(8):
            for x in range(8):
                if boardcopy[y][x]>0:
                    piecesy.append(y)
                    piecesx.append(x)
    elif playerk==-6:
        for y in range(8):
            for x in range(8):
                if boardcopy[y][x]<0:
                    piecesy.append(y)
                    piecesx.append(x)
    #
    if piecesx==[]:
        return []
    #
    while True:
        n = random.randint(0, len(piecesy) - 1)
        y = piecesy[n]
        x = piecesx[n]

        if boardcopy[y][x] == 1 or boardcopy[y][x] == -1:
            child = gorcBb(y, x, boardcopy, boardcopy[y][x])
        elif boardcopy[y][x] == 2 or boardcopy[y][x] == -2:
            child = gorcLl(y, x, boardcopy, boardcopy[y][x])
        elif boardcopy[y][x] == 3 or boardcopy[y][x] == -3:
            child = gorcXx(y, x, boardcopy, boardcopy[y][x])
        elif boardcopy[y][x] == 4 or boardcopy[y][x] == -4 or boardcopy[y][x] == -7 or boardcopy[y][x] == 7:
            child = gorcTt(y, x, boardcopy, boardcopy[y][x])
        elif boardcopy[y][x] == 5 or boardcopy[y][x] == -5:
            child = gorcQq(y, x, boardcopy, boardcopy[y][x])
        elif boardcopy[y][x] == 6 or boardcopy[y][x] == -6 or boardcopy[y][x] == -8 or boardcopy[y][x] == 8:
            child = gorcKk(y, x, boardcopy, boardcopy[y][x])
        #
        if child!=[]: 
            return child

def gorcKk2(y,x,boardc,player):
    childrenK= []
    if player==-6 or player==-8:
        if y+1<8 and x+1<8:
            if boardc[y+1][x+1]>=0:
                childrenK.append(1)
        if y+1<8 and x-1>-1:
            if boardc[y+1][x-1]>=0:
                childrenK.append(2)
        if y-1>-1 and x+1<8:
            if boardc[y-1][x+1]>=0:
                childrenK.append(3)
        if y-1>-1 and x+1<8:
            if boardc[y-1][x-1]>=0:
                childrenK.append(4)
        if x+1<8:
            if boardc[y][x+1]>=0:
                childrenK.append(5)
        if x-1>-1:
            if boardc[y][x-1]>=0:
                childrenK.append(6)
        if y+1<8:
            if boardc[y+1][x]>=0:
                childrenK.append(7)
        if y-1>-1:
            if boardc[y-1][x]>=0:
                childrenK.append(8)
        #
    elif player==6 or player==8:
        if y+1<8 and x+1<8:
            if boardc[y+1][x+1]<=0:
                childrenK.append(1)
        if y+1<8 and x-1>-1:
            if boardc[y+1][x-1]<=0:
                childrenK.append(2)
        if y-1>-1 and x+1<8:
            if boardc[y-1][x+1]<=0:
                childrenK.append(3)
        if y-1>-1 and x+1<8:
            if boardc[y-1][x-1]<=0:
                childrenK.append(4)
        if x+1<8:
            if boardc[y][x+1]<=0:
                childrenK.append(5)
        if x-1>-1:
            if boardc[y][x-1]<=0:
                childrenK.append(6)
        if y+1<8:
            if boardc[y+1][x]<=0:
                childrenK.append(7)
        if y-1>-1:
            if boardc[y-1][x]<=0:
                childrenK.append(8)
    #
    #rochade
    if player==-8:
        if boardc[0][0]==-7 and boardc[0][1]==0 and boardc[0][2]==0 and boardc[0][3]==0:
            boardcc=copy.deepcopy(boardc)
            boardcc[0][2]=-6
            boardcc[0][3]=-4
            boardcc[0][0]=0
            boardcc[0][4]=0
            legal=True
            for child in genchildren(boardcc,6):
                if child[0][2]>0 or child[0][3]>0 or child[0][4]>0:
                    legal=False
                    break
            if legal:
                childrenK.append(9)
        if boardc[0][7]==-7 and boardc[0][6]==0 and boardc[0][5]==0:
            boardcc=copy.deepcopy(boardc)
            boardcc[0][6]=-6
            boardcc[0][5]=-4
            boardcc[0][7]=0
            boardcc[0][4]=0
            legal=True
            for child in genchildren(boardcc,6):
                if child[0][4]>0 or child[0][5]>0 or child[0][6]>0:
                    legal=False
                    break
            if legal:
                childrenK.append(10)
    elif player==8:
        if boardc[7][0]==7 and boardc[7][1]==0 and boardc[7][2]==0 and boardc[7][3]==0:
            boardcc=copy.deepcopy(boardc)
            boardcc[7][2]=6
            boardcc[7][3]=4
            boardcc[7][0]=0
            boardcc[7][4]=0
            legal=True
            for child in genchildren(boardcc,-6):
                if child[7][2]<0 or child[7][3]<0 or child[7][4]<0:
                    legal=False
                    break
            if legal:
                childrenK.append(11)
        if boardc[7][7]==7 and boardc[7][6]==0 and boardc[7][5]==0:
            boardcc=copy.deepcopy(boardc)
            boardcc[7][6]=6
            boardcc[7][5]=4
            boardcc[7][7]=0
            boardcc[7][4]=0
            legal=True
            for child in genchildren(boardcc,-6):
                if child[7][4]<0 or child[7][5]<0 or child[7][6]<0:
                    legal=False
                    break
            if legal:
                childrenK.append(12)
    #
    if childrenK==[]:
        return []
    else:
        n=random.choice(childrenK)
        if n==1:
            boardc[y][x]=0
            boardc[y+1][x+1]=player
            return boardc
        elif n==2:
            boardc[y][x]=0
            boardc[y+1][x-1]=player
            return boardc
        elif n==3:
            boardc[y][x]=0
            boardc[y-1][x+1]=player
            return boardc
        elif n==4:
            boardc[y][x]=0
            boardc[y-1][x-1]=player
            return boardc
        elif n==5:
            boardc[y][x]=0
            boardc[y][x+1]=player
            return boardc
        elif n==6:
            boardc[y][x]=0
            boardc[y][x-1]=player
            return boardc
        elif n==7:
            boardc[y][x]=0
            boardc[y+1][x]=player
            return boardc
        elif n==8:
            boardc[y][x]=0
            boardc[y-1][x]=player
            return boardc
        elif n==9:
            boardc[0][2]=-6
            boardc[0][3]=-4
            boardc[0][0]=0
            boardc[0][4]=0
            return boardc
        elif n==10:
            boardc[0][6]=-6
            boardc[0][5]=-4
            boardc[0][7]=0
            boardc[0][4]=0
            return boardc
        elif n==11:
            boardc[7][2]=6
            boardc[7][3]=4
            boardc[7][0]=0
            boardc[7][4]=0
            return boardc
        elif n==12:
            boardc[7][6]=6
            boardc[7][5]=4
            boardc[7][7]=0
            boardc[7][4]=0
            return boardc

def gorcLl2(y,x,boardc,player):
    childrenL= []
    if player==-2:
        if y-2>-1 and x+1<8:
            if boardc[y-2][x+1]>=0:
                childrenL.append(1)
        if y-2>-1 and x-1>-1:
            if boardc[y-2][x-1]>=0:
                childrenL.append(2)
        if y+2<8 and x+1<8:
            if boardc[y+2][x+1]>=0:
                childrenL.append(3)
        if y+2<8 and x-1>-1:
            if boardc[y+2][x-1]>=0:
                childrenL.append(4)
        if y+1<8 and x+2<8:
            if boardc[y+1][x+2]>=0:
                childrenL.append(5)
        if y-1>-1 and x+2<8:
            if boardc[y-1][x+2]>=0:
                childrenL.append(6)
        if y+1<8 and x-2>-1:
            if boardc[y+1][x-2]>=0:
                childrenL.append(7)
        if y-1>-1 and x-2>-1:
            if boardc[y-1][x-2]>=0:
                childrenL.append(8)
    if player==2:
        if y-2>-1 and x+1<8:
            if boardc[y-2][x+1]<=0:
                childrenL.append(1)
        if y-2>-1 and x-1>-1:
            if boardc[y-2][x-1]<=0:
                childrenL.append(2)
        if y+2<8 and x+1<8:
            if boardc[y+2][x+1]<=0:
                childrenL.append(3)
        if y+2<8 and x-1>-1:
            if boardc[y+2][x-1]<=0:
                childrenL.append(4)
        if y+1<8 and x+2<8:
            if boardc[y+1][x+2]<=0:
                childrenL.append(5)
        if y-1>-1 and x+2<8:
            if boardc[y-1][x+2]<=0:
                childrenL.append(6)
        if y+1<8 and x-2>-1:
            if boardc[y+1][x-2]<=0:
                childrenL.append(7)
        if y-1>-1 and x-2>-1:
            if boardc[y-1][x-2]<=0:
                childrenL.append(8)
    #
    if childrenL==[]:
        return []
    else:
        n=random.choice(childrenL)
        if n==1:
            boardc[y][x]=0
            boardc[y-2][x+1]=player
            return boardc
        elif n==2:
            boardc[y][x]=0
            boardc[y-2][x-1]=player
            return boardc
        elif n==3:
            boardc[y][x]=0
            boardc[y+2][x+1]=player
            return boardc
        elif n==4:
            boardc[y][x]=0
            boardc[y+2][x-1]=player
            return boardc
        elif n==5:
            boardc[y][x]=0
            boardc[y+1][x+2]=player
            return boardc
        elif n==6:
            boardc[y][x]=0
            boardc[y-1][x+2]=player
            return boardc
        elif n==7:
            boardc[y][x]=0
            boardc[y+1][x-2]=player
            return boardc
        elif n==8:
            boardc[y][x]=0
            boardc[y-1][x-2]=player
            return boardc

def gorcTt(y,x,boardc,player):
    childrenT= []
    if player==-7:
        player=-4
    elif player==7:
        player=4
    #
    if player==-4:
        #rechts
        for i in range(7):
            if x+i+1<8:
                if boardc[y][x+i+1]>=0:
                    if boardc[y][x+i+1]!=0:
                        childrenT.append(i+1)
                        break
                    else:
                        childrenT.append(i+1)
                else:
                    break
            else:
                break
        #unten
        for i in range(7):
            if y+i+1<8:
                if boardc[y+i+1][x]>=0:
                    if boardc[y+i+1][x]!=0:
                        childrenT.append(10+i+1)
                        break
                    else:
                        childrenT.append(10+i+1)
                else:
                    break
            else:
                break
        #links
        for i in range(7):
            if x-i-1>-1:
                if boardc[y][x-i-1]>=0:
                    if boardc[y][x-i-1]!=0:
                        childrenT.append(20+i+1)
                        break
                    else:
                        childrenT.append(20+i+1)
                else:
                    break
            else:
                break
        #oben
        for i in range(7):
            if y-i-1>-1:
                if boardc[y-i-1][x]>=0:
                    if boardc[y-i-1][x]!=0:
                        childrenT.append(30+i+1)
                        break
                    else:
                        childrenT.append(30+i+1)
                else:
                    break
            else:
                break
    elif player==4:
        #rechts
        for i in range(7):
            if x+i+1<8:
                if boardc[y][x+i+1]<=0:
                    if boardc[y][x+i+1]!=0:
                        childrenT.append(i+1)
                        break
                    else:
                        childrenT.append(i+1)
                else:
                    break
            else:
                break
        #unten
        for i in range(7):
            if y+i+1<8:
                if boardc[y+i+1][x]<=0:
                    if boardc[y+i+1][x]!=0:
                        childrenT.append(10+i+1)
                        break
                    else:
                        childrenT.append(10+i+1)
                else:
                    break
            else:
                break
        #links
        for i in range(7):
            if x-i-1>-1:
                if boardc[y][x-i-1]<=0:
                    if boardc[y][x-i-1]!=0:
                        childrenT.append(20+i+1)
                        break
                    else:
                        childrenT.append(20+i+1)
                else:
                    break
            else:
                break
        #oben
        for i in range(7):
            if y-i-1>-1:
                if boardc[y-i-1][x]<=0:
                    if boardc[y-i-1][x]!=0:
                        childrenT.append(30+i+1)
                        break
                    else:
                        childrenT.append(30+i+1)
                else:
                    break
            else:
                break
    #
    if childrenT==[]:
        return []
    else:
        n=random.choice(childrenT)
        #rechts
        if n<10:
            boardc[y][x]=0
            boardc[y][x+n]=player
            return boardc
        #unten
        elif n<20 and n>10:
            boardc[y][x]=0
            boardc[y+(n-10)][x]=player
            return boardc
        #links
        elif n<30 and n>20:
            boardc[y][x]=0
            boardc[y][x-(n-20)]=player
            return boardc
        #oben
        elif n>30:
            boardc[y][x]=0
            boardc[y-(n-30)][x]=player
            return boardc

def gorcXx(y,x,boardc,player):
    childrenX= []
    if player==-3:
        #ur
        for i in range(7):
            if x+i+1<8 and y+i+1<8:
                if boardc[y+i+1][x+i+1]>=0:
                    if boardc[y+i+1][x+i+1]!=0:
                        childrenX.append(i+1)
                        break
                    else:
                        childrenX.append(i+1)
                else:
                    break
            else:
                break
        #ol
        for i in range(7):
            if y-i-1>-1 and x-i-1>-1:
                if boardc[y-i-1][x-i-1]>=0:
                    if boardc[y-i-1][x-i-1]!=0:
                        childrenX.append(10+i+1)
                        break
                    else:
                        childrenX.append(10+i+1)
                else:
                    break
            else:
                break
        #ul
        for i in range(7):
            if y+i+1<8 and x-i-1>-1:
                if boardc[y+i+1][x-i-1]>=0:
                    if boardc[y+i+1][x-i-1]!=0:
                        childrenX.append(20+i+1)
                        break
                    else:
                        childrenX.append(20+i+1)
                else:
                    break
            else:
                break
        #or
        for i in range(7):
            if y-i-1>-1 and x+i+1<8:
                if boardc[y-i-1][x+i+1]>=0:
                    if boardc[y-i-1][x+i+1]!=0:
                        childrenX.append(30+i+1)
                        break
                    else:
                        childrenX.append(30+i+1)
                else:
                    break
            else:
                break
    elif player==3:
        #ur
        for i in range(7):
            if x+i+1<8 and y+i+1<8:
                if boardc[y+i+1][x+i+1]<=0:
                    if boardc[y+i+1][x+i+1]!=0:
                        childrenX.append(i+1)
                        break
                    else:
                        childrenX.append(i+1)
                else:
                    break
            else:
                break
        #ol
        for i in range(7):
            if y-i-1>-1 and x-i-1>-1:
                if boardc[y-i-1][x-i-1]<=0:
                    if boardc[y-i-1][x-i-1]!=0:
                        childrenX.append(10+i+1)
                        break
                    else:
                        childrenX.append(10+i+1)
                else:
                    break
            else:
                break
        #ul
        for i in range(7):
            if y+i+1<8 and x-i-1>-1:
                if boardc[y+i+1][x-i-1]<=0:
                    if boardc[y+i+1][x-i-1]!=0:
                        childrenX.append(20+i+1)
                        break
                    else:
                        childrenX.append(20+i+1)
                else:
                    break
            else:
                break
        #or
        for i in range(7):
            if y-i-1>-1 and x+i+1<8:
                if boardc[y-i-1][x+i+1]<=0:
                    if boardc[y-i-1][x+i+1]!=0:
                        childrenX.append(30+i+1)
                        break
                    else:
                        childrenX.append(30+i+1)
                else:
                    break
            else:
                break
    #
    if childrenX==[]:
        return []
    else:
        n=random.choice(childrenX)
        #ur
        if n<10:
            boardc[y][x]=0
            boardc[y+n][x+n]=player
            return boardc
        #ol
        elif n<20 and n>10:
            boardc[y][x]=0
            boardc[y-(n-10)][x-(n-10)]=player
            return boardc
        #ul
        elif n<30 and n>20:
            boardc[y][x]=0
            boardc[y+(n-20)][x-(n-20)]=player
            return boardc
        #or
        elif n>30:
            boardc[y][x]=0
            boardc[y-(n-30)][x+(n-30)]=3
            return boardc

def gorcQq(y,x,boardc,player):
    childrenQ=[]
    if player==-5:
        #rechts
        for i in range(7):
            if x+i+1<8:
                if boardc[y][x+i+1]>=0:
                    if boardc[y][x+i+1]!=0:
                        childrenQ.append(i+1)
                        break
                    else:
                        childrenQ.append(i+1)
                else:
                    break
            else:
                break
        #unten
        for i in range(7):
            if y+i+1<8:
                if boardc[y+i+1][x]>=0:
                    if boardc[y+i+1][x]!=0:
                        childrenQ.append(10+i+1)
                        break
                    else:
                        childrenQ.append(10+i+1)
                else:
                    break
            else:
                break
        #links
        for i in range(7):
            if x-i-1>-1:
                if boardc[y][x-i-1]>=0:
                    if boardc[y][x-i-1]!=0:
                        childrenQ.append(20+i+1)
                        break
                    else:
                        childrenQ.append(20+i+1)
                else:
                    break
            else:
                break
        #oben
        for i in range(7):
            if y-i-1>-1:
                if boardc[y-i-1][x]>=0:
                    if boardc[y-i-1][x]!=0:
                        childrenQ.append(30+i+1)
                        break
                    else:
                        childrenQ.append(30+i+1)
                else:
                    break
            else:
                break
    elif player==5:
        #rechts
        for i in range(7):
            if x+i+1<8:
                if boardc[y][x+i+1]<=0:
                    if boardc[y][x+i+1]!=0:
                        childrenQ.append(i+1)
                        break
                    else:
                        childrenQ.append(i+1)
                else:
                    break
            else:
                break
        #unten
        for i in range(7):
            if y+i+1<8:
                if boardc[y+i+1][x]<=0:
                    if boardc[y+i+1][x]!=0:
                        childrenQ.append(10+i+1)
                        break
                    else:
                        childrenQ.append(10+i+1)
                else:
                    break
            else:
                break
        #links
        for i in range(7):
            if x-i-1>-1:
                if boardc[y][x-i-1]<=0:
                    if boardc[y][x-i-1]!=0:
                        childrenQ.append(20+i+1)
                        break
                    else:
                        childrenQ.append(20+i+1)
                else:
                    break
            else:
                break
        #oben
        for i in range(7):
            if y-i-1>-1:
                if boardc[y-i-1][x]<=0:
                    if boardc[y-i-1][x]!=0:
                        childrenQ.append(30+i+1)
                        break
                    else:
                        childrenQ.append(30+i+1)
                else:
                    break
            else:
                break
    #
    if player==-5:
        #ur
        for i in range(7):
            if x+i+1<8 and y+i+1<8:
                if boardc[y+i+1][x+i+1]>=0:
                    if boardc[y+i+1][x+i+1]!=0:
                        childrenQ.append(40+i+1)
                        break
                    else:
                        childrenQ.append(40+i+1)
                else:
                    break
            else:
                break
        #ol
        for i in range(7):
            if y-i-1>-1 and x-i-1>-1:
                if boardc[y-i-1][x-i-1]>=0:
                    if boardc[y-i-1][x-i-1]!=0:
                        childrenQ.append(50+i+1)
                        break
                    else:
                        childrenQ.append(50+i+1)
                else:
                    break
            else:
                break
        #ul
        for i in range(7):
            if y+i+1<8 and x-i-1>-1:
                if boardc[y+i+1][x-i-1]>=0:
                    if boardc[y+i+1][x-i-1]!=0:
                        childrenQ.append(60+i+1)
                        break
                    else:
                        childrenQ.append(60+i+1)
                else:
                    break
            else:
                break
        #or
        for i in range(7):
            if y-i-1>-1 and x+i+1<8:
                if boardc[y-i-1][x+i+1]>=0:
                    if boardc[y-i-1][x+i+1]!=0:
                        childrenQ.append(70+i+1)
                        break
                    else:
                        childrenQ.append(70+i+1)
                else:
                    break
            else:
                break
    elif player==5:
        #ur
        for i in range(7):
            if x+i+1<8 and y+i+1<8:
                if boardc[y+i+1][x+i+1]<=0:
                    if boardc[y+i+1][x+i+1]!=0:
                        childrenQ.append(40+i+1)
                        break
                    else:
                        childrenQ.append(40+i+1)
                else:
                    break
            else:
                break
        #ol
        for i in range(7):
            if y-i-1>-1 and x-i-1>-1:
                if boardc[y-i-1][x-i-1]<=0:
                    if boardc[y-i-1][x-i-1]!=0:
                        childrenQ.append(50+i+1)
                        break
                    else:
                        childrenQ.append(50+i+1)
                else:
                    break
            else:
                break
        #ul
        for i in range(7):
            if y+i+1<8 and x-i-1>-1:
                if boardc[y+i+1][x-i-1]<=0:
                    if boardc[y+i+1][x-i-1]!=0:
                        childrenQ.append(60+i+1)
                        break
                    else:
                        childrenQ.append(60+i+1)
                else:
                    break
            else:
                break
        #or
        for i in range(7):
            if y-i-1>-1 and x+i+1<8:
                if boardc[y-i-1][x+i+1]<=0:
                    if boardc[y-i-1][x+i+1]!=0:
                        childrenQ.append(70+i+1)
                        break
                    else:
                        childrenQ.append(70+i+1)
                else:
                    break
            else:
                break
    #
    if childrenQ==[]:
        return []
    else:
        n=random.choice(childrenQ)
        #rechts
        if n<10:
            boardc[y][x]=0
            boardc[y][x+n]=player
            return boardc
        #unten
        elif n<20 and n>10:
            boardc[y][x]=0
            boardc[y+(n-10)][x]=player
            return boardc
        #links
        elif n<30 and n>20:
            boardc[y][x]=0
            boardc[y][x-(n-20)]=player
            return boardc
        #oben
        elif n<40 and n>30:
            boardc[y][x]=0
            boardc[y-(n-30)][x]=player
            return boardc
        #ur
        if n<50 and n>40:
            boardc[y][x]=0
            boardc[y+(n-40)][x+(n-40)]=player
            return boardc
        #ol
        elif n<60 and n>50:
            boardc[y][x]=0
            boardc[y-(n-50)][x-(n-50)]=player
            return boardc
        #ul
        elif n<70 and n>60:
            boardc[y][x]=0
            boardc[y+(n-60)][x-(n-60)]=player
            return boardc
        #or
        elif n>70:
            boardc[y][x]=0
            boardc[y-(n-70)][x+(n-70)]=3
            return boardc

def gorcBb2(y,x,boardc,player):
    childrenB= []
    if player==-1:
        if y==1 and boardc[y+2][x]==0 and boardc[y+1][x]==0:
            childrenB.append(1)
        if y+1<8:
            if boardc[y+1][x]==0:
                childrenB.append(2)
        if x-1>-1 and y+1<8:
            if boardc[y+1][x-1]>0:
                childrenB.append(3)
        if x+1<8 and y+1<8:
            if boardc[y+1][x+1]>0:
                childrenB.append(4)
        #en passant
        if x-1>-1 and y+1<8:
            if boardc[y][x-1]==9 and boardc[y+1][x-1]==0:
                childrenB.append(5)
        if x+1<8 and y+1<8:
            if boardc[y][x+1]==9 and boardc[y+1][x+1]==0:
                childrenB.append(6)
    if player==1:
        if y==6 and boardc[y-2][x]==0 and boardc[y-1][x]==0:
            childrenB.append(1)
        if y-1>-1:
            if boardc[y-1][x]==0:
                childrenB.append(2)
        if x-1>-1 and y-1>-1:
            if boardc[y-1][x-1]<0:
                childrenB.append(3)
        if x+1<8 and y-1>-1:
            if boardc[y-1][x+1]<0:
                childrenB.append(4)
        #en passant
        if x-1>-1 and y-1>-1:
            if boardc[y][x-1]==-9 and boardc[y-1][x-1]==0:
                childrenB.append(5)
        if x+1<8 and y-1>-1:
            if boardc[y][x+1]==-9 and boardc[y-1][x+1]==0:
                childrenB.append(6)
    if player==-1:
        if childrenB==[]:
            return []
        else:
            n=random.choice(childrenB)
            if n==1:
                boardc[y][x]=0
                boardc[y+2][x]=-9
                return boardc
            elif n==2:
                boardc[y][x]=0
                boardc[y+1][x]=-1
                if y+1==7:
                    boardc[y+1][x]=-5
                return boardc
            elif n==3:
                boardc[y][x]=0
                boardc[y+1][x-1]=-1
                if y+1==7:
                    boardc[y+1][x-1]=-5
                return boardc
            elif n==4:
                boardc[y][x]=0
                boardc[y+1][x+1]=-1
                if y+1==7:
                    boardc[y+1][x+1]=-5
                return boardc
            elif n==5:
                boardc[y][x]=0
                boardc[y+1][x-1]=-1
                boardc[y][x-1]=0
                return boardc
            elif n==6:
                boardc[y][x]=0
                boardc[y+1][x+1]=-1
                boardc[y][x+1]=0
                return boardc
    elif player==1:
        if childrenB==[]:
            return []
        else:
            n=random.choice(childrenB)
            if n==1:
                boardc[y][x]=0
                boardc[y-2][x]=9
                return boardc
            elif n==2:
                boardc[y][x]=0
                boardc[y-1][x]=1
                if y-1==0:
                    boardc[y-1][x]=5
                return boardc
            elif n==3:
                boardc[y][x]=0
                boardc[y-1][x-1]=1
                if y-1==0:
                    boardc[y-1][x-1]=5
                return boardc
            elif n==4:
                boardc[y][x]=0
                boardc[y-1][x+1]=1
                if y-1==0:
                    boardc[y-1][x+1]=5
                return boardc
            elif n==5:
                boardc[y][x]=0
                boardc[y-1][x-1]=1
                boardc[y][x-1]=0
                return boardc
            elif n==6:
                boardc[y][x]=0
                boardc[y-1][x+1]=1
                boardc[y][x+1]=0
                return boardc

#gorc simpl

def generate_one_random_child(position, playerk):#für MCTS Simulation
    #wählt random Spielfigur aus, gen moves für Figur, wählt random move -> not all moves are equal, schneller
    boardcopy = copy.deepcopy(position)
    #
    #9&-9 zu 1&-1
    if playerk==6:
        for y in range(len(boardcopy)):
            for x in range(len(boardcopy[y])):
                if boardcopy[y][x]==9:
                    boardcopy[y][x]=1
    elif playerk==-6:
        for y in range(len(boardcopy)):
            for x in range(len(boardcopy[y])):
                if boardcopy[y][x]==-9:
                    boardcopy[y][x]=-1
    #
    piecesy=[]
    piecesx=[]
    if playerk==6:
        for y in range(8):
            for x in range(8):
                if boardcopy[y][x]>0:
                    piecesy.append(y)
                    piecesx.append(x)
    elif playerk==-6:
        for y in range(8):
            for x in range(8):
                if boardcopy[y][x]<0:
                    piecesy.append(y)
                    piecesx.append(x)
    #
    if piecesx==[]:
        return []
    #
    while True:
        n = random.randint(0, len(piecesy) - 1)
        y = piecesy[n]
        x = piecesx[n]

        if boardcopy[y][x] == 1 or boardcopy[y][x] == -1:
            child = gorcBb(y, x, boardcopy, boardcopy[y][x])
        elif boardcopy[y][x] == 2 or boardcopy[y][x] == -2:
            child = gorcLl(y, x, boardcopy, boardcopy[y][x])
        elif boardcopy[y][x] == 3 or boardcopy[y][x] == -3:
            child = gorcXx(y, x, boardcopy, boardcopy[y][x])
        elif boardcopy[y][x] == 4 or boardcopy[y][x] == -4 or boardcopy[y][x] == -7 or boardcopy[y][x] == 7:
            child = gorcTt(y, x, boardcopy, boardcopy[y][x])
        elif boardcopy[y][x] == 5 or boardcopy[y][x] == -5:
            child = gorcQq(y, x, boardcopy, boardcopy[y][x])
        elif boardcopy[y][x] == 6 or boardcopy[y][x] == -6 or boardcopy[y][x] == -8 or boardcopy[y][x] == 8:
            child = gorcKk(y, x, boardcopy, boardcopy[y][x])
        #
        if child!=[]: 
            return child

def gorcLl(y, x, boardc, player):
    childrenL=[]
    moves=[(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
    #
    for move in moves:
        new_y= y+move[0]
        new_x= x+move[1]
        if -1<new_y<8 and -1<new_x<8:
            if (player==-2 and boardc[new_y][new_x]>=0) or (player==2 and boardc[new_y][new_x]<=0):
                childrenL.append((new_y, new_x))
    #
    if childrenL!=[]:
        chosen_move=random.choice(childrenL)
        new_y=chosen_move[0]
        new_x=chosen_move[1]
        boardc[y][x]=0
        boardc[new_y][new_x]=player
        return boardc
    else:
        return []

def gorcBb(y,x,boardc,player):
    childrenB= []
    if player==-1:
        if y==1 and boardc[y+2][x]==0 and boardc[y+1][x]==0:
            childrenB.append(1)
        if y+1<8:
            if boardc[y+1][x]==0:
                childrenB.append(2)
        if x-1>-1 and y+1<8:
            if boardc[y+1][x-1]>0:
                childrenB.append(3)
        if x+1<8 and y+1<8:
            if boardc[y+1][x+1]>0:
                childrenB.append(4)
        #en passant
        if x-1>-1 and y+1<8:
            if boardc[y][x-1]==9 and boardc[y+1][x-1]==0:
                childrenB.append(5)
        if x+1<8 and y+1<8:
            if boardc[y][x+1]==9 and boardc[y+1][x+1]==0:
                childrenB.append(6)
    if player==1:
        if y==6 and boardc[y-2][x]==0 and boardc[y-1][x]==0:
            childrenB.append(1)
        if y-1>-1:
            if boardc[y-1][x]==0:
                childrenB.append(2)
        if x-1>-1 and y-1>-1:
            if boardc[y-1][x-1]<0:
                childrenB.append(3)
        if x+1<8 and y-1>-1:
            if boardc[y-1][x+1]<0:
                childrenB.append(4)
        #en passant
        if x-1>-1 and y-1>-1:
            if boardc[y][x-1]==-9 and boardc[y-1][x-1]==0:
                childrenB.append(5)
        if x+1<8 and y-1>-1:
            if boardc[y][x+1]==-9 and boardc[y-1][x+1]==0:
                childrenB.append(6)
    if player==-1:
        if childrenB==[]:
            return []
        else:
            n=random.choice(childrenB)
            if n==1:
                boardc[y][x]=0
                boardc[y+2][x]=-9
                return boardc
            elif n==2:
                boardc[y][x]=0
                boardc[y+1][x]=-1
                if y+1==7:
                    boardc[y+1][x]=-5
                return boardc
            elif n==3:
                boardc[y][x]=0
                boardc[y+1][x-1]=-1
                if y+1==7:
                    boardc[y+1][x-1]=-5
                return boardc
            elif n==4:
                boardc[y][x]=0
                boardc[y+1][x+1]=-1
                if y+1==7:
                    boardc[y+1][x+1]=-5
                return boardc
            elif n==5:
                boardc[y][x]=0
                boardc[y+1][x-1]=-1
                boardc[y][x-1]=0
                return boardc
            elif n==6:
                boardc[y][x]=0
                boardc[y+1][x+1]=-1
                boardc[y][x+1]=0
                return boardc
    elif player==1:
        if childrenB==[]:
            return []
        else:
            n=random.choice(childrenB)
            if n==1:
                boardc[y][x]=0
                boardc[y-2][x]=9
                return boardc
            elif n==2:
                boardc[y][x]=0
                boardc[y-1][x]=1
                if y-1==0:
                    boardc[y-1][x]=5
                return boardc
            elif n==3:
                boardc[y][x]=0
                boardc[y-1][x-1]=1
                if y-1==0:
                    boardc[y-1][x-1]=5
                return boardc
            elif n==4:
                boardc[y][x]=0
                boardc[y-1][x+1]=1
                if y-1==0:
                    boardc[y-1][x+1]=5
                return boardc
            elif n==5:
                boardc[y][x]=0
                boardc[y-1][x-1]=1
                boardc[y][x-1]=0
                return boardc
            elif n==6:
                boardc[y][x]=0
                boardc[y-1][x+1]=1
                boardc[y][x+1]=0
                return boardc

def gorcKk(y,x,boardc,player):
    childrenK= []
    #
    moves = [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)]
    counter=0
    for move in moves:
        dy=move[0]
        dx=move[1]
        new_y=y+dy
        new_x=x+dx
        if -1<new_y<8 and -1<new_x<8:
            if (player==-6 or player==-8) and boardc[new_y][new_x]>=0:
                childrenK.append(counter)
            elif (player==6 or player==8) and boardc[new_y][new_x]<=0:
                childrenK.append(counter)
        counter+=1
    #
    #rochade
    if player==-8:
        if boardc[0][0]==-7 and boardc[0][1]==0 and boardc[0][2]==0 and boardc[0][3]==0:
            boardcc=copy.deepcopy(boardc)
            boardcc[0][2]=-6
            boardcc[0][3]=-4
            boardcc[0][0]=0
            boardcc[0][4]=0
            legal=True
            for child in genchildren(boardcc,6):
                if child[0][2]>0 or child[0][3]>0 or child[0][4]>0:
                    legal=False
                    break
            if legal:
                childrenK.append(8)
        if boardc[0][7]==-7 and boardc[0][6]==0 and boardc[0][5]==0:
            boardcc=copy.deepcopy(boardc)
            boardcc[0][6]=-6
            boardcc[0][5]=-4
            boardcc[0][7]=0
            boardcc[0][4]=0
            legal=True
            for child in genchildren(boardcc,6):
                if child[0][4]>0 or child[0][5]>0 or child[0][6]>0:
                    legal=False
                    break
            if legal:
                childrenK.append(9)
    elif player==8:
        if boardc[7][0]==7 and boardc[7][1]==0 and boardc[7][2]==0 and boardc[7][3]==0:
            boardcc=copy.deepcopy(boardc)
            boardcc[7][2]=6
            boardcc[7][3]=4
            boardcc[7][0]=0
            boardcc[7][4]=0
            legal=True
            for child in genchildren(boardcc,-6):
                if child[7][2]<0 or child[7][3]<0 or child[7][4]<0:
                    legal=False
                    break
            if legal:
                childrenK.append(10)
        if boardc[7][7]==7 and boardc[7][6]==0 and boardc[7][5]==0:
            boardcc=copy.deepcopy(boardc)
            boardcc[7][6]=6
            boardcc[7][5]=4
            boardcc[7][7]=0
            boardcc[7][4]=0
            legal=True
            for child in genchildren(boardcc,-6):
                if child[7][4]<0 or child[7][5]<0 or child[7][6]<0:
                    legal=False
                    break
            if legal:
                childrenK.append(11)
    #
    if childrenK==[]:
        return []
    else:
        n=random.choice(childrenK)
        if n<8:
            boardc[y][x]=0
            move=moves[n]
            dy=move[0]
            dx=move[1]
            boardc[y+dy][x+dx]=player
            return boardc
        #rochade
        elif n==8:
            boardc[0][2]=-6
            boardc[0][3]=-4
            boardc[0][0]=0
            boardc[0][4]=0
            return boardc
        elif n==9:
            boardc[0][6]=-6
            boardc[0][5]=-4
            boardc[0][7]=0
            boardc[0][4]=0
            return boardc
        elif n==10:
            boardc[7][2]=6
            boardc[7][3]=4
            boardc[7][0]=0
            boardc[7][4]=0
            return boardc
        elif n==11:
            boardc[7][6]=6
            boardc[7][5]=4
            boardc[7][7]=0
            boardc[7][4]=0
            return boardc

def gorcTtXxQq(y, x, boardc, player, directions):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if player==-7:
        player=-4
    elif player==7:
        player=4

    children=[]

    for direction in directions:
        for i in range(1, 8):
            dy=direction[0]
            dx=direction[1]
            new_y = y+i*dy
            new_x = x+i*dx
            if -1<new_x<8 and -1<new_y<8:
                if (player==-4 and boardc[new_y][new_x]>=0) or (player==4 and boardc[new_y][new_x]<=0):
                    if boardc[new_y][new_x]==0:
                        children.append((y+i*dy, x+i*dx))
                    else:
                        children.append((y+i*dy, x+i*dx))
                        break
                else:
                    break
            else:
                break

    if children!=[]:
        move=random.choice(children)
        new_y=move[0]
        new_x=move[1]
        boardc[y][x]=0
        boardc[new_y][new_x]=player
        return boardc
    else:
        return []

#

def verloren(pos,player):
    eval=False
    if player==-6:
        player2=-8
    else:
        player2=8
    for p in range(8):
        for o in range(8):
            if pos[p][o]==player or pos[p][o]==player2:
                eval=True
    if eval:
        return False
    else:
        return True

#

Bb_matrix = [
    [ 0,  0,  0,  0,  0,  0,  0,  0],
    [ 1,  1,  1,  1,  1,  1,  1,  1],
    [ 2,  2,  2,  2,  2,  2,  2,  2],
    [ 3,  3,  4,  4,  4,  4,  3,  3],
    [ 3,  3,  4,  4,  4,  4,  3,  3],
    [ 2,  2,  2,  2,  2,  2,  2,  2],
    [ 1,  1,  1,  1,  1,  1,  1,  1],
    [ 0,  0,  0,  0,  0,  0,  0,  0]
]

Ll_matrix = [
    [-1, -3, -2, -2, -2, -2, -3, -1],
    [-1,  0,  0,  0,  0,  0,  0, -1],
    [-1,  0,  1,  1,  1,  1,  0, -1],
    [-1,  0,  1,  2,  2,  1,  0, -1],
    [-1,  0,  1,  2,  2,  1,  0, -1],
    [-1,  0,  1,  1,  1,  1,  0, -1],
    [-1,  0,  0,  0,  0,  0,  0, -1],
    [-1, -3, -2, -2, -2, -2, -3, -1]
]

Xx_matrix = [
    [-2, -1, -1, -1, -1, -1, -1, -2],
    [-1,  0,  0,  0,  0,  0,  0, -1],
    [-1,  0,  1,  1,  1,  1,  0, -1],
    [-1,  0,  1,  2,  2,  1,  0, -1],
    [-1,  0,  1,  2,  2,  1,  0, -1],
    [-1,  0,  1,  1,  1,  1,  0, -1],
    [-1,  0,  0,  0,  0,  0,  0, -1],
    [-2, -1, -1, -1, -1, -1, -1, -2]
]

Tt_matrix = [
    [ 0,  0,  0,  0,  0,  0,  0,  0],
    [ 1,  1,  1,  1,  1,  1,  1,  1],
    [ 1,  1,  1,  1,  1,  1,  1,  1],
    [ 1,  1,  1,  1,  1,  1,  1,  1],
    [ 1,  1,  1,  1,  1,  1,  1,  1],
    [ 1,  1,  1,  1,  1,  1,  1,  1],
    [ 1,  1,  1,  1,  1,  1,  1,  1],
    [ 0,  0,  0,  0,  0,  0,  0,  0]
]

Qq_matrix = [
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1,  0,  0,  0,  0,  0,  0, -1],
    [-1,  0,  1,  1,  1,  1,  0, -1],
    [-1,  0,  1,  2,  2,  1,  0, -1],
    [-1,  0,  1,  2,  2,  1,  0, -1],
    [-1,  0,  1,  1,  1,  1,  0, -1],
    [-1,  0,  0,  0,  0,  0,  0, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1]
]

K_matrix = [
    [ 2,  3,  1,  0,  0,  1,  3,  2],
    [ 2,  2,  0,  0,  0,  0,  2,  2],
    [-1, -2, -2, -2, -2, -2, -2, -1],
    [-2, -3, -3, -4, -4, -3, -3, -2],
    [-3, -4, -4, -5, -5, -4, -4, -3],
    [-3, -4, -4, -5, -5, -4, -4, -3],
    [-4, -5, -5, -6, -6, -5, -5, -4],
    [-4, -5, -5, -6, -6, -5, -5, -4]
]

k_matrix = [
    [ -4,  -5,  -5,  -6,  -6,  -5,  -5,  -4],
    [ -4,  -5,  -5,  -6,  -6,  -5,  -5,  -4],
    [ -3,  -4,  -4,  -5,  -5,  -4,  -4,  -3],
    [ -3,  -4,  -4,  -5,  -5,  -4,  -4,  -3],
    [ -2,  -3,  -3,  -4,  -4,  -3,  -3,  -2],
    [ -1,  -2,  -2,  -2,  -2,  -2,  -2,  -1],
    [  2,   2,   0,   0,   0,   0,   2,   2],
    [  2,   3,   1,   0,   0,   1,   3,   2]
]


other_Bb_matrix = [[-v for v in row] for row in Bb_matrix]
other_Ll_matrix = [[-v for v in row] for row in Ll_matrix]
other_Xx_matrix = [[-v for v in row] for row in Xx_matrix]
other_Tt_matrix = [[-v for v in row] for row in Tt_matrix]
other_Qq_matrix = [[-v for v in row] for row in Qq_matrix]
other_K_matrix = [[-v for v in row] for row in K_matrix]
other_k_matrix = [[-v for v in row] for row in k_matrix]


def evaluatepos(pos,playerk):
    #mit Matrixen+pawn structure
    val=0
    if playerk==6:
        for p in range(8):
            for o in range(8):
                if pos[p][o]==0:
                    pass
                #
                elif pos[p][o]==-1 or pos[p][o]==-9:
                    val+=-100
                    val+=other_Bb_matrix[p][o]
                    #pawn structure
                    if p+1<=7 and o+1<=7:
                        if pos[p+1][o+1]==-1 or pos[p+1][o+1]==-9:
                            val+=-1
                    if p-1>=0 and o-1>=0:
                        if pos[p-1][o-1]==-1 or pos[p-1][o-1]==-9:
                            val+=-1
                    if p+1<=7 and o-1>=0:
                        if pos[p+1][o-1]==-1 or pos[p+1][o-1]==-9:
                            val+=-1
                    if p-1>=0 and o+1<=7:
                        if pos[p-1][o+1]==-1 or pos[p-1][o+1]==-9:
                            val+=-1
                    #
                elif pos[p][o]==1 or pos[p][o]==9:
                    val+=+100
                    val+=Bb_matrix[p][o]
                    #pawn structure
                    if p+1<=7 and o+1<=7:
                        if pos[p+1][o+1]==1 or pos[p+1][o+1]==9:
                            val+=1
                    if p-1>=0 and o-1>=0:
                        if pos[p-1][o-1]==1 or pos[p-1][o-1]==9:
                            val+=1
                    if p+1<=7 and o-1>=0:
                        if pos[p+1][o-1]==1 or pos[p+1][o-1]==9:
                            val+=1
                    if p-1>=0 and o+1<=7:
                        if pos[p-1][o+1]==1 or pos[p-1][o+1]==9:
                            val+=1
                    #
                #
                elif pos[p][o]==-2:
                    val+=-300
                    val+=other_Ll_matrix[p][o]
                elif pos[p][o]==-3:
                    val+=-300
                    val+=other_Xx_matrix[o][p]
                elif pos[p][o]==-4 or pos[p][o]==-7:
                    val+=-500
                    val+=other_Tt_matrix[p][o]
                elif pos[p][o]==2:
                    val+=+300
                    val+=Ll_matrix[p][o]
                elif pos[p][o]==3:
                    val+=+300
                    val+=Xx_matrix[o][p]
                elif pos[p][o]==4 or pos[p][o]==7:
                    val+=+500
                    val+=Tt_matrix[p][o]
                #
                elif pos[p][o]==-5:
                    val+=-900
                    val+=other_Qq_matrix[p][o]
                elif pos[p][o]==-6 or pos[p][o]==-8:
                    val+=-100000
                    val+=other_K_matrix[p][o]
                elif pos[p][o]==5:
                    val+=+900
                    val+=Qq_matrix[p][o]
                elif pos[p][o]==6 or pos[p][o]==8:
                    val+=100000
                    val+=k_matrix[p][o]
    elif playerk==-6:
        for p in range(8):
            for o in range(8):
                if pos[p][o]==0:
                    pass
                #
                elif pos[p][o]==-1 or pos[p][o]==-9:
                    val+=+100
                    val+=Bb_matrix[p][o]
                    #pawn structure
                    if p+1<=7 and o+1<=7:
                        if pos[p+1][o+1]==-1 or pos[p+1][o+1]==-9:
                            val+=1
                    if p-1>=0 and o-1>=0:
                        if pos[p-1][o-1]==-1 or pos[p-1][o-1]==-9:
                            val+=1
                    if p+1<=7 and o-1>=0:
                        if pos[p+1][o-1]==-1 or pos[p+1][o-1]==-9:
                            val+=1
                    if p-1>=0 and o+1<=7:
                        if pos[p-1][o+1]==-1 or pos[p-1][o+1]==-9:
                            val+=1
                    #
                elif pos[p][o]==1 or pos[p][o]==9:
                    val+=-100
                    val+=other_Bb_matrix[p][o]
                    #pawn structure
                    if p+1<=7 and o+1<=7:
                        if pos[p+1][o+1]==1 or pos[p+1][o+1]==9:
                            val+=-1
                    if p-1>=0 and o-1>=0:
                        if pos[p-1][o-1]==1 or pos[p-1][o-1]==9:
                            val+=-1
                    if p+1<=7 and o-1>=0:
                        if pos[p+1][o-1]==1 or pos[p+1][o-1]==9:
                            val+=-1
                    if p-1>=0 and o+1<=7:
                        if pos[p-1][o+1]==1 or pos[p-1][o+1]==9:
                            val+=-1
                    #
                #
                elif pos[p][o]==-2:
                    val+=+300
                    val+=Ll_matrix[p][o]
                elif pos[p][o]==-3:
                    val+=+300
                    val+=Xx_matrix[p][o]
                elif pos[p][o]==-4 or pos[p][o]==-7:
                    val+=+500
                    val+=Tt_matrix[p][o]
                elif pos[p][o]==2:
                    val+=-300
                    val+=other_Ll_matrix[p][o]
                elif pos[p][o]==3:
                    val+=-300
                    val+=other_Xx_matrix[p][o]
                elif pos[p][o]==4 or pos[p][o]==7:
                    val+=-500
                    val+=other_Tt_matrix[p][o]
                #
                elif pos[p][o]==-5:
                    val+=+900
                    val+=Qq_matrix[p][o]
                elif pos[p][o]==-6 or pos[p][o]==-8:
                    val+=100000
                    val+=K_matrix[p][o]
                elif pos[p][o]==5:
                    val+=-900
                    val+=other_Qq_matrix[p][o]
                elif pos[p][o]==6 or pos[p][o]==8:
                    val+=-100000
                    val+=other_k_matrix[p][o]
    return val

def evaluatepos2(pos,playerk):
    #mit Matrixen
    val=0
    if playerk==6:
        for p in range(8):
            for o in range(8):
                if pos[p][o]==0:
                    pass
                #
                elif pos[p][o]==-1 or pos[p][o]==-9:
                    val+=-100
                    val+=other_Bb_matrix[p][o]
                elif pos[p][o]==1 or pos[p][o]==9:
                    val+=+100
                    val+=Bb_matrix[p][o]
                #
                elif pos[p][o]==-2:
                    val+=-300
                    val+=other_Ll_matrix[p][o]
                elif pos[p][o]==-3:
                    val+=-300
                    val+=other_Xx_matrix[o][p]
                elif pos[p][o]==-4 or pos[p][o]==-7:
                    val+=-500
                    val+=other_Tt_matrix[p][o]
                elif pos[p][o]==2:
                    val+=+300
                    val+=Ll_matrix[p][o]
                elif pos[p][o]==3:
                    val+=+300
                    val+=Xx_matrix[o][p]
                elif pos[p][o]==4 or pos[p][o]==7:
                    val+=+500
                    val+=Tt_matrix[p][o]
                #
                elif pos[p][o]==-5:
                    val+=-900
                    val+=other_Qq_matrix[p][o]
                elif pos[p][o]==-6 or pos[p][o]==-8:
                    val+=-100000
                    val+=other_K_matrix[p][o]
                elif pos[p][o]==5:
                    val+=+900
                    val+=Qq_matrix[p][o]
                elif pos[p][o]==6 or pos[p][o]==8:
                    val+=100000
                    val+=k_matrix[p][o]
    elif playerk==-6:
        for p in range(8):
            for o in range(8):
                if pos[p][o]==0:
                    pass
                #
                elif pos[p][o]==-1 or pos[p][o]==-9:
                    val+=+100
                    val+=Bb_matrix[p][o]
                elif pos[p][o]==1 or pos[p][o]==9:
                    val+=-100
                    val+=other_Bb_matrix[p][o]
                #
                elif pos[p][o]==-2:
                    val+=+300
                    val+=Ll_matrix[p][o]
                elif pos[p][o]==-3:
                    val+=+300
                    val+=Xx_matrix[p][o]
                elif pos[p][o]==-4 or pos[p][o]==-7:
                    val+=+500
                    val+=Tt_matrix[p][o]
                elif pos[p][o]==2:
                    val+=-300
                    val+=other_Ll_matrix[p][o]
                elif pos[p][o]==3:
                    val+=-300
                    val+=other_Xx_matrix[p][o]
                elif pos[p][o]==4 or pos[p][o]==7:
                    val+=-500
                    val+=other_Tt_matrix[p][o]
                #
                elif pos[p][o]==-5:
                    val+=+900
                    val+=Qq_matrix[p][o]
                elif pos[p][o]==-6 or pos[p][o]==-8:
                    val+=100000
                    val+=K_matrix[p][o]
                elif pos[p][o]==5:
                    val+=-900
                    val+=other_Qq_matrix[p][o]
                elif pos[p][o]==6 or pos[p][o]==8:
                    val+=-100000
                    val+=other_k_matrix[p][o]
    return val

def evaluatepos3(pos,playerk):
    #ohne Matrixen
    val=0
    if playerk==6:
        for p in range(8):
            for o in range(8):
                if pos[p][o]==0:
                    pass
                #
                elif pos[p][o]==-1 or pos[p][o]==-9:
                    val=val-100
                elif pos[p][o]==1 or pos[p][o]==9:
                    val=val+100
                #
                elif pos[p][o]==-2:
                    val=val-300
                elif pos[p][o]==-3:
                    val=val-300
                elif pos[p][o]==-4 or pos[p][o]==-7:
                    val=val-500
                elif pos[p][o]==2:
                    val=val+300
                elif pos[p][o]==3:
                    val=val+300
                elif pos[p][o]==4 or pos[p][o]==7:
                    val=val+500
                #
                elif pos[p][o]==-5:
                    val=val-900
                elif pos[p][o]==-6 or pos[p][o]==-8:
                    val+=-100000
                elif pos[p][o]==5:
                    val=val+900
                elif pos[p][o]==6 or pos[p][o]==8:
                    val+=100000
    elif playerk==-6:
        for p in range(8):
            for o in range(8):
                if pos[p][o]==0:
                    pass
                #
                elif pos[p][o]==-1 or pos[p][o]==-9:
                    val=val+100
                elif pos[p][o]==1 or pos[p][o]==9:
                    val=val-100
                #
                elif pos[p][o]==-2:
                    val=val+300
                elif pos[p][o]==-3:
                    val=val+300
                elif pos[p][o]==-4 or pos[p][o]==-7:
                    val=val+500
                elif pos[p][o]==2:
                    val=val-300
                elif pos[p][o]==3:
                    val=val-300
                elif pos[p][o]==4 or pos[p][o]==7:
                    val=val-500
                #
                elif pos[p][o]==-5:
                    val=val+900
                elif pos[p][o]==-6 or pos[p][o]==-8:
                    val+=100000
                elif pos[p][o]==5:
                    val=val-900
                elif pos[p][o]==6 or pos[p][o]==8:
                    val+=-100000
    return val

#

class Schach():
    def __init__(self):
        self.board=[]
        self.turn=0
        self.players=[]
        self.maxturns=200

    def play(self):
        #
        self.board=[
            [-7, -2, -3, -5, -8, -3, -2, -7],
            [-1, -1, -1, -1, -1, -1, -1, -1],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [7, 2, 3, 5, 8, 3, 2, 7]
        ]
        #
        self.players.clear()
        self.players.append(HumanPlayer(6))#k
        self.players.append(MinimaxPlayer(-6))#K
        #
        current=0
        while True:
            print(self.turn)
            printboard(self.board)
            player = self.players[current]
            if player.token==6:
                istamzug='k'
            else:
                istamzug='K'
            print(istamzug, ' ist am Zug')
            nextmove=player.get_move(copy.deepcopy(self.board))
            if nextmove!=[]:
                self.board=nextmove
            else:
                king_captured=False
                if player.token==6:
                    other=-6
                else:
                    other=6
                for child in genchildren(self.board,other):
                    if verloren(child,player.token):
                        king_captured=True
                if not king_captured:
                    print('UNENTSCHIEDEN')
                    return ' '
                else:
                    if player.token==6:
                        print('K HAT GEWONNEN')
                        return 'K'
                    elif player.token==-6:
                        print('k HAT GEWONNEN')
                        return 'k'
            #
            current = (current + 1) % 2
            self.turn+=1
            #
            if self.turn==self.maxturns:#für simulationen
                print('UNENTSCHIEDEN')
                return ' '
            #
        
#

class Player():
    def __init__(self, token):
        self.token = token

    def get_move(self, board):
        raise NotImplementedError('Not implemented')

#

class HumanPlayer(Player):
    def __init__(self, token):
        super().__init__(token)
        self.token=token

    def do_these_two_lists_have_the_same_elements(self, list1, list2):
        for row1, row2 in zip(list1, list2):
            for item1, item2 in zip(row1, row2):
                if item1 != item2:
                    return False
        return True

    def eingabe(self):
        while True:
            try:
                vx = int(input('von x: ')) - 1
                vy = int(input('von y: ')) - 1
                zx = int(input('zu x: ')) - 1
                zy = int(input('zu y: ')) - 1
            except:
                print('EINGABE NICHT KORREKT1')
                continue 

            if vy < 8 and vy > -1 and vx < 8 and vx > -1 and zy < 8 and zy > -1 and zx < 8 and zx > -1:
                return [vy, vx, zy, zx]
            else:
                print('EINGABE NICHT KORREKT1')
                continue 

    def player(self,pos):
        if self.token == 6:
            other_player = -6
        else:
            other_player = 6
        
        legal_moves = []
        legal_move_exists = False
        all_moves=genchildren(pos, self.token)

        for child_of_root in all_moves:
            king_is_killed = False
            for child_of_child in genchildren(child_of_root, other_player):
                if verloren(child_of_child, self.token):
                    king_is_killed = True
                    break
            if not king_is_killed:
                legal_move_exists = True
                legal_moves.append(child_of_root)
        
        if not legal_move_exists:
            return []
        
        while True:
            boardcopy = copy.deepcopy(pos)
            input_move = self.eingabe()

            vy, vx, zy, zx = input_move

            #update boardcopy
            #1&-1 zu 5&-5
            for feld in range(len(boardcopy[0])):
                if boardcopy[0][feld]==1:
                    boardcopy[0][feld]=5
            for feld in range(len(boardcopy[7])):
                if boardcopy[7][feld]==-1:
                    boardcopy[7][feld]=-5
            #9&-9 entfernen
            if self.token==-6:
                for y in range(len(boardcopy)):
                    for x in range(len(boardcopy[y])):
                        if boardcopy[y][x]==9:
                            boardcopy[y][x]=1
            elif self.token==6:
                for y in range(len(boardcopy)):
                    for x in range(len(boardcopy[y])):
                        if boardcopy[y][x]==-9:
                            boardcopy[y][x]=-1
            #spezielle Züge:
            special=False
            #rochade
            if vy==7 and vx==4 and zy==7 and zx==2 and self.token==6 and boardcopy[vy][vx]==8:
                special=True
                boardcopy[7][2]=6
                boardcopy[7][3]=4
                boardcopy[7][0]=0
                boardcopy[7][4]=0
            if vy==7 and vx==4 and zy==7 and zx==6 and self.token==6 and boardcopy[vy][vx]==8:
                special=True
                boardcopy[7][6]=6
                boardcopy[7][5]=4
                boardcopy[7][7]=0
                boardcopy[7][4]=0
            if vy==0 and vx==4 and zy==0 and zx==2 and self.token==-6 and boardcopy[vy][vx]==-8:
                special=True
                boardcopy[0][2]=-6
                boardcopy[0][3]=-4
                boardcopy[0][0]=0
                boardcopy[0][4]=0
            if vy==0 and vx==4 and zy==0 and zx==6 and self.token==-6 and boardcopy[vy][vx]==-8:
                special=True
                boardcopy[0][6]=-6
                boardcopy[0][5]=-4
                boardcopy[0][7]=0
                boardcopy[0][4]=0
            #Bb 2 nach vorne
            if boardcopy[vy][vx]==1 and vy==6 and boardcopy[zy][zx]==0 and boardcopy[vy-1][vx]==0 and vx==zx and zy==vy-2:
                special=True
                boardcopy[zy][zx]=9
                boardcopy[vy][vx]=0
            if boardcopy[vy][vx]==-1 and vy==1 and boardcopy[zy][zx]==0 and boardcopy[vy+1][vx]==0 and vx==zx and zy==vy+2:
                special=True
                boardcopy[zy][zx]=-9
                boardcopy[vy][vx]=0
            #en passant
            if boardcopy[vy][vx]==1 and zy==vy-1 and zx==vx-1 and boardcopy[zy][zx]==0:
                special=True
                boardcopy[vy][vx]=0
                boardcopy[zy][zx]=1
                boardcopy[vy][zx]=0
            if boardcopy[vy][vx]==1 and zy==vy-1 and zx==vx+1 and boardcopy[zy][zx]==0:
                special=True
                boardcopy[vy][vx]=0
                boardcopy[zy][zx]=1
                boardcopy[vy][zx]=0
            if boardcopy[vy][vx]==-1 and zy==vy+1 and zx==vx-1 and boardcopy[zy][zx]==0:
                special=True
                boardcopy[vy][vx]=0
                boardcopy[zy][zx]=-1
                boardcopy[vy][zx]=0
            if boardcopy[vy][vx]==-1 and zy==vy+1 and zx==vx+1 and boardcopy[zy][zx]==0:
                special=True
                boardcopy[vy][vx]=0
                boardcopy[zy][zx]=-1
                boardcopy[vy][zx]=0
            #normal bew/schlagen
            if not special:
                if boardcopy[vy][vx]==7:
                    boardcopy[zy][zx]=4
                elif boardcopy[vy][vx]==-7:
                    boardcopy[zy][zx]=-4
                elif boardcopy[vy][vx]==8:
                    boardcopy[zy][zx]=6
                elif boardcopy[vy][vx]==-8:
                    boardcopy[zy][zx]=-6
                else:
                    boardcopy[zy][zx]=boardcopy[vy][vx]
                boardcopy[vy][vx]=0
            #
            move_legal = False
            for legal_move in legal_moves:
                if self.do_these_two_lists_have_the_same_elements(boardcopy, legal_move):
                    move_legal = True
                    break
            
            if move_legal:
                return boardcopy
            else:
                printboard(boardcopy)
                print("legal_children")
                for s in legal_moves:
                    printboard(s)
                print("---------------------------------")
                printboard(pos)
                print('EINGABE NICHT KORREKT2')

    def get_move(self, board):
        return self.player(board)   

#

class MCTSPlayer(Player):
    def __init__(self, token):
        super().__init__(token)
        self.counter=0
        self.numberofiterations=0
        #-----
        self.maxtime=5
        self.c=math.sqrt(2)
        self.depth=2
        self.numberofsimulations=30
        #-----
        
    def mcts(self):
        start = time.time()
        #
        while True:
            self.counter+=1
            selectednode=self.rootnode.selectleafnode()
            if selectednode.children==[]:
                selectednode.backpropagate(selectednode.simulate(),selectednode.numberofsimulations)
            else:
                selectednode.expand()
            #
            if (time.time() - start) > self.maxtime:
                break

    def get_move(self,board):
        self.counter=0
        #
        self.rootnode=MCTSNode(self.token)
        self.rootnode.position=board
        self.rootnode.playeramzug=self.token
        self.rootnode.score=0
        self.rootnode.visits=0
        self.rootnode.children=[]
        #
        #
        #Illegale Züge weg
        self.rootnode.expand()
        number_of_legal_moves = 0
        legal_moves = []
        for child_of_root in self.rootnode.children:
            child_of_root.expand()
            king_is_killed = False
            for child_of_child in child_of_root.children:
                if verloren(child_of_child.position, self.rootnode.playeramzug):
                    king_is_killed = True
                    break
            if not king_is_killed:
                legal_moves.append(child_of_root)
                number_of_legal_moves += 1
        #
        self.rootnode.children=legal_moves
        #keine Züge mehr
        print("rootnode children",len(self.rootnode.children))
        print("number_of_legal_moves",number_of_legal_moves)
        if number_of_legal_moves==0:
            return []
        #
        #
        self.mcts()
        print(self.counter)
        bestmove=[]
        highestnumberofvisits=-1
        for rootnodechild in self.rootnode.children:
            if rootnodechild.visits>highestnumberofvisits:
                bestmove=rootnodechild
                highestnumberofvisits=rootnodechild.visits
        return bestmove.position

class MCTSNode(MCTSPlayer):
    def __init__(self,token):
        super().__init__(token)
        #
        self.position=[]
        self.playeramzug=0
        self.parent=None
        self.children=[]
        self.score=0
        self.visits=0
    
    def calculateubc(self):
        par=self.parent
        if self.visits==0:
            ubc=math.inf
        else:
            ubc=(self.score/self.visits)+self.c*(math.sqrt(math.log(par.visits/self.visits)))
        return ubc
    
    def expand(self):
        children=genchildren(self.position,self.playeramzug)
        for i in range(len(children)):
            self.numberofiterations+=1
            instance = MCTSNode(self.token)
            self.children.append(instance)
            #
            instance.position=children[i]
            if self.playeramzug==-6:
                instance.playeramzug=6
            elif self.playeramzug==6:
                instance.playeramzug=-6
            instance.parent=self
            instance.score=0
            instance.visits=0

    def simulate(self):
        value=0
        values=[]
        for j in range(self.numberofsimulations):
            pos=self.position
            player=self.playeramzug
            for i in range(self.depth):
                nextpos=generate_one_random_child(pos,player)
                if nextpos==[]:
                    break
                pos=nextpos
                if player==-1:
                    player=1
                elif player==1:
                    player=-1
            values.append(evaluatepos(pos,self.token))#wichtig das inarow mit token übereinstimmt.-+
        value=sum(values)/len(values)
        return value
    
    def selectleafnode(self):
        children = self.children
        bestvalue = -math.inf
        for child in children:
            ucbofchild = child.calculateubc()
            if ucbofchild > bestvalue:
                bestvalue = ucbofchild
                selectednode = child
        if selectednode.children == []:
            return selectednode
        else:
            return selectednode.selectleafnode()

    def backpropagate(self, newscore, numberofsimulations):
        self.score += newscore
        self.visits += numberofsimulations
        parent=self.parent
        #
        if parent is not None:
            parent.backpropagate(newscore, numberofsimulations)

#

class MinimaxPlayer(Player):
    #sucht bis max zeit erreicht ist, depth =+1, move sorting
    def __init__(self, token):
        super().__init__(token)
        self.maxtime=5
        self.starting_depth=1 #wenn suche bei layer1 nicht fertig wird: crash

    def minimaxer(self, depth, vergangene_zeit):
        start=time.time()
        for child in self.rootnode.children:
            if child.value==None or child.value>-500:#illegal moves are not searched
                child.minimax(-math.inf,math.inf,False, depth)
                print("a ",end="") # child wurde fertig berechnet(und ist legal)
                if ((time.time()+vergangene_zeit) - start) > self.maxtime:
                    break
        #
        values=[]
        for child in self.rootnode.children:
            if child.value>-500:#illegal move cant be chosen
                values.append(child.value)
        #
        if values!=[]:
            bestmoves=[]
            bestvalue=max(values)
            for child in self.rootnode.children:
                if child.value==bestvalue:
                    bestmoves.append(child)
            #output---------
            print("")
            print(values)
            print(bestvalue)
            #---------------
            bestmove=random.choice(bestmoves)
            return bestmove.position
        else:
            print("NO LEGAL MOVES LEFT")
            print(values)
            return []
    
    def get_move(self, board):
        start=time.time()
        global minimax_counter4
        minimax_counter4=0
        #rootnode
        self.rootnode=MinimaxNode()
        self.rootnode.position=board
        self.rootnode.playeramzug=self.token
        self.rootnode.value=None
        self.rootnode.token=self.token
        self.rootnode.depth=0
        self.rootnode.children=self.rootnode.expandnode()
        #
        depth=self.starting_depth
        bestmove=[]
        while (time.time() - start) < self.maxtime:
            print("DEPTH: ",depth)
            move=self.minimaxer(depth,(time.time() - start))
            if move!=[]:
                bestmove=move
            elif move==[] and depth==self.starting_depth+1:#No immediate legal moves left
                return []
            elif move==[]:
                break
            #
            if (time.time() - start) > self.maxtime:
                print("NICHT FERTIG")
            else:
                self.rootnode.sort(True)
                depth+=1
            if depth==20:
                break
            #
        print("---",minimax_counter4)
        return bestmove

class MinimaxNode():
    def __init__(self):
        self.value=None
        self.children=[]
        self.position=[]
        self.playeramzug=None
        self.token=None
        self.depth=None
        self.expanded=False

    def expandnode(self):
        children=genchildren(self.position,self.playeramzug)
        for i in range(len(children)):
            instance=MinimaxNode()
            instance.position=children[i]
            instance.playeramzug = -self.playeramzug
            instance.value=None
            instance.token=self.token
            instance.depth=self.depth+1
            instance.expanded=False
            self.children.append(instance)
        return self.children

    def minimax(self, alpha, beta, maxplayer, maxdepth):
        #
        global minimax_counter4
        minimax_counter4+=1
        #
        if self.playeramzug==6:
            other_player=-6
        else:
            other_player=6
        #
        if verloren(self.position, self.playeramzug):
            self.value = evaluatepos(self.position, self.token)
            return self.value
        #
        elif verloren(self.position, other_player):
            self.value = evaluatepos(self.position, self.token)
            return self.value
        #
        elif self.depth==maxdepth:
            self.value = evaluatepos(self.position, self.token)
            return self.value
        #
        if not self.expanded:
            self.expandnode()
            self.expanded=True
        #
        if self.children == []:
            self.value = evaluatepos(self.position, self.token)
            return self.value
        #
        if maxplayer:
            maxvalue = -math.inf
            for child in self.children:
                eval = child.minimax(alpha, beta, False, maxdepth)
                if eval>maxvalue:
                    maxvalue=eval
                # pruning
                if eval > alpha:
                    alpha = eval
                if beta <= alpha:
                    break
            self.value=maxvalue
            return maxvalue
        #
        else:
            minvalue = math.inf
            for child in self.children:
                eval = child.minimax(alpha, beta, True, maxdepth)
                if eval<minvalue:
                    minvalue=eval
                # pruning
                if eval < beta:
                    beta = eval
                if beta <= alpha:
                    break
            self.value=minvalue
            return minvalue
        
    def sort(self, maxplayer):
        not_none_children=[]
        none_children=[]
        for child in self.children:
            if child.value==None:
                none_children.append(child)
            else:
                not_none_children.append(child)
        #
        if maxplayer:
            sorted_children = sorted(not_none_children, key=lambda x: x.value, reverse=True)
            sorted_children.extend(none_children)
            self.children=sorted_children
            #
            for child in not_none_children:
                child.sort(False)
        #
        else:
            sorted_children = sorted(not_none_children, key=lambda x: x.value, reverse=False)
            sorted_children.extend(none_children)
            self.children=sorted_children
            #
            for child in not_none_children:
                child.sort(True)

#

def spielen(z):
    game =Schach()
    K_wins = 0
    k_wins=0
    unentschieden=0
    for i in range(z):
        game.turn=0
        r=game.play() 
        if r== 'K':
            K_wins += 1
        elif r=='k':
            k_wins+=1
        else:
            unentschieden+=1
        print('K:',K_wins)
        print('k:',k_wins)
        print('-:',unentschieden)
    print('FERTIG')

spielen(3)

#

#----------------------------------------------------------------test
board=[
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,-1,1,-1,0,0,0],
    [0,0,1,-6,1,0,0,0],
    [0,0,-1,1,-1,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
]

def test():
    for child in genchildren(board,-6):
        printboard(child)

#test()

#printboard(board)
#print(evaluatepos(board,6))
#----------------------------------------------------------------test

#evaluatepos verbessern mobility?
#board