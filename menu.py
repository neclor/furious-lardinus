from pygame import mixer
import pygame


pygame.init()
'''menu style:      TITLE
                Option1(game)
                Option2(quit)
                '''
screen_update =False
clock=pygame.time.Clock()



RFPS : float
def button_init(DIMENSIONS):
    global BUTTON_PLAY,BUTTON_QUIT,BUTTON_SETTINGS,button0_pos,button1_pos,button2_pos
    BUTTON_QUIT = pygame.Rect(DIMENSIONS[0]/2.0 -250/2, DIMENSIONS[1] / 2.0 ,250.0,100.0)
    BUTTON_PLAY = pygame.Rect(DIMENSIONS[0]/2.0 -250/2, DIMENSIONS[1]/ 3.0 + DIMENSIONS[1]/3 , 250.0,100.0 )
    BUTTON_SETTINGS = pygame.Rect(DIMENSIONS[0]/2.0 -250/2,DIMENSIONS[1]/2.0 + DIMENSIONS[1]/3, 250.0, 100.0 )
    button0_pos = (DIMENSIONS[0]/2.0 -250/2, DIMENSIONS[1] / 2.0  )
    button1_pos = (DIMENSIONS[0]/2.0 -250/2, DIMENSIONS[1]/ 3.0 + DIMENSIONS[1]/3) 
    button2_pos = (DIMENSIONS[0]/2.0 -250/2,DIMENSIONS[1]/2.0 + DIMENSIONS[1]/3 )



#+ sound yay!
def menu_image_init(DIMENSIONS,menu_music):
    global SELECT_BUTTON_COLOR,MENU_BG_COLOR, SELECT_BUTTON_CURSOR,BUTTON_COLOR, BG_image_center_X,quit_color,play_color,BG,THEME_SONG,settings_color
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
    settings_color=(0,0,0)
    #menu sond
    out_loud(menu_music)



def text_init():
    global TITLE_TEXT,QUIT_TEXT,PLAY_TEXT, TITLE_FONT, QUIT_FONT, PLAY_FONT,SETTINGS_FONT,SETTINGS_TEXT
    TITLE_FONT = pygame.font.Font("menu_fonts/Matrix-MZ4P.ttf",100)
    QUIT_FONT = pygame.font.Font("menu_fonts/Matrix-MZ4P.ttf",40)
    PLAY_FONT = pygame.font.Font("menu_fonts/Matrix-MZ4P.ttf",40)
    SETTINGS_FONT =  pygame.font.Font("menu_fonts\Matrix-MZ4P.ttf",40)

    TITLE_TEXT = TITLE_FONT.render("Furious Lardinus", True,(0,0,0))
    QUIT_TEXT = QUIT_FONT.render("QUIT GAME", True,quit_color)
    PLAY_TEXT = PLAY_FONT.render("PLAY",False,play_color)
    SETTINGS_TEXT = SETTINGS_FONT.render("SETTINGS",True,settings_color)



#timing initialisation and initialisation of the cursor's position
def timing_init():
    global T_anim_timing,down, upload_times,in_menu, key_timing, menu_music
    T_anim_timing = 0
    upload_times= 0
    down = 0
    in_menu = True
    key_timing = 101



  
def button(DIMENSIONS,menu_screen) -> None:
    global BUTTON_QUIT, BUTTON_PLAY,button0_pos,button1_pos,button2_pos
    pygame.draw.rect(menu_screen,BUTTON_COLOR,BUTTON_QUIT)
    menu_screen.blit(PLAY_TEXT,(DIMENSIONS[0]/2.0 -244/4, DIMENSIONS[1] / 2.0 +25.0 ))
    pygame.draw.rect(menu_screen,BUTTON_COLOR,BUTTON_PLAY)
    menu_screen.blit(QUIT_TEXT,(DIMENSIONS[0]/2.0 -244/2, DIMENSIONS[1] / 3.0 + DIMENSIONS[1]/3 +25))
    pygame.draw.rect(menu_screen,BUTTON_COLOR,BUTTON_SETTINGS)
    menu_screen.blit(SETTINGS_TEXT,(DIMENSIONS[0]/2.0 -244/2 + 15,DIMENSIONS[1]/2.0 + DIMENSIONS[1]/3 +25)) 
   

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
def check_mouse_On_button2():
        if (button2_pos[0]<=mouse_crs_position[0]<=button2_pos[0]+250) and (button2_pos[1]<=mouse_crs_position[1]<=button2_pos[1]+100):
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
    if keys[pygame.K_DOWN] and key_timing>RFPS/6:
        down += 1
        key_timing = 0
    elif keys[pygame.K_UP] and key_timing>RFPS/6:
        down -= 1
        key_timing = 0
    elif check_mouse_On_button0():
        down =3
    elif check_mouse_On_button1():
        down =1
    elif check_mouse_On_button2():
        down = 2
    down %= 3
    return down

def button_select(menu_screen,DIMENSIONS,in_menu,RFPS:float):
    global down,quit_color,play_color,settings_color,QUIT_TEXT,PLAY_TEXT,key_timing,SETTINGS_TEXT
    keys=pygame.key.get_pressed()
    key_timing+=1
    down = down_control(keys,down,RFPS)
    if down == 0:
        quit_color=(0,0,0)
        play_color=(0,210,0)
        settings_color=(0,0,0)
    if down == 1:
        quit_color=(0,210,0)
        play_color=(0,0,0)
        settings_color=(0,0,0)
    if down == 2:
        quit_color=(0,0,0)
        play_color=(0,0,0)
        settings_color=(0,210,0)


    if (down==1 and (keys[pygame.K_RETURN])) or (check_mouse_On_button1() and mouse_click()):
        print('hasquit')
        quit()
        
    elif (down==2 and (keys[pygame.K_RETURN])) or (check_mouse_On_button2() and mouse_click()):
        settings_menu(menu_screen, DIMENSIONS)
    
    elif (down==0 and (keys[pygame.K_RETURN])) or (mouse_click() and check_mouse_On_button0()):
        in_menu = False
        start_game()

    QUIT_TEXT = QUIT_FONT.render("QUIT GAME", True,(quit_color))
    PLAY_TEXT = PLAY_FONT.render("PLAY",False,(play_color))
    SETTINGS_TEXT = SETTINGS_FONT.render("SETTINGS", False,(settings_color))
    return in_menu

def menu_volume_button(menu_screen, DIMENSIONS):
    volume_text = PLAY_FONT.render("menu_volume",False,play_color)
    pygame.draw.rect(menu_screen,BUTTON_COLOR,BUTTON_QUIT)
    menu_screen.blit(volume_text,(DIMENSIONS[0]/2.0 -244/2, DIMENSIONS[1] / 2.0 +25.0 ))
def menu_settings_quit(menu_screen, DIMENSIONS):
    exit_settings = PLAY_FONT.render("apply settings", False, quit_color)
    pygame.draw.rect(menu_screen,BUTTON_COLOR, BUTTON_PLAY)
    menu_screen.blit(exit_settings,(DIMENSIONS[0]/2.0 -244/2, DIMENSIONS[1]/ 3.0 + DIMENSIONS[1]/3 +25))

def settings_button(menu_screen, DIMENSIONS):
    global menu_volume,in_settings,BG_MUSIC
    menu_volume_button(menu_screen, DIMENSIONS)
    menu_settings_quit(menu_screen, DIMENSIONS)
    if check_mouse_On_button0() and mouse_click():
        menu_volume -= 0.25
    if menu_volume<0:
        menu_volume += 1.25
    
    if check_mouse_On_button1() and mouse_click():
        in_settings = False
    
    pygame.mixer.music.set_volume(menu_volume)
    

def settings_menu(menu_screen,DIMENSIONS):
    global menu_volume, in_settings
    in_settings = True
    settings_screen = pygame.display.set_mode(DIMENSIONS)
    menu_volume = 1.0
    while in_settings:
        #must remove####
        RFPS=clock.get_fps()
        print(RFPS)
        clock.tick(60)
        ################
        menu_BG(menu_screen, DIMENSIONS)
        mouse_position()
        button_init(DIMENSIONS)
        settings_button(menu_screen, DIMENSIONS)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        


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

def menu_init(DIMENSIONS,menu_music):
    menu_image_init(DIMENSIONS,menu_music)
    text_init()
    timing_init()
    button_init(DIMENSIONS)
    

def out_loud(menu_music):
    global BG_MUSIC
    if menu_music:
        menu_music = False
        BG_MUSIC=pygame.mixer_music.load('menu_sond/Furious_lardinous_menu(test)theme(mp3).mp3')
        pygame.mixer_music.play()




#start game 

def start_game():
    i=0
    if i<1:
        i+=1
        mixer.init()
        mixer.music.load("menu_sond/realistic-shotgun-cocking-sound-38640.mp3")
        mixer.music.play(1)
        pygame.time.wait(800)
    quit()
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



