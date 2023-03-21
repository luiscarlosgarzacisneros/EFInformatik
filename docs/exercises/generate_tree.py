import copy

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]
board2 = [
    ['X', ' ', ' '],
    [' ', 'X', 'X'],
    [' ', ' ', ' '],
]


tree = []
positioncounter = -1


def generate_children(boa, player, parentn, depth):
    # tree: [[[child1],[child2],[childn],[position matrix],[position number],[parent position number],[depth]],[...]]

    global positioncounter
    positioncounter = positioncounter + 1
    boardposition = []
    y = 0
    boardcopy = copy.deepcopy(boa)

    if depth < 4:
        for i in range(3):
            x = 0
            for j in range(3):
                if boardcopy[x][y] == ' ':
                    boardcopy[x][y] = str(player)
                    boardposition.append(boardcopy)
                    boardcopy = copy.deepcopy(boa)
                else:
                    pass
                x = x + 1
            y = y + 1
        boardposition.append(copy.deepcopy(boa))  # position
        boardposition.append(positioncounter)  # positionnummer (id)
        boardposition.append(parentn)  # parentposition
        boardposition.append(copy.deepcopy(depth))  # anzahl züge, um auf diese position zu kommen
        tree.append(copy.deepcopy(boardposition))  # alle mögliche nächste positionen

        if player == 'O':
            newplayer = 'X'
        else:
            newplayer == 'O'
    else:
        pass


generate_children(board, 'O', -1, 0)
generate_children(board2, 'O', 0, 1)

x = 0
for pp in range(len(tree)):
    y = 0
    for p in range(len(tree[x])):
        print(tree[x][y])
        y = y + 1
    x = x + 1
