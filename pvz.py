import pygame
BOARD_SIZE_X = 10
BOARD_SIZE_Y = 5
SQUARE_SIZE = 60
SQUARE01_COLOR = (0, 243, 0)
SQUARE02_COLOR = (0, 145, 0)
MENU_SIZE = 60
MENU_COLOR = (100, 100, 250)


SQUARE_HOVER_COLOR = (150, 150, 150)
CIRCLE_COLOR = (0, 255, 0)
CROSS_COLOR = (0, 0, 255)
COLOR_BLUE = (0, 0, 255)


board = []
for y in range(0, BOARD_SIZE_Y, 1):
    row = []
    for x in range(0, BOARD_SIZE_X, 1):
        row.append(0)
    board.append(row)

for i in range(BOARD_SIZE_Y):
    board[i][0] = 1

window  = pygame.display.set_mode((BOARD_SIZE_X*SQUARE_SIZE,(BOARD_SIZE_Y*SQUARE_SIZE) + MENU_SIZE))

def draw_board():

    window.fill(SQUARE01_COLOR)
    odd = 0
    pygame.draw.rect(window, MENU_COLOR, (0, 0, BOARD_SIZE_X*SQUARE_SIZE, MENU_SIZE))
    for j in range(BOARD_SIZE_Y):
        if odd ==0:
            odd=1
        else:
            odd =0
        for index in range(0, BOARD_SIZE_X, 2):
            pygame.draw.rect(window, SQUARE02_COLOR, ((index+odd) * SQUARE_SIZE, (j * SQUARE_SIZE) + MENU_SIZE, SQUARE_SIZE , SQUARE_SIZE))


def game_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

def game_update():
    pygame.display.flip()
    
    
def game_output():
    pass   

draw_board()
print(board)
while True:
    game_input()
    game_update()
    game_output()
