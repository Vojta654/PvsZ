import pygame
import sys

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

# image load - potřeba vybrat správnou velikost
zombie = pygame.image.load("data/zombie.png")
zombieKybl = pygame.image.load("data/zombieKybl.png")
peashooter = pygame.image.load("data/peashooter.png")

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


def zombie_moveing():  # pohyb zombi, asi bude potřeba vytvořit další funkci na vytváření zombie a pole s jejich lokací
    pass

#pokus o animované obrázky, buď funguje animace, nebo pohyb. Na animaci zatím kašlem a tedy půjde uělat pohyb mnihem jednodušeji
class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        self.sprites = []
        self.sprites.append(pygame.image.load("data/Zombie_1.png"))

        self.image = self.sprites[0]

        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

    def update(self):
        self.image = self.sprites[0]
        pygame.sprite.Group.empty(showed_zombies)
        showed_zombies.add(player)


showed_zombies = pygame.sprite.Group()

pygame.display.set_caption("idk")
player = Player(loc_X, loc_Y)
showed_zombies.add(player)
# game loop

while True:
    game_input()
    game_update()
    #game_output()
    loc_X -= 1
    print(loc_X)
    player = Player(loc_X, loc_Y)
    showed_zombies.draw(window)
    showed_zombies.update()
    pygame.display.flip()
    clock.tick(30)

