import pygame,sys, os, random
import Constants as c
bullets = []
peashooters = []
sunflowers = []
suns = []
mowers = []
pygame.init()
clock = pygame.time.Clock()
sunCoin = 100
def count_x(number_x):
    return number_x * c.SQUARE_SIZE_X


def count_y(number_y):
    return number_y * c.SQUARE_SIZE_Y


window = pygame.display.set_mode((count_x(c.BOARD_SIZE_X), count_y(c.BOARD_SIZE_Y) + c.MENU_SIZE))
time = 0

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
    global plant_type
    window.fill(c.SQUARE01_COLOR)
    odd = 0
    pygame.draw.rect(window, c.MENU_COLOR, (0, 0, count_x(c.BOARD_SIZE_X), c.MENU_SIZE))
    for j in range(c.BOARD_SIZE_Y):
        if odd == 0:
            odd = 1
        else:
            odd = 0
        for index in range(0, c.BOARD_SIZE_X, 2):
            pygame.draw.rect(window, c.SQUARE02_COLOR, (count_x(index + odd), count_y(j) + c.MENU_SIZE, c.SQUARE_SIZE_X, c.SQUARE_SIZE_Y))
    # menu - vykreslení polí, na kterých bude možno vybírat kytky k položení
    for index in range(3):
        if index +2 == plant_type:
            color = c.BLACK
        else:
            color = c.GREY
        pygame.draw.rect(window, color, (count_x(index) + 1, 2, c.SQUARE_SIZE_X - 2, c.SQUARE_SIZE_Y - 4))
    if plant_type == 4:
        font = pygame.font.Font('HERMES 1943.ttf', 32)
        text = font.render("Jsi chudej", True, c.RED)
        window.blit(text, (count_x(8), 25))





    #menu - obrázky rostlin + box na počítání peněz
    window.blit(c.peashooterImage, (c.SQUARE_SIZE_X +10, 20))

    window.blit(c.sunflowerImage, (0, 10))
    pygame.draw.rect(window, c.WHITE, c.MONEY_COUNTER_BOX) ##### rámeček s textem
    font = pygame.font.Font('HERMES 1943.ttf', 32)
    text = font.render(str(sunCoin), True, c.BLACK)
    window.blit(text, (count_x(8), 25))


# input - možnost vybírání a pokládání rostlin
def game_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            on_key_down(event)
        elif event.type == pygame.MOUSEMOTION:
            on_mouse_motion(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            on_mouse_up(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            on_mouse_down(event)


current = 0, 0

def on_mouse_motion(event):
    global current
    mx, my = event.pos
    x = mx // c.SQUARE_SIZE_X
    y = my // c.SQUARE_SIZE_Y
    current = x, y


plant_type = 0
def on_key_down(event):
    global plant_type
    if event.key == pygame.K_q:#sunflower
        if sunCoin >= 50:
            plant_type = 2
        elif sunCoin < 50:
            plant_type = 0
    elif event.key == pygame.K_w: #peashooter
        if sunCoin >= 100:
            plant_type = 3
        elif sunCoin < 100:
            plant_type = 0
    elif event.key == pygame.K_a:
        plant_type = 1
     
plants = [[], [],[],[],[]]
def on_mouse_up(event):
    global current, plant_type, sunCoin
    x,y = current
    if y > 0 and board[y-1][x] == 0:
        board[y-1][x] = plant_type
        if plant_type == 3:
            peashooters.append([count_x(x + 0.6), count_y(y + 0.2), 0])
            plants[y-1].append([x, y, c.PEASHOOTERHP, 0])# x,y, HP, mode
            sunCoin -= 100
        if plant_type == 2:
            sunflowers.append([count_x(x), count_y(y), 0])
            plants[y-1].append([x, y, c.SUNFLOWERHP, 0])
            sunCoin -= 50
        plant_type = 0

def on_mouse_down(event):
    global sunCoin, current
    x,y = current
    for sun in suns:
        if x == sun[0] // c.SQUARE_SIZE_X and y == sun[1]// c.SQUARE_SIZE_Y:
            sunCoin += 250
            suns.remove(sun)

def game_update():
    draw_board()
    check_contact()
    platns_zombie_contact()
    plants_hp()




def create_bullets():
    for plant_bullet in peashooters:
        if plant_bullet[2] % 135 == 0:
            bullets.append([plant_bullet[0], plant_bullet[1]])
        plant_bullet[2] += 1
def move_mowers():
    global plant_type





    
def move_bullets():  # updatuje polohu střel
    for bullet in bullets:
        bullet_loc_x = bullet[0]
        bullet_loc_x += c.PEASHOOTER_SPEED
        bullet[0] = bullet_loc_x        
        pygame.draw.rect(window, c.BULLET_COLOR, (bullet_loc_x, bullet[1], c.BULLET_SIZE, c.BULLET_SIZE))
        if bullet[0] > 1200:
            bullets.remove(bullet)
        
            
def sunflower_suns():
    for sunflower in sunflowers:
        if sunflower[2] % 60 == 0:
            suns.append([sunflower[0] + random.randint(0, 68), sunflower[1] + 100])
        sunflower[2] +=1

def draw_suns():
    for sun in suns:
        window.blit(c.sunImage, (sun[0], sun[1]))

def check_contact():
    for bullet in bullets:
        line = int(bullet[1] // c.SQUARE_SIZE_Y) -1
        if len(normalZombiesList[line]) >0:
            if bullet[0] > normalZombiesList[line][0][0] + 35 and bullet[0] < normalZombiesList[line][0][0] + 45:
                normalZombiesList[line][0][3] -=1
                bullets.remove(bullet)
            if normalZombiesList[line][0][3] == 0:
                normalZombiesList[line].remove(normalZombiesList[line][0])
            
def mower_move(y):
    global plant_type


    plant_type = 0

def game_output():
    draw_plants()
    sunflower_suns()
    draw_suns()
    create_bullets()
    move_bullets()
    gamelevel_one()
    updateNormalZombie()
    



normalZombiesList  = [[],[],[],[],[]] #jedbotlivé pole je jedna řádka ve hře
mowerList = []
for i in range(1, 6):
    mowerList.append([c.SQUARE_SIZE_X, count_y(i), 0])
#podívá se do board[][], kde jsou uložený pozice rostlin a tyto rostliny zobrazí
def draw_plants():
    for ind in range(c.BOARD_SIZE_Y):
        line = board[ind]
        for j in range(len(line)):
            square = line[j]
            if square == 2:
                window.blit(c.sunflowerImage, (count_x(j), count_y(ind + 1)+10))#sunflower
            elif square ==3:
                window.blit(c.peashooterImage, (count_x(j)+10, count_y(ind + 1)+20))#peashooter
            elif square == 1:
                window.blit(c.mower_manImage, (5, count_y(ind+1)+10))
                print(mowerList)



def updateNormalZombie():
    for line in range(len(normalZombiesList)): #pro každý řádek
        for zombik in range(len(normalZombiesList[line])):
            zombie_x = normalZombiesList[line][zombik][0]
            if normalZombiesList[line][zombik][4] == 0:
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
            if normalZombiesList[line][zombik][4] == 1:
                zombie_x -= c.ZOMBIE_SPEED  # posunutí do leva
                zombie_y = normalZombiesList[line][zombik][1]
                currentZombieImage = normalZombiesList[line][zombik][2]
                currentZombieImage += 1  # další snímek v animaci
                if currentZombieImage == len(c.NormalZombieAttackImages):
                    currentZombieImage = 0
                normalZombiesList[line][zombik][2] = currentZombieImage
                window.blit(c.NormalZombieAttackImages[currentZombieImage], (zombie_x, zombie_y))

def create_normal_zombie(lineNum):
    normalZombiesList[lineNum].append([c.ZOMBIE_START_LOCATION, count_y(lineNum+1), 1, c.NormalZombieHP, 0])#udaje pro jednotlivého zombíka [x souřadnice, y souřadnice, aktuální snímek, životy, mode] mode = jde/žere kytku

def gamelevel_one():
    if round(time, 2) == 1:
        create_normal_zombie(random.randint(0, 4))
    if round(time, 2) == 15:
        create_normal_zombie(random.randint(0, 4))
    if round(time, 2) == 15:
        create_normal_zombie(random.randint(0, 4))

def platns_zombie_contact():
    for ind in range(5):
        zombieLine = normalZombiesList[ind]
        for zombik in zombieLine:
            zombie_x = zombik[0]
            for plant in plants[ind]:
                if zombie_x < count_x(plant[0]):
                    zombik[4] = 1
                    plant[3] = 1

def plants_hp():
    for index in range(len(plants)):
        plantLine = plants[index]
        for plant in plantLine:
            pl_x = plant[0]
            pl_y = plant[1]
            if plant[3]==1:
                plant[2] -= 1
                print(plant[2])
                if plant[2] == 0:
                    plants[index].remove(plant)
                    board[pl_y-1][pl_x] = 0
                    normalZombiesList[index][0][4] =0
                    print("já jsem tu kytku snědl")

while True:
    game_input()
    game_update()
    game_output()
    pygame.display.flip()
    time += (1/30)
    clock.tick(30)

# 1. Z indexu cisel => na indexy slovne, takze misto plant[0] => plant.x

#bude se v updateNormalZombie(): dívat jaký je move a podle toho se bude buď pohybovat s animací 1 nebo bude stát a dělat animaci 2