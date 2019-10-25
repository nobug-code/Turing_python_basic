
def wins(check, game_board):
    if ((game_board[6] == check and game_board[7] == check and game_board[8] == check)
            or (game_board[3] == check and game_board[4] == check and game_board[5] == check)
            or (game_board[0] == check and game_board[1] == check and game_board[2] == check)
            or (game_board[7] == check and game_board[4] == check and game_board[1] == check)
            or (game_board[6] == check and game_board[3] == check and game_board[0] == check)
            or (game_board[8] == check and game_board[5] == check and game_board[2] == check)
            or (game_board[6] == check and game_board[4] == check and game_board[2] == check)
            or (game_board[8] == check and game_board[4] == check and game_board[0] == check)):
        return True
    else:
        return False

def checkGame(game_board, turn):
    if(turn == 'computer'):
        check = 'X'
    else:
        check = 'O'
    if((game_board[6] == check and game_board[7] == check and game_board[8] == check)
        or(game_board[3] == check and game_board[4] == check and game_board[5] == check)
        or(game_board[0] == check and game_board[1] == check and game_board[2] == check)
        or (game_board[7] == check and game_board[4] == check and game_board[1] == check)
        or (game_board[6] == check and game_board[3] == check and game_board[0] == check)
        or (game_board[8] == check and game_board[5] == check and game_board[2] == check)
        or (game_board[6] == check and game_board[4] == check and game_board[2] == check)
        or (game_board[8] == check and game_board[4] == check and game_board[0] == check)):
        return True
    else:
        return False
