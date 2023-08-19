import copy
import random
import time
import math

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

#

def keinezugmoeglichkeiten(pos,player):
    if genchildren(pos,player)==[]:
        return True
    else:
        return False

def verloren1(pos,player):
    if player==1:
        player2=2
    else:
        player2=-2
    eval=0
    for sl in range(len(pos)):
        for o in range(pos[sl].count(player)):
            eval=eval+1
        for p in range(pos[sl].count(player2)):
            eval=eval+1
    if eval==0:
        return True
    else:
        return False

def verloren2(pos,player):
    eval=0
    if player==1:
        player2=2
    else:
        player2=-2
    for sl in range(len(pos)):
        for o in range(pos[sl].count(player)):
            eval=eval+1
        for p in range(pos[sl].count(player2)):
            eval=eval+1
    if eval==0:
        return True
    elif keinezugmoeglichkeiten(pos,player):
        return True
    else:
        return False

#

childrens=[]
childrensWM=[]

def genchildren(position, player):
    children1=[]
    children2=[]
    boardcopy = copy.deepcopy(position)
    for y in range(8):
        for x in range(8):
            if player==1:
                if boardcopy[y][x] == 1:
                    if y-1>-1 and x-1>-1 and boardcopy[y-1][x-1]==0:
                        boardcopy[y-1][x-1]=1
                        boardcopy[y][x]=0
                        if y-1==0:
                            boardcopy[y-1][x-1]=2
                            children1.append(boardcopy)
                        children2.append(boardcopy)
                        boardcopy = copy.deepcopy(position)
                    if y-1>-1 and x+ 1<8 and boardcopy[y-1][x+ 1]==0:
                        boardcopy[y-1][x+ 1]=1
                        boardcopy[y][x]=0
                        if y-1==0:
                            boardcopy[y-1][x+1]=2
                            children1.append(boardcopy)
                        children2.append(boardcopy)
                        boardcopy = copy.deepcopy(position)
                    else:
                        pass
                    #
                    for h in genchildrenschlagen(y,x,boardcopy,1,True):
                        children1.append(h)
                #
                elif boardcopy[y][x] == 2:
                    for r in genchildrenWM(y,x,boardcopy,2):
                        children1.append(r)
            elif player==-1:
                if boardcopy[y][x] == -1:
                    if y+ 1<8 and x-1>-1 and  boardcopy[y+ 1][x-1]==0:
                        boardcopy[y+1][x-1]=-1
                        boardcopy[y][x]=0
                        if y+1==7:
                            boardcopy[y+1][x-1]=-2
                            children1.append(boardcopy)
                        children2.append(boardcopy)
                        boardcopy = copy.deepcopy(position)
                    if y+ 1<8 and x+ 1<8 and boardcopy[y+ 1][x+ 1]==0:
                        boardcopy[y+ 1][x+ 1]=-1
                        boardcopy[y][x]=0
                        if y+1==7:
                            boardcopy[y+1][x+1]=-2
                            children1.append(boardcopy)
                        children2.append(boardcopy)
                        boardcopy = copy.deepcopy(position)
                    else:
                        pass
                    #
                    for h in genchildrenschlagen(y,x,boardcopy,-1,True):
                        children1.append(h)
                #
                elif boardcopy[y][x] == -2:
                    for r in genchildrenWM(y,x,boardcopy,-2):
                        children1.append(r)
    #
    children1.extend(children2)
    #
    return children1

def genchildrenschlagen(y,x,position,player,new):
    global childrens
    if new:
        childrens=[]
    boardcopy = copy.deepcopy(position)
    if player==1:
        if y-2>-1 and x-2>-1 and  boardcopy[y-2][x-2]==0:
            if boardcopy[y-1][x-1]<0:
                boardcopy[y-1][x-1]=0
                boardcopy[y-2][x-2]=1
                boardcopy[y][x]=0
                if y-2==0:
                    boardcopy[y-2][x-2]=2
                childrens.append(copy.deepcopy(boardcopy))
                genchildrenschlagen(y-2,x-2,boardcopy,player,False)
                boardcopy = copy.deepcopy(position)
        if y-2>-1 and x+ 2<8 and  boardcopy[y-2][x+2]==0:
            if boardcopy[y-1][x+ 1]<0:
                boardcopy[y-1][x+1]=0
                boardcopy[y-2][x+2]=1
                boardcopy[y][x]=0
                if y-2==0:
                    boardcopy[y-2][x+2]=2
                childrens.append(copy.deepcopy(boardcopy))
                genchildrenschlagen(y-2,x+2,boardcopy,player,False)
                boardcopy = copy.deepcopy(position)
    elif player==-1:
        if y+ 2<8 and x-2>-1 and boardcopy[y+2][x-2]==0:
            if boardcopy[y+ 1][x-1]>0:
                boardcopy[y+1][x-1]=0
                boardcopy[y+2][x-2]=-1
                boardcopy[y][x]=0
                if y+2==7:
                    boardcopy[y+2][x-2]=-2
                childrens.append(copy.deepcopy(boardcopy))
                genchildrenschlagen(y+2,x-2,boardcopy,player,False)
                boardcopy = copy.deepcopy(position)
        if y+ 2<8 and x+ 2<8 and boardcopy[y+2][x+2]==0:
            if boardcopy[y+ 1][x+ 1]>0:
                boardcopy[y+1][x+1]=0
                boardcopy[y+2][x+2]=-1
                boardcopy[y][x]=0
                if y+2==7:
                    boardcopy[y+2][x+2]=-2
                childrens.append(copy.deepcopy(boardcopy))
                genchildrenschlagen(y+2,x+2,boardcopy,player,False)
                boardcopy = copy.deepcopy(position)
    childrens.reverse()
    return childrens

def genchildrenWM(y,x,pos,player):
    childrenWM1=[]
    childrenWM2=[]
    boardcopy=copy.deepcopy(pos)
    schlagen=False
    if player==-2:
        for o in range(7):
            schlagen=False
            if y+1+o>7 or x+1+o>7:
                break
            if boardcopy[y+1+o][x+1+o]<0:
                break
            if boardcopy[y+1+o][x+1+o]>0:
                if not y+2+o>7:
                    if not x+2+o>7:
                        schlagen=True
            if boardcopy[y+1+o][x+1+o]==0:
                boardcopy[y+1+o][x+1+o]=-2
                boardcopy[y][x]=0
                childrenWM2.append(boardcopy)
                boardcopy=copy.deepcopy(pos)
            if schlagen:
                if boardcopy[y+2+o][x+2+o]==0:
                    boardcopy[y+2+o][x+2+o]=-2
                    boardcopy[y][x]=0
                    boardcopy[y+1+o][x+1+o]=0
                    childrenWM1.append(boardcopy)
                    for r in genchildrenschlagenWM(y+2+o,x+2+o,boardcopy,-2,True):
                        childrenWM1.append(r)
                    boardcopy=copy.deepcopy(pos)
                    schlagen=False
                    break
                else:
                    break
        for o in range(7):
            schlagen=False
            if y+1+o>7 or x-1-o<0:
                break
            if boardcopy[y+1+o][x-1-o]<0:
                break
            if boardcopy[y+1+o][x-1-o]>0:
                if not y+2+o>7:
                    if not x-2-o<0:
                        schlagen=True
            if boardcopy[y+1+o][x-1-o]==0:
                boardcopy[y+1+o][x-1-o]=-2
                boardcopy[y][x]=0
                childrenWM2.append(boardcopy)
                boardcopy=copy.deepcopy(pos)
            if schlagen:
                if boardcopy[y+2+o][x-2-o]==0:
                    boardcopy[y+2+o][x-2-o]=-2
                    boardcopy[y][x]=0
                    boardcopy[y+1+o][x-1-o]=0
                    childrenWM1.append(boardcopy)
                    for r in genchildrenschlagenWM(y+2+o,x-2-o,boardcopy,-2,True):
                        childrenWM1.append(r)
                    boardcopy=copy.deepcopy(pos)
                    schlagen=False
                    break
                else:
                    break
        for o in range(7):
            schlagen=False
            if y-1-o<0 or x-1-o<0:
                break
            if boardcopy[y-1-o][x-1-o]<0:
                break
            if boardcopy[y-1-o][x-1-o]>0:
                if y-2-o>-1:
                    if x-2-o>-1: 
                        schlagen=True
            if boardcopy[y-1-o][x-1-o]==0:
                boardcopy[y-1-o][x-1-o]=-2
                boardcopy[y][x]=0
                childrenWM2.append(boardcopy)
                boardcopy=copy.deepcopy(pos)
            if schlagen:
                if boardcopy[y-2-o][x-2-o]==0:
                    boardcopy[y-2-o][x-2-o]=-2
                    boardcopy[y][x]=0
                    boardcopy[y-1-o][x-1-o]=0
                    childrenWM1.append(boardcopy)
                    for r in genchildrenschlagenWM(y-2-o,x-2-o,boardcopy,-2,True):
                        childrenWM1.append(r)
                    boardcopy=copy.deepcopy(pos)
                    schlagen=False
                    break
                else:
                    break
        for o in range(7):
            schlagen=False
            if y-1-o<0 or x+1+o>7:
                break
            if boardcopy[y-1-o][x+1+o]<0:
                break
            if boardcopy[y-1-o][x+1+o]>0:
                if y-2-o>-1:
                    if not x+2+o>7:               
                        schlagen=True
            if boardcopy[y-1-o][x+1+o]==0:
                boardcopy[y-1-o][x+1+o]=-2
                boardcopy[y][x]=0               
                childrenWM2.append(boardcopy)
                boardcopy=copy.deepcopy(pos)
            if schlagen:
                if boardcopy[y-2-o][x+2+o]==0:
                    boardcopy[y-2-o][x+2+o]=-2
                    boardcopy[y][x]=0
                    boardcopy[y-1-o][x+1+o]=0
                    childrenWM1.append(boardcopy)
                    for r in genchildrenschlagenWM(y-2-o,x+2+o,boardcopy,-2,True):
                        childrenWM1.append(r)
                    boardcopy=copy.deepcopy(pos)
                    schlagen=False
                    break
                else:
                    break
    elif player==2:
        schlagen=False
        for o in range(7):
            if y+1+o>7 or x+1+o>7:
                break
            if boardcopy[y+1+o][x+1+o]>0:
                break
            if boardcopy[y+1+o][x+1+o]<0:
                if not y+2+o>7:
                    if not x+2+o>7:
                        schlagen=True
            if boardcopy[y+1+o][x+1+o]==0:
                boardcopy[y+1+o][x+1+o]=2
                boardcopy[y][x]=0
                childrenWM2.append(boardcopy)
                boardcopy=copy.deepcopy(pos)
            if schlagen:
                if boardcopy[y+2+o][x+2+o]==0:
                    boardcopy[y+2+o][x+2+o]=2
                    boardcopy[y][x]=0
                    boardcopy[y+1+o][x+1+o]=0
                    childrenWM1.append(boardcopy)
                    for r in genchildrenschlagenWM(y+2+o,x+2+o,boardcopy,2,True):
                        childrenWM1.append(r)
                    boardcopy=copy.deepcopy(pos)
                    schlagen=False
                    break
                else:
                    break
        for o in range(7):
            schlagen=False
            if y+1+o>7 or x-1-o<0:
                break
            if boardcopy[y+1+o][x-1-o]>0:
                break
            if boardcopy[y+1+o][x-1-o]<0:
                if not y+2+o>7:
                    if not x-2-o<0:
                        schlagen=True
            if boardcopy[y+1+o][x-1-o]==0:
                boardcopy[y+1+o][x-1-o]=2
                boardcopy[y][x]=0
                childrenWM2.append(boardcopy)
                boardcopy=copy.deepcopy(pos)
            if schlagen:
                if boardcopy[y+2+o][x-2-o]==0:
                    boardcopy[y+2+o][x-2-o]=2
                    boardcopy[y][x]=0
                    boardcopy[y+1+o][x-1-o]=0
                    childrenWM1.append(boardcopy)
                    for r in genchildrenschlagenWM(y+2+o,x-2-o,boardcopy,2,True):
                        childrenWM1.append(r)
                    boardcopy=copy.deepcopy(pos)
                    schlagen=False
                    break
                else:
                    break
        for o in range(7):
            schlagen=False
            if y-1-o<0 or x-1-o<0:
                break
            if boardcopy[y-1-o][x-1-o]>0:
                break
            if boardcopy[y-1-o][x-1-o]<0:
                if not y-2-o<0:
                    if not x-2-o<0: 
                        schlagen=True
            if boardcopy[y-1-o][x-1-o]==0:
                boardcopy[y-1-o][x-1-o]=2
                boardcopy[y][x]=0
                childrenWM2.append(boardcopy)
                boardcopy=copy.deepcopy(pos)
            if schlagen:
                if boardcopy[y-2-o][x-2-o]==0:
                    boardcopy[y-2-o][x-2-o]=2
                    boardcopy[y][x]=0
                    boardcopy[y-1-o][x-1-o]=0
                    childrenWM1.append(boardcopy)
                    for r in genchildrenschlagenWM(y-2-o,x-2-o,boardcopy,2,True):
                        childrenWM1.append(r)
                    boardcopy=copy.deepcopy(pos)
                    schlagen=False
                    break
                else:
                    break
        for o in range(7):
            schlagen=False
            if y-1-o<0 or x+1+o>7:
                break
            if boardcopy[y-1-o][x+1+o]>0:
                break
            if boardcopy[y-1-o][x+1+o]<0:
                if not y-2-o<0:
                    if not x+2+o>7:
                        schlagen=True
            if boardcopy[y-1-o][x+1+o]==0:
                boardcopy[y-1-o][x+1+o]=2
                boardcopy[y][x]=0
                childrenWM2.append(boardcopy)
                boardcopy=copy.deepcopy(pos)
            if schlagen:
                if boardcopy[y-2-o][x+2+o]==0:
                    boardcopy[y-2-o][x+2+o]=2
                    boardcopy[y][x]=0
                    boardcopy[y-1-o][x+1+o]=0
                    childrenWM1.append(boardcopy)
                    for r in genchildrenschlagenWM(y-2-o,x+2+o,boardcopy,2,True):
                        childrenWM1.append(r)
                    boardcopy=copy.deepcopy(pos)
                    schlagen=False
                    break
                else:
                    break
    childrenWM1.extend(childrenWM2)
    return childrenWM1

def genchildrenschlagenWM(y,x,pos,player,new):
    global childrensWM
    if new:
        childrensWM=[]
    #
    boardcopy=copy.deepcopy(pos)
    if player==-2:
        for o in range(7):
            if y+2+o>7 or x+2+o>7:
                break
            if boardcopy[y+1+o][x+1+o]<0:
                break
            if boardcopy[y+1+o][x+1+o]>0:
                if boardcopy[y+2+o][x+2+o]==0:
                    boardcopy[y+2+o][x+2+o]=-2
                    boardcopy[y+1+o][x+1+o]=0
                    boardcopy[y][x]=0
                    childrensWM.append(boardcopy)
                    genchildrenschlagenWM(y+2+o,x+2+o,boardcopy,-2,False)
                    boardcopy=copy.deepcopy(pos)
                    break
                else:
                    break
        for o in range(7):
            if y-2-o<0 or x+2+o>7:
                break
            if boardcopy[y-1-o][x+1+o]<0:
                break
            if boardcopy[y-1-o][x+1+o]>0:
                if boardcopy[y-2-o][x+2+o]==0:
                    boardcopy[y-2-o][x+2+o]=-2
                    boardcopy[y-1-o][x+1+o]=0
                    boardcopy[y][x]=0
                    childrensWM.append(boardcopy)
                    genchildrenschlagenWM(y-2-o,x+2+o,boardcopy,-2,False)
                    boardcopy=copy.deepcopy(pos)
                    break
                else:
                    break
        for o in range(7):
            if y-2-o<0 or x-2-o<0:
                break
            if boardcopy[y-1-o][x-1-o]<0:
                break
            if boardcopy[y-1-o][x-1-o]>0:
                if boardcopy[y-2-o][x-2-o]==0:
                    boardcopy[y-2-o][x-2-o]=-2
                    boardcopy[y-1-o][x-1-o]=0
                    boardcopy[y][x]=0
                    childrensWM.append(boardcopy)
                    genchildrenschlagenWM(y-2-o,x-2-o,boardcopy,-2,False)
                    boardcopy=copy.deepcopy(pos)
                    break
                else:
                    break
        for o in range(7):
            if y+2+o>7 or x-2-o<0:
                break
            if boardcopy[y+1+o][x-1-o]<0:
                break
            if boardcopy[y+1+o][x-1-o]>0:
                if boardcopy[y+2+o][x-2-o]==0:
                    boardcopy[y+2+o][x-2-o]=-2
                    boardcopy[y+1+o][x-1-o]=0
                    boardcopy[y][x]=0
                    childrensWM.append(boardcopy)
                    genchildrenschlagenWM(y+2+o,x-2-o,boardcopy,-2,False)
                    boardcopy=copy.deepcopy(pos)
                    break
                else:
                    break
    if player==2:
        for o in range(7):
            if y+2+o>7 or x+2+o>7:
                break
            if boardcopy[y+1+o][x+1+o]>0:
                break
            if boardcopy[y+1+o][x+1+o]<0:
                if boardcopy[y+2+o][x+2+o]==0:
                    boardcopy[y+2+o][x+2+o]=2
                    boardcopy[y+1+o][x+1+o]=0
                    boardcopy[y][x]=0
                    childrensWM.append(boardcopy)
                    genchildrenschlagenWM(y+2+o,x+2+o,boardcopy,2,False)
                    boardcopy=copy.deepcopy(pos)
                    break
                else:
                    break
        for o in range(7):
            if y-2-o<0 or x+2+o>7:
                break
            if boardcopy[y-1-o][x+1+o]>0:
                break
            if boardcopy[y-1-o][x+1+o]<0:
                if boardcopy[y-2-o][x+2+o]==0:
                    boardcopy[y-2-o][x+2+o]=2
                    boardcopy[y-1-o][x+1+o]=0
                    boardcopy[y][x]=0
                    childrensWM.append(boardcopy)
                    genchildrenschlagenWM(y-2-o,x+2+o,boardcopy,2,False)
                    boardcopy=copy.deepcopy(pos)
                    break
                else:
                    break
        for o in range(7):
            if y-2-o<0 or x-2-o<0:
                break
            if boardcopy[y-1-o][x-1-o]>0:
                break
            if boardcopy[y-1-o][x-1-o]<0:
                if boardcopy[y-2-o][x-2-o]==0:
                    boardcopy[y-2-o][x-2-o]=2
                    boardcopy[y-1-o][x-1-o]=0
                    boardcopy[y][x]=0
                    childrensWM.append(boardcopy)
                    genchildrenschlagenWM(y-2-o,x-2-o,boardcopy,2,False)
                    boardcopy=copy.deepcopy(pos)
                    break
                else:
                    break
        for o in range(7):
            if y+2+o>7 or x-2-o<0:
                break
            if boardcopy[y+1+o][x-1-o]>0:
                break
            if boardcopy[y+1+o][x-1-o]<0:
                if boardcopy[y+2+o][x-2-o]==0:
                    boardcopy[y+2+o][x-2-o]=2
                    boardcopy[y+1+o][x-1-o]=0
                    boardcopy[y][x]=0
                    childrensWM.append(boardcopy)
                    genchildrenschlagenWM(y+2+o,x-2-o,boardcopy,2,False)
                    boardcopy=copy.deepcopy(pos)
                    break
                else:
                    break
    childrensWM.reverse()
    return childrensWM

#

def evaluatepos(pos,player):
    eval=0
    if player==1:
        anz_X=0
        anz_O=0
        anz_W=0
        anz_M=0
        for sl in range(len(pos)):
            for o in range(pos[sl].count(1)):
                eval=eval+9
                anz_X=anz_X+1
            for o in range(pos[sl].count(-1)):
                eval=eval-1
                anz_O=anz_O+1
            for o in range(pos[sl].count(2)):
                eval=eval+49
                anz_W=anz_W+1
            for o in range(pos[sl].count(-2)):
                eval=eval-51
                anz_M=anz_M+1
        if anz_X==0 and anz_W==0:
            eval=eval-8888
        elif anz_O==0 and anz_M==0:
            eval=eval+8888
        return eval
    elif player==-1:
        anz_X=0
        anz_O=0
        anz_W=0
        anz_M=0
        for sl in range(len(pos)):
            for o in range(pos[sl].count(1)):
                eval=eval-11
                anz_X=anz_X+1
            for o in range(pos[sl].count(-1)):
                eval=eval+9
                anz_O=anz_O+1
            for o in range(pos[sl].count(2)):
                eval=eval-51
                anz_W=anz_W+1
            for o in range(pos[sl].count(-2)):
                eval=eval+49
                anz_M=anz_M+1
        if anz_X==0 and anz_W==0:
            eval=eval+8888
        elif anz_O==0 and anz_M==0:
            eval=eval-8888
        return eval

#

class Dame():
    def __init__(self):
        self.board = []
        self.turn=0
        self.players=[]
        self.max_turns=50
    
    def play(self):
        self.board = [
        [0,-1,0,-1,0,-1,0,-1],
        [-1,0,-1,0,-1,0,-1,0],
        [0,-1,0,-1,0,-1,0,-1],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [1,0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0],
        ]
        #
        self.turn=0
        #
        # Spieler:innen vorbereiten
        # X spielt immer zuerst
        self.players.clear()
        self.players.append(Minimax4Player(1))
        self.players.append(Minimax4Player(-1))
        #
        current=0
        while True:
            if self.turn==self.max_turns:
                break
            print(self.turn)
            printboard(self.board)
            player = self.players[current]
            if player.token==1:
                istamzug='X'
            else:
                istamzug='O'
            print(istamzug, ' ist am Zug')
            new_board=player.get_move(copy.deepcopy(self.board))
            if new_board!=[]:
                self.board=new_board
            current = (current + 1) % 2
            self.turn+=1
            if verloren2(self.board,-1)or verloren2(self.board,1):
                break
        printboard(self.board)
        if verloren2(self.board,1):
            print('O HAT GEWONNEN')
            return 'O'
        elif verloren2(self.board,-1):
            print('X HAT GEWONNEN')
            return 'X'
        else:
            print('UNENTSCHIEDEN')
            return ' '

#

class Player():
    def __init__(self, token):
        self.token = token

    def get_move(self, board):
        raise NotImplementedError('Not implemented')

#---

class HumanPlayer(Player):
    def __init__(self, token):
        super().__init__(token)

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

    def schlagen_moeglich_XO(self,y,x,pos):
        moeglich=False
        if self.token==1:
            if y-2>-1 and x-2>-1:
                if pos[y-2][x-2]==0 and pos[y-1][x-1]<0:
                    moeglich=True
            if y-2>-1 and x+2<8:
                if pos[y-2][x+2]==0 and pos[y-1][x+1]<0:
                    moeglich=True
        elif self.token==-1:
            if y+2<8 and x-2>-1:
                if pos[y+2][x-2]==0 and pos[y+1][x-1]>0:
                    moeglich=True
            if y+2<8 and x+2<8:
                if pos[y+2][x+2]==0 and pos[y+1][x+1]>0:
                    moeglich=True
        return moeglich

    def schlagen_moeglich_WM(self,y,x,pos):
        moeglich=False
        if self.token==1:
            for i in range(7):
                if y+2+i>7 or x+2+i>7:
                    break
                if pos[y+1+i][x+1+i]>0:
                    break
                if pos[y+1+i][x+1+i]<0:
                    if pos[y+2+i][x+2+i]==0:
                        moeglich=True
                        break
                    else:
                        break
            if not moeglich:
                for i in range(7):
                    if y-2-i<0 or x+2+i>7:
                        break
                    if pos[y-1-i][x+1+i]>0:
                        break
                    if pos[y-1-i][x+1+i]<0:
                        if pos[y-2-i][x+2+i]==0:
                            moeglich=True
                            break
                        else:
                            break
            if not moeglich:
                for i in range(7):
                    if y-2-i<0 or x-2-i<0:
                        break
                    if pos[y-1-i][x-1-i]>0:
                        break
                    if pos[y-1-i][x-1-i]<0:
                        if pos[y-2-i][x-2-i]==0:
                            moeglich=True
                            break
                        else:
                            break
            if not moeglich:
                for i in range(7):
                    if y+2+i>7 or x-2-i<0:
                        break
                    if pos[y+1+i][x-1-i]>0:
                        break
                    if pos[y+1+i][x-1-i]<0:
                        if pos[y+2+i][x-2-i]==0:
                            moeglich=True
                            break
                        else:
                            break
        elif self.token==-1:
            for i in range(7):
                if y+2+i>7 or x+2+i>7:
                    break
                if pos[y+1+i][x+1+i]<0:
                    break
                if pos[y+1+i][x+1+i]>0:
                    if pos[y+2+i][x+2+i]==0:
                        moeglich=True
                        break
                    else:
                        break
            if not moeglich:
                for i in range(7):
                    if y-2-i<0 or x+2+i>7:
                        break
                    if pos[y-1-i][x+1+i]<0:
                        break
                    if pos[y-1-i][x+1+i]>0:
                        if pos[y-2-i][x+2+i]==0:
                            moeglich=True
                            break
                        else:
                            break
            if not moeglich:
                for i in range(7):
                    if y-2-i<0 or x-2-i<0:
                        break
                    if pos[y-1-i][x-1-i]<0:
                        break
                    if pos[y-1-i][x-1-i]>0:
                        if pos[y-2-i][x-2-i]==0:
                            moeglich=True
                            break
                        else:
                            break
            if not moeglich:
                for i in range(7):
                    if y+2+i>7 or x-2-i<0:
                        break
                    if pos[y+1+i][x-1-i]<0:
                        break
                    if pos[y+1+i][x-1-i]>0:
                        if pos[y+2+i][x-2-i]==0:
                            moeglich=True
                            break
                        else:
                            break
        #
        return moeglich

    def player_schlagen_XO(self,vy,vx,zy,zx,pos):
        if self.schlagen_moeglich_XO(vy,vx,pos):
            if zx==vx and vy==zy:
                pass
            if self.token==1:
                if zy==vy-2 and zx==vx-2 and pos[vy][vx]==1 and pos[zy][zx]==0:
                    if pos[vy-1][vx-1]<0:
                        pos[vy][vx]=0
                        pos[zy][zx]=1
                        if zy==0:
                            pos[zy][zx]=2
                        pos[vy-1][vx-1]=0
                        printboard(pos)
                        #
                        vy = zy
                        vx = zx
                        if self.schlagen_moeglich_XO(vy,vx,pos):
                            while True:
                                if eingabeschlagen(pos,vy,vx)==True:
                                    break
                                else:
                                    continue
                            zy = es[0]
                            zx = es[1]
                            self.player_schlagen_XO(vy,vx,zy,zx,pos)

                if zy==vy-2 and zx==vx+2 and pos[vy][vx]==1 and pos[zy][zx]==0:
                    if pos[vy-1][vx+1]<0:
                        pos[vy][vx]=0
                        pos[zy][zx]=1
                        if zy==0:
                            pos[zy][zx]=2
                        pos[vy-1][vx+1]=0
                        printboard(pos)
                        #
                        vy = zy
                        vx = zx
                        if self.schlagen_moeglich_XO(vy,vx,pos):
                            while True:
                                if eingabeschlagen(pos,vy,vx)==True:
                                    break
                                else:
                                    continue
                            zy = es[0]
                            zx = es[1]
                            self.player_schlagen_XO(vy,vx,zy,zx,pos)
            elif self.token==-1:
                pass
    
    
    def player(self,pos):
        while True:
            korrekt=False
            input_move = self.eingabe()
            vy, vx, zy, zx = input_move
            #
            if self.token==1:
                #X normal
                if zy==vy-1 and zx==vx-1 and pos[vy][vx]==1 and pos[zy][zx]==0:
                    korrekt=True
                    pos[vy][vx]=0
                    pos[zy][zx]=1
                    if zy==0:
                        pos[zy][zx]=2
                elif zy==vy-1 and zx==vx+1 and pos[vy][vx]==1 and pos[zy][zx]==0:
                    korrekt=True
                    pos[vy][vx]=0
                    pos[zy][zx]=1
                    if zy==0:
                        pos[zy][zx]=2
                #X schlagen
            elif self.token==-1:
                #O normal
                if zy==vy+1 and zx==vx-1 and pos[vy][vx]==-1 and pos[zy][zx]==0:
                    korrekt=True
                    pos[vy][vx]=0
                    pos[zy][zx]=-1
                    if zy==7:
                        pos[zy][zx]=-2
                elif zy==vy+1 and zx==vx+1 and pos[vy][vx]==-1 and pos[zy][zx]==0:
                    korrekt=True
                    pos[vy][vx]=0
                    pos[zy][zx]=-1
                    if zy==7:
                        pos[zy][zx]=-2
                #O schlagen
            #
            if korrekt:
                return pos 
            else:
                print('EINGABE NICHT KORREKT2')

    def get_move(self, board):
        return self.player(copy.deepcopy(board))   

#---

#gorc fehlt

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
        
    def mcts(self,board):
        self.rootnode=MCTSNode(self.token)
        self.rootnode.position=board
        self.rootnode.playeramzug=self.token
        self.rootnode.score=0
        self.rootnode.visits=0
        self.rootnode.children=[]
        #
        self.rootnode.expand()
        start = time.time()
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
        self.mcts(board)
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
            if self.playeramzug==-1:
                instance.playeramzug=1
            elif self.playeramzug==1:
                instance.playeramzug=-1
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
                pos=nextpos
                if player==-1:
                    player=1
                elif player==1:
                    player=-1
            values.append(inarow(pos,self.token))#wichtig das inarow mit token übereinstimmt.-+
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

        if parent is not None:
            parent.backpropagate(newscore, numberofsimulations)

#---

minimax_counter4=0

class Minimax4Player(Player):
    #sucht bis max zeit erreicht ist, depth =+1, move sorting
    def __init__(self, token):
        super().__init__(token)
        self.maxtime=5
        self.starting_depth=1 #wenn suche bei layer1 nicht fertig wird: crash

    def minimaxer(self, depth, vergangene_zeit):
        start=time.time()
        for child in self.rootnode.children:
            child.minimax(-math.inf,math.inf,False, depth)
            print("a ",end="") # child wurde fertig berechnet
            if ((time.time()+vergangene_zeit) - start) > self.maxtime:
                break
        #
        values=[]
        for child in self.rootnode.children:
            values.append(child.value)
        #
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
    
    def get_move(self, board):
        start=time.time()
        global minimax_counter4
        minimax_counter4=0
        #rootnode
        self.rootnode=Minimax4Node()
        self.rootnode.position=board
        self.rootnode.playeramzug=self.token
        self.rootnode.value=None
        self.rootnode.token=self.token
        self.rootnode.depth=0
        self.rootnode.children=self.rootnode.expandnode()
        #
        depth=self.starting_depth
        while (time.time() - start) < self.maxtime:
            print("DEPTH: ",depth)
            move=self.minimaxer(depth,(time.time() - start))
            bestmove=move
            if (time.time() - start) > self.maxtime:
                print("NICHT FERTIG")
            else:
                self.rootnode.sort(True)
                depth+=1
        print("---",minimax_counter4)
        return bestmove

class Minimax4Node():
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
            instance=Minimax4Node()
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
        if self.depth==maxdepth:
            self.value = evaluatepos(self.position, self.token)
            return self.value
        elif verloren1(self.position, 1) or verloren1(self.position, -1):
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
            if self.playeramzug==self.token:
                self.value = -8888
            else:
                self.value = +8888
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
    game =Dame()
    x_wins = 0
    o_wins=0
    unentschieden=0
    for i in range(z):
        r=game.play() 
        if r== 'X':
            x_wins += 1
        elif r=='O':
            o_wins+=1
        else:
            unentschieden+=1
        print('X:',x_wins)
        print('O:',o_wins)
        print('-:',unentschieden)
    print('FERTIG')

spielen(20)