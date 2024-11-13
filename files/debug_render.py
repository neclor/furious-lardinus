import pygame
import math
import inputs
import render

DIMENSIONS = (1280, 1024)
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0,   0,   0  )
RED   = (255, 0,   0  )
GREEN = (0,   255, 0  )
BLUE  = (0,   0,   255)

WALL_HEIGHT = 900

SIZE = 20
FOV = 3.1416 / 2.0
RESOLUTION = 50

playing = True

colors = [
    BLACK,
    WHITE,
    RED,
    GREEN,
    BLUE
]

window = pygame.display.set_mode(DIMENSIONS)

player = {
    'position': pygame.Vector2(1.5, 1.5),
    'look_vec': pygame.Vector2(1.0, 0.0),
    'velocity': 5.0
}


def main() -> None:
    global playing
    pygame.init()
    pygame.event.pump()

    time = -1
    delta = 1

    render.change_map(create_map())

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
        window.fill(BLACK)
        render.raycast(FOV, RESOLUTION, WALL_HEIGHT, player, DIMENSIONS, colors, window)
        pygame.display.flip()

        # time shenanigans
        delta = (pygame.time.get_ticks() - time)/1000
        time = pygame.time.get_ticks()
        clock.tick(FPS)
        if delta > 0:
            print(round(1 / delta))
        print(delta)

# debug


# each number represents the index of colors the renderer will use
# so a wall number 3 will use the color colors[3], so a GREEN WALL
# and index 0 is not a BLACK wall, it is empty space
def create_map():
    return [
        [1,1,1,1,4,1,1,1],
        [1,0,0,0,0,0,0,1],
        [1,0,1,0,0,0,0,1],
        [1,0,0,0,0,0,0,1],
        [4,0,0,0,0,1,2,1],
        [3,0,0,0,0,0,0,1],
        [2,0,0,0,0,0,0,1],
        [1,2,3,4,1,1,1,1]
    ]

main()