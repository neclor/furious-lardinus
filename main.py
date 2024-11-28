import pygame
import menu

DIMENSIONS = (1280, 1024)

in_menu = playing = True

clock=pygame.time.Clock()


def stat_FPS():
    global RFPS
    RFPS=clock.get_fps()
    print(RFPS)


window = pygame.display.set_mode(DIMENSIONS)
FPS = 300
def main() -> None:
    global playing,in_menu
    pygame.init()
    menu.menu_init(DIMENSIONS)
    while playing:
        clock.tick(FPS)
        stat_FPS()
        playing=menu.menu(window,DIMENSIONS,in_menu,RFPS)
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
                quit()


main()
