import pygame

pygame.init()
'''menu style:      TITLE
                Option1(game)
                Option2(quit)
                '''
MENU_COLOR = (180,100,0)
BUTTON_COLOR = (120,180,120)

TITLE_FONT = pygame.font.Font("Matrix-MZ4P.ttf",80)
QUIT_FONT = pygame.font.Font("Matrix-MZ4P.ttf",40)
TITLE_TEXT = TITLE_FONT.render("Furious Lardinus", True,(0,0,0))
QUIT_TEXT = QUIT_FONT.render("QUIT GAME", True,(0,0,0))

def button_init(DIMENSIONS):
    global BUTTON_QUIT
    BUTTON_QUIT = pygame.Rect(DIMENSIONS[0]/2.0 -250/2, DIMENSIONS[1] / 2.0 ,250.0,100.0)

def menu(menu_screen,DIMENSIONS):
    button_init(DIMENSIONS)
    menu_screen.fill(MENU_COLOR)
    menu_screen.blit(TITLE_TEXT, (DIMENSIONS[0]/4,DIMENSIONS[1]/8))
    pygame.draw.rect(menu_screen,BUTTON_COLOR,BUTTON_QUIT)
    menu_screen.blit(QUIT_TEXT,(DIMENSIONS[0]/2.0 -250/2, DIMENSIONS[1] / 2.0 +25.0 ))

    
