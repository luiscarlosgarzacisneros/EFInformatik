#Gorc Variante2 schach

class GorcMove():
    def __init__(self):
        self.y=None
        self.x=None
        self.piece_type=None
        self.move_type=None

    def gorcKk2(self,boardc):
        n=self.move_type
        player=self.piece_type
        y=self.y
        x=self.x
        #
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

    def gorcLl2(self,boardc):
        n=self.move_type
        player=self.piece_type
        y=self.y
        x=self.x
        #
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

    def gorcTt2(self,boardc):
        n=self.move_type
        player=self.piece_type
        y=self.y
        x=self.x
        #
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

    def gorcXx2(self,boardc):
        n=self.move_type
        player=self.piece_type
        y=self.y
        x=self.x
        #
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

    def gorcQq2(self,boardc):
        n=self.move_type
        player=self.piece_type
        y=self.y
        x=self.x
        #
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

    def gorcBb2(self,boardc):
        n=self.move_type
        player=self.piece_type
        y=self.y
        x=self.x
        #
        if player==-1:
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

def generate_one_random_child2(position, playerk):#für MCTS Simulation
    #gen alle moves für alle Spielfiguren, move random auswählen -> all moves are equal, langsam
    boardcopy = copy.deepcopy(position)
    moves=[]
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
    if playerk==6:
        for y in range(8):
            for x in range(8):
                if boardcopy[y][x] == 1:
                    moves.extend(gorcBb1(y, x, boardcopy, 1))
                elif boardcopy[y][x] ==2:
                    moves.extend(gorcLl1(y, x, boardcopy, 2))
                elif boardcopy[y][x] == 3:
                    moves.extend(gorcXx1(y, x, boardcopy, 3))
                elif boardcopy[y][x] == 4 or boardcopy[y][x] == 7:
                    moves.extend(gorcTt1(y, x, boardcopy, 4))
                elif boardcopy[y][x] == 5:
                    moves.extend(gorcQq1(y, x, boardcopy, 5))
                elif boardcopy[y][x] == 6 or boardcopy[y][x] == 8:
                    moves.extend(gorcKk1(y, x, boardcopy, boardcopy[y][x]))
    elif playerk==-6:
        for y in range(8):
            for x in range(8):
                if boardcopy[y][x] == -1:
                    moves.extend(gorcBb1(y, x, boardcopy, -1))
                elif boardcopy[y][x] ==-2:
                    moves.extend(gorcLl1(y, x, boardcopy, -2))
                elif boardcopy[y][x] == -3:
                    moves.extend(gorcXx1(y, x, boardcopy, -3))
                elif boardcopy[y][x] == -4 or boardcopy[y][x] == -7:
                    moves.extend(gorcTt1(y, x, boardcopy, -4))
                elif boardcopy[y][x] == -5:
                    moves.extend(gorcQq1(y, x, boardcopy, -5))
                elif boardcopy[y][x] == -6 or boardcopy[y][x] == -8:
                    moves.extend(gorcKk1(y, x, boardcopy, boardcopy[y][x]))
    #
    if moves==[]:
        return []
    else:
        move=random.choice(moves)
    #
    if move.piece_type==1 or move.piece_type==-1:
        board_of_move=move.gorcBb2(boardcopy)
    elif move.piece_type==2 or move.piece_type==-2:
        board_of_move=move.gorcLl2(boardcopy)
    elif move.piece_type==3 or move.piece_type==-3:
        board_of_move=move.gorcXx2(boardcopy)
    elif move.piece_type==4 or move.piece_type==-4:
        board_of_move=move.gorcTt2(boardcopy)
    elif move.piece_type==5 or move.piece_type==-5:
        board_of_move=move.gorcQq2(boardcopy)
    elif move.piece_type==6 or move.piece_type==-6:
        board_of_move=move.gorcKk2(boardcopy)
    #
    return board_of_move
    
def gorcKk1(y,x,boardc,player):
    childrenK= []
    moves=[]
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
    if player==8:
        player=6
    elif player==-8:
        player=-6
    #
    if player==-6:
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
    elif player==6:
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
    for child in childrenK:
        instance=GorcMove()
        instance.piece_type=player
        instance.move_type=child
        instance.y=y
        instance.x=x
        moves.append(instance)
    #
    return moves

def gorcLl1(y,x,boardc,player):
    childrenL= []
    moves=[]
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
    for child in childrenL:
        instance=GorcMove()
        instance.piece_type=player
        instance.move_type=child
        instance.y=y
        instance.x=x
        moves.append(instance)
    #
    return moves

def gorcTt1(y,x,boardc,player):
    childrenT= []
    moves=[]
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
    for child in childrenT:
        instance=GorcMove()
        instance.piece_type=player
        instance.move_type=child
        instance.y=y
        instance.x=x
        moves.append(instance)
    #
    return moves

def gorcXx1(y,x,boardc,player):
    childrenX= []
    moves=[]
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
    for child in childrenX:
        instance=GorcMove()
        instance.piece_type=player
        instance.move_type=child
        instance.y=y
        instance.x=x
        moves.append(instance)
    #
    return moves

def gorcQq1(y,x,boardc,player):
    childrenQ=[]
    moves=[]
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
    for child in childrenQ:
        instance=GorcMove()
        instance.piece_type=player
        instance.move_type=child
        instance.y=y
        instance.x=x
        moves.append(instance)
    #
    return moves

def gorcBb1(y,x,boardc,player):
    childrenB= []
    moves=[]
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
    #
    for child in childrenB:
        instance=GorcMove()
        instance.piece_type=player
        instance.move_type=child
        instance.y=y
        instance.x=x
        moves.append(instance)
    #
    return moves


#Gorc nsmpl schach

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

#dm gench

def genchildrenWM2(y,x,pos,player):
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

def genchildrenschlagenWM2(y,x,pos,player,new):
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

#dm gorc

def gorcWMschlagen2(y,x,boardc,player,delete_list):
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
        gorc_WM_schlagen_children.append(((y+1) * 10) + (((x+1) + 100)))
        gorc_WM_schlagen_children_delete.append(delete_list)
                  
def gorcWM2(y,x,boardc,player):
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
            n_y = (n-100)//10
            n_x = (n-100)%10
            #
            boardc[y][x]=0
            boardc[n_y][n_x]=player
            delete=gorc_WM_schlagen_children_delete[gorc_WM_schlagen_children.index(n)]
            for feld in delete:
                boardc[feld[0]][feld[1]]=0
            return boardc
   