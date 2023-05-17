import pygame
BOARD_SIZE_X = 10
BOARD_SIZE_Y = 5
SQUARE_SIZE_X = 120
SQUARE_SIZE_Y = 150
SQUARE01_COLOR = (79, 150, 4)
SQUARE02_COLOR = (3, 115, 3)
MENU_SIZE = SQUARE_SIZE_Y
MENU_COLOR = (100, 100, 250)
BLACK = (0, 0, 0) # menu buttons backgrounb color
MONEY_COUNTER = (SQUARE_SIZE_X * 8, 10, SQUARE_SIZE_X *2 - 10, SQUARE_SIZE_Y /2)
WHITE = (255,255,255)
BULLET_COLOR = (150, 30, 30)
BULLET_SIZE = 30
bullets = []  # (x,y)

ZOMBIE_SPEED = 0.8 # o kolik se posunou za jedent tik
# image load - potřeba vybrat správnou velikost
zombie = pygame.image.load("data/zombie.png")
zombieKybl = pygame.image.load("data/zombieKybl.png")
peashooter = pygame.image.load("data/peashooter.png")
sunflower = pygame.image.load("data/sunflower.png")
zombieImages = []
Z_START_LOCATION = 9.5 * SQUARE_SIZE_X