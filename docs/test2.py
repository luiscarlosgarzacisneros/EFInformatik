# Möglichkeitenbaum

import copy

# boards--------------
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]
board2 = [
    ['U', 'U', 'U'],
    ['U', 'U', 'U'],
    [' ', ' ', ' '],
]
# --------------------


# generate_children variabeln-----
tree = []
positioncounter = -1
# ---------------------------------


# -------------------------------------------------------------------------------------------------------------
def generate_children(boa, player, parentn, depth):
    # tree: [[[child1],[child2],[childn],[position matrix],[position number],[parent position number],[depth]],[...]]

    global positioncounter
    boardposition = []
    children = []
    y = 0
    boardcopy = copy.deepcopy(boa)

    if depth < 4:
        positioncounter = positioncounter + 1

        # children generieren
        for i in range(3):
            x = 0
            for j in range(3):
                if boardcopy[x][y] == ' ':
                    boardcopy[x][y] = str(player)
                    children.append(boardcopy)
                    boardcopy = copy.deepcopy(boa)
                else:
                    pass
                x = x + 1
            y = y + 1

        # children werden zu tree appended, zusatzinfos von parent-pos
        boardposition.append(copy.deepcopy(children))
        boardposition.append(copy.deepcopy(boa))  # position
        boardposition.append(positioncounter)  # positionnummer (id)
        boardposition.append(parentn)  # parentposition
        boardposition.append(copy.deepcopy(depth))  # anzahl züge, um auf diese position zu kommen
        tree.extend(copy.deepcopy(boardposition))  # alle mögliche nächste positionen

        # spieler wird gewechselt
        newplayer = 'O'
        if player == 'O':
            newplayer = 'X'
        else:
            newplayer == 'O'

        # children von children werden rekursiv generiert
        parentid = copy.deepcopy(positioncounter)
        for e in range(len(children)):
            matrix = copy.deepcopy(children[e])
            generate_children(matrix, newplayer, parentid, depth + 1)

    else:
        pass
# -------------------------------------------------------------------------------------------------------------


# output-------------------------------
generate_children(board2, 'O', -1, 0)
print(tree)
# -------------------------------------


# ----------------------------
# children of the position
# position
#
# position number id
# parent position number id
# depth of position
# ----------------------------
