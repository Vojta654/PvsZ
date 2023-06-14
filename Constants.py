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
YELLOW = (255,255,0)
#bullets setting
BULLET_COLOR = (150, 30, 30)
BULLET_SIZE = 30
bullets = []  # (x,y)
PEASHOOTER_SPEED = 8
PEASHOOTERHP =  3* FPS
SUNFLOWERHP = 3*FPS
MOWER_SPEED = 5
#boomerang settings
BOOMERANG_X = 30
BOOMERANG_Y = 4
BOOMERANG_SPEED = 10
BOOMERANG_RANGE = 650
BOOMERANG_HP = 4* FPS
# image load - potřeba vybrat správnou velikost
zombie = pygame.image.load("data/zombie.png")
zombieKyblImage = pygame.image.load("data/zombieKybl.png")

#flower image load
peashooterImage = pygame.image.load("data/peashooter.png")
sunflowerImage = pygame.image.load("data/sunflower.png")
boomerangImage = pygame.image.load("data/boomerang.png")
sunImage = pygame.image.load("data/sun.png")
mower_manImage = pygame.image.load("data/mower_men.png")
#NormalZombie
NormalZombieHP = 3
CONEHEADZOMBIE_HP = 5
BUCKETHEADZOMBIE_HP = 7
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

ConeheadZombieImages = []
for i in range(21):
    img = pygame.image.load(os.path.join("data/ConeheadZombie/ConeheadZombie", "ConeheadZombie_" + str(i) + ".png"))
    ConeheadZombieImages.append(img)


ConeheadZombieAttackImages = []
for i in range(11):
    img = pygame.image.load(os.path.join("data/ConeheadZombie/ConeheadZombieAttack", "ConeheadZombieAttack_" + str(i) + ".png"))
    ConeheadZombieAttackImages.append(img)


BucketheadZombieImages = []
for i in range(15):
    img = pygame.image.load(os.path.join("data/BucketheadZombie/BucketheadZombie", "BucketheadZombie_" + str(i) + ".png"))
    BucketheadZombieImages.append(img)


BucketheadZombieAttackImages = []
for i in range(11):
    img = pygame.image.load(os.path.join("data/BucketheadZombie/BucketheadZombieAttack", "BucketheadZombieAttack_" + str(i) + ".png"))
    BucketheadZombieAttackImages.append(img)

print("loaded")