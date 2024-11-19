import pygame
import menu

DIMENSIONS = (1280, 1024)

playing = True
in_menu = True

window = pygame.display.set_mode(DIMENSIONS)

def main() -> None:
    global playing,in_menu
    pygame.init()

    menu.menu(window,DIMENSIONS,in_menu)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            pygame.quit()
            quit()

main()