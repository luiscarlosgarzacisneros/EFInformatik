import copy
import random


class VierGewinnt():
    def __init__(self):
        self.board = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ]
        #
        self.turn=0
        #
    
    def printboard(self, board):
        print('  1   2   3   4   5   6   7')
        print('-----------------------------')
        for i in range(6):
            print('I ', end='')
            for j in range(7):
                print(board[i][j], end='')
                print(' I ', end='')
            print('')
            print('-----------------------------')

    def fall(self, board, y, x, player):
        if y <= 4:
            if board[y + 1][x] == ' ':
                board[y + 1][x] = player
                board[y][x] = ' '
                y = y + 1
                self.fall(board, y, x, player)
            else:
                pass

    def gewonnen(self,board, player):
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

    def gameover(self,boar):
        isover = True
        for q in range(6):
            if boar[q].count(' ') > 0:
                isover = False
        return isover

    class HumanPlayer(VierGewinnt):
        def __init__(self, token):
            super().__init__(token)

        def player(self, board):
            try:
                x = int(input('x: ')) - 1
                if board[0][x] == ' ':
                    board[0][x] = 'X'
                    self.fall(board, 0, x, 'X')
                else:
                    print('FELD BESETZT')
                    self.player()
            except:
                print('EINGABE NICHT KORREKT')
                self.player()
    
    class ComputerPlayer(VierGewinnt):
        def __init__(self, token):
            super().__init__(token)
            self.minimaxc = 0
            self.d = 5
            self.nextmoves = []
            self.scores = []
            self.move = []
            self.moves=[]
            self.bestscores=[]

        def inarow(self,board, player, otherplayer):
            score=0
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
                    if board[w][q] == ' ':
                        empty=empty+ 1
                    if board[w][q + 1] == ' ':
                        empty=empty+ 1
                    if board[w][q + 2] == ' ':
                        empty=empty+ 1
                    if board[w][q + 3] == ' ':
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
                    if board[w][q] == ' ':
                        empty=empty+ 1
                    if board[w + 1][q] == ' ':
                        empty=empty+ 1
                    if board[w + 2][q] == ' ':
                        empty=empty+ 1
                    if board[w + 3][q] == ' ':
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
                    if board[w][q] == ' ':
                        empty=empty+ 1
                    if board[w + 1][q + 1] == ' ':
                        empty=empty+ 1
                    if board[w + 2][q + 2] == ' ':
                        empty=empty+ 1
                    if board[w + 3][q + 3] == ' ':
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
                    if board[w][q + 3] == ' ':
                        empty=empty+ 1
                    if board[w + 1][q + 2] == ' ':
                        empty=empty+ 1
                    if board[w + 2][q + 1] == ' ':
                        empty=empty+ 1
                    if board[w + 3][q] == ' ':
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
        #
        def genchildren(self,position, playerk):
            children = []
            boardcopy = copy.deepcopy(position)
            for x in range(7):
                if boardcopy[0][x] == ' ':
                    boardcopy[0][x] = str(playerk)
                    self.fall(boardcopy, 0, x, playerk)
                    children.append(boardcopy)
                    boardcopy = copy.deepcopy(position)
            #
            global minimaxc
            minimaxc = minimaxc + 1
            #
            return children
        #
        def minimax(self,position, depth, maxplayer, alpha, beta):
            # X:maxplayer,spieler O:minplayer,computer
            # Spieler
            # alpha: best maxpl, beta: best minpl
            if maxplayer:
                playerj = 'X'
            else:
                playerj = 'O'

            # return
            pos =copy.deepcopy(position)

            f=self.inarow(pos,'X','O')
            if self.gewonnen(position, 'O') == True or self.gewonnen(position, 'X') == True:
                return f
            elif depth == self.d:
                return f
            elif self.genchildren(position, playerj) == []:
                return f
            #
            if maxplayer:
                maxvalue = -100000000000
                for child in self.genchildren(position, playerj):
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
                minvalue = 1000000000000
                for child in self.genchildren(position, playerj):
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
            global minimaxc
            minimaxc = 0
            self.nextmoves.clear()
            self.scores.clear()
            self.move.clear()
            self.moves.clear()
            for firstgenchild in self.genchildren(boa, 'O'):
                self.nextmoves.append(copy.deepcopy(firstgenchild))
                self.scores.append(self.minimax(firstgenchild, 1, True, -10000000000000000000, 1000000000000000000000))
            #
            print(self.scores)
            #
            for y in range(len(self.scores)):
                if self.scores[y]==(min(self.scores)):
                    self.moves.append(copy.deepcopy(self.nextmoves[y]))
            self.move.extend(copy.deepcopy(random.choice(self.moves)))
        #         