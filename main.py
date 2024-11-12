import pygame
import menu_test

DIMENSIONS = (1280, 1024)

playing = True

window = pygame.display.set_mode(DIMENSIONS)

def main() -> None:
    global playing
    pygame.init()
    while playing:
        menu_test.menu(window,DIMENSIONS)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
                quit()

main()