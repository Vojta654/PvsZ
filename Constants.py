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
#repeater pea
REPEATER_PEA_HP = 5 * FPS
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
ZOMBIE_SPEED = 0.6 # o kolik se posunou za jedent tik
NormalZombieImages = []

ZOMBIE_SIZE = (175, 156)
for i in range(22):
    img = pygame.image.load(os.path.join("data/NormalZombie", "Zombie_" + str(i) + ".png"))
    image = pygame.transform.scale(img, ZOMBIE_SIZE)
    NormalZombieImages.append(image)
ZOMBIE_START_LOCATION = BOARD_SIZE_X * SQUARE_SIZE_X

NormalZombieAttackImages = []
for i in range(21):
    img = pygame.image.load(os.path.join("data/NormalZombie/attack", "ZombieAttack_" + str(i) + ".png"))
    image = pygame.transform.scale(img, ZOMBIE_SIZE)
    NormalZombieAttackImages.append(image)

ConeheadZombieImages = []
for i in range(21):
    img = pygame.image.load(os.path.join("data/ConeheadZombie/ConeheadZombie", "ConeheadZombie_" + str(i) + ".png"))
    image = pygame.transform.scale(img, ZOMBIE_SIZE)
    ConeheadZombieImages.append(image)


ConeheadZombieAttackImages = []
for i in range(11):
    img = pygame.image.load(os.path.join("data/ConeheadZombie/ConeheadZombieAttack", "ConeheadZombieAttack_" + str(i) + ".png"))
    image = pygame.transform.scale(img, ZOMBIE_SIZE)
    ConeheadZombieAttackImages.append(image)


BucketheadZombieImages = []
for i in range(15):
    img = pygame.image.load(os.path.join("data/BucketheadZombie/BucketheadZombie", "BucketheadZombie_" + str(i) + ".png"))
    image = pygame.transform.scale(img, ZOMBIE_SIZE)
    BucketheadZombieImages.append(image)


BucketheadZombieAttackImages = []
for i in range(11):
    img = pygame.image.load(os.path.join("data/BucketheadZombie/BucketheadZombieAttack", "BucketheadZombieAttack_" + str(i) + ".png"))
    image = pygame.transform.scale(img, ZOMBIE_SIZE)
    BucketheadZombieAttackImages.append(image)


#plants images
SUNFLOWER_IMAGE_SIZE = (116, 120)
sunflowerImages = []
for i in range(18):
    img = pygame.image.load(os.path.join("data/Plants/SunFlower", "SunFlower_" + str(i) + ".png"))
    image = pygame.transform.scale(img, SUNFLOWER_IMAGE_SIZE)
    sunflowerImages.append(image)
    
    
PEASHOOTER_IMAGE_SIZE = (116, SQUARE_SIZE_X)
peashooterImages = []
for i in range(13):
    img = pygame.image.load(os.path.join("data/Plants/Peashooter", "Peashooter_" + str(i) + ".png"))
    image = pygame.transform.scale(img, PEASHOOTER_IMAGE_SIZE)
    peashooterImages.append(image)
    
print(len(peashooterImages))

repeaterPeaImages = []
for i in range(15):
    img = pygame.image.load(os.path.join("data/Plants/RepeaterPea", "RepeaterPea_" + str(i) + ".png"))
    image = pygame.transform.scale(img, PEASHOOTER_IMAGE_SIZE)
    repeaterPeaImages.append(image)
    
print(len(repeaterPeaImages))
