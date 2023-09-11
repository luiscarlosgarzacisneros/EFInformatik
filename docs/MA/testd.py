import copy
import random
import time
import math

board = [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,-1,0,0,0,0,0],
            [0,0,0,1,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,1,0,1,0,0],
            [0,0,0,0,0,0,0,0]
        ]

#

#

schlagen_XO_c=3
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
            delete_list_1=[]
            delete_list_1.extend(delete_list)
            delete_list_1.append([y-1,x-1])
            gorcXOschlagen(y-2,x-2,boardc,player,delete_list_1)
        if y-2>-1 and x+2<8 and  boardc[y-2][x+2]==0 and boardc[y-1][x+1]<0:
            geschlagen=True
            delete_list_2=[]
            delete_list_2.extend(delete_list)
            delete_list_2.append([y-1,x+1])
            gorcXOschlagen(y-2,x+2,boardc,player,delete_list_2)
        if not geschlagen:
            gorc_XO_schlagen_children.append((y+1) * 10 + (x+1))
            gorc_XO_schlagen_children_delete.append(delete_list)
    elif player==-1:
        if y+2<8 and x-2>-1 and boardc[y+2][x-2]==0 and boardc[y+1][x-1]>0:
            geschlagen=True
            delete_list_1=[]
            delete_list_1.extend(delete_list)
            delete_list_1.append([y+1,x-1])
            gorcXOschlagen(y+2,x-2,boardc,player,delete_list_1)
        if y+2<8 and x+2<8 and boardc[y+2][x+2]==0 and boardc[y+1][x+1]>0:
            geschlagen=True
            delete_list_2=[]
            delete_list_2.extend(delete_list)
            delete_list_2.append([y+1,x+1])
            gorcXOschlagen(y+2,x+2,boardc,player,delete_list_2)
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
        print(gorc_XO_schlagen_children_delete)
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
                n_y = n//10-1
                n_x = n%10-1
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
                n_y = n//10-1
                n_x = n%10-1
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
    directions=[(1,1), (-1,1), (1,-1), (-1,-1)]
    if player==2:
        for direction in directions:
            dy=direction[0]
            dx=direction[1]
            for i in range(1,8):
                if y+i*dy>7 or x+i*dx>7 or y+i*dy<0 or x+i*dx<0:
                    break
                if boardc[y+i*dy][x+i*dx]>0:
                    break
                if boardc[y+i*dy][x+i*dx]<0:
                    r=False
                    for piece in delete_list: #um or/ul inf recursion zu verhindern
                        if piece[0]==y+i*dy and piece[1]==x+i*dx:
                            r=True
                            break
                    if r:
                        break
                    if not y+(i+1)*dy>7 and not x+(i+1)*dx>7 and not y+(i+1)*dy<0 and not x+(i+1)*dx<0 and boardc[y+(i+1)*dy][x+(i+1)*dx]==0:
                        geschlagen=True
                        delete_list.append([y+i*dy, x+i*dx])
                        gorcWMschlagen(y+(i+1)*dy,x+(i+1)*dx,boardc,player,delete_list)#
                        break
                    else:
                        break
    #
    elif player==-2:
        for direction in directions:
            dy=direction[0]
            dx=direction[1]
            for i in range(1,8):
                if y+i*dy>7 or x+i*dx>7 or y+i*dy<0 or x+i*dx<0:
                    break
                if boardc[y+i*dy][x+i*dx]<0:
                    break
                if boardc[y+i*dy][x+i*dx]>0:
                    r=False
                    for piece in delete_list: #um or/ul inf recursion zu verhindern
                        if piece[0]==y+i*dy and piece[1]==x+i*dx:
                            r=True
                            break
                    if r:
                        break
                    if not y+(i+1)*dy>7 and not x+(i+1)*dx>7 and not y+(i+1)*dy<0 and not x+(i+1)*dx<0 and boardc[y+(i+1)*dy][x+(i+1)*dx]==0:
                        geschlagen=True
                        delete_list.append([y+i*dy, x+i*dx])
                        gorcWMschlagen(y+(i+1)*dy,x+(i+1)*dx,boardc,player,delete_list)#
                        break
                    else:
                        break
    #
    if not geschlagen:
        gorc_WM_schlagen_children.append(((y+1) * 10) + (((x+1) + 100)))
        gorc_WM_schlagen_children_delete.append(delete_list)

def gorcWM(y,x,boardc,player):
    #
    childrenWM=[]
    directions=[(1,1,10), (1,-1,20), (-1,1,30), (-1,-1,40)]
    gorc_WM_schlagen_children.clear()
    gorc_WM_schlagen_children_delete.clear()
    #
    if player==2:
        for direction in directions:
            dy=direction[0]
            dx=direction[1]
            d=direction[2]
            for i in range(1,8):
                if y+i*dy>7 or x+i*dx>7 or y+i*dy<0 or x+i*dx<0:
                    break
                if boardc[y+i*dy][x+i*dx]>0:
                    break
                if boardc[y+i*dy][x+i*dx]==0:
                    childrenWM.append(d+i)
                if boardc[y+i*dy][x+i*dx]<0:
                    if not y+(i+1)*dy>7 and not x+(i+1)*dx>7 and not y+(i+1)*dy<0 and not x+(i+1)*dx<0:
                        if boardc[y+(i+1)*dy][x+(i+1)*dx]==0:
                            gorcWMschlagen(y,x,boardc,player,[])
                            break
                        else:
                            break
                    else:
                        break
    #
    elif player==-2:
        for direction in directions:
            dy=direction[0]
            dx=direction[1]
            d=direction[2]
            for i in range(1,8):
                if y+i*dy>7 or x+i*dx>7 or y+i*dy<0 or x+i*dx<0:
                    break
                if boardc[y+i*dy][x+i*dx]<0:
                    break
                if boardc[y+i*dy][x+i*dx]==0:
                    childrenWM.append(d+i)
                if boardc[y+i*dy][x+i*dx]>0:
                    if not y+(i+1)*dy>7 and not x+(i+1)*dx>7 and not y+(i+1)*dy<0 and not x+(i+1)*dx<0:
                        if boardc[y+(i+1)*dy][x+(i+1)*dx]==0:
                            gorcWMschlagen(y,x,boardc,player,[])
                            break
                        else:
                            break
                    else:
                        break   
    #
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
            n_y = ((n-100)//10)-1
            n_x = ((n-100)%10)-1
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
    for i in range(30): #für wenn figuren vorhanden sind, aber keinen zug
        child=[]
        n = random.randint(0, len(piecesy) - 1)
        y = piecesy[n]
        x = piecesx[n]
        #
        if player==1:
            if boardcopy[y][x]==1:
                child=gorcXO(y,x,boardcopy,1)
            elif boardcopy[y][x]==2:
                pass
                child=gorcWM(y,x,boardcopy,2)
        elif player==-1:
            if boardcopy[y][x]==-1:
                child=gorcXO(y,x,boardcopy,-1)
            elif boardcopy[y][x]==-2:
                pass
                child=gorcWM(y,x,boardcopy,-2)
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
    ne=generate_one_random_child(board, -1)
    if ne!=[]:
        printboard(ne)
        break
    else:
        print("F")


#fertig