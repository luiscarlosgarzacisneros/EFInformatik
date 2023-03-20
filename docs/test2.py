import copy

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]


class position:
    def __init__(self, children):
        self.children = children


tree = []
posd1 = position(tree)


def generate_children(boa):
    boardcopy = copy.deepcopy(boa)
    y = 0
    for i in range(3):
        x = 0
        for j in range(3):
            if boardcopy[x][y] == ' ':
                boardcopy[x][y] = 'O'
                tree.append(boardcopy)
                boardcopy = copy.deepcopy(boa)
            else:
                pass
            x = x + 1
        y = y + 1
    # tree.append parentpos


generate_children(board)
print(posd1.children)
