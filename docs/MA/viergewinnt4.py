import copy
import random
import time
import math

#

def gewonnen(board, player):
    gew = False
    # horizontal
    for q in range(4):
        for w in range(6):
            if board[w][q] == player and board[w][q + 1] == player and board[w][q + 2] == player and board[w][q + 3] == player:
                gew = True
    # vertikal
    for q in range(7):
        for w in range(3):
            if board[w][q] == player and board[w + 1][q] == player and board[w + 2][q] == player and board[w + 3][q] == player:
                gew = True
    # diagonal1
    for q in range(4):
        for w in range(3):
            if board[w][q] == player and board[w + 1][q + 1] == player and board[w + 2][q + 2] == player and board[w + 3][q + 3] == player:
                gew = True
    # diagonal2
    for q in range(4):
        for w in range(3):
            if board[w][q + 3] == player and board[w + 1][q + 2] == player and board[w + 2][q + 1] == player and board[w + 3][q] == player:
                gew = True
    return gew

def gameover(boar):
    isover = True
    for q in range(6):
        if boar[q].count(0) > 0:
            isover = False
    return isover

def fall( board, y, x, player):
    if y <= 4:
        if board[y + 1][x] == 0:
            board[y + 1][x] = player
            board[y][x] = 0
            y = y + 1
            fall(board, y, x, player)
        else:
            pass

def inarow(board,player):
    score=0
    if player==1:
        otherplayer=-1
    elif player==-1:
        otherplayer=1
    # horizontal
    for q in range(4):
        for w in range(6):
            empty=0
            other=0
            filled=0
            #
            if board[w][q] == player:
                filled=filled+ 1
            elif board[w][q] == 0:
                empty=empty+ 1
            elif board[w][q] == otherplayer:
                other=other+ 1
            #
            if board[w][q + 1] == player:
                filled=filled+ 1
            elif board[w][q + 1] == 0:
                empty=empty+ 1
            elif board[w][q + 1] == otherplayer:
                other=other+ 1
            #
            if board[w][q + 2] == player:
                filled=filled+ 1
            elif board[w][q + 2] == 0:
                empty=empty+ 1
            elif board[w][q + 2] == otherplayer:
                other=other+ 1
            #
            if board[w][q + 3] == player:
                filled=filled+ 1
            elif board[w][q + 3] == 0:
                empty=empty+ 1
            elif board[w][q + 3] == otherplayer:
                other=other+ 1
            #
            if other==0:
                if filled==4:
                    score=score+10000
                elif filled==3:
                    score=score+1000
                elif filled==2:
                    score=score+3
            elif filled==0:
                if other==4:
                    score=score-10000
                elif other==3:
                    score=score-100
                elif other==2:
                    score=score-3
    # vertikal
    for q in range(7):
        for w in range(3):
            empty=0
            other=0
            filled=0
            #
            if board[w][q] == player:
                filled=filled+ 1
            elif board[w][q] == 0:
                empty=empty+ 1
            elif board[w][q] == otherplayer:
                other=other+ 1
            #
            if board[w + 1][q] == player:
                filled=filled+ 1
            elif board[w + 1][q] == 0:
                empty=empty+ 1
            elif board[w + 1][q] == otherplayer:
                other=other+ 1
            #
            if board[w + 2][q] == player:
                filled=filled+ 1
            elif board[w + 2][q] == 0:
                empty=empty+ 1
            elif board[w + 2][q] == otherplayer:
                other=other+ 1
            #
            if board[w + 3][q] == player:
                filled=filled+ 1
            elif board[w + 3][q] == 0:
                empty=empty+ 1
            elif board[w + 3][q] == otherplayer:
                other=other+ 1
            #
            if other==0:
                if filled==4:
                    score=score+10000
                elif filled==3:
                    score=score+10
                elif filled==2:
                    score=score+1
            elif filled==0:
                if other==4:
                    score=score-10000
                elif other==3:
                    score=score-30
                elif other==2:
                    score=score-1
    # diagonal1
    for q in range(4):
        for w in range(3):
            empty=0
            other=0
            filled=0
            #
            if board[w][q] == player:
                filled=filled+ 1
            elif board[w][q] == 0:
                empty=empty+ 1
            elif board[w][q] == otherplayer:
                other=other+ 1
            #
            if board[w + 1][q + 1] == player:
                filled=filled+ 1
            elif board[w + 1][q + 1] == 0:
                empty=empty+ 1
            elif board[w + 1][q + 1] == otherplayer:
                other=other+ 1
            #
            if board[w + 2][q + 2] == player:
                filled=filled+ 1
            elif board[w + 2][q + 2] == 0:
                empty=empty+ 1
            elif board[w + 2][q + 2] == otherplayer:
                other=other+ 1
            #
            if board[w + 3][q + 3] == player:
                filled=filled+ 1
            elif board[w + 3][q + 3] == 0:
                empty=empty+ 1
            elif board[w + 3][q + 3] == otherplayer:
                other=other+ 1
            #
            if other==0:
                if filled==4:
                    score=score+10000
                elif filled==3:
                    score=score+1000
                elif filled==2:
                    score=score+3
            elif filled==0:
                if other==4:
                    score=score-10000
                elif other==3:
                    score=score-100
                elif other==2:
                    score=score-3
    # diagonal2
    for q in range(4):
        for w in range(3):
            empty=0
            other=0
            filled=0
            #
            if board[w][q + 3] == player:
                filled=filled+ 1
            elif board[w][q + 3] == 0:
                empty=empty+ 1
            elif board[w][q + 3] == otherplayer:
                other=other+ 1
            #
            if board[w + 1][q + 2] == player:
                filled=filled+ 1
            elif board[w + 1][q + 2] == 0:
                empty=empty+ 1
            elif board[w + 1][q + 2] == otherplayer:
                other=other+ 1
            #
            if board[w + 2][q + 1] == player:
                filled=filled+ 1
            elif board[w + 2][q + 1] == 0:
                empty=empty+ 1
            elif board[w + 2][q + 1] == otherplayer:
                other=other+ 1
            #
            if board[w + 3][q] == player:
                filled=filled+ 1
            elif board[w + 3][q] == 0:
                empty=empty+ 1
            elif board[w + 3][q] == otherplayer:
                other=other+ 1
            #
            if other==0:
                if filled==4:
                    score=score+10000
                elif filled==3:
                    score=score+1000
                elif filled==2:
                    score=score+3
            elif filled==0:
                if other==4:
                    score=score-10000
                elif other==3:
                    score=score-100
                elif other==2:
                    score=score-3
    return score

def genchildren(position, player):
    children = []
    boardcopy = copy.deepcopy(position)
    for x in range(7):
        if boardcopy[0][x] == 0:
            boardcopy[0][x] = player
            fall(boardcopy, 0, x, player)
            children.append(boardcopy)
            boardcopy = copy.deepcopy(position)
    #
    return children

def generate_one_random_child(position,player):#für Monte Carlo Simulation
        boardcopy = copy.deepcopy(position)
        while True:
            x=random.randint(0,6)
            if boardcopy[0][x] == 0:
                break
        boardcopy[0][x] = player
        fall(boardcopy, 0, x, player)
        return boardcopy

#
minimax_counter4=0
minimax_counter3=0
#

class VierGewinnt():
    def __init__(self):
        self.board = []
        self.turn=0
        self.players=[]
    
    def printboard(self, board):
        print('  1   2   3   4   5   6   7')
        print('-----------------------------')
        for i in range(6):
            print('I ', end='')
            for j in range(7):
                if board[i][j]==1:
                    print('X', end='')
                elif board[i][j]==-1:
                    print('O', end='')
                else:
                    print(' ', end='')
                print(' I ', end='')
            print('')
            print('-----------------------------')

    def play(self):
        self.board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
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
            print(self.turn)
            self.printboard(self.board)
            player = self.players[current]
            if player.token==1:
                istamzug='X'
            else:
                istamzug='O'
            print(istamzug, ' ist am Zug')
            self.board=player.get_move(copy.deepcopy(self.board))
            current = (current + 1) % 2
            self.turn+=1
            if gameover(self.board) or gewonnen(self.board,-1)or gewonnen(self.board,1):
                break
        self.printboard(self.board)
        if gewonnen(self.board,-1):
            print('O HAT GEWONNEN')
            return 'O'
        elif gewonnen(self.board,1):
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

#

class HumanPlayer(Player):
    def __init__(self, token):
        super().__init__(token)

    def player(self, board):
        try:
            x = int(input('x: ')) - 1
            if board[0][x] == 0:
                board[0][x] = self.token
                fall(board, 0, x, self.token)
            else:
                print('FELD BESETZT')
                self.player(board)
        except:
            print('EINGABE NICHT KORREKT')
            self.player(board)

    def get_move(self, board):
        self.player(board)
        return board

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

#

class Minimax1Player(Player):
    def __init__(self, token):
        super().__init__(token)
        self.token=token
        self.minimaxc = 0
        self.d = 5
        self.nextmoves = []
        self.scores = []
        self.move = []
        self.moves=[]
        self.bestscores=[]

    def minimax(self,position, depth, maxplayer, alpha, beta):
        # Spieler
        # alpha: best maxpl, beta: best minpl
        self.minimaxc = self.minimaxc + 1
        # return
        if maxplayer:
            playerj = 1
        else:
            playerj = -1

        if gewonnen(position, -1) == True or gewonnen(position, 1) == True:
            return inarow(position,1)
        elif depth == self.d:
            return inarow(position,1)
        children=genchildren(position, playerj)
        if children == []:
            return inarow(position,1)
        #
        if maxplayer:
            maxvalue = -math.inf
            for child in children:
                value = self.minimax(child, depth + 1, False, alpha, beta)
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
            minvalue = math.inf
            for child in children:
                value = self.minimax(child, depth + 1, True, alpha, beta)
                if value < minvalue:
                    minvalue = value
                # pruning
                if value < beta:
                    beta = value
                if beta <= alpha:
                    break
            return minvalue
    #
    def minimaxer(self,boa):
        self.minimaxc = 0
        self.nextmoves.clear()
        self.scores.clear()
        self.move.clear()
        self.moves.clear()
        if self.token==-1:
            maxplother=True
        else:
            maxplother=False
        for firstgenchild in genchildren(boa, self.token):
            self.nextmoves.append(copy.deepcopy(firstgenchild))
            self.scores.append(self.minimax(firstgenchild, 1, maxplother, -math.inf, math.inf))
        #
        print(self.scores)
        #
        if self.token==-1:
            minormax=min
        else:
            minormax=max
        #
        print(min(self.scores))
        for y in range(len(self.scores)):
            if self.scores[y]==(minormax(self.scores)):
                self.moves.append(copy.deepcopy(self.nextmoves[y]))
        self.move = copy.deepcopy(random.choice(self.moves))
    #         
    def get_move(self, board):
        self.minimaxer(board)
        return self.move

#

class Minimax2Player(Player):
    #sucht bis max depth erreicht ist
    def __init__(self, token):
        super().__init__(token)
        self.maxdepth=5
    
    def minimaxer(self,board):
        #rootnode
        self.rootnode=Minimax2Node()
        self.rootnode.position=board
        self.rootnode.playeramzug=self.token
        self.rootnode.value=None
        self.rootnode.children=[]
        self.rootnode.token=self.token
        self.rootnode.depth=0
        #
        for child in self.rootnode.expandnode():
            child.minimax(-math.inf,math.inf,False,self.maxdepth)
    
    def get_move(self, board):
        self.minimaxer(board)
        values=[]
        bestmoves=[]
        for child in self.rootnode.children:
            values.append(child.value)
        bestvalue=max(values)
        print(values)
        for child in self.rootnode.children:
            if child.value==bestvalue:
                bestmoves.append(child)
        print(bestvalue)
        bestmove=random.choice(bestmoves)
        return bestmove.position

class Minimax2Node():
    def __init__(self):
        self.value=None
        self.children=[]
        self.position=[]
        self.playeramzug=None
        self.token=None
        self.depth=None

    def expandnode(self):
        children=genchildren(self.position,self.playeramzug)
        for i in range(len(children)):
            instance=Minimax2Node()
            instance.position=children[i]
            instance.playeramzug = -self.playeramzug
            instance.value=None
            instance.token=self.token
            instance.depth=self.depth+1
            self.children.append(instance)
        return self.children

    def minimax(self, alpha, beta, maxplayer, maxdepth):
        #
        if self.depth==maxdepth:
            self.value = inarow(self.position, self.token)
            return self.value
        elif gewonnen(self.position, 1) or gewonnen(self.position, -1):
            self.value = inarow(self.position, self.token)
            return self.value
        #
        children=self.expandnode()
        #
        if children == []:
            self.value = inarow(self.position, self.token)
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
            
#

class Minimax3Player(Player):
    #sucht bis max zeit erreicht ist, depth =+1
    def __init__(self, token):
        super().__init__(token)
        self.maxtime=5
        self.starting_depth=1 #wenn suche bei layer1 nicht fertig wird: crash

    def minimaxer(self, depth, vergangene_zeit):
        start=time.time()
        suche_fertig=True
        for child in self.rootnode.children:
            child.minimax(-math.inf,math.inf,False, depth)
            if ((time.time()+vergangene_zeit) - start) > self.maxtime:
                suche_fertig=False
                break
            print("k ",end="") # child wurde fertig berechnet
        
        #
        if suche_fertig:
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
        else:
            return []
    
    def get_move(self, board):
        start=time.time()
        global minimax_counter3
        minimax_counter3=0
        #rootnode
        self.rootnode=Minimax3Node()
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
            if  (time.time() - start) < self.maxtime:
                bestmove=move
                depth+=1
            else:
                print("NICHT FERTIG")
        print("---",minimax_counter3)
        return bestmove

class Minimax3Node():
    def __init__(self):
        self.value=None
        self.children=[]
        self.position=[]
        self.playeramzug=None
        self.token=None
        self.depth=None

    def expandnode(self):
        children=genchildren(self.position,self.playeramzug)
        for i in range(len(children)):
            instance=Minimax3Node()
            instance.position=children[i]
            instance.playeramzug = -self.playeramzug
            instance.value=None
            instance.token=self.token
            instance.depth=self.depth+1
            self.children.append(instance)
        return self.children

    def minimax(self, alpha, beta, maxplayer, maxdepth):
        global minimax_counter3
        minimax_counter3+=1
        #
        if self.depth==maxdepth:
            self.value = inarow(self.position, self.token)
            return self.value
        elif gewonnen(self.position, 1) or gewonnen(self.position, -1):
            self.value = inarow(self.position, self.token)
            return self.value
        #
        children=self.expandnode()
        #
        if children == []:
            self.value = inarow(self.position, self.token)
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
#

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
            self.value = inarow(self.position, self.token)
            return self.value
        elif gewonnen(self.position, 1) or gewonnen(self.position, -1):
            self.value = inarow(self.position, self.token)
            return self.value
        #
        if self.expanded:
            children=self.children
        else:
            children=self.expandnode()
            self.expanded=True
        #
        if children == []:
            self.value = inarow(self.position, self.token)
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
    game =VierGewinnt()
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