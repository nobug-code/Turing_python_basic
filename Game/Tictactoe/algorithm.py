import math
from UseApi import empty_cells
from gameCheck import wins, checkGame

def minmax(depth, player, game_board, computer_mark, user_mark):

    if player == "computer":#max
        best = [-1, -math.inf]
    else:#player == "user" #min
        best = [-1, +math.inf]

    if depth == 0 or checkGame(game_board, player):
        score = evaluate(computer_mark, user_mark, game_board)
        return [-1, score]

    for cell in empty_cells(game_board):
        location = cell
        if(player == "computer"):
            game_board[location] = computer_mark
            player = "user"
        else:
            game_board[location] = user_mark
            player = "computer"

        score = minmax(depth -1, player, game_board, computer_mark, user_mark)
        game_board[location] = "U"
        score[0] = location
        if player == "user":
            if(score[1] > best[1]):
                best = score #max
        else:
            if(score[1] < best[1]):
                best = score # min
    return best

def evaluate(computer_mark, user_mark, game_board):

    if(wins(computer_mark, game_board)):
        score = 1
    elif(wins(user_mark, game_board)):
        score = -1
    else:
        score = 0
    return score
