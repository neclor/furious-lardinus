import pygame

DIMENSIONS = (1280, 1024)

playing = True

window = pygame.display.set_mode(DIMENSIONS)

player = {
    'position': pygame.Vector2,
    'look_vec': pygame.Vector2,
    'velocity': float
}


def main() -> None:
    global playing
    pygame.init()
    while playing:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
                quit()

main()