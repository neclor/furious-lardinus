import pygame
import inputs

DIMENSIONS = (1280, 1024)

playing = True

window = pygame.display.set_mode(DIMENSIONS)

player = {
    'position': pygame.Vector2(0.0, 0.0),
    'look_vec': pygame.Vector2(1.0, 0.0),
    'velocity': 1.0
}


def main() -> None:
    global playing
    pygame.init()
    while playing:
        inputs.keyboard(player)
        #print((player['position'].x, player['position'].y))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
                quit()

main()