import pygame


import time
from typing import Any, Callable, Dict

testing: Dict[str, Dict[str, int | float]] = {}

def add_test(funcName: str, time: float) -> None:
    global testing
    if not funcName in testing:
        testing[funcName] = {
            "time": 0,
            "n": 0
        }
    testing[funcName]["time"] += time
    testing[funcName]["n"] += 1

def time_tester(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
    def wrapper(*args: Any):
        global testing
        t0 = time.time()
        result = func(*args)
        add_test(func.__name__, time.time() - t0)
        return result
    return wrapper

def test_tick() -> None:
    global testing
    for elem in testing:
        n = testing[elem]["n"]
        time = testing[elem]["time"]
        print(f"{elem: <30s}: {n:<10d} {time}")
        testing[elem]["time"] = 0
        testing[elem]["n"] = 0
        
    






pygame.init()
'''menu style:      TITLE
                Option1(game)
                Option2(quit)
                '''
screen_update =False
#
def button_init(DIMENSIONS):
    global BUTTON_PLAY,BUTTON_QUIT
    BUTTON_QUIT = pygame.Rect(DIMENSIONS[0]/2.0 -250/2, DIMENSIONS[1] / 2.0 ,250.0,100.0)
    BUTTON_PLAY = pygame.Rect(DIMENSIONS[0]/2.0 -250/2, DIMENSIONS[1]/ 3.0 + DIMENSIONS[1]/3 , 250.0,100.0 )
#clock
clock=pygame.time.Clock()
#game's name
pygame.display.set_caption('Furious Lardinous')
#BG_IMAGE = pygame.image.load("menu_images\WALL_FURIOUS_EYE1.png")
SELECT_BUTTON_CURSOR=pygame.image.load("menu_images\Skeleton_arm.png")
MOUSE_MENU_CURSOR = pygame.image.load("menu_images\Cursor.png")
MENU_BG_COLOR = (0,90,100)
BUTTON_COLOR = (120,100,120)
SELECT_BUTTON_COLOR= (120,180,120,0.1)
GAME_ICON = pygame.image.load("menu_images/furious_lardinous_icon.png")
BG = pygame.image.load("menu_images\BG.png")
BG_image_center = (BG.get_size()[0])/2
#game-menu cursor
pygame.mouse.set_cursor(pygame.cursors.Cursor((64,0),MOUSE_MENU_CURSOR))
pygame.display.set_icon(GAME_ICON)

quit_selected=0
play_selected=0

in_manu = True

TITLE_FONT = pygame.font.Font("menu_fonts\Matrix-MZ4P.ttf",100)
QUIT_FONT = pygame.font.Font("menu_fonts\Matrix-MZ4P.ttf",40)
PLAY_FONT = pygame.font.Font("menu_fonts\Matrix-MZ4P.ttf",40)
'''Title_music=pygame.mixer_music.load()'''
TITLE_TEXT = TITLE_FONT.render("Furious Lardinus", True,(0,0,0))
QUIT_TEXT = QUIT_FONT.render("QUIT GAME", True,(0,quit_selected,0))
PLAY_TEXT = PLAY_FONT.render("PLAY",False,(0,play_selected,0))


#timing initialisation and initialisation of the cursor's position
T_anim_timing: int = 0
upload_times: int = 0
down: int = 0

def exit_game():
    quit()

@time_tester  
def button(DIMENSIONS,menu_screen) -> None:
    global BUTTON_QUIT, BUTTON_PLAY,button0_pos,button1_pos
    pygame.draw.rect(menu_screen,BUTTON_COLOR,BUTTON_QUIT)
    menu_screen.blit(PLAY_TEXT,(DIMENSIONS[0]/2.0 -244/4, DIMENSIONS[1] / 2.0 +25.0 ))
    button0_pos = (DIMENSIONS[0]/2.0 -250/2, DIMENSIONS[1] / 2.0  )
    pygame.draw.rect(menu_screen,BUTTON_COLOR,BUTTON_PLAY)
    menu_screen.blit(QUIT_TEXT,(DIMENSIONS[0]/2.0 -244/2, DIMENSIONS[1] / 3.0 + DIMENSIONS[1]/3 +25))
    button1_pos = (DIMENSIONS[0]/2.0 -250/2, DIMENSIONS[1]/ 3.0 + DIMENSIONS[1]/3) 
    
@time_tester
def mouse_position():
    global mouse_crs_position
    mouse_crs_position = pygame.mouse.get_pos()
@time_tester
def mouse_click():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            return True
@time_tester
def check_mouse_On_button0():
    global mouse_crs_position,button0_pos
    if (button0_pos[0]<=mouse_crs_position[0]<=button0_pos[0]+250) and (button0_pos[1]<=mouse_crs_position[1]<=button0_pos[1]+100):
        return True
    else:
        return False
def check_mouse_On_button1():
    if (button1_pos[0]<=mouse_crs_position[0]<=button1_pos[0]+250) and (button1_pos[1]<=mouse_crs_position[1]<=button1_pos[1]+100):
        return True
    else:
        return False
@time_tester    
def button_select(menu_screen,DIMENSIONS,in_menu):
    global down,quit_selected,play_selected,QUIT_TEXT,PLAY_TEXT, in_manu
    keys=pygame.key.get_pressed()
    mouse_click()
    if ( down==0) or check_mouse_On_button0() :
        down=0
        menu_screen.blit(SELECT_BUTTON_CURSOR,(DIMENSIONS[0]/2.0 -384, DIMENSIONS[1] / 3.0))
        quit_selected=0
        play_selected=210
        QUIT_TEXT = QUIT_FONT.render("QUIT GAME", True,(0,quit_selected,0))
        PLAY_TEXT = PLAY_FONT.render("PLAY",False,(0,play_selected,0))
    elif (down==1):
        menu_screen.blit(SELECT_BUTTON_CURSOR,(DIMENSIONS[0]/2.0 -384, DIMENSIONS[1] / 2.0))
    if ((keys[pygame.K_DOWN] and down==0) or down==1)or check_mouse_On_button1():
        down=1
        play_selected=0
        quit_selected=210
    if keys[pygame.K_UP]:
        down=0
        quit_selected=0
        play_selected=210
    if down==1 and (keys[pygame.K_RETURN] or (mouse_click() and check_mouse_On_button1())):
        exit_game()
    if down==0 and (keys[pygame.K_RETURN] or (mouse_click() and check_mouse_On_button0())):
        in_manu = in_menu = False 
        start_game()    
    QUIT_TEXT = QUIT_FONT.render("QUIT GAME", True,(0,quit_selected,0))
    PLAY_TEXT = PLAY_FONT.render("PLAY",False,(0,play_selected,0))

@time_tester
def title_animation(menu_screen,DIMENSIONS):
    global T_anim_timing,TITLE_TEXT,upload_times,screen_update
    T_anim_timing +=1
    if T_anim_timing>1200:
        T_anim_timing=0
    if 480>T_anim_timing >= 450 or 542>T_anim_timing>=520 :
        TITLE_TEXT = TITLE_FONT.render("F̴̵̨͚̲͕͖̣͍͓̥̫̥̩̉̒̀͋͗̓ͨ̍̈́̃͋̆̾ͭͪ͐̈́́̈́͜͝ů̸̸̴̸̦̯͇̦̮̮̻̩̞̹̹̪̺͈̝͈͋ͩ́́̎ͮ̒͐ͥ̈́̓ͩ̆́͜͝ͅr̵̡̘͖͙͔̪̫͆̈͌ͦi̵̷̧̨̨͓͉̠̹̬̠̳̺͈͇̮̰̘̯̽͗ͩ̅̌̀̅̽̓̕̚͜͜͝͞ͅo̵̵̷̡̡̝̮̜̞̙̟̟͈̮͎͐̌ͧ̆ͮ̓̏̏͂̄ͭ̉̑̑̿̆̋ͬ̏̋͛͘͜͟͢͝͞͝ü͚̖̙̫̺̻̔͊̑̊ͫ͟s̴̴̷̡̛̲̭̬̞͙͔̘̲̖̩̤̺̫̑̍̂͗̎̅͒̆ͥ̓ͯͬ̈́͐͘̕͞͡ͅ Ļ̸̵̧̢̢̫̦̬̖̗̱̦̳̣̘̣̭̖̯̹̠̫͉ͮ̇́̃̋͗̍̍͂͂̓ͥͬ̋͟͜͟͢ȁ̵̟͓ͤ͊ͫ̚r̶̵̭̪̞̖̥̥̟̠̻͇̭̳͉̭̟̗̩̝͗̄̐̓̈̎̏̋̄̎͌͐̊͌ͤͥ̀͊͘d̏͌ͭ̓ͅi͈͇̗̤̟ͥ̍̎͌͟n̻̩ͯͪ̈́͋ͮừ̱̥̗̳̮̞̅͋̓͘͟_s̯̭̥̏ͤ̀ͪ̈", True,(255,0,0))
        menu_screen.blit(TITLE_TEXT, (DIMENSIONS[0]/4-40,DIMENSIONS[1]/5 -15))
        return True
    else:
        TITLE_TEXT = TITLE_FONT.render("Furious Lardinus", True,(0,0,0))
        menu_screen.blit(TITLE_TEXT, (DIMENSIONS[0]/4-40,DIMENSIONS[1]/4))
        return False
@time_tester
def menu_BG(menu_screen, DIMENSIONS):
    global screen_update
    if title_animation(menu_screen, DIMENSIONS) or screen_update ==True:
        menu_screen.blit(BG,(DIMENSIONS[0]/2-BG_image_center,-64))
        screen_update = False


#start game 

def start_game():
    pass
'''write code here'''

@time_tester
def tick(menu_screen,DIMENSIONS, in_menu):
    menu_BG(menu_screen,DIMENSIONS)
    #menu_animation and button_animation/render 
    title_animation(menu_screen,DIMENSIONS)
    button(DIMENSIONS,menu_screen)
    #menu_inputs
    mouse_position()
    button_select(menu_screen,DIMENSIONS,in_menu)
    pygame.display.flip()
    
    menu_screen.fill(MENU_BG_COLOR)
    test_tick()



def menu(menu_screen,DIMENSIONS, in_menu):
    while in_manu:
        tick(menu_screen,DIMENSIONS, in_menu)



    
