import pygame
import sys

pygame.init()
'''menu style:      TITLE
                Option1(game)
                Option2(quit)
                '''

#BG_IMAGE = pygame.image.load("menu_images\WALL_FURIOUS_EYE1.png")
SELECT_BUTTON_CURSOR=pygame.image.load("menu_images\Skeleton_arm.png")

MENU_BG_COLOR = (0,90,100)
BUTTON_COLOR = (120,100,120)
SELECT_BUTTON_COLOR= (120,180,120,0.1)

quit_selected=0
play_selected=0

TITLE_FONT = pygame.font.Font("Matrix-MZ4P.ttf",100)
QUIT_FONT = pygame.font.Font("Matrix-MZ4P.ttf",40)
PLAY_FONT = pygame.font.Font("Matrix-MZ4P.ttf",40)
#Title_music=pygame.mixer_music.load()
TITLE_TEXT = TITLE_FONT.render("Furious Lardinus", True,(0,0,0))
QUIT_TEXT = QUIT_FONT.render("QUIT GAME", True,(0,quit_selected,0))
PLAY_TEXT = PLAY_FONT.render("PLAY",False,(0,play_selected,0))


#timing initialisation and initialisation of the cursor's position
T_anim_timing: int = 0
upload_times=0
down=0
crsr_init = False

def exit_game():
    quit()
        
def button_init(DIMENSIONS,menu_screen) -> None:
    global BUTTON_QUIT, BUTTON_PLAY
    BUTTON_QUIT = pygame.Rect(DIMENSIONS[0]/2.0 -250/2, DIMENSIONS[1] / 2.0 ,250.0,100.0)
    BUTTON_PLAY = pygame.Rect(DIMENSIONS[0]/2.0 -250/2, DIMENSIONS[1]/ 3.0 + DIMENSIONS[1]/3 , 250.0,100.0 )
    pygame.draw.rect(menu_screen,BUTTON_COLOR,BUTTON_QUIT)
    menu_screen.blit(PLAY_TEXT,(DIMENSIONS[0]/2.0 -244/4, DIMENSIONS[1] / 2.0 +25.0 ))
    pygame.draw.rect(menu_screen,BUTTON_COLOR,BUTTON_PLAY)
    menu_screen.blit(QUIT_TEXT,(DIMENSIONS[0]/2.0 -244/2, DIMENSIONS[1] / 3.0 + DIMENSIONS[1]/3 +25))

def button_select(menu_screen,DIMENSIONS):
    global down,quit_selected,play_selected,QUIT_TEXT,PLAY_TEXT
    keys=pygame.key.get_pressed()
    if ( down==0):
        menu_screen.blit(SELECT_BUTTON_CURSOR,(DIMENSIONS[0]/2.0 -384, DIMENSIONS[1] / 3.0))
        quit_selected=0
        play_selected=210
        QUIT_TEXT = QUIT_FONT.render("QUIT GAME", True,(0,quit_selected,0))
        PLAY_TEXT = PLAY_FONT.render("PLAY",False,(0,play_selected,0))
    elif (down==1):
        menu_screen.blit(SELECT_BUTTON_CURSOR,(DIMENSIONS[0]/2.0 -384, DIMENSIONS[1] / 2.0))
    if ((keys[pygame.K_DOWN] and down==0) or down==1):
        down=1
        play_selected=0
        quit_selected=210
    if keys[pygame.K_UP]:
        down=0
        quit_selected=0
        play_selected=210
    if down==1 and keys[pygame.K_RETURN] or pygame.mouse.get_pos:
        print("aya")
        exit_game()

    QUIT_TEXT = QUIT_FONT.render("QUIT GAME", True,(0,quit_selected,0))
    PLAY_TEXT = PLAY_FONT.render("PLAY",False,(0,play_selected,0))

def title_animation(menu_screen,DIMENSIONS):
    global T_anim_timing,TITLE_TEXT,upload_times
    T_anim_timing +=1
    if 480>T_anim_timing >= 450 or 542>T_anim_timing>=520 :
        TITLE_TEXT = TITLE_FONT.render("F̴̵̨͚̲͕͖̣͍͓̥̫̥̩̉̒̀͋͗̓ͨ̍̈́̃͋̆̾ͭͪ͐̈́́̈́͜͝ů̸̸̴̸̦̯͇̦̮̮̻̩̞̹̹̪̺͈̝͈͋ͩ́́̎ͮ̒͐ͥ̈́̓ͩ̆́͜͝ͅr̵̡̘͖͙͔̪̫͆̈͌ͦi̵̷̧̨̨͓͉̠̹̬̠̳̺͈͇̮̰̘̯̽͗ͩ̅̌̀̅̽̓̕̚͜͜͝͞ͅo̵̵̷̡̡̝̮̜̞̙̟̟͈̮͎͐̌ͧ̆ͮ̓̏̏͂̄ͭ̉̑̑̿̆̋ͬ̏̋͛͘͜͟͢͝͞͝ü͚̖̙̫̺̻̔͊̑̊ͫ͟s̴̴̷̡̛̲̭̬̞͙͔̘̲̖̩̤̺̫̑̍̂͗̎̅͒̆ͥ̓ͯͬ̈́͐͘̕͞͡ͅ Ļ̸̵̧̢̢̫̦̬̖̗̱̦̳̣̘̣̭̖̯̹̠̫͉ͮ̇́̃̋͗̍̍͂͂̓ͥͬ̋͟͜͟͢ȁ̵̟͓ͤ͊ͫ̚r̶̵̭̪̞̖̥̥̟̠̻͇̭̳͉̭̟̗̩̝͗̄̐̓̈̎̏̋̄̎͌͐̊͌ͤͥ̀͊͘d̏͌ͭ̓ͅi͈͇̗̤̟ͥ̍̎͌͟n̻̩ͯͪ̈́͋ͮừ̱̥̗̳̮̞̅͋̓͘͟_s̯̭̥̏ͤ̀ͪ̈", True,(255,0,0))
        menu_screen.blit(TITLE_TEXT, (DIMENSIONS[0]/4-40,DIMENSIONS[1]/5 -15))
    else:
        TITLE_TEXT = TITLE_FONT.render("Furious Lardinus", True,(0,0,0))
        menu_screen.blit(TITLE_TEXT, (DIMENSIONS[0]/4-40,DIMENSIONS[1]/4))
    if T_anim_timing>1200:
        T_anim_timing=0


def menu(menu_screen,DIMENSIONS):
    menu_screen.fill(MENU_BG_COLOR)
    #menu_inputs
    button_select(menu_screen,DIMENSIONS)
    #menu_animation and button_animation/render 
    title_animation(menu_screen,DIMENSIONS)
    button_init(DIMENSIONS,menu_screen)
    


    
