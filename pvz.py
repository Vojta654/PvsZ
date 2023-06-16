import pygame,sys, os, random
import Constants as c
bullets = []
suns = []
mowers = []
pygame.init()
clock = pygame.time.Clock()
sunCoin = 250
difficulty = 0
def count_x(number_x):
    return number_x * c.SQUARE_SIZE_X


def count_y(number_y):
    return number_y * c.SQUARE_SIZE_Y


def count_ticks(second):
    return second * c.FPS


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
normalZombiesList  = [[],[],[],[],[]] #jedbotlivé pole je jedna řádka ve hře
mowerList = []

for i in range(1, 6):
    mowerList.append([0, count_y(i), 0])

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
    for index in range(4):
        if index +2 == plant_type:
            color = c.BLACK
        else:
            color = c.GREY
        pygame.draw.rect(window, color, (count_x(index) + 1, 2, c.SQUARE_SIZE_X - 2, c.SQUARE_SIZE_Y - 4))





    #menu - obrázky rostlin + box na počítání peněz
    

    window.blit(c.sunflowerImage, (0, 10))
    window.blit(c.peashooterImage, (count_x(1) +10, 20))
    window.blit(c.boomerangImage, (count_x(2)-2, 0))
    window.blit(c.repeaterPeaImages[3], (count_x(3)-2, 20))

    
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
    plant_type = 0
    if event.key == pygame.K_q:#sunflower
        if sunCoin >= 50:
            plant_type = 2

    elif event.key == pygame.K_w: #peashooter
        if sunCoin >= 100:
            plant_type = 3

    elif event.key == pygame.K_e: #sunflower
        if sunCoin >= 150:
            plant_type = 4
    elif event.key == pygame.K_r: #repeaterPea
        if sunCoin >= 200:
            plant_type = 5



     
plants = [[], [],[],[],[]]
def on_mouse_up(event):
    global current, plant_type, sunCoin
    x,y = current
    if y > 0 and board[y-1][x] == 0 and y < count_y(c.BOARD_SIZE_Y)-5:
        board[y-1][x] = plant_type
        if plant_type == 3:
            plants[y-1].append([x, y, c.PEASHOOTERHP, 0, 3, 0, 0])# x,y, HP, mode, plant type,timer, image_number
            sunCoin -= 100
        if plant_type == 2:
            plants[y-1].append([x, y, c.SUNFLOWERHP, 0, 2, 30, 0])# x,y, HP, mode, plant type,timer
            sunCoin -= 50
        if plant_type == 4:
            plants[y-1].append([x, y, c.BOOMERANG_HP, 0, 4, 0])# x,y, HP, mode, plant type, create boomerang
            sunCoin -= 150
        if plant_type == 5:
            plants[y-1].append([x, y, c.REPEATER_PEA_HP, 0, 5, 0, 0])# x,y, HP, mode, plant type, timer, image_num
            sunCoin -= 200
        plant_type = 0

def on_mouse_down(event):
    global sunCoin, current
    x,y = current
    for sun in suns:
        if x == sun[0] // c.SQUARE_SIZE_X and y == sun[1]// c.SQUARE_SIZE_Y:
            sunCoin += 50
            suns.remove(sun)

def game_update():
    mode_reset()
    platns_zombie_contact()
    check_contact()

    plants_hp()
    mower_move()
    update_plants()
    update_boomerang()

def mode_reset():
    for line in range(5):
        for plant in plants[line]:
            plant[3] = 0
        for zombik in normalZombiesList[line]:
            if zombik[4] >= 10:
                zombik[4] -= 10

def update_plants():
    for index in range(len(plants)):
        line_plant = plants[index]
        for plant in line_plant:
            if plant[4] == 2:#sunflower
                sunflower_suns(plant)
                plant[6] += 0.3
                plant[6] = round(plant[6], 3)
                if plant[6] >= len(c.sunflowerImages) - 1:
                    plant[6] = 0
                    
                    
            elif plant[4] == 3:#peashooter
                create_bullets(plant)
                plant[6] += 0.3
                plant[6] = round(plant[6], 3)
                if plant[6] >= len(c.peashooterImages) - 1:
                    plant[6] = 0
            elif plant[4] == 4:#boomerang
                create_boomerang(plant)
                
            elif plant[4] == 5:# repeater pea
                create_bullets(plant)
                plant[6] += 0.3
                plant[6] = round(plant[6], 3)
                if plant[6] >= len(c.repeaterPeaImages) - 1:
                    plant[6] = 0
sndBullet = 0                
def create_bullets(plant):
    global sndBullet
   
    if plant[4] == 3:
        if plant[5] % count_ticks(4) == 0:
            bullets.append([count_x(plant[0])+ 10, count_y(plant[1] +0.25)])
        plant[5] += 1
    elif plant[4] == 5:
        if plant[5] % count_ticks(4) == 0 :
            bullets.append([count_x(plant[0])+ 10, count_y(plant[1] +0.25)])
            sndBullet = plant[5] + 8
            
            
        if plant[5] == sndBullet:
            bullets.append([count_x(plant[0])+ 10, count_y(plant[1] +0.25)])
        plant[5] += 1

    
def move_bullets():  # updatuje polohu střel
    for bullet in bullets:
        bullet[0] += c.PEASHOOTER_SPEED
        pygame.draw.rect(window, c.BULLET_COLOR, (bullet[0], bullet[1], c.BULLET_SIZE, c.BULLET_SIZE))
        if bullet[0] > 1200:
            bullets.remove(bullet)
        
            
def sunflower_suns(plant):
    if plant[5] % count_ticks(5) == 0:
        suns.append([count_x(plant[0]) + random.randint(0, 68), count_y(plant[1]) + 100])
       
    plant[5] +=1


def draw_suns():
    for sun in suns:
        window.blit(c.sunImage, (sun[0], sun[1]))

boomerangs = []
def create_boomerang(plant):
    if plant[5] == 0:
        boomerangs.append([count_x(plant[0]) + 30,count_x(plant[0]) + 30, count_y(plant[1]) + 50, 0]) # start position, x, y, mode(front/ back), 
        plant[5] = 1
        
def update_boomerang():
    for boomerang in boomerangs:
        if boomerang[3] == 0:
            if boomerang[1] < boomerang[0] +c.BOOMERANG_RANGE or boomerang[0] > boomerang[1]:
                boomerang[1]+= c.BOOMERANG_SPEED
            else:
                boomerang[3]=1
        if boomerang[3] == 1:
            boomerang[1] -= c.BOOMERANG_SPEED
            if boomerang[0] > boomerang[1]:
                boomerang[3] = 0
        if boomerang[3] == -1:
            boomerangs.remove(boomerang)
            
        
def draw_boomerang():
    for boomerang in boomerangs:
        pygame.draw.rect(window, c.YELLOW, (boomerang[1], boomerang[2], c.BOOMERANG_X, c.BOOMERANG_Y))
        
def check_contact():
    for bullet in bullets: #peashoter bullet contact check
        line = int(bullet[1] // c.SQUARE_SIZE_Y) -1
        if len(normalZombiesList[line]) >0:
            if bullet[0] > normalZombiesList[line][0][0] + 25 and bullet[0] > normalZombiesList[line][0][0] + 26 + c.ZOMBIE_SPEED * c.PEASHOOTER_SPEED: # if hit: -1HP, bullet remove
                normalZombiesList[line][0][3] -=1
                bullets.remove(bullet)
                
            if normalZombiesList[line][0][3] == 0:
                normalZombiesList[line].remove(normalZombiesList[line][0])
    for boomerang in boomerangs: # boomerang contact check
        line = int(boomerang[2] // c.SQUARE_SIZE_Y) -1
        if len(normalZombiesList[line]) > 0:
            for zombik in normalZombiesList[line]:
                
                if boomerang[1] >= zombik[0]+50 and boomerang[1] < zombik[0]+ 51 + c.ZOMBIE_SPEED*c.BOOMERANG_SPEED:
                    zombik[3] -=1
                if normalZombiesList[line][0][3] == 0:
                    normalZombiesList[line].remove(zombik)

def mower_move():
    for mower in mowerList:
        if mower[2] == 1:
            if mower[0] < count_x(c.BOARD_SIZE_X):
                mower[0] += c.MOWER_SPEED
                index = mower[1]// c.SQUARE_SIZE_Y -1


                for zombik in normalZombiesList[index]:
                    if zombik[0] > mower[0] + 20 and zombik[0] < mower[0] + 70:
                        normalZombiesList[index].remove(zombik)
           

def draw_mower():
    for mower in mowerList:
        window.blit(c.mower_manImage, (mower[0], mower[1] + 10))



def game_output():
    draw_board()
    draw_plants2()
    draw_suns()
    move_bullets()
    gamelevel_one()
    updateNormalZombie()
    draw_mower()
    draw_boomerang()



def draw_plants2():
    for lineNum in range(5):
        for plant in plants[lineNum]:
            if plant[4] == 2:
                window.blit(c.sunflowerImages[round(plant[6])], (count_x(plant[0]), count_y(plant[1])+10))#sunflower
            elif plant[4] ==3:
                window.blit(c.peashooterImages[round(plant[6])], (count_x(plant[0])+10, count_y(plant[1])+20))#peashooter
            elif plant[4] ==4:
                window.blit(c.boomerangImage, (count_x(plant[0]) -2, count_y(plant[1])))#boomerang - plant
            elif plant[4] ==5:
                window.blit(c.repeaterPeaImages[round(plant[6])], (count_x(plant[0]) -2, count_y(plant[1]) +15))#repeater pea - plant


def draw_plants():
    for ind in range(c.BOARD_SIZE_Y):
        line = board[ind]
        for j in range(len(line)):
            square = line[j]
            if square == 2:
                window.blit(c.sunflowerImages[plant[5]], (count_x(j), count_y(ind + 1)+10))#sunflower
            elif square ==3:
                window.blit(c.peashooterImage, (count_x(j)+10, count_y(ind + 1)+20))#peashooter
            elif square ==4:
                window.blit(c.boomerangImage, (count_x(j) -2, count_y(ind + 1)))#boomerang - plant




def plants_hp():
    for index in range(len(plants)):
        plantLine = plants[index]
        for plant in plantLine:
            pl_x = plant[0]
            pl_y = plant[1]
            if plant[3]==1:
                plant[2] -= 1
                if plant[2] == 0:

                    plants[index].remove(plant)
                    board[pl_y-1][pl_x] = 0
                    if plant[4] == 4:
                        for boomerang in boomerangs: #odebere boomerang když umře kytka
                            if plant[0] ==( boomerang[1] -30) // c.SQUARE_SIZE_X:
                                boomerangs.remove(boomerang)





def updateNormalZombie():
    for line in range(len(normalZombiesList)): #pro každý řádek
        for zombik in range(len(normalZombiesList[line])):
            zombie_x = normalZombiesList[line][zombik][0]
            if zombie_x < c.SQUARE_SIZE_X - 70:
                mowerList[line][2] = 1
            if zombie_x < -80:
                loose()
            zombie_y = normalZombiesList[line][zombik][1]
            # normal zombie
            if normalZombiesList[line][zombik][4] == 0: # animace walk

                currentZombieImage = normalZombiesList[line][zombik][2]
                currentZombieImage += 0.8 #další snímek v animaci
                zombie_x -= c.ZOMBIE_SPEED #posunutí do leva
                if currentZombieImage >= len(c.NormalZombieImages) - 1:
                    currentZombieImage = 0
                #uložení změněných hodnot
                normalZombiesList[line][zombik][0] = zombie_x
                normalZombiesList[line][zombik][2] = currentZombieImage
                #zobrazení
                window.blit(c.NormalZombieImages[round(currentZombieImage)], (zombie_x, zombie_y - 5))
            if normalZombiesList[line][zombik][4] == 10: # animace attack
                currentZombieImage = normalZombiesList[line][zombik][2]
                currentZombieImage += 0.5  # další snímek v animaci
                if currentZombieImage >= len(c.NormalZombieAttackImages) - 1:
                    currentZombieImage = 0
                normalZombiesList[line][zombik][2] = currentZombieImage
                window.blit(c.NormalZombieAttackImages[round(currentZombieImage)], (zombie_x, zombie_y - 5))
                
            # cone head zombie
            if normalZombiesList[line][zombik][4] == 1: # animace walk

                currentZombieImage = normalZombiesList[line][zombik][2]
                currentZombieImage += 0.6 #další snímek v animaci
                zombie_x -= c.ZOMBIE_SPEED #posunutí do leva
                if currentZombieImage >= len(c.ConeheadZombieImages) -1:
                    currentZombieImage = 0
                #uložení změněných hodnot
                normalZombiesList[line][zombik][0] = zombie_x
                normalZombiesList[line][zombik][2] = currentZombieImage
                #zobrazení
                window.blit(c.ConeheadZombieImages[round(currentZombieImage)], (zombie_x, zombie_y - 5))
            
            if normalZombiesList[line][zombik][4] == 11: # animace attack
                currentZombieImage = normalZombiesList[line][zombik][2]
                currentZombieImage += 0.5  # další snímek v animaci
                if currentZombieImage >= len(c.ConeheadZombieAttackImages) - 1:
                    currentZombieImage = 0
                normalZombiesList[line][zombik][2] = currentZombieImage
                window.blit(c.ConeheadZombieAttackImages[round(currentZombieImage)], (zombie_x, zombie_y - 5))
                
                
            #buckethead zombie
            if normalZombiesList[line][zombik][4] == 2: # animace walk

                currentZombieImage = normalZombiesList[line][zombik][2]
                currentZombieImage += 0.4 #další snímek v animaci
                zombie_x -= c.ZOMBIE_SPEED #posunutí do leva
                if currentZombieImage >= len(c.BucketheadZombieImages) -1:
                    currentZombieImage = 0
                #uložení změněných hodnot
                normalZombiesList[line][zombik][0] = zombie_x
                normalZombiesList[line][zombik][2] = currentZombieImage
                #zobrazení
                window.blit(c.BucketheadZombieImages[round(currentZombieImage)], (zombie_x, zombie_y))
                
            if normalZombiesList[line][zombik][4] == 12: # animace attack
                currentZombieImage = normalZombiesList[line][zombik][2]
                currentZombieImage += 0.4  # další snímek v animaci
                if currentZombieImage >= len(c.BucketheadZombieAttackImages) -1:
                    currentZombieImage = 0
                normalZombiesList[line][zombik][2] = currentZombieImage
                window.blit(c.BucketheadZombieAttackImages[round(currentZombieImage)], (zombie_x, zombie_y))

def create_normal_zombie(lineNum, type):
    hp = 0
    if type == 0:
        hp = c.NormalZombieHP
    elif type == 1:
        hp = c.CONEHEADZOMBIE_HP
    elif type == 2:
        hp = c.BUCKETHEADZOMBIE_HP
        
    normalZombiesList[lineNum].append([c.ZOMBIE_START_LOCATION, count_y(lineNum+1), 1, hp, type])
    #udaje pro jednotlivého zombíka [x souřadnice, y souřadnice, aktuální snímek, životy, mode] mode = jde/žere kytku +typ 0, 1, 2 jde; 10, 11, 12 žere

def gamelevel_one():
    global difficulty
    if round(time, 2) % 2 == 0:
        create_normal_zombie(random.randint(0, 4), random.randint(0, difficulty))
    if round(time) % 30 == 0 and round(time) > 1:
        difficulty =1
    if round(time) % 60 == 0 and round(time) > 1:
        difficulty = 2 
        
    
def platns_zombie_contact():
    for ind in range(5):
        zombieLine = normalZombiesList[ind]
        for plant in plants[ind]:
            for zombik in zombieLine:
                zombie_x = zombik[0]
                if zombie_x <= count_x(plant[0]) and zombie_x >= count_x(plant[0]) - 100:
                    zombik[4] += 10 #set zombik animation to eat plant
                    plant[3] = 1 # set plant to remove

                    
def loose():
    window.fill(c.BLACK)
    font = pygame.font.Font('HERMES 1943.ttf', 170)
    text = font.render("you lost", True, c.RED)
    window.blit(text, (100, 100))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()






while True:
    game_input()
    game_update()
    game_output()
    pygame.display.flip()
    time += (1/c.FPS)
    clock.tick(c.FPS)

# 1. Z indexu cisel => na indexy slovne, takze misto plant[0] => plant.x
