import pygame, sys, random

loc_X = 0
loc_Y = 0
class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load("data/Zombie_1.png"))
        self.sprites.append(pygame.image.load("data/Zombie_2.png"))
        self.sprites.append(pygame.image.load("data/Zombie_3.png"))
        self.sprites.append(pygame.image.load("data/Zombie_4.png"))
        self.sprites.append(pygame.image.load("data/Zombie_5.png"))
        self.sprites.append(pygame.image.load("data/Zombie_6.png"))
        self.sprites.append(pygame.image.load("data/Zombie_7.png"))
        self.sprites.append(pygame.image.load("data/Zombie_8.png"))
        self.sprites.append(pygame.image.load("data/Zombie_9.png"))
        self.sprites.append(pygame.image.load("data/Zombie_10.png"))
        self.sprites.append(pygame.image.load("data/Zombie_11.png"))
        self.sprites.append(pygame.image.load("data/Zombie_12.png"))
        self.sprites.append(pygame.image.load("data/Zombie_13.png"))
        self.sprites.append(pygame.image.load("data/Zombie_14.png"))
        self.sprites.append(pygame.image.load("data/Zombie_15.png"))
        self.sprites.append(pygame.image.load("data/Zombie_16.png"))
        self.sprites.append(pygame.image.load("data/Zombie_17.png"))
        self.sprites.append(pygame.image.load("data/Zombie_18.png"))
        self.sprites.append(pygame.image.load("data/Zombie_19.png"))
        self.sprites.append(pygame.image.load("data/Zombie_20.png"))
        self.sprites.append(pygame.image.load("data/Zombie_21.png"))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()

        self.rect.topleft = [pos_x, pos_y]




    def update(self):
        self.current_sprite +=1
        if self.current_sprite == len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]

        self.rect.move_ip(1, 0)

# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Animation")

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()

player = Player(loc_X, loc_Y)
moving_sprites.add(player)
print(moving_sprites)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    loc_X -=1
    player = Player(loc_X, loc_Y)
    # Drawing
    screen.fill((0, 0, 0))
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()

    clock.tick(30)