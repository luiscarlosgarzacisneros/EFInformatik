import copy
import random
import time
import math


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
            if board[w][q + 1] == player:
                filled=filled+ 1
            if board[w][q + 2] == player:
                filled=filled+ 1
            if board[w][q + 3] == player:
                filled=filled+ 1
            #
            if board[w][q] == 0:
                empty=empty+ 1
            if board[w][q + 1] == 0:
                empty=empty+ 1
            if board[w][q + 2] == 0:
                empty=empty+ 1
            if board[w][q + 3] == 0:
                empty=empty+ 1
            #
            if board[w][q] == otherplayer:
                other=other+ 1
            if board[w][q + 1] == otherplayer:
                other=other+ 1
            if board[w][q + 2] == otherplayer:
                other=other+ 1
            if board[w][q + 3] == otherplayer:
                other=other+ 1
            #
            if other==0:
                if filled==4:
                    score=score+10000
                if filled==3:
                    score=score+100
                if filled==2:
                    score=score+3
            elif filled==0:
                if other==4:
                    score=score-10000
                if other==3:
                    score=score-100
                if other==2:
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
            if board[w + 1][q] == player:
                filled=filled+ 1
            if board[w + 2][q] == player:
                filled=filled+ 1
            if board[w + 3][q] == player:
                filled=filled+ 1
            #
            if board[w][q] == 0:
                empty=empty+ 1
            if board[w + 1][q] == 0:
                empty=empty+ 1
            if board[w + 2][q] == 0:
                empty=empty+ 1
            if board[w + 3][q] == 0:
                empty=empty+ 1
            #
            if board[w][q] == otherplayer:
                other=other+ 1
            if board[w + 1][q] == otherplayer:
                other=other+ 1
            if board[w + 2][q] == otherplayer:
                other=other+ 1
            if board[w + 3][q] == otherplayer:
                other=other+ 1
            #
            if other==0:
                if filled==4:
                    score=score+10000
                if filled==3:
                    score=score+50
                if filled==2:
                    score=score+1
            elif filled==0:
                if other==4:
                    score=score-10000
                if other==3:
                    score=score-50
                if other==2:
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
            if board[w + 1][q + 1] == player:
                filled=filled+ 1
            if board[w + 2][q + 2] == player:
                filled=filled+ 1
            if board[w + 3][q + 3] == player:
                filled=filled+ 1
            #
            if board[w][q] == 0:
                empty=empty+ 1
            if board[w + 1][q + 1] == 0:
                empty=empty+ 1
            if board[w + 2][q + 2] == 0:
                empty=empty+ 1
            if board[w + 3][q + 3] == 0:
                empty=empty+ 1
            #
            if board[w][q] == otherplayer:
                other=other+ 1
            if board[w + 1][q + 1] == otherplayer:
                other=other+ 1
            if board[w + 2][q + 2] == otherplayer:
                other=other+ 1
            if board[w + 3][q + 3] == otherplayer:
                other=other+ 1
            #
            if other==0:
                if filled==4:
                    score=score+10000
                if filled==3:
                    score=score+100
                if filled==2:
                    score=score+3
            elif filled==0:
                if other==4:
                    score=score-10000
                if other==3:
                    score=score-100
                if other==2:
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
            if board[w + 1][q + 2] == player:
                filled=filled+ 1
            if board[w + 2][q + 1] == player:
                filled=filled+ 1
            if board[w + 3][q] == player:
                filled=filled+ 1
            #
            if board[w][q + 3] == 0:
                empty=empty+ 1
            if board[w + 1][q + 2] == 0:
                empty=empty+ 1
            if board[w + 2][q + 1] == 0:
                empty=empty+ 1
            if board[w + 3][q] == 0:
                empty=empty+ 1
            #
            if board[w][q + 3] == otherplayer:
                other=other+ 1
            if board[w + 1][q + 2] == otherplayer:
                other=other+ 1
            if board[w + 2][q + 1] == otherplayer:
                other=other+ 1
            if board[w + 3][q] == otherplayer:
                other=other+ 1
            #
            if other==0:
                if filled==4:
                    score=score+10000
                if filled==3:
                    score=score+100
                if filled==2:
                    score=score+3
            elif filled==0:
                if other==4:
                    score=score-10000
                if other==3:
                    score=score-100
                if other==2:
                    score=score-3
    return score
    
def genchildren(position, playerk):
    children = []
    boardcopy = copy.deepcopy(position)
    for x in range(7):
        if boardcopy[0][x] == 0:
            boardcopy[0][x] = str(playerk)
            fall(boardcopy, 0, x, playerk)
            children.append(boardcopy)
            boardcopy = copy.deepcopy(position)
    #
    return children

#

class VierGewinnt():
    def __init__(self):
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
        self.players.append(MinimaxPlayer(1))
        self.players.append(MinimaxPlayer(-1))
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

class MinimaxPlayer(Player):
    def __init__(self, token):
        super().__init__(token)
        self.token=token
        self.minimaxc = 0
        self.d = 4
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
        elif genchildren(position, playerj) == []:
            return inarow(position,1)
        #
        if maxplayer:
            maxvalue = -math.inf
            for child in genchildren(position, playerj):
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
            for child in genchildren(position, playerj):
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
        print('Best score: ',min(self.scores))
        for y in range(len(self.scores)):
            if self.scores[y]==(minormax(self.scores)):
                self.moves.append(copy.deepcopy(self.nextmoves[y]))
        self.move = copy.deepcopy(random.choice(self.moves))
    #         
    def get_move(self, board):
        self.minimaxer(board)
        return self.move

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
        #-----
        self.maxtime=4
        self.c=math.sqrt(2)
        self.numberofiterations=0
        self.depth=4
        self.numberofsimulations=50
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
                nextpos=random.choice(genchildren(pos,player))
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

class Minimax2Player(Player):
    def __init__(self, token):
        super().__init__(token)
        self.numberoflayers=5

    def minimaxer(self,board):
        #rootnode
        self.rootnode=Minimax2Node()
        self.rootnode.position=board
        self.rootnode.playeramzug=self.token
        self.rootnode.value=None
        self.rootnode.children=[]
        self.rootnode.token=self.token
        #layerzero
        self.layerzero=Minimax2Layer()
        self.layerzero.nodes=[self.rootnode]
        #
        layer=self.layerzero
        for i in range(self.numberoflayers):
            layer.expandlayer()


    def get_move(self, board):
        pass

class Minimax2Layer():
    def __init__(self):
        self.nodes=[]

    def expandlayer(self):
        newlayer= Minimax2Layer()
        for node in self.nodes:
            node.expand()
            newlayer.nodes.append(node)
        return newlayer

    def sort(self):
        pass #notimplementedyet

class Minimax2Node():
    def __init__(self):
        #
        self.maxtime=5
        #
        self.value=None
        self.children=[]
        self.position=[]
        self.playeramzug=None
        self.token=None

    def expandnode(self):
        children=genchildren(self.position,self.playeramzug)
        for i in range(len(children)):
            instance=Minimax2Node()
            instance.position=children[i]
            if self.playeramzug==1:
                instance.playeramzug=-1
            elif self.playeramzug==-1:
                instance.playeramzug=1
            instance.value=None
            instance.token=self.token
            self.children.append(instance)

    def minimax(self,alpha,beta):
        #
        if gewonnen(self.position,1) or gewonnen(self.position, -1):
            self.value=inarow(self.position,self.token)
            return self.value
        elif self.children==[]:
            self.value=inarow(self.position,self.token)
            return self.value
        #
        if self.playeramzug==1:
            maxvalue=-math.inf
            for child in self.children:
                eval=child.minimax(alpha,beta)
                maxvalue = max(maxvalue, eval)
                #pruning
                alpha = max(alpha, eval)
                if alpha >= beta:
                    break
            self.value=maxvalue
            return maxvalue
        #
        elif self.playeramzug==-1:
            minvalue=math.inf
            for child in self.children:
                eval=child.minimax(alpha,beta)
                minvalue = min(minvalue, eval)
                #pruning
                beta = min(beta, eval)
                if alpha >= beta:
                    break
            self.value=minvalue
            return minvalue


#VierGewinnt().play()

#O=MCTSPlayer
#X=MinimaxPlayer
#Wins zaehlen
game =VierGewinnt()
x_wins = 0
o_wins=0
unentschieden=0
for i in range(10):
    r=game.play() 
    if r== 'X':
        x_wins += 1
    elif r=='O':
        o_wins+=1
    else:
        unentschieden+=1
    print('X:',x_wins)
    print('O:',o_wins)
    print('unentschieden',unentschieden)
print('FERTIG')

#Minimax:zeit und sort
#minmax2 funktioniert nicht