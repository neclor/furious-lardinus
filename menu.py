import pygame


pygame.init()
'''menu style:      TITLE
                Option1(game)
                Option2(quit)
                '''
screen_update =False
#
RFPS : float
def button_init(DIMENSIONS):
    global BUTTON_PLAY,BUTTON_QUIT,button0_pos,button1_pos
    BUTTON_QUIT = pygame.Rect(DIMENSIONS[0]/2.0 -250/2, DIMENSIONS[1] / 2.0 ,250.0,100.0)
    BUTTON_PLAY = pygame.Rect(DIMENSIONS[0]/2.0 -250/2, DIMENSIONS[1]/ 3.0 + DIMENSIONS[1]/3 , 250.0,100.0 )
    button0_pos = (DIMENSIONS[0]/2.0 -250/2, DIMENSIONS[1] / 2.0  )
    button1_pos = (DIMENSIONS[0]/2.0 -250/2, DIMENSIONS[1]/ 3.0 + DIMENSIONS[1]/3) 




#BG_IMAGE = pygame.image.load("menu_images\WALL_FURIOUS_EYE1.png")
def menu_image_init():
    global SELECT_BUTTON_COLOR,MENU_BG_COLOR, SELECT_BUTTON_CURSOR,BUTTON_COLOR, BG_image_center_X,quit_color,play_color,BG
    SELECT_BUTTON_CURSOR=pygame.image.load("menu_images\Skeleton_arm.png")
    MOUSE_MENU_CURSOR = pygame.image.load("menu_images\Cursor.png")
    MENU_BG_COLOR = (110,10,10)
    BUTTON_COLOR = (120,100,120)
    SELECT_BUTTON_COLOR= (120,180,120,0.1)
    GAME_ICON = pygame.image.load("menu_images/furious_lardinous_icon.png")
    BG = pygame.image.load("menu_images\BG.png").convert()
    BG_image_center_X = (BG.get_size()[0])/2
    BG_image_center_Y = (BG.get_size()[1])/2
    BG = pygame.transform.scale(BG,(BG_image_center_X*2,BG_image_center_Y*2))
    BG_image_center_X = (BG.get_size()[0])/2
    #game-menu cursor
    pygame.mouse.set_cursor(pygame.cursors.Cursor((64,0),MOUSE_MENU_CURSOR))
    pygame.display.set_icon(GAME_ICON)
    #button color when selected
    quit_color=(0,0,0)
    play_color=(0,0,0)


def text_init():
    global TITLE_TEXT,QUIT_TEXT,PLAY_TEXT, TITLE_FONT, QUIT_FONT, PLAY_FONT
    TITLE_FONT = pygame.font.Font("menu_fonts\Matrix-MZ4P.ttf",100)
    QUIT_FONT = pygame.font.Font("menu_fonts\Matrix-MZ4P.ttf",40)
    PLAY_FONT = pygame.font.Font("menu_fonts\Matrix-MZ4P.ttf",40)

    TITLE_TEXT = TITLE_FONT.render("Furious Lardinus", True,(0,0,0))
    QUIT_TEXT = QUIT_FONT.render("QUIT GAME", True,quit_color)
    PLAY_TEXT = PLAY_FONT.render("PLAY",False,play_color)


#timing initialisation and initialisation of the cursor's position
def timing_init():
    global T_anim_timing,down, upload_times,in_menu, key_timing
    T_anim_timing = 0
    upload_times= 0
    down = 0
    in_menu = True
    key_timing = 101


  
def button(DIMENSIONS,menu_screen) -> None:
    global BUTTON_QUIT, BUTTON_PLAY,button0_pos,button1_pos
    pygame.draw.rect(menu_screen,BUTTON_COLOR,BUTTON_QUIT)
    menu_screen.blit(PLAY_TEXT,(DIMENSIONS[0]/2.0 -244/4, DIMENSIONS[1] / 2.0 +25.0 ))
    
    pygame.draw.rect(menu_screen,BUTTON_COLOR,BUTTON_PLAY)
    menu_screen.blit(QUIT_TEXT,(DIMENSIONS[0]/2.0 -244/2, DIMENSIONS[1] / 3.0 + DIMENSIONS[1]/3 +25))
   

def cursor_draw(DIMENSIONS,menu_screen):
    menu_screen.blit(SELECT_BUTTON_CURSOR,(DIMENSIONS[0]/2.0 -384, DIMENSIONS[1] / (3.0-down)))

def interactive_element_draw(DIMENSIONS,menu_screen):
    button(DIMENSIONS,menu_screen)
    #cursor_draw(DIMENSIONS,menu_screen)

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
    
def mouse_position():
    global mouse_crs_position
    mouse_crs_position = pygame.mouse.get_pos()

def mouse_click():
    if (check_mouse_On_button0() or check_mouse_On_button1()):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True

def keys_up():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            return True

def down_control(keys,down,RFPS:float):
    global key_timing
    if keys[pygame.K_DOWN] and key_timing>RFPS/8:
        down += 1
        key_timing = 0
    elif keys[pygame.K_UP] and key_timing>RFPS/8:
        down -= 1
        key_timing = 0
    elif check_mouse_On_button0():
        down =2
    elif check_mouse_On_button1():
        down =1
    down %= 2
    return down

def button_select(menu_screen,DIMENSIONS,in_menu,RFPS:float):
    global down,quit_color,play_color,QUIT_TEXT,PLAY_TEXT,key_timing
    keys=pygame.key.get_pressed()
    key_timing+=1
    down = down_control(keys,down,RFPS)
    if down == 0:
        quit_color=(0,0,0)
        play_color=(0,210,0)

    if down == 1:
        quit_color=(0,210,0)
        play_color=(0,0,0)


    if (down==1 and (keys[pygame.K_RETURN])) or (check_mouse_On_button1() and mouse_click()):
        print('hasquit')
        quit()

    if (down==0 and (keys[pygame.K_RETURN])) or (mouse_click() and check_mouse_On_button0()):
        in_menu = False 
        start_game()    

    QUIT_TEXT = QUIT_FONT.render("QUIT GAME", True,(quit_color))
    PLAY_TEXT = PLAY_FONT.render("PLAY",False,(play_color))
    return in_menu


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

def menu_BG(menu_screen, DIMENSIONS):
    global screen_update
    menu_screen.blit(BG,(DIMENSIONS[0]/2-BG_image_center_X,-64))
    screen_update = False

def menu_init(DIMENSIONS):
    menu_image_init()
    text_init()
    timing_init()
    button_init(DIMENSIONS)


#start game 

def start_game():
    quit()
    pass
'''write code here'''



def menu(menu_screen,DIMENSIONS, in_menu,RFPS:float):
    menu_BG(menu_screen,DIMENSIONS)
    #menu_animation and button_animation/render
    mouse_position()
    button(DIMENSIONS,menu_screen) 
    button_select(menu_screen,DIMENSIONS,in_menu,RFPS)
    interactive_element_draw(DIMENSIONS,menu_screen)
    title_animation(menu_screen,DIMENSIONS)
    #menu_inputs
    
    return in_menu



    
