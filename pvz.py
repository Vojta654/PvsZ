import pygame,sys, os, random
import Constants as c
bullets = []
suns = []
mowers = []
pygame.init()
clock = pygame.time.Clock()
sunCoin = 100
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
    global color
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
    for index in range(5):
        if index == highlighted_slot:
            color = c.BLACK
        else:
            color = c.GREY
        pygame.draw.rect(window, color, (count_x(index) + 1, 2, c.SQUARE_SIZE_X - 2, c.SQUARE_SIZE_Y - 4))





    #menu - obrázky rostlin + box na počítání peněz
    for index in range(len(selected_plants)):
        window.blit(all_plants_images[selected_plants[index] - 2], (count_x(index), count_y(0) + 20))

    
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
prizes = {
    2 : 50,
    3 : 100,
    4 : 150,
    5 : 200,
    6 : 50,
    7 : 25,
    8 : 200,
    0 : 0
    #addplant
}
remove_mode = 0
highlighted_slot = None
def on_key_down(event):
    global highlighted_slot, remove_mode
    global plant_type
    plant_type = 0
    if event.key == pygame.K_q:#slot1
        plant_type = selected_plants[0]
        if check_sunCoin(plant_type):
            highlighted_slot = 0
        
        
    elif event.key == pygame.K_w: #slot2
        plant_type = selected_plants[1]
        if check_sunCoin(plant_type):
            highlighted_slot = 1
    
    elif event.key == pygame.K_e: #slot3
        plant_type = selected_plants[2]
        if check_sunCoin(plant_type):
            highlighted_slot = 2
        
    elif event.key == pygame.K_r: #slot4
        plant_type = selected_plants[3]
        if check_sunCoin(plant_type):
            highlighted_slot = 3
        
    elif event.key == pygame.K_t: #slot5
        plant_type = selected_plants[4]
        if check_sunCoin(plant_type):
            highlighted_slot = 4
    
    elif event.key == pygame.K_BACKSPACE:
        remove_mode = 1


def check_sunCoin(typ):
    global plant_type, highlighted_slot
    if prizes[typ] <= sunCoin:
        return True
    else:
        plant_type = 0
        return False
        
     
plants = [[], [],[],[],[]]
def on_mouse_up(event):
    global current, plant_type, sunCoin, highlighted_slot
    x,y = current
    if y > 0 and board[y-1][x] == 0 and y < count_y(c.BOARD_SIZE_Y)-5:
        board[y-1][x] = plant_type
        if plant_type == 2:
            plants[y-1].append([x, y, c.SUNFLOWERHP, 0, 2, 30, 0])# x,y, HP, mode, plant type,timer
            sunCoin -= prizes[2]
        elif plant_type == 3:
            plants[y-1].append([x, y, c.PEASHOOTERHP, 0, 3, 0, 0])# x,y, HP, mode, plant type,timer, image_number
            sunCoin -= prizes[3]
        elif plant_type == 4:
            plants[y-1].append([x, y, c.BOOMERANG_HP, 0, 4, 0])# x,y, HP, mode, plant type, create boomerang
            sunCoin -= prizes[4]
        elif plant_type == 5:
            plants[y-1].append([x, y, c.REPEATER_PEA_HP, 0, 5, 0, 0])# x,y, HP, mode, plant type, timer, image_num
            sunCoin -= prizes[5]
        elif plant_type == 6:
            plants[y-1].append([x, y, c.WALL_NUT_HP, 0, 6, 0, 0])# x,y, HP, mode, plant type, timer, image_num
            sunCoin -= prizes[6]
        elif plant_type == 7:
            plants[y-1].append([x, y, 1, 0, 7, 0, 0])# x,y, HP, mode, plant type, timer, image_num
            sunCoin -= prizes[7]
        elif plant_type == 8:
            plants[y-1].append([x, y, c.LASER_BEAN_HP, 0, 8, 1, 0])# x,y, HP, mode, plant type, timer, image_num
            sunCoin -= prizes[8]
        plant_type = 0
        highlighted_slot = None

def on_mouse_down(event):
    global sunCoin, current, remove_mode
    x,y = current
    if remove_mode == 0:
        for sun in suns:
            if x == sun[0] // c.SQUARE_SIZE_X and y == sun[1]// c.SQUARE_SIZE_Y:
                sunCoin += 50
                suns.remove(sun)
    if remove_mode == 1:
        board[y -1][x] =0
        for line in range(5):
            for plant in plants[line]:
                if plant[0] == x and plant[1] == y:
                    plants[line].remove(plant)
                    remove_mode = 0
                    for num in range(prizes[plant[4]]//50):
                        suns.append([count_x(plant[0]) + random.randint(0, 68), count_y(plant[1]) + 100])
                    break
        
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
            elif plant[4] == 8:
                create_laser(plant, index) 
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
        
lasers = []
def create_laser(plant, index):
    if plant[5] % count_ticks(2) == 0:
        lasers.append([count_x(plant[0]), count_y(plant[1]), c.FPS])
        for zombik in normalZombiesList[index]:
            if zombik[0] > count_x(plant[0]) and zombik[0] < window.get_width() - 20:    
                zombik[3] -= 150
                if zombik[3] <= 0:
                    normalZombiesList[index].remove(zombik) 
    plant[5] +=1
            
            
def draw_lasers():
    for laser in lasers:
        if laser[2] >=0:
            pygame.draw.rect(window, c.GREEN, (laser[0] + 60, laser[1] + 60, window.get_width() - laser[0], 15))
        laser[2] -=1
        if laser[2] < 0:
            lasers.remove(laser)
            
            
def check_contact():
    for bullet in bullets: #peashoter bullet contact check
        line = int(bullet[1] // c.SQUARE_SIZE_Y) -1
        if len(normalZombiesList[line]) >0:
            if bullet[0] > normalZombiesList[line][0][0] + 25 and bullet[0] > normalZombiesList[line][0][0] + 26 + c.ZOMBIE_SPEED * c.PEASHOOTER_SPEED: # if hit: -1HP, bullet remove
                normalZombiesList[line][0][3] -= 350
                bullets.remove(bullet)
                
            if normalZombiesList[line][0][3] == 0:
                normalZombiesList[line].remove(normalZombiesList[line][0])
    for boomerang in boomerangs: # boomerang contact check
        line = int(boomerang[2] // c.SQUARE_SIZE_Y) -1
        if len(normalZombiesList[line]) > 0:
            for zombik in normalZombiesList[line]:
                
                if boomerang[1] >= zombik[0]+50 and boomerang[1] < zombik[0]+ 52 + c.ZOMBIE_SPEED*c.BOOMERANG_SPEED:
                    zombik[3] -= 200
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
    draw_plants()
    draw_suns()
    move_bullets()
    gamelevel_one()
    updateNormalZombie()
    draw_mower()
    draw_boomerang()
    draw_lasers()



def draw_plants():
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
            elif plant[4] ==6:
                window.blit(c.wallNutImage, (count_x(plant[0]) +10, count_y(plant[1]) +15))#wall nut
            elif plant[4] ==7:
                window.blit(c.potatoeBombImage, (count_x(plant[0]) +10, count_y(plant[1]) +50))#potatoe bomb
            elif plant[4] ==8:
                window.blit(c.laserBeanImage, (count_x(plant[0]) +10, count_y(plant[1]) +10))#laser bean
            #addplant


def plants_hp():
    for index in range(len(plants)):
        plantLine = plants[index]
        for plant in plantLine:
            pl_x = plant[0]
            pl_y = plant[1]
            if plant[2] <= 0:
                plants[index].remove(plant)
                board[pl_y-1][pl_x] = 0
                if plant[4] == 4:
                    for boomerang in boomerangs: #odebere boomerang když umře kytka
                        if count_x(plant[0]) ==( boomerang[0] -30):
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
                    plant[2] -= 1 # set plant to remove HPs
                    if plant[4] == 7: #potatoe bomb
                        plant[2] = -1
                        normalZombiesList[ind].remove(zombik)
                        for zombie in normalZombiesList[ind]:
                            if abs(zombie[0] - zombik[0]) <= 50:
                                normalZombiesList[ind].remove(zombie)

                    
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
def game_input0():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEMOTION:
            on_mouse_motion(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            on_mouse_up0(event)
            
all_plants_images = [c.sunflowerImage, c.peashooterImage, c.boomerangImage, c.repeaterPeaImages[3], c.wallNutImage, c.potatoeBombImage, c.laserBeanImage]#addplant
selected_plants = []
for i in range(c.NUM_PLANTS):
    selected_plants.append(0)

def on_mouse_up0(event):
    global current, plant_type, sunCoin
    x,y = current
    if y == 1:
        if x == 0:
            print("sunflower")
            plant_type = 2
        elif x == 1:
            plant_type = 3
            print("peashooterImage")
        elif x == 2:
            plant_type = 4
            print("boomerangImage")
        elif x == 3:
            plant_type = 5
            print("repeaterPeaImages")
        elif x == 4:
            plant_type = 6
            print("wallNutImage")
        elif x == 5:
            plant_type = 7
            print("potatoeBombImage")
        elif x == 6:
            plant_type = 8
            print("laserBeanImage")
        
        #addplant
        if plant_type >= 2:
            for index in range(len(selected_plants)):
                if selected_plants[index] == 0 and plant_type not in selected_plants:
                    selected_plants[index] = plant_type  
                    plant_type = 0
            
    elif y == 5 and x == 9:
        start_game()
    if y == 0:
        selected_plants.remove(selected_plants[x])
        selected_plants.append(0)
        
def draw_all_plants():
    for index in range(len(all_plants_images)):
        plant = all_plants_images[index]
        window.blit(plant, (count_x(index), count_y(1) + 20))
    

def draw_selected_plants():
    for index in range(c.NUM_PLANTS):
        if selected_plants[index] != 0:
            window.blit(all_plants_images[selected_plants[index] - 2], (count_x(index), count_y(0) + 20))
    
def start_game():
    global menu
    if 0 not in selected_plants:
        menu = False

menu = True
def draw_menu():
    window.fill(c.SQUARE01_COLOR)
    #vykreslení menu kam se budou dávat vybrané kytky
    for index in range(c.NUM_PLANTS):
            if index +2 == plant_type:
                color = c.BLACK
            else:
                color = c.GREY
            pygame.draw.rect(window, color, (count_x(index) + 1, 2, c.SQUARE_SIZE_X - 2, c.SQUARE_SIZE_Y - 4))
                
    #confirmation button
    pygame.draw.rect(window, c.YELLOW, (count_x(9), count_y(5), c.SQUARE_SIZE_X, c.SQUARE_SIZE_Y))

while menu:#selecting menu
    game_input0()
    draw_menu()
    draw_all_plants()
    draw_selected_plants()
    pygame.display.flip()
    

while True:
    game_input()
    game_update()
    game_output()
    pygame.display.flip()
    time += (1/c.FPS)
    clock.tick(c.FPS)

# 1. Z indexu cisel => na indexy slovne, takze misto plant[0] => plant.x
