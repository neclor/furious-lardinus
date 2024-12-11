
from pygame import mixer
import pygame


pygame.init()


clock=pygame.time.Clock()

menu_volume = 1.0

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
    MOUSE_MENU_CURSOR = pygame.image.load("menu_images/Cursor.png")
    MENU_BG_COLOR = (110,10,10)
    BUTTON_COLOR = (120,100,120)
    SELECT_BUTTON_COLOR= (120,180,120,0.1)
    GAME_ICON = pygame.image.load("menu_images/FL_logo.png")
    BG = pygame.image.load("menu_images\BG.png").convert()
    BG_image_center_X = (BG.get_size()[0])/2
    BG = pygame.transform.scale(BG,(DIMENSIONS[0],DIMENSIONS[1]))
    BG_image_center_X = (BG.get_size()[0])/2
    BG_image_center_Y = (BG.get_size()[1])/2
    #game-menu cursor
    pygame.mouse.set_cursor(pygame.cursors.Cursor((0,0),MOUSE_MENU_CURSOR))
    pygame.display.set_icon(GAME_ICON)
    #button color when selected
    quit_color=(0,0,0)
    play_color=(0,0,0)
    settings_color=(0,0,0)
    #menu sond
    out_loud(menu_music)



def text_init():
    global TITLE_TEXT,QUIT_TEXT,PLAY_TEXT, TITLE_FONT, QUIT_FONT, PLAY_FONT,SETTINGS_FONT,SETTINGS_TEXT,SETTINGS_BUTTON_FONT
    TITLE_FONT = pygame.font.Font("menu_fonts\Pixel Game.otf",120)
    QUIT_FONT = pygame.font.Font("menu_fonts\Pixel Game.otf",60)
    PLAY_FONT = pygame.font.Font("menu_fonts\Pixel Game.otf",60)
    SETTINGS_FONT =  pygame.font.Font("menu_fonts\Pixel Game.otf",60)
    SETTINGS_BUTTON_FONT= pygame.font.Font("menu_fonts\Pixel Game.otf",40)

    TITLE_TEXT = TITLE_FONT.render("Furious Lardinus", True,(0,0,0))
    QUIT_TEXT = QUIT_FONT.render("QUIT GAME", True,quit_color)
    PLAY_TEXT = PLAY_FONT.render("PLAY",False,play_color)
    SETTINGS_TEXT = SETTINGS_FONT.render("SETTINGS",True,settings_color)



#timing initialisation and initialisation of the cursor's position
def timing_init():
    global T_anim_timing,down, upload_times,in_menu, key_timing, menu_music,settings_key_timing
    T_anim_timing = 0
    upload_times= 0
    down = 0
    in_menu = True
    key_timing = 101
    settings_key_timing =1


  
def button(DIMENSIONS,menu_screen) -> None:
    global BUTTON_QUIT, BUTTON_PLAY,button0_pos,button1_pos,button2_pos
    pygame.draw.rect(menu_screen,BUTTON_COLOR,BUTTON_QUIT)
    menu_screen.blit(PLAY_TEXT,(DIMENSIONS[0]/2.0 -244/4, DIMENSIONS[1] / 2.0 +25.0 ))
    pygame.draw.rect(menu_screen,BUTTON_COLOR,BUTTON_PLAY)
    menu_screen.blit(QUIT_TEXT,(DIMENSIONS[0]/2.0 -210/2, DIMENSIONS[1] / 3.0 + DIMENSIONS[1]/3 +25))
    pygame.draw.rect(menu_screen,BUTTON_COLOR,BUTTON_SETTINGS)
    menu_screen.blit(SETTINGS_TEXT,(DIMENSIONS[0]/2.0 -244/2 + 15,DIMENSIONS[1]/2.0 + DIMENSIONS[1]/3 +25)) 
   

def cursor_draw(DIMENSIONS,menu_screen):
    menu_screen.blit(SELECT_BUTTON_CURSOR,(DIMENSIONS[0]/2.0 -384, DIMENSIONS[1] / (3.0-down)))

def interactive_element_draw(DIMENSIONS,menu_screen):
    button(DIMENSIONS,menu_screen)
    #cursor_draw(DIMENSIONS,menu_screen)

def check_mouse_On_button():
    global mouse_crs_position,button0_pos,down
    if (button0_pos[0]<=mouse_crs_position[0]<=button0_pos[0]+250) and (button0_pos[1]<=mouse_crs_position[1]<=button0_pos[1]+100):
        return 0;down =3
    if (button1_pos[0]<=mouse_crs_position[0]<=button1_pos[0]+250) and (button1_pos[1]<=mouse_crs_position[1]<=button1_pos[1]+100):
        return 1;down=1
    if (button2_pos[0]<=mouse_crs_position[0]<=button2_pos[0]+250) and (button2_pos[1]<=mouse_crs_position[1]<=button2_pos[1]+100):
        return 2;down=2
    else:
        return -1

def mouse_position():
    global mouse_crs_position
    mouse_crs_position = pygame.mouse.get_pos()

def mouse_click():
    if (check_mouse_On_button() <= 0):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
                return True

def keys_up():
    for event in pygame.event.get():
        if event.type == pygame.KEYUP and keys[pygame.K_RETURN]:
            return True
        else:
            return False

def down_control(keys,down,RFPS:float):
    global key_timing
    if keys[pygame.K_DOWN] and key_timing>RFPS/6:
        down += 1
        key_timing = 0
    elif keys[pygame.K_UP] and key_timing>RFPS/6:
        down -= 1
        key_timing = 0
    down %= 3
    return down

def down_control_for_settings(keys,down,RFPS:float):
    global settings_key_timing
    if keys[pygame.K_DOWN] and settings_key_timing>RFPS/6:
        down += 1
        settings_key_timing = 0
    elif keys[pygame.K_UP] and settings_key_timing>RFPS/6:
        down -= 1
        settings_key_timing = 0
    down %= 2
    return down

def button_select(menu_screen,DIMENSIONS,in_menu,RFPS:float,FPS):
    global down,quit_color,play_color,settings_color,QUIT_TEXT,PLAY_TEXT,key_timing,SETTINGS_TEXT,keys
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


    if (down==1 and (keys[pygame.K_RETURN])) or (check_mouse_On_button()==1 and mouse_click()):
        print('hasquit')
        quit()
        
    elif (down==2 and (keys[pygame.K_RETURN])) or (check_mouse_On_button()==2 and mouse_click()):
        settings_menu(menu_screen, DIMENSIONS,FPS)
    
    elif (down==0 and (keys[pygame.K_RETURN])) or (mouse_click() and check_mouse_On_button()==3):
        in_menu = False
        start_game()

    QUIT_TEXT = QUIT_FONT.render("QUIT GAME", True,(quit_color))
    PLAY_TEXT = PLAY_FONT.render("PLAY",False,(play_color))
    SETTINGS_TEXT = SETTINGS_FONT.render("SETTINGS", False,(settings_color))
    return in_menu

def menu_volume_button(menu_screen, DIMENSIONS):
    menu_volume_text = SETTINGS_BUTTON_FONT.render("menu volume:",False,(0,0,0))
    volume_text = SETTINGS_BUTTON_FONT.render("%5.3u" %(menu_volume*100)+"%",False,(play_color))
    pygame.draw.rect(menu_screen,BUTTON_COLOR,BUTTON_QUIT)
    menu_screen.blit(volume_text,(DIMENSIONS[0]/2.0 -50, DIMENSIONS[1] / 2.0 +25 ))
    menu_screen.blit(menu_volume_text,(DIMENSIONS[0]/2.0 -200/2, DIMENSIONS[1] / 2.0 -30 ))
def menu_settings_quit(menu_screen, DIMENSIONS):
    exit_settings = SETTINGS_BUTTON_FONT.render("apply settings", False, quit_color)
    pygame.draw.rect(menu_screen,BUTTON_COLOR, BUTTON_PLAY)
    menu_screen.blit(exit_settings,(DIMENSIONS[0]/2.0 -220/2, DIMENSIONS[1]/ 3.0 + DIMENSIONS[1]/3 +25))

def settings_button(menu_screen, DIMENSIONS,RFPS):
    global menu_volume,in_settings,BG_MUSIC,down,play_color,quit_color,settings_key_timing
    settings_key_timing+=1
    keys = pygame.key.get_pressed()
    menu_volume_button(menu_screen, DIMENSIONS)
    menu_settings_quit(menu_screen, DIMENSIONS)
    down=down_control_for_settings(keys,down,RFPS)
    if down==0:
        play_color = (0,210,0)
        quit_color = (0,0,0)
    if down ==1:
        quit_color = (0,210,0)
        play_color = (0,0,0)
    if (check_mouse_On_button()==3 and mouse_click()) or (down ==0 and (keys[pygame.K_RETURN] and keys_up() and settings_key_timing >15 )):
        menu_volume -= 0.25
        settings_key_timing = 0
    if menu_volume<0:
        menu_volume += 1.25
    menu_volume_button(menu_screen, DIMENSIONS)
    if (check_mouse_On_button()==1 and mouse_click() ) or (down ==1 and (keys[pygame.K_RETURN] and keys_up())):
        settings_key_timing = 0
        in_settings = False
    pygame.mixer.music.set_volume(menu_volume)

def settings_menu(menu_screen,DIMENSIONS,FPS):
    global menu_volume, in_settings
    in_settings = True
    settings_screen = pygame.display.set_mode(DIMENSIONS)
    
    while in_settings:
        #must remove####
        RFPS=clock.get_fps()
        print(RFPS)
        ################
        clock.tick(FPS)
        menu_BG(menu_screen, DIMENSIONS)
        mouse_position()
        button_init(DIMENSIONS)
        settings_button(menu_screen, DIMENSIONS,RFPS)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        


def title_animation(menu_screen,DIMENSIONS):
    global T_anim_timing,TITLE_TEXT,upload_times,TITLE_FONT
    T_anim_timing +=1
    if T_anim_timing>1200:
        T_anim_timing=0
    if 480>T_anim_timing >= 450 or 542>T_anim_timing>=520 :
        TITLE_FONT = pygame.font.Font("menu_fonts\Matrix-MZ4P.ttf",100)
        TITLE_TEXT = TITLE_FONT.render("Furious Lardinus", True,(255,0,0))
        menu_screen.blit(TITLE_TEXT, (DIMENSIONS[0]/5,DIMENSIONS[1]/4.2))
        return True
    else:
        TITLE_FONT = pygame.font.Font("menu_fonts\Pixel Game.otf",120)
        TITLE_TEXT = TITLE_FONT.render("Furious Lardinus", True,(0,0,0))
        menu_screen.blit(TITLE_TEXT, (DIMENSIONS[0]/4-40,DIMENSIONS[1]/4))
        return False

def menu_BG(menu_screen, DIMENSIONS):

    menu_screen.blit(BG,(0,0))


def menu_init(DIMENSIONS,menu_music):
    menu_image_init(DIMENSIONS,menu_music)
    text_init()
    timing_init()
    button_init(DIMENSIONS)
    

def out_loud(menu_music):
    global BG_MUSIC
    if menu_music:
        menu_music = False
        BG_MUSIC=pygame.mixer_music.load('menu_sond/furious_lardinous_menu_theme.ogg')
        pygame.mixer_music.play(10)




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


    
def menu(menu_screen,DIMENSIONS, in_menu,RFPS:float,FPS):
    menu_BG(menu_screen,DIMENSIONS)
    #menu_animation and button_animation/render
    mouse_position()
    button(DIMENSIONS,menu_screen) 
    button_select(menu_screen,DIMENSIONS,in_menu,RFPS,FPS)
    interactive_element_draw(DIMENSIONS,menu_screen)
    title_animation(menu_screen,DIMENSIONS)


    #menu_inputs
    
    return in_menu



