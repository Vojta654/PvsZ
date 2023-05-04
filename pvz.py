import pygame
BOARD_SZE_X = 20
BOARD_SZE_Y = 5
SQUARE_SIZE = 40
SQUARE01_COLOR = (0, 243, 0)
SQUARE02_COLOR = (0, 145, 0)
MENU_SIZE = 50
MENU_COLOR = (100, 100, 250)


SQUARE_HOVER_COLOR = (150, 150, 150)
CIRCLE_COLOR = (0, 255, 0)
CROSS_COLOR = (0, 0, 255)


board = []
for y in range(0, BOARD_SZE_Y, 1):
    row = []
    for x in range(0, BOARD_SZE_X, 1):
        row.append(0)
    board.append(row)

current_square = (-1, -1)
player_turn = 1

window  = pygame.display.set_mode((BOARD_SZE_X*SQUARE_SIZE,(BOARD_SZE_Y*SQUARE_SIZE) + MENU_SIZE))

def draw_board():

    window.fill(SQUARE01_COLOR)
    odd = 0
    pygame.draw.rect(window, MENU_COLOR, (0, 0, BOARD_SZE_X*SQUARE_SIZE, MENU_SIZE))
    for j in range(BOARD_SZE_Y):
        if odd ==0:
            odd=1
        else:
            odd =0
        for index in range(0, BOARD_SZE_X, 2):
            pygame.draw.rect(window, SQUARE02_COLOR, ((index+odd) * SQUARE_SIZE, (j * SQUARE_SIZE) + MENU_SIZE, SQUARE_SIZE , SQUARE_SIZE))


def game_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

def game_update():
    draw_board()
    pygame.display.flip()
while True:
    game_update()
    game_input()
