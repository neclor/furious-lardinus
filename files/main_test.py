import pygame
import inputs

DIMENSIONS = (1280, 1024)
FPS = 30

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
    pygame.event.pump()

    time = -1
    delta = 1

    clock = pygame.time.Clock()
    while playing:
        # inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
                quit()
        inputs.keyboard(player, delta)
        
        # displays
        print((player['position'], player['look_vec']))
        pygame.display.flip()

        # time shenanigans
        time = pygame.time.get_ticks()
        clock.tick(FPS)
        delta = (time - pygame.time.get_ticks())/1000

main()