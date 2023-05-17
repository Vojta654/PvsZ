import pygame,sys, os


pygame.init()

clock = pygame.time.Clock()

BOARD_SIZE_X = 10
BOARD_SIZE_Y = 5
SQUARE_SIZE_X = 120
SQUARE_SIZE_Y = 150
SQUARE01_COLOR = (79, 150, 4)
SQUARE02_COLOR = (3, 115, 3)
MENU_SIZE = SQUARE_SIZE_Y
MENU_COLOR = (100, 100, 250)
BLACK = (0, 0, 0)  # menu buttons backgrounb color
BULLET_COLOR = (150, 30, 30)
BULLET_SIZE = 30
bullets = []  # (x,y)
loc_X = 500
loc_Y = 100


ZOMBIE_SPEED = 0.8 # o kolik se posunou za jedent tik
# image load - potřeba vybrat správnou velikost
zombie = pygame.image.load("data/zombie.png")
zombieKybl = pygame.image.load("data/zombieKybl.png")
peashooter = pygame.image.load("data/peashooter.png")
zombieImages = []
Z_START_LOCATION = 9.5 * SQUARE_SIZE_X
for i in range(22):
    img = pygame.image.load(os.path.join("data", "Zombie_" + str(i) + ".png"))
    zombieImages.append(img)
window = pygame.display.set_mode((BOARD_SIZE_X * SQUARE_SIZE_X, (BOARD_SIZE_Y * SQUARE_SIZE_Y) + MENU_SIZE))

# příprava na umisťování rostlin - bude použit podobný kod jako v gomoku
plant_loc = []  # buď pole s souřadenicemi rostlin nebo 2 v board[][]

# vykreslení hrací plochy v listu - možná bude použito k uložení pozic rostlin
board = []
for y in range(0, BOARD_SIZE_Y, 1):
    row = []
    for x in range(0, BOARD_SIZE_X, 1):
        row.append(0)
    board.append(row)

for i in range(BOARD_SIZE_Y):  # tam kde bude jedna se dají sekačky
    board[i][0] = 1


def draw_board():
    window.fill(SQUARE01_COLOR)
    odd = 0
    pygame.draw.rect(window, MENU_COLOR, (0, 0, BOARD_SIZE_X * SQUARE_SIZE_X, MENU_SIZE))
    for j in range(BOARD_SIZE_Y):
        if odd == 0:
            odd = 1
        else:
            odd = 0
        for index in range(0, BOARD_SIZE_X, 2):
            pygame.draw.rect(window, SQUARE02_COLOR, (
            (index + odd) * SQUARE_SIZE_X, (j * SQUARE_SIZE_Y) + MENU_SIZE, SQUARE_SIZE_X, SQUARE_SIZE_Y))
    # menu - vykreslení polí, na kterých bude možno vybírat kytky k položení
    for index in range(3):
        pygame.draw.rect(window, BLACK, (index * SQUARE_SIZE_X + 1, 2, SQUARE_SIZE_X - 2, SQUARE_SIZE_Y - 4))

    # test pokládání rostlin a zombie
    window.blit(peashooter, (10, 10))
    #window.blit(zombie, (500, 10))

    #window.blit(zombieKybl, (300, 480))

    for index in range(1, 6):
        window.blit(peashooter, (130, 10 + index * SQUARE_SIZE_Y))


# input - možnost vybírání a pokládání rostlin
def game_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


def game_update():
    draw_board()


# vytvoření cvičných kulek
for index in range(5):
    bullets.append((1.5 * SQUARE_SIZE_X, MENU_SIZE + (index + 0.5) * SQUARE_SIZE_Y - BULLET_SIZE / 2))


# bude voláno pomocí nějakého časovače, možná bude potřeba předat nějkaý parametr
def create_bullets():  # střela se vytvoří na souřadnici rostliny (bude přepočet na potřenné místo) a její souřadnice se bullets.append((x,y)), pak budou muset bý mazány

    for coords in bullets:
        x, y = coords
        pygame.draw.rect(window, BULLET_COLOR, (x, y, BULLET_SIZE, BULLET_SIZE))


def move_bullets():  # updatuje polohu střel, je potřeba pole, kde jsou uloženz polohy každé střely - bullets[g
    for index in range(len(bullets)):
        x, y = bullets[index]
        bullets[index] = x + 1, y


def game_output():
    create_bullets()
    move_bullets()

zombieCoords  = []
for i in range(1, 6):
    zombieCoords.append([Z_START_LOCATION, i*SQUARE_SIZE_Y, 1])

#zombieCoords = [[1000, 300, 1], [1000, 500, 10]]
def zombie_moveing():  # pohyb zombi, asi bude potřeba vytvořit další funkci na vytváření zombie a pole s jejich lokací
    pass

def showZombie():
    for i in range(len(zombieCoords)):
        zombie_x = zombieCoords[i][0]
        zombie_y = zombieCoords[i][1]
        currentZombie = zombieCoords[i][2]
        currentZombie += 1
        zombie_x -= ZOMBIE_SPEED
        if currentZombie == len(zombieImages):
            currentZombie = 0
        zombieCoords[i][0] = zombie_x
        zombieCoords[i][2] = currentZombie
        window.blit(zombieImages[currentZombie], (zombie_x, zombie_y))

currentZombie = 0
zombie_location_Y = 500
while True:
    game_input()
    game_update()
    game_output()
    showZombie()

    pygame.display.flip()
    clock.tick(30)

