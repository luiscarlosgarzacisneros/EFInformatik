import copy
import time
import random


#1:b
#2:l
#3:x
#4:t
#5:q
#6:k

#
minimaxc = 0
d = 4
nextmoves = []
scores = []
move = []
moves=[]
bestscores=[]
maxtime = 20
firstchildren=[]

#

def genchildren(position, playerk):
    children = []
    boardcopy = copy.deepcopy(position)
    #
    if playerk==6:
        y = 0
        for i in range(8):
            x = 0
            for j in range(8):
                if boardcopy[y][x]==1:
                    for h in gcBb(y,x,boardcopy,1):
                        children.append(h)
                if boardcopy[y][x]==6:
                    for h in gcKk(y,x,boardcopy,6):
                        children.append(h)
                if boardcopy[y][x]==4:
                    for h in gcTt(y,x,boardcopy,4):
                        children.append(h)
                if boardcopy[y][x]==3:
                    for h in gcXx(y,x,boardcopy,3):
                        children.append(h)
                if boardcopy[y][x]==5:
                    for h in gcQq(y,x,boardcopy,5):
                        children.append(h)
                if boardcopy[y][x]==2:
                    for h in gcLl(y,x,boardcopy,2):
                        children.append(h)

                x = x + 1
            y = y + 1
    if playerk==-6:
        y = 0
        for i in range(8):
            x = 0
            for j in range(8):
                if boardcopy[y][x]==-1:
                    for h in gcBb(y,x,boardcopy,-1):
                        children.append(h)
                if boardcopy[y][x]==-6:
                    for h in gcKk(y,x,boardcopy,-6):
                        children.append(h)
                if boardcopy[y][x]==-4:
                    for h in gcTt(y,x,boardcopy,-4):
                        children.append(h)
                if boardcopy[y][x]==-3:
                    for h in gcXx(y,x,boardcopy,-3):
                        children.append(h)
                if boardcopy[y][x]==-5:
                    for h in gcQq(y,x,boardcopy,-5):
                        children.append(h)
                if boardcopy[y][x]==-3:
                    for h in gcLl(y,x,boardcopy,-3):
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
    if player==-6:
        if y+1<8 and x+1<8:
            if boardc[y+1][x+1]>=0:
                boardc[y][x]=0
                boardc[y+1][x+1]=-6
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
        if y+1<8 and x-1>-1:
            if boardc[y+1][x-1]>=0:
                boardc[y][x]=0
                boardc[y+1][x-1]=-6
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
        if y-1>-1 and x+1<8:
            if boardc[y-1][x+1]>=0:
                boardc[y][x]=0
                boardc[y-1][x+1]=-6
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
        if y-1>-1 and x+1<8:
            if boardc[y-1][x-1]>=0:
                boardc[y][x]=0
                boardc[y-1][x-1]=-6
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
        if x+1<8:
            if boardc[y][x+1]>=0:
                boardc[y][x]=0
                boardc[y][x+1]=-6
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
        if x-1>-1:
            if boardc[y][x-1]>=0:
                boardc[y][x]=0
                boardc[y][x-1]=-6
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
        if y+1<8:
            if boardc[y+1][x]>=0:
                boardc[y][x]=0
                boardc[y+1][x]=-6
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
        if y-1>-1:
            if boardc[y-1][x]>=0:
                boardc[y][x]=0
                boardc[y-1][x]=-6
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
    if player==6:
        if y+1<8 and x+1<8:
            if boardc[y+1][x+1]<=0:
                boardc[y][x]=0
                boardc[y+1][x+1]=6
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
        if y+1<8 and x-1>-1:
            if boardc[y+1][x-1]<=0:
                boardc[y][x]=0
                boardc[y+1][x-1]=6
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
        if y-1>-1 and x+1<8:
            if boardc[y-1][x+1]<=0:
                boardc[y][x]=0
                boardc[y-1][x+1]=6
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
        if y-1>-1 and x+1<8:
            if boardc[y-1][x-1]<=0:
                boardc[y][x]=0
                boardc[y-1][x-1]=6
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
        if x+1<8:
            if boardc[y][x+1]<=0:
                boardc[y][x]=0
                boardc[y][x+1]=6
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
        if x-1>-1:
            if boardc[y][x-1]<=0:
                boardc[y][x]=0
                boardc[y][x-1]=6
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
        if y+1<8:
            if boardc[y+1][x]<=0:
                boardc[y][x]=0
                boardc[y+1][x]=6
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
        if y-1>-1:
            if boardc[y-1][x]<=0:
                boardc[y][x]=0
                boardc[y-1][x]=6
                childrenK.append(boardc)
                boardc=copy.deepcopy(pos)
    return childrenK

def gcLl(y,x,pos,player):
    boardc=copy.deepcopy(pos)
    childrenL= []
    if player==-2:
        if y-2>-1 and x+1<8:
            if boardc[y-2][x+1]>=0:
                boardc[y][x]=0
                boardc[y-2][x+1]=-2
                childrenL.append(boardc)
                boardc=copy.deepcopy(pos)
        if y-2>-1 and x-1>-1:
            if boardc[y-2][x-1]>=0:
                boardc[y][x]=0
                boardc[y-2][x-1]=-2
                childrenL.append(boardc)
                boardc=copy.deepcopy(pos)
        if y+2<8 and x+1<8:
            if boardc[y+2][x+1]>=0:
                boardc[y][x]=0
                boardc[y+2][x+1]=-2
                childrenL.append(boardc)
                boardc=copy.deepcopy(pos)
        if y+2<8 and x-1>-1:
            if boardc[y+2][x-1]>=0:
                boardc[y][x]=0
                boardc[y+2][x-1]=-2
                childrenL.append(boardc)
                boardc=copy.deepcopy(pos)
        if y+1<8 and x+2<8:
            if boardc[y+1][x+2]>=0:
                boardc[y][x]=0
                boardc[y+1][x+2]=-2
                childrenL.append(boardc)
                boardc=copy.deepcopy(pos)
        if y-1>-1 and x+2<8:
            if boardc[y-1][x+2]>=0:
                boardc[y][x]=0
                boardc[y-1][x+2]=-2
                childrenL.append(boardc)
                boardc=copy.deepcopy(pos)
        if y+1<8 and x-2>-1:
            if boardc[y+1][x-2]>=0:
                boardc[y][x]=0
                boardc[y+1][x-2]=-2
                childrenL.append(boardc)
                boardc=copy.deepcopy(pos)
        if y-1>-1 and x-2>-1:
            if boardc[y-1][x-2]>=0:
                boardc[y][x]=0
                boardc[y-1][x-2]=-2
                childrenL.append(boardc)
                boardc=copy.deepcopy(pos)
    if player==2:
        if y-2>-1 and x+1<8:
            if boardc[y-2][x+1]<=0:
                boardc[y][x]=0
                boardc[y-2][x+1]=2
                childrenL.append(boardc)
                boardc=copy.deepcopy(pos)
        if y-2>-1 and x-1>-1:
            if boardc[y-2][x-1]<=0:
                boardc[y][x]=0
                boardc[y-2][x-1]=2
                childrenL.append(boardc)
                boardc=copy.deepcopy(pos)
        if y+2<8 and x+1<8:
            if boardc[y+2][x+1]<=0:
                boardc[y][x]=0
                boardc[y+2][x+1]=2
                childrenL.append(boardc)
                boardc=copy.deepcopy(pos)
        if y+2<8 and x-1>-1:
            if boardc[y+2][x-1]<=0:
                boardc[y][x]=0
                boardc[y+2][x-1]=2
                childrenL.append(boardc)
                boardc=copy.deepcopy(pos)
        if y+1<8 and x+2<8:
            if boardc[y+1][x+2]<=0:
                boardc[y][x]=0
                boardc[y+1][x+2]=2
                childrenL.append(boardc)
                boardc=copy.deepcopy(pos)
        if y-1>-1 and x+2<8:
            if boardc[y-1][x+2]<=0:
                boardc[y][x]=0
                boardc[y-1][x+2]=2
                childrenL.append(boardc)
                boardc=copy.deepcopy(pos)
        if y+1<8 and x-2>-1:
            if boardc[y+1][x-2]<=0:
                boardc[y][x]=0
                boardc[y+1][x-2]=2
                childrenL.append(boardc)
                boardc=copy.deepcopy(pos)
        if y-1>-1 and x-2>-1:
            if boardc[y-1][x-2]<=0:
                boardc[y][x]=0
                boardc[y-1][x-2]=2
                childrenL.append(boardc)
                boardc=copy.deepcopy(pos)
    return childrenL

def gcTt(y,x,pos,player):
    boardc=copy.deepcopy(pos)
    childrenT= []
    if player==-4:
        for i in range(7):
            if x+i+1<8:
                if boardc[y][x+i+1]>=0:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=0
                    boardc[y][x+i+1]=-4
                    childrenT.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y][x+i+1]!=0:
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y+i+1<8:
                if boardc[y+i+1][x]>=0:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=0
                    boardc[y+i+1][x]=-4
                    childrenT.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y+i+1][x]!=0:
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if x-i-1>-1:
                if boardc[y][x-i-1]>=0:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=0
                    boardc[y][x-i-1]=-4
                    childrenT.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y][x-i-1]!=0:
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1:
                if boardc[y-i-1][x]>=0:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=0
                    boardc[y-i-1][x]=-4
                    childrenT.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y-i-1][x]!=0:
                        break
                else:
                    break
            else:
                break
    if player==4:
        for i in range(7):
            if x+i+1<8:
                if boardc[y][x+i+1]<=0:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=0
                    boardc[y][x+i+1]=4
                    childrenT.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y][x+i+1]!=0:
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y+i+1<8:
                if boardc[y+i+1][x]<=0:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=0
                    boardc[y+i+1][x]=4
                    childrenT.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y+i+1][x]!=0:
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if x-i-1>-1:
                if boardc[y][x-i-1]<=0:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=0
                    boardc[y][x-i-1]=4
                    childrenT.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y][x-i-1]!=0:
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1:
                if boardc[y-i-1][x]<=0:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=0
                    boardc[y-i-1][x]=4
                    childrenT.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y-i-1][x]!=0:
                        break
                else:
                    break
            else:
                break
    return childrenT

def gcXx(y,x,pos,player):
    boardc=copy.deepcopy(pos)
    childrenX= []
    if player==-3:
        for i in range(7):
            if x+i+1<8 and y+i+1<8:
                if boardc[y+i+1][x+i+1]>=0:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=0
                    boardc[y+i+1][x+i+1]=-3
                    childrenX.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y+i+1][x+i+1]!=0:
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1 and x-i-1>-1:
                if boardc[y-i-1][x-i-1]>=0:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=0
                    boardc[y-i-1][x-i-1]=-3
                    childrenX.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y-i-1][x-i-1]!=0:
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y+i+1<8 and x-i-1>-1:
                if boardc[y+i+1][x-i-1]>=0:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=0
                    boardc[y+i+1][x-i-1]=-3
                    childrenX.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y+i+1][x-i-1]!=0:
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1 and x+i+1<8:
                if boardc[y-i-1][x+i+1]>=0:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=0
                    boardc[y-i-1][x+i+1]=-3
                    childrenX.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y-i-1][x+i+1]!=0:
                        break
                else:
                    break
            else:
                break
    if player==3:
        for i in range(7):
            if x+i+1<8 and y+i+1<8:
                if boardc[y+i+1][x+i+1]<=0:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=0
                    boardc[y+i+1][x+i+1]=3
                    childrenX.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y+i+1][x+i+1]!=0:
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1 and x-i-1>-1:
                if boardc[y-i-1][x-i-1]<=0:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=0
                    boardc[y-i-1][x-i-1]=3
                    childrenX.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y-i-1][x-i-1]!=0:
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y+i+1<8 and x-i-1>-1:
                if boardc[y+i+1][x-i-1]<=0:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=0
                    boardc[y+i+1][x-i-1]=3
                    childrenX.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y+i+1][x-i-1]!=0:
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1 and x+i+1<8:
                if boardc[y-i-1][x+i+1]<=0:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=0
                    boardc[y-i-1][x+i+1]=3
                    childrenX.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y-i-1][x+i+1]!=0:
                        break
                else:
                    break
            else:
                break
    return childrenX

def gcQq(y,x,pos,player):
    boardc=copy.deepcopy(pos)
    childrenQ= []
    if player==-5:
        for i in range(7):
            if x+i+1<8:
                if boardc[y][x+i+1]>=0:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=0
                    boardc[y][x+i+1]=-5
                    childrenQ.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y][x+i+1]!=0:
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y+i+1<8:
                if boardc[y+i+1][x]>=0:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=0
                    boardc[y+i+1][x]=-5
                    childrenQ.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y+i+1][x]!=0:
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if x-i-1>-1:
                if boardc[y][x-i-1]>=0:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=0
                    boardc[y][x-i-1]=-5
                    childrenQ.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y][x-i-1]!=0:
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1:
                if boardc[y-i-1][x]>=0:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=0
                    boardc[y-i-1][x]=-5
                    childrenQ.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y-i-1][x]!=0:
                        break
                else:
                    break
            else:
                break
    if player==5:
        for i in range(7):
            if x+i+1<8:
                if boardc[y][x+i+1]<=0:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=0
                    boardc[y][x+i+1]=5
                    childrenQ.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y][x+i+1]!=0:
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y+i+1<8:
                if boardc[y+i+1][x]<=0:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=0
                    boardc[y+i+1][x]=5
                    childrenQ.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y+i+1][x]!=0:
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if x-i-1>-1:
                if boardc[y][x-i-1]<=0:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=0
                    boardc[y][x-i-1]=5
                    childrenQ.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y][x-i-1]!=0:
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1:
                if boardc[y-i-1][x]<=0:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=0
                    boardc[y-i-1][x]=5
                    childrenQ.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y-i-1][x]!=0:
                        break
                else:
                    break
            else:
                break
    if player==-5:
        for i in range(7):
            if x+i+1<8 and y+i+1<8:
                if boardc[y+i+1][x+i+1]>=0:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=0
                    boardc[y+i+1][x+i+1]=-5
                    childrenQ.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y+i+1][x+i+1]!=0:
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1 and x-i-1>-1:
                if boardc[y-i-1][x-i-1]>=0:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=0
                    boardc[y-i-1][x-i-1]=-5
                    childrenQ.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y-i-1][x-i-1]!=0:
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y+i+1<8 and x-i-1>-1:
                if boardc[y+i+1][x-i-1]>=0:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=0
                    boardc[y+i+1][x-i-1]=-5
                    childrenQ.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y+i+1][x-i-1]!=0:
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1 and x+i+1<8:
                if boardc[y-i-1][x+i+1]>=0:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=0
                    boardc[y-i-1][x+i+1]=-5
                    childrenQ.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y-i-1][x+i+1]!=0:
                        break
                else:
                    break
            else:
                break
    if player==5:
        for i in range(7):
            if x+i+1<8 and y+i+1<8:
                if boardc[y+i+1][x+i+1]<=0:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=0
                    boardc[y+i+1][x+i+1]=5
                    childrenQ.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y+i+1][x+i+1]!=0:
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1 and x-i-1>-1:
                if boardc[y-i-1][x-i-1]<=0:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=0
                    boardc[y-i-1][x-i-1]=5
                    childrenQ.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y-i-1][x-i-1]!=0:
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y+i+1<8 and x-i-1>-1:
                if boardc[y+i+1][x-i-1]<=0:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=0
                    boardc[y+i+1][x-i-1]=5
                    childrenQ.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y+i+1][x-i-1]!=0:
                        break
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1 and x+i+1<8:
                if boardc[y-i-1][x+i+1]<=0:
                    boardcc=copy.deepcopy(boardc)
                    boardc[y][x]=0
                    boardc[y-i-1][x+i+1]=5
                    childrenQ.append(boardc)
                    boardc=copy.deepcopy(pos)
                    if boardcc[y-i-1][x+i+1]!=0:
                        break
                else:
                    break
            else:
                break
    return childrenQ

def gcBb(y,x,pos,player):
    boardc=copy.deepcopy(pos)
    childrenB= []
    if player==-1:
        if y==1 and boardc[y+2][x]==0 and boardc[y+1][x]==0:
            boardc[y][x]=0
            boardc[y+2][x]=-1
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
    if player==1:
        if y==6 and boardc[y-2][x]==0 and boardc[y-1][x]==0:
            boardc[y][x]=0
            boardc[y-2][x]=1
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
    return childrenB

#

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

def evaluatepos(pos,playerk):
    val=0
    if playerk==6:
        for p in range(8):
            for o in range(8):
                if pos[p][o]==-6:
                    val=val-1000
                if pos[p][o]==-5:
                    val=val-9
                if pos[p][o]==-4:
                    val=val-5
                if pos[p][o]==-2:
                    val=val-3
                if pos[p][o]==-3:
                    val=val-3
                if pos[p][o]==-1:
                    val=val-1
                #
                if pos[p][o]==6:
                    val=val+1000
                if pos[p][o]==5:
                    val=val+9
                if pos[p][o]==4:
                    val=val+5
                if pos[p][o]==2:
                    val=val+3
                if pos[p][o]==3:
                    val=val+3
                if pos[p][o]==1:
                    val=val+1
    elif playerk==-6:
        for p in range(8):
            for o in range(8):
                if pos[p][o]==-6:
                    val=val+1000
                if pos[p][o]==-5:
                    val=val+9
                if pos[p][o]==-4:
                    val=val+5
                if pos[p][o]==-2:
                    val=val+3
                if pos[p][o]==-3:
                    val=val+3
                if pos[p][o]==-1:
                    val=val+1
                #
                if pos[p][o]==6:
                    val=val-1000
                if pos[p][o]==5:
                    val=val-9
                if pos[p][o]==4:
                    val=val-5
                if pos[p][o]==2:
                    val=val-3
                if pos[p][o]==3:
                    val=val-3
                if pos[p][o]==1:
                    val=val-1
    return val

#

class Schach():
    def __init__(self):
        self.board=[
            [-4, -2, -3, -5, -6, -3, -2, -4],
            [-1, -1, -1, -1, -1, -1, -1, -1],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [4, 2, 3, 5, 6, 3, 2, 4]
        ]
        self.turn=0
        self.players=[]

    def printboard(self,board):
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
                print(' I ', end='')
            print(i + 1)
            print('---------------------------------')

    def play(self):
        #
        self.board=[
            [-4, -2, -3, -5, -6, -3, -2, -4],
            [-1, -1, -1, -1, -1, -1, -1, -1],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [4, 2, 3, 5, 6, 3, 2, 4]
        ]
        #
        self.players.clear()
        self.players.append(HumanPlayer(6))
        self.players.append(HumanPlayer(-6))
        #
        current=0
        while True:
            print(self.turn)
            self.printboard(self.board)
            player = self.players[current]
            if player.token==6:
                istamzug='k'
            else:
                istamzug='K'
            print(istamzug, ' ist am Zug')
            self.board=player.get_move(copy.deepcopy(self.board))
            current = (current + 1) % 2
            self.turn+=1
            if verloren(self.board,-6) or verloren(self.board,6):
                break
        self.printboard(self.board)
        if verloren(self.board,6):
            print('K HAT GEWONNEN')
            return 'K'
        elif verloren(self.board,-6):
            print('k HAT GEWONNEN')
            return 'k'
        else:
            print('UNENTSCHIEDEN')
            return ' '
        
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
        self.e=[]

    def eingabe(self,pos):
        self.e.clear()
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
            if pos[vy][vx]==1:
                #2nachv
                if vy==6 and pos[zy][zx]==0 and pos[vy-1][vx]==0 and vx==zx and zy==vy-2:
                    korrekt=True
                #1nachv normal bew
                if pos[zy][zx]==0 and vx==zx and zy==vy-1:
                    korrekt=True
                #schlagen
                if pos[zy][zx]<0 and zy==vy-1 and vx-1==zx:
                    korrekt=True
                if pos[zy][zx]<0 and zy==vy-1 and vx+1==zx:
                    korrekt=True
            #B
            if pos[vy][vx]==-1:
                #2nachv
                if vy==1 and pos[zy][zx]==0 and pos[vy+1][vx]==0 and vx==zx and zy==vy+2:
                    korrekt=True
                #1nachv normal bew
                if pos[zy][zx]==0 and vx==zx and zy==vy+1:
                    korrekt=True
                #schlagen
                if pos[zy][zx]>0 and zy==vy+1 and vx-1==zx:
                    korrekt=True
                if pos[zy][zx]>0 and zy==vy+1 and vx+1==zx:
                    korrekt=True
            #kK
            if (pos[vy][vx]==6 and pos[zy][zx]<=0) or (pos[vy][vx]==-6 and pos[zy][zx]>=0):
                #vertikal
                if vx-1==zx and zy==vy:
                    korrekt=True
                if vx+1==zx and zy==vy:
                    korrekt=True
                #horizontal
                if vx==zx and zy==vy-1:
                    korrekt=True
                if vx==zx and zy==vy+1:
                    korrekt=True
                #diagonal
                if vx-1==zx and zy==vy-1:
                    korrekt=True
                if vx+1==zx and zy==vy-1:
                    korrekt=True
                if vx+1==zx and zy==vy+1:
                    korrekt=True
                if vx-1==zx and zy==vy+1:
                    korrekt=True
            #tT
            if (pos[vy][vx]==4 and pos[zy][zx]<=0) or (pos[vy][vx]==-4 and pos[zy][zx]>=0):
                #vertikal
                if vx==zx:
                    #nach unten
                    if vy<zy:
                        pathclear=True
                        f=1
                        while True:
                            if vy+f==zy:
                                break
                            if pos[vy+f][vx]!=0:
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
                            if pos[vy-f][vx]!=0:
                                pathclear=False
                                break
                            f=f+1
                        if pathclear:
                            korrekt=True
                #horizontal
                if vy==zy:
                    #nach rechts
                    if vx<zx:
                        pathclear=True
                        f=1
                        while True:
                            if vx+f==zx:
                                break
                            if pos[vy][vx+f]!=0:
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
                            if pos[vy][vx-f]!=0:
                                pathclear=False
                                break
                            f=f+1
                        if pathclear:
                            korrekt=True
            #xX
            if (pos[vy][vx]==3 and pos[zy][zx]<=0) or (pos[vy][vx]==-3 and pos[zy][zx]>=0):
                pathclear=False
                for u in range(8):
                    if zy>vy and zx>vx:
                        if vx+u+1==zx and vy+u+1==zy:
                            pathclear=True
                            break
                        if pos[vy+u+1][vx+u+1]!=0:
                            break
                    if zy<vy and zx>vx:
                        if vx+u+1==zx and vy-u-1==zy:
                            pathclear=True
                            break
                        if pos[vy-u-1][vx+u+1]!=0:
                            break
                    if zy>vy and zx<vx:
                        if vx-u-1==zx and vy+u+1==zy:
                            pathclear=True
                            break
                        if pos[vy+u+1][vx-1-u]!=0:
                            break
                    if zy<vy and zx<vx:
                        if vx-1-u==zx and vy-u-1==zy:
                            pathclear=True
                            break
                        if pos[vy-u-1][vx-u-1]!=0:
                            break
                if pathclear:
                    korrekt=True
            #qQ
            if (pos[vy][vx]==5 and pos[zy][zx]<=0) or (pos[vy][vx]==-5 and pos[zy][zx]>=0):
                pathcleart=False
                for u in range(8):
                    if zy>vy and zx>vx:
                        if vx+u+1==zx and vy+u+1==zy:
                            pathcleart=True
                            break
                        if pos[vy+u+1][vx+u+1]!=0:
                            break
                    if zy<vy and zx>vx:
                        if vx+u+1==zx and vy-u-1==zy:
                            pathcleart=True
                            break
                        if pos[vy-u-1][vx+u+1]!=0:
                            break
                    if zy>vy and zx<vx:
                        if vx-u-1==zx and vy+u+1==zy:
                            pathcleart=True
                            break
                        if pos[vy+u+1][vx-1-u]!=0:
                            break
                    if zy<vy and zx<vx:
                        if vx-1-u==zx and vy-u-1==zy:
                            pathcleart=True
                            break
                        if pos[vy-u-1][vx-u-1]!=0:
                            break
                if pathcleart:
                    korrekt=True
                #vertikal
                if vx==zx:
                    #nach unten
                    if vy<zy:
                        pathclearl=True
                        f=1
                        while True:
                            if vy+f==zy:
                                break
                            if pos[vy+f][vx]!=0:
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
                            if pos[vy-f][vx]!=0:
                                pathclearl=False
                                break
                            f=f+1
                        if pathclearl:
                            korrekt=True
                #horizontal
                if vy==zy:
                    #nach rechts
                    if vx<zx:
                        pathclearl=True
                        f=1
                        while True:
                            if vx+f==zx:
                                break
                            if pos[vy][vx+f]!=0:
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
                            if pos[vy][vx-f]!=0:
                                pathclearl=False
                                break
                            f=f+1
                        if pathclearl:
                            korrekt=True
            #lL
            if (pos[vy][vx]==2 and pos[zy][zx]<=0) or (pos[vy][vx]==-2 and pos[zy][zx]>=0):
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
            self.e.append(vy)
            self.e.append(vx)
            self.e.append(zy)
            self.e.append(zx)
            return True
        else:
            print('EINGABE NICHT KORREKT')
            return False

    def player(self,pos):
        while True:
            if self.eingabe(pos)==True:
                break
            else:
                continue
        #
        vy = self.e[0]
        vx = self.e[1]
        zy = self.e[2]
        zx = self.e[3]
        #
        pos[zy][zx]=pos[vy][vx]
        pos[vy][vx]=0
        for feld in pos[0]:
            if pos[0][feld]==1:
                pos[0][feld]=5
        for feld in pos[7]:
            if pos[0][feld]==-1:
                pos[0][feld]=-5

    def get_move(self, board):
        self.player(board)
        return board

#

def minimax(position, depth, maxplayer, alpha, beta):
    # X:maxplayer,spieler O:minplayer,computer
    # Spieler
    # alpha: best maxpl, beta: best minpl
    if maxplayer:
        playerj = 6
    else:
        playerj = -6

    # return
    if verloren(position, -6) == True:
        return evaluatepos(position)
    elif verloren(position, 6) == True:
        return evaluatepos(position)
    elif depth == d:
        return evaluatepos(position)
    children=genchildren(position, playerj)
    if children == []:
        return evaluatepos(position)
    #
    if maxplayer:
        maxvalue = -100000000000
        for child in children:
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
        for child in children:
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
    for firstgenchild in genchildren(boa, -6):
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

#

def spielen(z):
    game =Schach()
    K_wins = 0
    k_wins=0
    unentschieden=0
    for i in range(z):
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

spielen(20)

