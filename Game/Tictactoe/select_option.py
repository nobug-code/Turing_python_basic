import random

def selectMark():
    mark = ''
    while(mark != 'X' and mark != 'O'):
        mark = input("Select X or O :")
        mark = mark.upper()
    if(mark == 'X'):
        return ['X', 'O']
    else:
        return ['O', 'X']

def selectTurn():
    if(random.randint(0,1) == 0):
        return 'person'
    else:
        return 'computer'

def position_check(game_board, num):
    if(game_board[num] == "U"):
        return True
    else:
        return False