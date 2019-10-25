######################################
# 1. O,X인지 정한다.
#2. 턴을 랜덤하게 정한다.
#3. 유저 행동
#    3.1 선택한다.(올바른 선택지 인지 확인)
#    3.2 표시
#    3.3 이겼는지 확인
#    3.4 비겼는지 확인
#    3.5 턴 바꿈
#4. 컴퓨터 행동
#    4.1 선택한다.
#    4.2 표시
#    4.3 이겼는지 확인
#    4.4 비겼는지 확인
#    4.5 턴 바꿈
#####################################
#8.29 작업은 코드를 나누는 작업 까지 진행했다.
#8.30 에는 이미지를 입히는 작업을 진행 할 것이다.

from select_option import selectMark, selectTurn, position_check
from map import cleanGame, empty_cells, get_number_from_pos
from gameCheck import checkGame, wins
import random
from algorithm import minmax
from drawGame import Draw
import pygame
from pygame.locals import *
import time

window_width = 800
window_height = 500
board_width = 500
bg_color = (128, 128, 128)
fps = 90
fps_clock = pygame.time.Clock()

#생각해 봐야 됨
#하드하게 받는것 대신 어떻게 넣을 수 있나

def main():

    pygame.init()
    surface = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Tic tac toc game")
    surface.fill(bg_color)
    draw_game = Draw(surface)
    draw_game.init_game()


    game_board = cleanGame()
    turn = selectTurn()
    is_finish = True
    #change this part
    user_mark = "O"
    computer_mark ="X"

    while True:
        depth = len(empty_cells(game_board))
        if (turn == "person"):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pass
                elif event.type == MOUSEBUTTONUP:
                    number = get_number_from_pos(event.pos)
                    if (position_check(game_board, number) != True):
                        continue
                    else:  # else 가 아니면 게임을 진행하면 된다. 바둑돌을 놓으면 된다.
                        draw_game.draw_stone(0, number)
                        game_board[number] = "O"

                        if (checkGame(game_board, turn)):
                            draw_game.draw_font()
                            break
                        else:
                            print('Computer turn ')
                            turn = "computer"
        else:
            time.sleep(1)
            if depth == 9:
                location = random.randrange(0, 3)
                num = location
            else:
                move = minmax(depth, turn, game_board, computer_mark, user_mark)
                num = move[0]
            game_board[num] = computer_mark
            draw_game.draw_stone(1, num)
            if (wins(computer_mark, game_board)):
                print('Computer win')
                break
            else:
                print('User turn ')
                turn = "person"

        pygame.display.update()
        fps_clock.tick(fps)

if __name__ == '__main__':
    main()
