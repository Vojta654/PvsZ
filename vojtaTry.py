import pygame,sys, os, random
import Constants as c
def count_x(number_x):
    return number_x * c.SQUARE_SIZE_X


def count_y(number_y):
    return number_y * c.SQUARE_SIZE_Y


def count_ticks(second):
    return second * c.FPS
plant_type = 0
window = pygame.display.set_mode((count_x(c.BOARD_SIZE_X), count_y(c.BOARD_SIZE_Y) + c.MENU_SIZE))
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

# input - možnost vybírání a pokládání rostlin
def game_input0():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEMOTION:
            on_mouse_motion(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            on_mouse_up0(event)
        

current = 0, 0

def on_mouse_motion(event):
    global current
    mx, my = event.pos
    x = mx // c.SQUARE_SIZE_X
    y = my // c.SQUARE_SIZE_Y
    current = x, y

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
        
            
def start_game():
    if 0 not in selected_plants:
        file = open("datasave.txt", "w")
        data = ""
        for index in range(len(selected_plants)):
            data += str(selected_plants[index])+ "\n"
        file.write(data)
        file.close
        os.system("pvz.py")   
        exit()
                   
            
all_plants_images = [c.sunflowerImage, c.peashooterImage, c.boomerangImage, c.repeaterPeaImages[3], c.wallNutImage]
selected_plants = []
for i in range(c.NUM_PLANTS):
    selected_plants.append(0)


def draw_all_plants():
    for index in range(len(all_plants_images)):
        plant = all_plants_images[index]
        window.blit(plant, (count_x(index), count_y(1) + 20))
    

def draw_selected_plants():
    for index in range(c.NUM_PLANTS):
        if selected_plants[index] != 0:
            window.blit(all_plants_images[selected_plants[index] - 2], (count_x(index), count_y(0) + 20))
    


while True:
    game_input0()
    draw_all_plants()
    draw_selected_plants()
    pygame.display.flip()
    