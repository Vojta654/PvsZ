import pygame,sys, os, random
import Constants as c

pygame.init()
clock = pygame.time.Clock()

window = pygame.display.set_mode((c.BOARD_SIZE_X * c.SQUARE_SIZE_X, (c.BOARD_SIZE_Y * c.SQUARE_SIZE_Y) + c.MENU_SIZE))


# vykreslení hrací plochy v listu - je použito k uložení pozic rostlin
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

    #menu - obrázky rostlin + box na počítání peněz
    window.blit(c.peashooterImage, (10, 10))
    window.blit(c.sunflowerImage, (c.SQUARE_SIZE_X, 10))
    pygame.draw.rect(window, c.WHITE, c.MONEY_COUNTER_BOX) ##### rámeček s textem
    font = pygame.font.Font('HERMES 1943.ttf', 32)
    text = font.render('Sluníčka', True, c.BLACK)
    window.blit(text, (c.SQUARE_SIZE_X * 8, 25))



# input - možnost vybírání a pokládání rostlin
def game_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            on_key_down(event)
        elif event.type == pygame.MOUSEMOTION:
            on_mouse_motion(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            on_mouse_down(event)


def on_mouse_down(event):
    global current, plant_type
    print(current)
    x,y = current
    board[y-1][x] = plant_type
    plant_type = 0

plant_type = 0
def on_key_down(event):
    global plant_type
    print(plant_type)
    if event.key == pygame.K_q:
        plant_type = 2
    elif event.key == pygame.K_w:
        plant_type = 3
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
        c.bullets[index] = x + c.BULLET_SPEED, y


def game_output():
    create_bullets()
    move_bullets()
    updateNormalZombie()
    draw_plants()
print(c.MONEY_COUNTER_BOX)

#test zobrazení normálních zombíků
normalZombiesList  = [[],[],[],[],[]]
for i in range(1, 6):
    print(str(i))
    normalZombiesList[i-1].append([c.ZOMBIE_START_LOCATION, i*c.SQUARE_SIZE_Y, 1, c.NormalZombieHP])#udaje pro jednotlivého zombíka [x souřadnice, y souřadnice, aktuální snímek, životy]

#podívá se do board[][], kde jsou uložený pozice rostlin a tyto rostliny zobrazí
def draw_plants():
    for ind in range(c.BOARD_SIZE_Y):
        line = board[ind]
        for j in range(len(line)):
            square = line[j]
            if square == 2:
                window.blit(c.sunflowerImage, (j*c.SQUARE_SIZE_X, (ind + 1) * c.SQUARE_SIZE_Y+10))#sunflower
            elif square ==3:
                window.blit(c.peashooterImage, (j * c.SQUARE_SIZE_X+10, (ind + 1) * c.SQUARE_SIZE_Y+20))#peashooter

print(board)
current = 0
def on_mouse_motion(event):
    global current
    mx, my = event.pos
    x = mx // c.SQUARE_SIZE_X
    y = my // c.SQUARE_SIZE_Y
    current = x, y


def updateNormalZombie():
    for line in range(len(normalZombiesList)): #pro každý řádek
        for zombik in range(len(normalZombiesList[line])):
            zombie_x = normalZombiesList[line][zombik][0]
            zombie_y = normalZombiesList[line][zombik][1]
            currentZombieImage = normalZombiesList[line][zombik][2]
            currentZombieImage += 1 #další snímek v animaci
            zombie_x -= c.ZOMBIE_SPEED #posunutí do leva
            if currentZombieImage == len(c.NormalZombieImages):
                currentZombieImage = 0
            #uložení změněných hodnot
            normalZombiesList[line][zombik][0] = zombie_x
            normalZombiesList[line][zombik][2] = currentZombieImage
            #zobrazení
            window.blit(c.NormalZombieImages[currentZombieImage], (zombie_x, zombie_y))


def gamelevel_one():
    pass


while True:
    game_input()
    game_update()
    game_output()
    pygame.display.flip()
    clock.tick(30)

