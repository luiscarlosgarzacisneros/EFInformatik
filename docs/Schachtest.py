import copy
import time
import random
import math


#1:b
#2:l
#3:x
#4:t
#5:q
#6:k
#7:not moved towert
#8:not moved kingk
#9:en passant b

#-1:B
#-2:L
#-3:X
#-4:T
#-5:Q
#-6:K
#-7:not moved towerT
#-8:not moved kingK
#-9:en passant B


#
minimaxc=0
#

def genchildren(position, playerk):
    children = []
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
                elif position[y][x]==9:
                    for h in gcBb(y,x,position,1):
                        children.append(h)
                elif position[y][x]==6:
                    for h in gcKk(y,x,position,6):
                        children.append(h)
                elif position[y][x]==4 or position[y][x]==7:
                    for h in gcTt(y,x,position,4):
                        children.append(h)
                elif position[y][x]==3:
                    for h in gcXx(y,x,position,3):
                        children.append(h)
                elif position[y][x]==5:
                    for h in gcQq(y,x,position,5):
                        children.append(h)
                elif position[y][x]==6:
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
                elif position[y][x]==-9:
                    for h in gcBb(y,x,position,-1):
                        children.append(h)
                elif position[y][x]==-6:
                    for h in gcKk(y,x,position,-6):
                        children.append(h)
                elif position[y][x]==-4 or position[y][x]==-7:
                    for h in gcTt(y,x,position,-4):
                        children.append(h)
                elif position[y][x]==-3:
                    for h in gcXx(y,x,position,-3):
                        children.append(h)
                elif position[y][x]==-5:
                    for h in gcQq(y,x,position,-5):
                        children.append(h)
                elif position[y][x]==-3:
                    for h in gcLl(y,x,position,-3):
                        children.append(h)
                elif position[y][x]==-8:
                    for h in gcKk(y,x,position,-8):
                        children.append(h)
    #
    global minimaxc
    minimaxc = minimaxc + 1
    #
    return children

def gcKk(y,x,pos,player):
    boardc=copy.deepcopy(pos)
    childrenK= []
    if player==-6 or player==-8:
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
    elif player==6 or player==8:
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
                    if boardc[y][x+i+1]!=0:
                        boardc[y][x]=0
                        boardc[y][x+i+1]=-4
                        childrenT.append(boardc)
                        boardc=copy.deepcopy(pos)
                        break
                    else:
                        boardc[y][x]=0
                        boardc[y][x+i+1]=-4
                        childrenT.append(boardc)
                        boardc=copy.deepcopy(pos)
                else:
                    break
            else:
                break
        for i in range(7):
            if y+i+1<8:
                if boardc[y+i+1][x]>=0:
                    if boardc[y+i+1][x]!=0:
                        boardc[y][x]=0
                        boardc[y+i+1][x]=-4
                        childrenT.append(boardc)
                        boardc=copy.deepcopy(pos)
                        break
                    else:
                        boardc[y][x]=0
                        boardc[y+i+1][x]=-4
                        childrenT.append(boardc)
                        boardc=copy.deepcopy(pos)
                else:
                    break
            else:
                break
        for i in range(7):
            if x-i-1>-1:
                if boardc[y][x-i-1]>=0:
                    if boardc[y][x-i-1]!=0:
                        boardc[y][x]=0
                        boardc[y][x-i-1]=-4
                        childrenT.append(boardc)
                        boardc=copy.deepcopy(pos)
                        break
                    else:
                        boardc[y][x]=0
                        boardc[y][x-i-1]=-4
                        childrenT.append(boardc)
                        boardc=copy.deepcopy(pos)
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1:
                if boardc[y-i-1][x]>=0:
                    if boardc[y-i-1][x]!=0:
                        boardc[y][x]=0
                        boardc[y-i-1][x]=-4
                        childrenT.append(boardc)
                        boardc=copy.deepcopy(pos)
                        break
                    else:
                        boardc[y][x]=0
                        boardc[y-i-1][x]=-4
                        childrenT.append(boardc)
                        boardc=copy.deepcopy(pos)
                else:
                    break
            else:
                break
    elif player==4:
        for i in range(7):
            if x+i+1<8:
                if boardc[y][x+i+1]<=0:
                    if boardc[y][x+i+1]!=0:
                        boardc[y][x]=0
                        boardc[y][x+i+1]=4
                        childrenT.append(boardc)
                        boardc=copy.deepcopy(pos)
                        break
                    else:
                        boardc[y][x]=0
                        boardc[y][x+i+1]=4
                        childrenT.append(boardc)
                        boardc=copy.deepcopy(pos)
                else:
                    break
            else:
                break
        for i in range(7):
            if y+i+1<8:
                if boardc[y+i+1][x]<=0:
                    if boardc[y+i+1][x]!=0:
                        boardc[y][x]=0
                        boardc[y+i+1][x]=4
                        childrenT.append(boardc)
                        boardc=copy.deepcopy(pos)
                        break
                    else:
                        boardc[y][x]=0
                        boardc[y+i+1][x]=4
                        childrenT.append(boardc)
                        boardc=copy.deepcopy(pos)
                else:
                    break
            else:
                break
        for i in range(7):
            if x-i-1>-1:
                if boardc[y][x-i-1]<=0:
                    if boardc[y][x-i-1]!=0:
                        boardc[y][x]=0
                        boardc[y][x-i-1]=4
                        childrenT.append(boardc)
                        boardc=copy.deepcopy(pos)
                        break
                    else:
                        boardc[y][x]=0
                        boardc[y][x-i-1]=4
                        childrenT.append(boardc)
                        boardc=copy.deepcopy(pos)
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1:
                if boardc[y-i-1][x]<=0:
                    if boardc[y-i-1][x]!=0:
                        boardc[y][x]=0
                        boardc[y-i-1][x]=4
                        childrenT.append(boardc)
                        boardc=copy.deepcopy(pos)
                        break
                    else:
                        boardc[y][x]=0
                        boardc[y-i-1][x]=4
                        childrenT.append(boardc)
                        boardc=copy.deepcopy(pos)
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
                    if boardc[y+i+1][x+i+1]!=0:
                        boardc[y][x]=0
                        boardc[y+i+1][x+i+1]=-3
                        childrenX.append(boardc)
                        boardc=copy.deepcopy(pos)
                        break
                    else:
                        boardc[y][x]=0
                        boardc[y+i+1][x+i+1]=-3
                        childrenX.append(boardc)
                        boardc=copy.deepcopy(pos)
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1 and x-i-1>-1:
                if boardc[y-i-1][x-i-1]>=0:
                    if boardc[y-i-1][x-i-1]!=0:
                        boardc[y][x]=0
                        boardc[y-i-1][x-i-1]=-3
                        childrenX.append(boardc)
                        boardc=copy.deepcopy(pos)
                        break
                    else:
                        boardc[y][x]=0
                        boardc[y-i-1][x-i-1]=-3
                        childrenX.append(boardc)
                        boardc=copy.deepcopy(pos)
                else:
                    break
            else:
                break
        for i in range(7):
            if y+i+1<8 and x-i-1>-1:
                if boardc[y+i+1][x-i-1]>=0:
                    if boardc[y+i+1][x-i-1]!=0:
                        boardc[y][x]=0
                        boardc[y+i+1][x-i-1]=-3
                        childrenX.append(boardc)
                        boardc=copy.deepcopy(pos)
                        break
                    else:
                        boardc[y][x]=0
                        boardc[y+i+1][x-i-1]=-3
                        childrenX.append(boardc)
                        boardc=copy.deepcopy(pos)
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1 and x+i+1<8:
                if boardc[y-i-1][x+i+1]>=0:
                    if boardc[y-i-1][x+i+1]!=0:
                        boardc[y][x]=0
                        boardc[y-i-1][x+i+1]=-3
                        childrenX.append(boardc)
                        boardc=copy.deepcopy(pos)
                        break
                    else:
                        boardc[y][x]=0
                        boardc[y-i-1][x+i+1]=-3
                        childrenX.append(boardc)
                        boardc=copy.deepcopy(pos)
                else:
                    break
            else:
                break
    if player==3:
        for i in range(7):
            if x+i+1<8 and y+i+1<8:
                if boardc[y+i+1][x+i+1]<=0:
                    if boardc[y+i+1][x+i+1]!=0:
                        boardc[y][x]=0
                        boardc[y+i+1][x+i+1]=3
                        childrenX.append(boardc)
                        boardc=copy.deepcopy(pos)
                        break
                    else:
                        boardc[y][x]=0
                        boardc[y+i+1][x+i+1]=3
                        childrenX.append(boardc)
                        boardc=copy.deepcopy(pos)
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1 and x-i-1>-1:
                if boardc[y-i-1][x-i-1]<=0:
                    if boardc[y-i-1][x-i-1]!=0:
                        boardc[y][x]=0
                        boardc[y-i-1][x-i-1]=3
                        childrenX.append(boardc)
                        boardc=copy.deepcopy(pos)
                        break
                    else:
                        boardc[y][x]=0
                        boardc[y-i-1][x-i-1]=3
                        childrenX.append(boardc)
                        boardc=copy.deepcopy(pos)
                else:
                    break
            else:
                break
        for i in range(7):
            if y+i+1<8 and x-i-1>-1:
                if boardc[y+i+1][x-i-1]<=0:
                    if boardc[y+i+1][x-i-1]!=0:
                        boardc[y][x]=0
                        boardc[y+i+1][x-i-1]=3
                        childrenX.append(boardc)
                        boardc=copy.deepcopy(pos)
                        break
                    else:
                        boardc[y][x]=0
                        boardc[y+i+1][x-i-1]=3
                        childrenX.append(boardc)
                        boardc=copy.deepcopy(pos)
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1 and x+i+1<8:
                if boardc[y-i-1][x+i+1]<=0:
                    if boardc[y-i-1][x+i+1]!=0:
                        boardc[y][x]=0
                        boardc[y-i-1][x+i+1]=3
                        childrenX.append(boardc)
                        boardc=copy.deepcopy(pos)
                        break
                    else:
                        boardc[y][x]=0
                        boardc[y-i-1][x+i+1]=3
                        childrenX.append(boardc)
                        boardc=copy.deepcopy(pos)
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
                    if boardc[y][x+i+1]!=0:
                        boardc[y][x]=0
                        boardc[y][x+i+1]=-5
                        childrenQ.append(boardc)
                        boardc=copy.deepcopy(pos)
                        break
                    else:
                        boardc[y][x]=0
                        boardc[y][x+i+1]=-5
                        childrenQ.append(boardc)
                        boardc=copy.deepcopy(pos)
                else:
                    break
            else:
                break
        for i in range(7):
            if y+i+1<8:
                if boardc[y+i+1][x]>=0:
                    if boardc[y+i+1][x]!=0:
                        boardc[y][x]=0
                        boardc[y+i+1][x]=-5
                        childrenQ.append(boardc)
                        boardc=copy.deepcopy(pos)
                        break
                    else:
                        boardc[y][x]=0
                        boardc[y+i+1][x]=-5
                        childrenQ.append(boardc)
                        boardc=copy.deepcopy(pos)
                else:
                    break
            else:
                break
        for i in range(7):
            if x-i-1>-1:
                if boardc[y][x-i-1]>=0:
                    if boardc[y][x-i-1]!=0:
                        boardc[y][x]=0
                        boardc[y][x-i-1]=-5
                        childrenQ.append(boardc)
                        boardc=copy.deepcopy(pos)
                        break
                    else:
                        boardc[y][x]=0
                        boardc[y][x-i-1]=-5
                        childrenQ.append(boardc)
                        boardc=copy.deepcopy(pos)
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1:
                if boardc[y-i-1][x]>=0:
                    if boardc[y-i-1][x]!=0:
                        boardc[y][x]=0
                        boardc[y-i-1][x]=-5
                        childrenQ.append(boardc)
                        boardc=copy.deepcopy(pos)
                        break
                    else:
                        boardc[y][x]=0
                        boardc[y-i-1][x]=-5
                        childrenQ.append(boardc)
                        boardc=copy.deepcopy(pos)
                else:
                    break
            else:
                break
    if player==5:
        for i in range(7):
            if x+i+1<8:
                if boardc[y][x+i+1]<=0:
                    if boardc[y][x+i+1]!=0:
                        boardc[y][x]=0
                        boardc[y][x+i+1]=5
                        childrenQ.append(boardc)
                        boardc=copy.deepcopy(pos)
                        break
                    else:
                        boardc[y][x]=0
                        boardc[y][x+i+1]=5
                        childrenQ.append(boardc)
                        boardc=copy.deepcopy(pos)
                else:
                    break
            else:
                break
        for i in range(7):
            if y+i+1<8:
                if boardc[y+i+1][x]<=0:
                    if boardc[y+i+1][x]!=0:
                        boardc[y][x]=0
                        boardc[y+i+1][x]=5
                        childrenQ.append(boardc)
                        boardc=copy.deepcopy(pos)
                        break
                    else:
                        boardc[y][x]=0
                        boardc[y+i+1][x]=5
                        childrenQ.append(boardc)
                        boardc=copy.deepcopy(pos)
                else:
                    break
            else:
                break
        for i in range(7):
            if x-i-1>-1:
                if boardc[y][x-i-1]<=0:
                    if boardc[y][x-i-1]!=0:
                        boardc[y][x]=0
                        boardc[y][x-i-1]=5
                        childrenQ.append(boardc)
                        boardc=copy.deepcopy(pos)
                        break
                    else:
                        boardc[y][x]=0
                        boardc[y][x-i-1]=5
                        childrenQ.append(boardc)
                        boardc=copy.deepcopy(pos)
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1:
                if boardc[y-i-1][x]<=0:
                    if boardc[y-i-1][x]!=0:
                        boardc[y][x]=0
                        boardc[y-i-1][x]=5
                        childrenQ.append(boardc)
                        boardc=copy.deepcopy(pos)
                        break
                    else:
                        boardc[y][x]=0
                        boardc[y-i-1][x]=5
                        childrenQ.append(boardc)
                        boardc=copy.deepcopy(pos)
                else:
                    break
            else:
                break
    if player==-5:
        for i in range(7):
            if x+i+1<8 and y+i+1<8:
                if boardc[y+i+1][x+i+1]>=0:
                    if boardc[y+i+1][x+i+1]!=0:
                        boardc[y][x]=0
                        boardc[y+i+1][x+i+1]=-5
                        childrenQ.append(boardc)
                        boardc=copy.deepcopy(pos)
                        break
                    else:
                        boardc[y][x]=0
                        boardc[y+i+1][x+i+1]=-5
                        childrenQ.append(boardc)
                        boardc=copy.deepcopy(pos)
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1 and x-i-1>-1:
                if boardc[y-i-1][x-i-1]>=0:
                    if boardc[y-i-1][x-i-1]!=0:
                        boardc[y][x]=0
                        boardc[y-i-1][x-i-1]=-5
                        childrenQ.append(boardc)
                        boardc=copy.deepcopy(pos)
                        break
                    else:
                        boardc[y][x]=0
                        boardc[y-i-1][x-i-1]=-5
                        childrenQ.append(boardc)
                        boardc=copy.deepcopy(pos)
                else:
                    break
            else:
                break
        for i in range(7):
            if y+i+1<8 and x-i-1>-1:
                if boardc[y+i+1][x-i-1]>=0:
                    if boardc[y+i+1][x-i-1]!=0:
                        boardc[y][x]=0
                        boardc[y+i+1][x-i-1]=-5
                        childrenQ.append(boardc)
                        boardc=copy.deepcopy(pos)
                        break
                    else:
                        boardc[y][x]=0
                        boardc[y+i+1][x-i-1]=-5
                        childrenQ.append(boardc)
                        boardc=copy.deepcopy(pos)
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1 and x+i+1<8:
                if boardc[y-i-1][x+i+1]>=0:
                    if boardc[y-i-1][x+i+1]!=0:
                        boardc[y][x]=0
                        boardc[y-i-1][x+i+1]=-5
                        childrenQ.append(boardc)
                        boardc=copy.deepcopy(pos)
                        break
                    else:
                        boardc[y][x]=0
                        boardc[y-i-1][x+i+1]=-5
                        childrenQ.append(boardc)
                        boardc=copy.deepcopy(pos)
                else:
                    break
            else:
                break
    if player==5:
        for i in range(7):
            if x+i+1<8 and y+i+1<8:
                if boardc[y+i+1][x+i+1]<=0:
                    if boardc[y+i+1][x+i+1]!=0:
                        boardc[y][x]=0
                        boardc[y+i+1][x+i+1]=5
                        childrenQ.append(boardc)
                        boardc=copy.deepcopy(pos)
                        break
                    else:
                        boardc[y][x]=0
                        boardc[y+i+1][x+i+1]=5
                        childrenQ.append(boardc)
                        boardc=copy.deepcopy(pos)
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1 and x-i-1>-1:
                if boardc[y-i-1][x-i-1]<=0:
                    if boardc[y-i-1][x-i-1]!=0:
                        boardc[y][x]=0
                        boardc[y-i-1][x-i-1]=5
                        childrenQ.append(boardc)
                        boardc=copy.deepcopy(pos)
                        break
                    else:
                        boardc[y][x]=0
                        boardc[y-i-1][x-i-1]=5
                        childrenQ.append(boardc)
                        boardc=copy.deepcopy(pos)
                else:
                    break
            else:
                break
        for i in range(7):
            if y+i+1<8 and x-i-1>-1:
                if boardc[y+i+1][x-i-1]<=0:
                    if boardc[y+i+1][x-i-1]!=0:
                        boardc[y][x]=0
                        boardc[y+i+1][x-i-1]=5
                        childrenQ.append(boardc)
                        boardc=copy.deepcopy(pos)
                        break
                    else:
                        boardc[y][x]=0
                        boardc[y+i+1][x-i-1]=5
                        childrenQ.append(boardc)
                        boardc=copy.deepcopy(pos)
                else:
                    break
            else:
                break
        for i in range(7):
            if y-i-1>-1 and x+i+1<8:
                if boardc[y-i-1][x+i+1]<=0:
                    if boardc[y-i-1][x+i+1]!=0:
                        boardc[y][x]=0
                        boardc[y-i-1][x+i+1]=5
                        childrenQ.append(boardc)
                        boardc=copy.deepcopy(pos)
                        break
                    else:
                        boardc[y][x]=0
                        boardc[y-i-1][x+i+1]=5
                        childrenQ.append(boardc)
                        boardc=copy.deepcopy(pos)
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

#

def generate_one_random_child(position, playerk):#für Monte Carlo Simulation
    boardcopy = copy.deepcopy(position)
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

def gorcKk(y,x,boardc,player):
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

def gorcLl(y,x,boardc,player):
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
    if player==-1:
        if childrenB==[]:
            return []
        else:
            n=random.choice(childrenB)
            if n==1:
                boardc[y][x]=0
                boardc[y+2][x]=-1
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
    elif player==1:
        if childrenB==[]:
            return []
        else:
            n=random.choice(childrenB)
            if n==1:
                boardc[y][x]=0
                boardc[y-2][x]=1
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

def evaluatepos(pos,playerk):
    val=0
    if playerk==6:
        for p in range(8):
            for o in range(8):
                if pos[p][o]==0:
                    pass
                #
                elif pos[p][o]==-1 or pos[p][o]==-9:
                    val=val-1
                elif pos[p][o]==1 or pos[p][o]==9:
                    val=val+1
                #
                elif pos[p][o]==-2:
                    val=val-3
                elif pos[p][o]==-3:
                    val=val-3
                elif pos[p][o]==-4 or pos[p][o]==-7:
                    val=val-5
                elif pos[p][o]==2:
                    val=val+3
                elif pos[p][o]==3:
                    val=val+3
                elif pos[p][o]==4 or pos[p][o]==7:
                    val=val+5
                #
                elif pos[p][o]==-5:
                    val=val-9
                elif pos[p][o]==-6 or pos[p][o]==-8:
                    val+=-1000
                elif pos[p][o]==5:
                    val=val+9
                elif pos[p][o]==6 or pos[p][o]==8:
                    val+=1000
    elif playerk==-6:
        for p in range(8):
            for o in range(8):
                if pos[p][o]==0:
                    pass
                #
                elif pos[p][o]==-1 or pos[p][o]==-9:
                    val=val+1
                elif pos[p][o]==1 or pos[p][o]==9:
                    val=val-1
                #
                elif pos[p][o]==-2:
                    val=val+3
                elif pos[p][o]==-3:
                    val=val+3
                elif pos[p][o]==-4 or pos[p][o]==-7:
                    val=val+5
                elif pos[p][o]==2:
                    val=val-3
                elif pos[p][o]==3:
                    val=val-3
                elif pos[p][o]==4 or pos[p][o]==7:
                    val=val-5
                #
                elif pos[p][o]==-5:
                    val=val+9
                elif pos[p][o]==-6 or pos[p][o]==-8:
                    val+=1000
                elif pos[p][o]==5:
                    val=val-9
                elif pos[p][o]==6 or pos[p][o]==8:
                    val+=-1000
    return val

#

class Schach():
    def __init__(self):
        self.board=[]
        self.turn=0
        self.players=[]
        self.maxturns=200

    def printboard(self,board):
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

    def play(self):
        #
        self.board=[
            [0,0,0,0,-8,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [7,0,0,0,8,0,0,7]
        ]
        #
        self.players.clear()
        self.players.append(HumanPlayer(6))#k
        self.players.append(MinimaxPlayer(-6))#K
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
            current = (current + 1) % 2
            self.turn+=1
            #
            if self.turn==self.maxturns:
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
        self.e=[]
        self.rochade=0
        self.en_passant=False
        self.bB_2_nach_vorne=False

    def eingabe(self,pos):
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
                elif pos[zy][zx]==0 and vx==zx and zy==vy-1:
                    korrekt=True
                #schlagen
                elif pos[zy][zx]<0 and zy==vy-1 and vx-1==zx:
                    korrekt=True
                elif pos[zy][zx]<0 and zy==vy-1 and vx+1==zx:
                    korrekt=True
                #en passant
                elif zy==vy-1 and vx-1==zx and pos[zy][zx]==0 and pos[vy][zx]==-9:
                    korrekt=True
                    self.en_passant=True
                elif zy==vy-1 and vx+1==zx and pos[zy][zx]==0 and pos[vy][zx]==-9:
                    korrekt=True
                    self.en_passant=True
            #B
            elif pos[vy][vx]==-1:
                #2nachv
                if vy==1 and pos[zy][zx]==0 and pos[vy+1][vx]==0 and vx==zx and zy==vy+2:
                    korrekt=True
                #1nachv normal bew
                elif pos[zy][zx]==0 and vx==zx and zy==vy+1:
                    korrekt=True
                #schlagen
                elif pos[zy][zx]>0 and zy==vy+1 and vx-1==zx:
                    korrekt=True
                elif pos[zy][zx]>0 and zy==vy+1 and vx+1==zx:
                    korrekt=True
                #en passant
                elif zy==vy+1 and vx-1==zx and pos[zy][zx]==0 and pos[vy][zx]==9:
                    korrekt=True
                    self.en_passant=True
                elif zy==vy+1 and vx+1==zx and pos[zy][zx]==0 and pos[vy][zx]==9:
                    korrekt=True
                    self.en_passant=True
            #kK
            elif (pos[vy][vx]==6 and pos[zy][zx]<=0) or (pos[vy][vx]==-6 and pos[zy][zx]>=0) or (pos[vy][vx]==8 and pos[zy][zx]<=0) or (pos[vy][vx]==-8 and pos[zy][zx]>=0):
                #vertikal
                if vx-1==zx and zy==vy:
                    korrekt=True
                elif vx+1==zx and zy==vy:
                    korrekt=True
                #horizontal
                elif vx==zx and zy==vy-1:
                    korrekt=True
                elif vx==zx and zy==vy+1:
                    korrekt=True
                #diagonal
                elif vx-1==zx and zy==vy-1:
                    korrekt=True
                elif vx+1==zx and zy==vy-1:
                    korrekt=True
                elif vx+1==zx and zy==vy+1:
                    korrekt=True
                elif vx-1==zx and zy==vy+1:
                    korrekt=True
                #rochade
                if pos[vy][vx]==-8:
                    if zy==0 and zx==2 and pos[0][0]==-7 and pos[0][1]==0 and pos[0][2]==0 and pos[0][3]==0:
                        boardc=copy.deepcopy(pos)
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
                            korrekt=True
                            self.rochade=1
                    elif zy==0 and zx==6 and pos[0][7]==-7 and pos[0][6]==0 and pos[0][5]==0:
                        boardc=copy.deepcopy(pos)
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
                            korrekt=True
                            self.rochade=2
                elif pos[vy][vx]==8:
                    if zy==7 and zx==2 and pos[7][0]==7 and pos[7][1]==0 and pos[7][2]==0 and pos[7][3]==0:
                        boardc=copy.deepcopy(pos)
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
                            korrekt=True
                            self.rochade=1
                    elif zy==7 and zx==6 and pos[7][7]==7 and pos[7][6]==0 and pos[7][5]==0:
                        boardc=copy.deepcopy(pos)
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
                            korrekt=True
                            self.rochade=2
            #tT
            elif (pos[vy][vx]==4 and pos[zy][zx]<=0) or (pos[vy][vx]==-4 and pos[zy][zx]>=0) or (pos[vy][vx]==7 and pos[zy][zx]<=0) or (pos[vy][vx]==-7 and pos[zy][zx]>=0):
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
                    elif vy>zy:
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
                elif vy==zy:
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
                    elif vx>zx:
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
            elif (pos[vy][vx]==3 and pos[zy][zx]<=0) or (pos[vy][vx]==-3 and pos[zy][zx]>=0):
                pathclear=False
                for u in range(8):
                    if zy>vy and zx>vx:
                        if vx+u+1==zx and vy+u+1==zy:
                            pathclear=True
                            break
                        if pos[vy+u+1][vx+u+1]!=0:
                            break
                    elif zy<vy and zx>vx:
                        if vx+u+1==zx and vy-u-1==zy:
                            pathclear=True
                            break
                        if pos[vy-u-1][vx+u+1]!=0:
                            break
                    elif zy>vy and zx<vx:
                        if vx-u-1==zx and vy+u+1==zy:
                            pathclear=True
                            break
                        if pos[vy+u+1][vx-1-u]!=0:
                            break
                    elif zy<vy and zx<vx:
                        if vx-1-u==zx and vy-u-1==zy:
                            pathclear=True
                            break
                        if pos[vy-u-1][vx-u-1]!=0:
                            break
                if pathclear:
                    korrekt=True
            #qQ
            elif (pos[vy][vx]==5 and pos[zy][zx]<=0) or (pos[vy][vx]==-5 and pos[zy][zx]>=0):
                pathcleart=False
                for u in range(8):
                    if zy>vy and zx>vx:
                        if vx+u+1==zx and vy+u+1==zy:
                            pathcleart=True
                            break
                        if pos[vy+u+1][vx+u+1]!=0:
                            break
                    elif zy<vy and zx>vx:
                        if vx+u+1==zx and vy-u-1==zy:
                            pathcleart=True
                            break
                        if pos[vy-u-1][vx+u+1]!=0:
                            break
                    elif zy>vy and zx<vx:
                        if vx-u-1==zx and vy+u+1==zy:
                            pathcleart=True
                            break
                        if pos[vy+u+1][vx-1-u]!=0:
                            break
                    elif zy<vy and zx<vx:
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
                    elif vy>zy:
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
                elif vy==zy:
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
                    elif vx>zx:
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
            elif (pos[vy][vx]==2 and pos[zy][zx]<=0) or (pos[vy][vx]==-2 and pos[zy][zx]>=0):
                if zy==vy-2 and zx==vx+1:
                    korrekt=True
                elif zy==vy-2 and zx==vx-1:
                    korrekt=True
                elif zy==vy+2 and zx==vx+1:
                    korrekt=True
                elif zy==vy+2 and zx==vx-1:
                    korrekt=True
                elif zy==vy+1 and zx==vx+2:
                    korrekt=True
                elif zy==vy-1 and zx==vx+2:
                    korrekt=True
                elif zy==vy+1 and zx==vx-2:
                    korrekt=True
                elif zy==vy-1 and zx==vx-2:
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
        boardcopy=copy.deepcopy(pos)
        #
        #9&-9 zu 1&-1
        if self.token==6:
            for y in range(len(boardcopy)):
                for x in range(len(boardcopy[y])):
                    if boardcopy[y][x]==9:
                        boardcopy[y][x]=1
        elif self.token==-6:
            for y in range(len(boardcopy)):
                for x in range(len(boardcopy[y])):
                    if boardcopy[y][x]==-9:
                        boardcopy[y][x]=-1
        #
        if self.token==6:
            other_player=-6
        else:
            other_player=6
        #
        # Existiert Zug?
        legal_move_exists = False
        for child_of_root in genchildren(pos, self.token):
            king_is_killed = False
            for child_of_child in genchildren(child_of_root, other_player):
                if verloren(child_of_child, self.token):
                    king_is_killed = True
                    break
            if not king_is_killed:
                legal_move_exists = True
                break  # Exit loop when legal move is found

        # No legal moves
        if not legal_move_exists:
            return []
        #
        while True:
            while True:
                if self.eingabe(boardcopy)==True:
                    break
                else:
                    continue
            #
            #
            #
            vy = self.e[0]
            vx = self.e[1]
            zy = self.e[2]
            zx = self.e[3]
            #
            boardcopy[zy][zx]=boardcopy[vy][vx]
            boardcopy[vy][vx]=0
            #en passant
            if self.en_passant:
                boardcopy[vy][zx]=0
            #2nachvorne
            if self.bB_2_nach_vorne:
                if self.token==6:
                    boardcopy[zy][zx]=9
                elif self.token==-6:
                    boardcopy[zy][zx]=-9
            #rochade
            if self.rochade==1:
                if self.token==6:
                    boardcopy[zy][zx+1]=4
                    boardcopy[7][0]=0
                elif self.token==-6:
                    boardcopy[zy][zx+1]=-4
                    boardcopy[7][0]=0
            elif self.rochade==2:
                if self.token==6:
                    boardcopy[zy][zx-1]=4
                    boardcopy[7][7]=0
                elif self.token==-6:
                    boardcopy[zy][zx-1]=-4
                    boardcopy[7][7]=0
            #
            for feld in range(len(boardcopy[0])):
                if boardcopy[0][feld]==1:
                    boardcopy[0][feld]=5
            for feld in range(len(boardcopy[7])):
                if boardcopy[7][feld]==-1:
                    boardcopy[7][feld]=-5
            #
            #
            #
            #legal oder nicht
            falsch=False
            for child in genchildren(boardcopy,other_player):
                if verloren(child, self.token):
                    print('SCHACH')
                    falsch=True
                    boardcopy=copy.deepcopy(pos)
                    break
                    
            if not falsch:
                break
        #
        return boardcopy

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
            if selectednode.is_it_a_new_node():
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
    
    def is_it_a_new_node(self):
        if self.children==[]:
            return True
        else:
            return False

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
            if child.value>-500:#illegal moved cant be chosen
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
        if self.expanded:
            children=self.children
        else:
            children=self.expandnode()
            self.expanded=True
        #
        if children == []:
            self.value = evaluatepos(self.position, self.token)
            return self.value
        #
        if maxplayer:
            maxvalue = -math.inf
            for child in children:
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
            for child in children:
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


#----------------------------------------------------------------
board=[
    [-7,0,0,0,-8,0,0,-7],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [7,0,0,0,8,0,0,7]
]

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
            elif board[i][j]==4 or board[i][j]==7:
                print('t', end='')
            elif board[i][j]==5:
                print('q', end='')
            elif board[i][j]==6 or board[i][j]==8:
                print('k', end='')
            elif board[i][j]==-1:
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
            #
            elif board[i][j]==9:
                print('f', end='')
            elif board[i][j]==-9:
                print('F', end='')
            #
            print(' I ', end='')
        print(i + 1)
        print('---------------------------------')

def test():
    for child in genchildren(board,6):
        printboard(child)

#test()
#----------------------------------------------------------------


#Human: keine rochade, MCTS: kein en passant
#Minimax wenn legal moves left in depth 1 aber nicht tiefer-> verloren?