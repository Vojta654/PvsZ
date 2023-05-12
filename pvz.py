
import pygame
pygame.init()

clock = pygame.time.Clock()

BOARD_SIZE_X = 10
BOARD_SIZE_Y = 5
SQUARE_SIZE = 120
SQUARE01_COLOR = (79, 150, 4)
SQUARE02_COLOR = (3, 115, 3)
MENU_SIZE = SQUARE_SIZE
MENU_COLOR = (100, 100, 250)
BLACK = (0, 0, 0) # menu buttons backgrounb color
BULLET_COLOR = (150, 30, 30)
BULLET_SIZE = 30
bullets = [] # (x,y)

#image load - potřeba vybrat správnou velikost
zombie = pygame.image.load("zombie.png")
zombieKybl = pygame.image.load("zombieKybl.png")
peashooter = pygame.image.load("peashooter.png")

window = pygame.display.set_mode((BOARD_SIZE_X * SQUARE_SIZE, (BOARD_SIZE_Y * SQUARE_SIZE) + MENU_SIZE))


#vytvoření cvičných kulek
for index in range(5):
    bullets.append(( 1.5 * SQUARE_SIZE - BULLET_SIZE/2, (index+0.5)*SQUARE_SIZE + MENU_SIZE - BULLET_SIZE/2))

#příprava na umisťování rostlin - bude použit podobný kod jako v gomoku
plant_loc = [] #buď pole s souřadenicemi rostlin nebo 1 v board[][]


#vykreslení hrací plochy v listu - možná bude použito k uložení pozic rostlin
board = []
for y in range(0, BOARD_SIZE_Y, 1):
    row = []
    for x in range(0, BOARD_SIZE_X, 1):
        row.append(0)
    board.append(row)

for i in range(BOARD_SIZE_Y):#tam kde bude jedna se dají sekačky
    board[i][0] = 1


def draw_board():
    window.fill(SQUARE01_COLOR)
    odd = 0
    pygame.draw.rect(window, MENU_COLOR, (0, 0, BOARD_SIZE_X * SQUARE_SIZE, MENU_SIZE))
    for j in range(BOARD_SIZE_Y):
        if odd == 0:
            odd = 1
        else:
            odd = 0
        for index in range(0, BOARD_SIZE_X, 2):
            pygame.draw.rect(window, SQUARE02_COLOR, ((index + odd) * SQUARE_SIZE, (j * SQUARE_SIZE) + MENU_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    #menu - vykreslení polí, na kterých bude možno vybírat kytky k položení
    for index in range(3):
        pygame.draw.rect(window, BLACK, (index * SQUARE_SIZE+1, 2, SQUARE_SIZE-2, SQUARE_SIZE - 4))

    #test pokládání rostlin a zombie
    window.blit(peashooter, (10, 10))
    window.blit(zombie, (500, 10))

    window.blit(zombieKybl, (300, 480))
    for index in range(1, 6):
        window.blit(peashooter, (130,10+ index*120))


#input - možnost vybírání a pokládání rostlin
def game_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


def game_update():
    draw_board()

# bude voláno pomocí nějakého časovače, možná bude potřeba předat nějkaý parametr
def create_bullets():#střela se vytvoří na souřadnici rostliny (bude přepočet na střed) a její souřadnice se bullets.append((x,y)), pak budou muset bý mazány
    for coords in bullets:
        x, y = coords
        pygame.draw.rect(window, BULLET_COLOR, (x, y, BULLET_SIZE, BULLET_SIZE))


def move_bullets(): #updatuje polohu střel, je potřeba pole, kde jsou uloženz polohy každé střely - bullets[g
    for index in range(len(bullets)):
        x, y = bullets[index]
        bullets[index] = x+1, y


def game_output():
    create_bullets()
    move_bullets()


def zombie_moveing(): # pohyb zombi, asi bude potřeba vytvořit další funkci na vytváření zombie a pole s jejich lokací
    pass


#game loop
while True:
    game_input()
    game_update()
    game_output()
    pygame.display.flip()
    clock.tick(30)
