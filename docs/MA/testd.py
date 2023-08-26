import copy
import random
import time
import math

board = [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,-1,0,0,0,-1,0,0],
            [0,0,-1,0,-1,0,0,0],
            [0,0,0,1,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]
        ]

#--------------------nicht fertig

schlagen_XO_c=2
schlagen_WM_c=5
WM_c=5

gorc_XO_schlagen_children=[]
gorc_XO_schlagen_children_delete=[]
gorc_WM_schlagen_children=[]
gorc_WM_schlagen_children_delete=[]

def gorcXOschlagen(y,x,boardc,player,delete_list):
    geschlagen=False
    if player==1:
        if y-2>-1 and x-2>-1 and boardc[y-2][x-2]==0 and boardc[y-1][x-1]<0:
            geschlagen=True
            delete_list.append([y-1,x-1])
            gorcXOschlagen(y-2,x-2,boardc,player,delete_list)
        if y-2>-1 and x+2<8 and  boardc[y-2][x+2]==0 and boardc[y-1][x+1]<0:
            geschlagen=True
            delete_list.append([y-1,x+1])
            gorcXOschlagen(y-2,x+2,boardc,player,delete_list)
        if not geschlagen:
            gorc_XO_schlagen_children.append((y+1) * 10 + (x+1))
            gorc_XO_schlagen_children_delete.append(delete_list)
    elif player==-1:
        if y+2<8 and x-2>-1 and boardc[y+2][x-2]==0 and boardc[y+1][x-1]>0:
            geschlagen=True
            delete_list.append([y+1,x-1])
            gorcXOschlagen(y+2,x-2,boardc,player,delete_list)
        if y+2<8 and x+2<8 and boardc[y+2][x+2]==0 and boardc[y+1][x+1]>0:
            geschlagen=True
            delete_list.append([y+1,x+1])
            gorcXOschlagen(y+2,x+2,boardc,player,delete_list)
        if not geschlagen:
            gorc_XO_schlagen_children.append((y+1) * 10 + (x+1))
            gorc_XO_schlagen_children_delete.append(delete_list)

def gorcXO(y,x,boardc,player):
    #
    childrenXO=[]
    gorc_XO_schlagen_children.clear()
    gorc_XO_schlagen_children_delete.clear()
    #
    if player==1:
        #normal
        if y-1>-1 and x-1>-1 and boardc[y-1][x-1]==0:
            childrenXO.append(1)
        if y-1>-1 and x+ 1<8 and boardc[y-1][x+1]==0:
            childrenXO.append(2)
        #schlagen
        if y-2>-1 and x-2>-1 and  boardc[y-2][x-2]==0:
            if boardc[y-1][x-1]<0:
                gorcXOschlagen(y,x,boardc,player,[])
        if y-2>-1 and x+ 2<8 and  boardc[y-2][x+2]==0:
            if boardc[y-1][x+1]<0:
                gorcXOschlagen(y,x,boardc,player,[])
    elif player==-1:
        #normal
        if y+1<8 and x-1>-1 and  boardc[y+1][x-1]==0:
            childrenXO.append(1)
        if y+1<8 and x+ 1<8 and boardc[y+1][x+1]==0:
            childrenXO.append(2)
        #schlagen
        if y+2<8 and x-2>-1 and boardc[y+2][x-2]==0:
            if boardc[y+1][x-1]>0:
                gorcXOschlagen(y,x,boardc,player,[])
        if y+2<8 and x+ 2<8 and boardc[y+2][x+2]==0:
            if boardc[y+1][x+1]>0:
                gorcXOschlagen(y,x,boardc,player,[])
    #
    for i in range(schlagen_XO_c):
        childrenXO.extend(gorc_XO_schlagen_children)
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
                n_str = str(n)
                n_y = int(n_str[0])-1
                n_x = int(n_str[1])-1
                boardc[y][x]=0
                if n_y==0:
                    boardc[n_y][n_x]=2
                else:
                    boardc[n_y][n_x]=1
                delete=gorc_XO_schlagen_children_delete[gorc_XO_schlagen_children.index(n)]
                for feld in delete:
                    boardc[feld[0]][feld[1]]=0
                return boardc
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
                n_str = str(n)
                n_y = int(n_str[0])-1
                n_x = int(n_str[1])-1
                boardc[y][x]=0
                if n_y==0:
                    boardc[n_y][n_x]=-2
                else:
                    boardc[n_y][n_x]=-1
                delete=gorc_XO_schlagen_children_delete[gorc_XO_schlagen_children.index(n)]
                for feld in delete:
                    boardc[feld[0]][feld[1]]=0
                return boardc   

def gorcWMschlagen(y,x,boardc,player,delete_list):
    geschlagen=False
    if player==2:
        #1: ur
        for i in range(7):
            if y+1+i>7 or x+1+i>7:
                break
            if boardc[y+1+i][x+1+i]>0:
                break
            if boardc[y+1+i][x+1+i]<0:
                r=False
                for piece in delete_list: #um or/ul inf recursion zu verhindern
                    if piece[0]==y+1+i and piece[1]==x+1+i:
                        r=True
                        break
                if r:
                    break
                if not y+2+i>7 and not x+2+i>7 and boardc[y+2+i][x+2+i]==0:
                    print("1")
                    geschlagen=True
                    delete_list.append([y+1+i, x+1+i])
                    gorcWMschlagen(y+2+i,x+2+i,boardc,player,delete_list)#
                    break
                else:
                    break
        #2: ul
        for i in range(7):
            if y+1+i>7 or x-1-i<0:
                break
            if boardc[y+1+i][x-1-i]>0:
                break
            if boardc[y+1+i][x-1-i]<0:
                r=False
                for piece in delete_list: #um or/ul inf recursion zu verhindern
                    if piece[0]==y+1+i and piece[1]==x-1-i:
                        r=True
                        break
                if r:
                    break
                if not y+2+i>7 and not x-2-i<0 and boardc[y+2+i][x-2-i]==0:
                    print("2")
                    geschlagen=True
                    delete_list.append([y+1+i, x-1-i])
                    gorcWMschlagen(y+2+i,x-2-i,boardc,player,delete_list)#
                    break
                else:
                    break
        #3: or 
        for i in range(7):
            if y-1-i<0 or x+1+i>7:
                break
            if boardc[y-1-i][x+1+i]>0:
                break
            if boardc[y-1-i][x+1+i]<0:
                r=False
                for piece in delete_list: #um or/ul inf recursion zu verhindern
                    if piece[0]==y-1-i and piece[1]==x+1+i:
                        r=True
                        break
                if r:
                    break
                if not y-2-i<0 and not x+2+i>7 and boardc[y-2-i][x+2+i]==0:
                    print("3")
                    geschlagen=True
                    delete_list.append([y-1-i, x+1+i])
                    gorcWMschlagen(y-2-i,x+2+i,boardc,player,delete_list)#
                    break
                else:
                    break
        #4: ol
        for i in range(7):
            if y-1-i<0 or x-1-i<0:
                break
            if boardc[y-1-i][x-1-i]>0:
                break
            if boardc[y-1-i][x-1-i]<0:
                r=False
                for piece in delete_list: #um or/ul inf recursion zu verhindern
                    if piece[0]==y-1-i and piece[1]==x-1-i:
                        r=True
                        break
                if r:
                    break
                if not y-2-i<0 and not x-2-i<0 and boardc[y-2-i][x-2-i]==0:
                    print("4")
                    geschlagen=True
                    delete_list.append([y-1-i, x-1-i])
                    gorcWMschlagen(y-2-i,x-2-i,boardc,player,delete_list)#
                    break
                else:
                    break
    #
    elif player==-2:
        #1: ur
        for i in range(7):
            if y+1+i>7 or x+1+i>7:
                break
            if boardc[y+1+i][x+1+i]<0:
                break
            if boardc[y+1+i][x+1+i]>0:
                r=False
                for piece in delete_list: #um or/ul inf recursion zu verhindern
                    if piece[0]==y+1+i and piece[1]==x+1+i:
                        r=True
                        break
                if r:
                    break
                if not y+2+i>7 and not x+2+i>7 and boardc[y+2+i][x+2+i]==0:
                    geschlagen=True
                    delete_list.append([y+1+i, x+1+i])
                    gorcWMschlagen(y+2+i,x+2+i,boardc,player,delete_list)
                    break
                else:
                    break
        #2: ul
        for i in range(7):
            if y+1+i>7 or x-1-i<0:
                break
            if boardc[y+1+i][x-1-i]<0:
                break
            if boardc[y+1+i][x-1-i]>0:
                r=False
                for piece in delete_list: #um or/ul inf recursion zu verhindern
                    if piece[0]==y+1+i and piece[1]==x-1-i:
                        r=True
                        break
                if r:
                    break
                if not y+2+i>7 and not x-2-i<0 and boardc[y+2+i][x-2-i]==0:
                    geschlagen=True
                    delete_list.append([y+1+i, x-1-i])
                    gorcWMschlagen(y+2+i,x-2-i,boardc,player,delete_list)
                    break
                else:
                    break
        #3: or 
        for i in range(7):
            if y-1-i<0 or x+1+i>7:
                break
            if boardc[y-1-i][x+1+i]<0:
                break
            if boardc[y-1-i][x+1+i]>0:
                r=False
                for piece in delete_list: #um or/ul inf recursion zu verhindern
                    if piece[0]==y-1-i and piece[1]==x+1+i:
                        r=True
                        break
                if r:
                    break
                if not y-2-i<0 and not x+2+i>7 and boardc[y-2-i][x+2+i]==0:
                    geschlagen=True
                    delete_list.append([y-1-i, x+1+i])
                    gorcWMschlagen(y-2-i,x+2+i,boardc,player,delete_list)
                    break
                else:
                    break
        #4: ol
        for i in range(7):
            if y-1-i<0 or x-1-i<0:
                break
            if boardc[y-1-i][x-1-i]<0:
                break
            if boardc[y-1-i][x-1-i]>0:
                r=False
                for piece in delete_list: #um or/ul inf recursion zu verhindern
                    if piece[0]==y-1-i and piece[1]==x-1-i:
                        r=True
                        break
                if r:
                    break
                if not y-2-i<0 and not x-2-i<0 and boardc[y-2-i][x-2-i]==0:
                    geschlagen=True
                    delete_list.append([y-1-i, x-1-i])
                    gorcWMschlagen(y-2-i,x-2-i,boardc,player,delete_list)
                    break
                else:
                    break
    #
    if not geschlagen:
        print("not geschlagen")
        gorc_WM_schlagen_children.append(((y+1) * 10) + (((x+1) + 100)))
        gorc_WM_schlagen_children_delete.append(delete_list)
    else:
        print("geschlagen")
                  
def gorcWM(y,x,boardc,player):
    #
    childrenWM=[]
    gorc_WM_schlagen_children.clear()
    gorc_WM_schlagen_children_delete.clear()
    #
    if player==2:
        #1: ur
        for i in range(7):
            if y+1+i>7 or x+1+i>7:
                break
            if boardc[y+1+i][x+1+i]>0:
                break
            if boardc[y+1+i][x+1+i]==0:
                childrenWM.append(11+i)
            if boardc[y+1+i][x+1+i]<0:
                if not y+2+i>7 and not x+2+i>7:
                    if boardc[y+2+i][x+2+i]==0:
                        gorcWMschlagen(y,x,boardc,player,[])
                        break
                    else:
                        break
                else:
                    break
        #2: ul
        for i in range(7):
            if y+1+i>7 or x-1-i<0:
                break
            if boardc[y+1+i][x-1-i]>0:
                break
            if boardc[y+1+i][x-1-i]==0:
                childrenWM.append(21+i)
            if boardc[y+1+i][x-1-i]<0:
                if not y+2+i>7 and not x-2-i<0:
                    if boardc[y+2+i][x-2-i]==0:
                        gorcWMschlagen(y,x,boardc,player,[])
                        break
                    else:
                        break
                else:
                    break
        #3: or 
        for i in range(7):
            if y-1-i<0 or x+1+i>7:
                break
            if boardc[y-1-i][x+1+i]>0:
                break
            if boardc[y-1-i][x+1+i]==0:
                childrenWM.append(31+i)
            if boardc[y-1-i][x+1+i]<0:
                if not y-2-i<0 and not x+2+i>7:
                    if boardc[y-2-i][x+2+i]==0:
                        gorcWMschlagen(y,x,boardc,player,[])
                        break
                    else:
                        break
                else:
                    break
        #4: ol
        for i in range(7):
            if y-1-i<0 or x-1-i<0:
                break
            if boardc[y-1-i][x-1-i]>0:
                break
            if boardc[y-1-i][x-1-i]==0:
                childrenWM.append(41+i)
            if boardc[y-1-i][x-1-i]<0:
                if not y-2-i<0 and not x-2-i<0:
                    if boardc[y-2-i][x-2-i]==0:
                        gorcWMschlagen(y,x,boardc,player,[])
                        break
                    else:
                        break
                else:
                    break
    elif player==-2:
        #1: ur
        for i in range(7):
            if y+1+i>7 or x+1+i>7:
                break
            if boardc[y+1+i][x+1+i]<0:
                break
            if boardc[y+1+i][x+1+i]==0:
                childrenWM.append(11+i)
            if boardc[y+1+i][x+1+i]>0:
                if not y+2+i>7 and not x+2+i>7:
                    if boardc[y+2+i][x+2+i]==0:
                        gorcWMschlagen(y,x,boardc,player,[])
                        break
                    else:
                        break
                else:
                    break
        #2: ul
        for i in range(7):
            if y+1+i>7 or x-1-i<0:
                break
            if boardc[y+1+i][x-1-i]<0:
                break
            if boardc[y+1+i][x-1-i]==0:
                childrenWM.append(21+i)
            if boardc[y+1+i][x-1-i]>0:
                if not y+2+i>7 and not x-2-i<0:
                    if boardc[y+2+i][x-2-i]==0:
                        gorcWMschlagen(y,x,boardc,player,[])
                        break
                    else:
                        break
                else:
                    break
        #3: or 
        for i in range(7):
            if y-1-i<0 or x+1+i>7:
                break
            if boardc[y-1-i][x+1+i]<0:
                break
            if boardc[y-1-i][x+1+i]==0:
                childrenWM.append(31+i)
            if boardc[y-1-i][x+1+i]>0:
                if not y-2-i<0 and not x+2+i>7:
                    if boardc[y-2-i][x+2+i]==0:
                        gorcWMschlagen(y,x,boardc,player,[])
                        break
                    else:
                        break
                else:
                    break
        #4: ol
        for i in range(7):
            if y-1-i<0 or x-1-i<0:
                break
            if boardc[y-1-i][x-1-i]<0:
                break
            if boardc[y-1-i][x-1-i]==0:
                childrenWM.append(41+i)
            if boardc[y-1-i][x-1-i]>0:
                if not y-2-i<0 and not x-2-i<0:
                    if boardc[y-2-i][x-2-i]==0:
                        gorcWMschlagen(y,x,boardc,player,[])
                        break
                    else:
                        break
                else:
                    break
    #
    print(gorc_WM_schlagen_children)
    for i in range(schlagen_WM_c):
        childrenWM.extend(gorc_WM_schlagen_children)
    #
    if childrenWM==[]:
        return []
    else:
        n=random.choice(childrenWM)
        #ur
        if n>10 and n<20:
            boardc[y][x]=0
            boardc[y+(n-10)][x+(n-10)]=2
            return boardc
        #ul
        elif n>20 and n<30:
            boardc[y][x]=0
            boardc[y+(n-20)][x-(n-20)]=2
            return boardc
        #or
        elif n>30 and n<40:
            boardc[y][x]=0
            boardc[y-(n-30)][x+(n-30)]=2
            return boardc
        #ol
        elif n>40 and n<50:
            boardc[y][x]=0
            boardc[y-(n-40)][x-(n-40)]=2
            return boardc
        #schlagen
        elif n>100:
            n_str = str(n-100)
            n_y = int(n_str[0])-1
            n_x = int(n_str[1])-1
            #
            boardc[y][x]=0
            boardc[n_y][n_x]=player
            delete=gorc_WM_schlagen_children_delete[gorc_WM_schlagen_children.index(n)]
            for feld in delete:
                boardc[feld[0]][feld[1]]=0
            return boardc
    
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
                    pass
                    for i in range(WM_c):
                        piecesy.append(y)
                        piecesx.append(x)
    elif player==-1:
        for y in range(8):
            for x in range(8):
                if boardcopy[y][x]==-1:
                    piecesy.append(y)
                    piecesx.append(x)
                elif boardcopy[y][x]==-2:
                    pass
                    for i in range(WM_c):
                        piecesy.append(y)
                        piecesx.append(x)
    #
    if piecesx==[]:
        return []
    #
    for i in range(30):
        child=[]
        n = random.randint(0, len(piecesy) - 1)
        y = piecesy[n]
        x = piecesx[n]
        #
        if player==1:
            if boardcopy[y][x]==1:
                child=gorcXO(y,x,position,1)
            elif boardcopy[y][x]==2:
                pass
                child=gorcWM(y,x,position,2)
        elif player==-1:
            if boardcopy[y][x]==-1:
                child=gorcXO(y,x,position,-1)
            elif boardcopy[y][x]==-2:
                pass
                child=gorcWM(y,x,position,-2)
        #
        if child!=[]: 
            break
    #
    if child!=[]: 
        return child
    else: 
        return []

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
printboard(board)
while True:
    ne=generate_one_random_child(board, 1)
    if ne!=[]:
        break
printboard(ne)

#was wenn figuren vorhanden sind, aber keinen zug?