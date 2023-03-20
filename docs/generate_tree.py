import copy

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]


def gameover(board, xoro):
    # board ist in dieser funktion die ausgewählte matrix, nicht DAS board.
    # horizontal
    if board[0][0] == xoro and board[0][1] == xoro and board[0][2] == xoro:
        return True
    elif board[1][0] == xoro and board[1][1] == xoro and board[1][2] == xoro:
        return True
    elif board[2][0] == xoro and board[2][1] == xoro and board[2][2] == xoro:
        return True
    # vertikal
    elif board[0][0] == xoro and board[1][0] == xoro and board[2][0] == xoro:
        return True
    elif board[0][1] == xoro and board[1][1] == xoro and board[2][1] == xoro:
        return True
    elif board[0][2] == xoro and board[1][2] == xoro and board[2][2] == xoro:
        return True
    # diagonal
    elif board[0][0] == xoro and board[1][1] == xoro and board[2][2] == xoro:
        return True
    elif board[0][2] == xoro and board[1][1] == xoro and board[2][0] == xoro:
        return True
    else:
        return False


def evaluatepos(board):
    # board ist hier wieder das ausgawählte Spielfeld
    if gameover(board, 'X') == True:
        return 100
    elif gameover(board, 'O') == True:
        return -100


def minimax(position, depth, maxplayer):
    # X:maxplayer,spieler O:minplayer,computer
    if depth == 0 or gameover(board, 'O') == True or gameover(board, 'X') == True:
        return evaluatepos(positionboard)

    if maxplayer:
        maxvalue = -100
        for child in position:
            value = minimax(child, depth - 1, False)
            maxvalue = max(value, maxvalue)
        return maxvalue

    if not maxplayer:
        minvalue = 100
        for child in position:
            value = minimax(child, depth - 1, True)
            minvalue = min(value, minvalue)
        return minvalue


def generate_children(v, player):
    tree = []
    boardcopy = copy.deepcopy(board)
    y = 0
    for i in range(3):
        x = 0
        for j in range(3):
            if boardcopy[x][y] == ' ':
                boardcopy[x][y] = 'O'
                tree.append(boardcopy)
                boardcopy = copy.deepcopy(board)
            else:
                pass
            x = x + 1
        y = y + 1


generate_children()
