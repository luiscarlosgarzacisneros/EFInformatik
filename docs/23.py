import copy
import time
import random

board = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
]
#
minimaxc = 0
d = 8
nextmoves = []
scores = []
move = []
moves=[]
bestscores=[]
maxtime = 20
#


def printboard(board):
    print('  1   2   3   4   5   6   7')
    print('-----------------------------')
    for i in range(6):
        print('I ', end='')
        for j in range(7):
            print(board[i][j], end='')
            print(' I ', end='')
        print('')
        print('-----------------------------')


def fall(board, y, x, player):
    if y <= 4:
        if board[y + 1][x] == ' ':
            board[y + 1][x] = player
            board[y][x] = ' '
            y = y + 1
            fall(board, y, x, player)
        else:
            pass


def player():
    try:
        x = int(input('x: ')) - 1
        if board[0][x] == ' ':
            board[0][x] = 'X'
            fall(board, 0, x, 'X')
        else:
            print('FELD BESETZT')
            player()
    except:
        print('EINGABE NICHT KORREKT')
        player()


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

def inarow(board, player, otherplayer):
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
                    score=score+100
                if filled==3:
                    score=score+10
                if filled==2:
                    score=score+3
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
                    score=score+100
                if filled==3:
                    score=score+10
                if filled==2:
                    score=score+3
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
                    score=score+100
                if filled==3:
                    score=score+10
                if filled==2:
                    score=score+3
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
                    score=score+100
                if filled==3:
                    score=score+10
                if filled==2:
                    score=score+3
    return score


def evaluatepos(board):
    score=0
    score=(inarow(board,'X','O'))-(inarow(board,'O','X'))
    return score
    
print(evaluatepos(board))

# funktioniert nicht