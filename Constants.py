import pygame, os
#board setiings
BOARD_SIZE_X = 10
BOARD_SIZE_Y = 5
SQUARE_SIZE_X = 120
SQUARE_SIZE_Y = 150
SQUARE01_COLOR = (10, 130, 4)
SQUARE02_COLOR = (3, 100, 3)
MENU_SIZE = SQUARE_SIZE_Y
MENU_COLOR = (100, 100, 250)
MONEY_COUNTER_BOX = (SQUARE_SIZE_X * 8, 10, SQUARE_SIZE_X *2 - 10, SQUARE_SIZE_Y /2)
FPS = 30
#colors
BLACK = (0, 0, 0) # menu buttons backgrounb color
GREY = (169,169,169)
WHITE = (255,255,255)
GREEM = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
#bullets setting
BULLET_COLOR = (150, 30, 30)
BULLET_SIZE = 30
bullets = []  # (x,y)
PEASHOOTER_SPEED = 8
PEASHOOTERHP =  2* 30
SUNFLOWERHP = 2*30
MOWER_SPEED = 5
# image load - potřeba vybrat správnou velikost
zombie = pygame.image.load("data/zombie.png")
zombieKyblImage = pygame.image.load("data/zombieKybl.png")

#flower image load
peashooterImage = pygame.image.load("data/peashooter.png")
sunflowerImage = pygame.image.load("data/sunflower.png")
sunImage = pygame.image.load("data/sun.png")
mower_manImage = pygame.image.load("data/mower_men.png")
#NormalZombie
NormalZombieHP = 3
ZOMBIE_SPEED = 1 # o kolik se posunou za jedent tik
NormalZombieImages = []
for i in range(22):
    img = pygame.image.load(os.path.join("data/NormalZombie", "Zombie_" + str(i) + ".png"))
    NormalZombieImages.append(img)
ZOMBIE_START_LOCATION = BOARD_SIZE_X * SQUARE_SIZE_X

NormalZombieAttackImages = []
for i in range(21):
    img = pygame.image.load(os.path.join("data/NormalZombie/attack", "ZombieAttack_" + str(i) + ".png"))
    NormalZombieAttackImages.append(img)
