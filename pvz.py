import pygame,sys, os
import Constants as c

pygame.init()

clock = pygame.time.Clock()



for i in range(22):
    img = pygame.image.load(os.path.join("data", "Zombie_" + str(i) + ".png"))
    c.zombieImages.append(img)
window = pygame.display.set_mode((c.BOARD_SIZE_X * c.SQUARE_SIZE_X, (c.BOARD_SIZE_Y * c.SQUARE_SIZE_Y) + c.MENU_SIZE))

# příprava na umisťování rostlin - bude použit podobný kod jako v gomoku
plant_loc = []  # buď pole s souřadenicemi rostlin nebo 2 v board[][]

# vykreslení hrací plochy v listu - možná bude použito k uložení pozic rostlin
board = []
for y in range(0, c.BOARD_SIZE_Y, 1):
    row = []
    for x in range(0, c.BOARD_SIZE_X, 1):
        row.append(0)
    board.append(row)

for i in range(c.BOARD_SIZE_Y):  # tam kde bude jedna se dají sekačky
    board[i][0] = 1


def draw_board():
    window.fill(c.SQUARE01_COLOR)
    odd = 0
    pygame.draw.rect(window, c.MENU_COLOR, (0, 0, c.BOARD_SIZE_X * c.SQUARE_SIZE_X, c.MENU_SIZE))
    for j in range(c.BOARD_SIZE_Y):
        if odd == 0:
            odd = 1
        else:
            odd = 0
        for index in range(0, c.BOARD_SIZE_X, 2):
            pygame.draw.rect(window, c.SQUARE02_COLOR, (
            (index + odd) * c.SQUARE_SIZE_X, (j * c.SQUARE_SIZE_Y) + c.MENU_SIZE, c.SQUARE_SIZE_X, c.SQUARE_SIZE_Y))
    # menu - vykreslení polí, na kterých bude možno vybírat kytky k položení
    for index in range(3):
        pygame.draw.rect(window, c.BLACK, (index * c.SQUARE_SIZE_X + 1, 2, c.SQUARE_SIZE_X - 2, c.SQUARE_SIZE_Y - 4))

    # test pokládání rostlin a zombie
    window.blit(c.peashooter, (10, 10))
    window.blit(c.sunflower, (c.SQUARE_SIZE_X, 10))
    #window.blit(zombie, (500, 10))
    pygame.draw.rect(window, c.WHITE, c.MONEY_COUNTER)
    #window.blit(zombieKybl, (300, 480))

    font = pygame.font.Font("HERMES 1943.ttf", 40)
    text = font.render("pokus",True, c.BLACK)
    window.blit(text, (c.SQUARE_SIZE_X * 8, 10))


    for index in range(1, 6):
        window.blit(c.peashooter, (130, 10 + index * c.SQUARE_SIZE_Y))


# input - možnost vybírání a pokládání rostlin
def game_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


def game_update():
    draw_board()


# vytvoření cvičných kulek
for index in range(5):
    c.bullets.append((1.5 * c.SQUARE_SIZE_X, c.MENU_SIZE + (index + 0.5) * c.SQUARE_SIZE_Y - c.BULLET_SIZE / 2))


# bude voláno pomocí nějakého časovače, možná bude potřeba předat nějkaý parametr
def create_bullets():  # střela se vytvoří na souřadnici rostliny (bude přepočet na potřenné místo) a její souřadnice se bullets.append((x,y)), pak budou muset bý mazány

    for coords in c.bullets:
        x, y = coords
        pygame.draw.rect(window, c.BULLET_COLOR, (x, y, c.BULLET_SIZE, c.BULLET_SIZE))


def move_bullets():  # updatuje polohu střel, je potřeba pole, kde jsou uloženz polohy každé střely - bullets[g
    for index in range(len(c.bullets)):
        x, y = c.bullets[index]
        c.bullets[index] = x + 1, y


def game_output():
    create_bullets()
    move_bullets()
    showZombie()


zombieCoords  = []
for i in range(1, 6):
    zombieCoords.append([c.Z_START_LOCATION, i*c.SQUARE_SIZE_Y, 1])

#zombieCoords = [[1000, 300, 1], [1000, 500, 10]]
def zombie_moveing():  # pohyb zombi, asi bude potřeba vytvořit další funkci na vytváření zombie a pole s jejich lokací
    pass

def showZombie():
    for i in range(len(zombieCoords)):
        zombie_x = zombieCoords[i][0]
        zombie_y = zombieCoords[i][1]
        currentZombieImage = zombieCoords[i][2]
        currentZombieImage += 1
        zombie_x -= c.ZOMBIE_SPEED
        if currentZombieImage == len(c.zombieImages):
            currentZombieImage = 0
        zombieCoords[i][0] = zombie_x
        zombieCoords[i][2] = currentZombieImage
        window.blit(c.zombieImages[currentZombieImage], (zombie_x, zombie_y))

currentZombie = 0

while True:
    game_input()
    game_update()
    game_output()


    pygame.display.flip()
    clock.tick(30)

