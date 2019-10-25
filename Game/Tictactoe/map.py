
def empty_cells(game_board):
    cells = []
    for i, y in enumerate(game_board):
        if(y == 'U'):
            cells.append(i)
    return cells

def cleanGame():
    #3 x 3
    # -1 , 0, 1
    game_board = ["U" for i in range(9)]
    return game_board

def get_number_from_pos(point):
    x, y = point
    pos = [[0, 0], [100, 0], [200, 0],
           [0, 100], [100, 100], [200, 100],
           [0, 200], [100, 200], [200, 200]]
    point = 0
    for rect_x, rect_y in pos:
        if (x >= rect_x and x <= rect_x + 100 and y >= rect_y and y <= rect_y + 100):
            return point
        point += 1


def get_pos_from_number(number):
    pos = [[0, 0], [100, 0], [200, 0],
           [0, 100], [100, 100], [200, 100],
           [0, 200], [100, 200], [200, 200]]

    return pos[number]
