import pygame
import math
import inputs
import render

DIMENSIONS = (1280, 1024)
FPS = 300
WHITE = (255, 255, 255)
WHITE_GREY = (200, 200, 200)
BLACK = (0, 0, 0)

WALL_HEIGHT = 900
WALL_SCALE = 1.0

SIZE = 20
FOV = 3.1416 / 2.0
RESOLUTION = 50

playing = True

window = pygame.display.set_mode(DIMENSIONS)

player = {
    'position': pygame.Vector2(2.0, 2.0),
    'look_vec': pygame.Vector2(-1.0, 0.0),
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
        raycast(FOV, RESOLUTION, player)
        display_map(render.map)
        pygame.draw.circle(window, WHITE, (player['position'].x * SIZE, y_to_map(SIZE * player['position'].y)), SIZE / 3.0)
        pygame.display.flip()

        # time shenanigans
        delta = (pygame.time.get_ticks() - time)/1000
        time = pygame.time.get_ticks()
        clock.tick(FPS)
        if delta > 0:
            print(round(1 / delta))
        print(delta)

# debug

def create_map():
    return [
        [1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,1],
        [1,0,1,0,0,0,0,1],
        [1,0,0,0,0,0,0,1],
        [1,0,0,0,0,1,1,1],
        [1,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1]
    ]

def raycast(fov: float, resolution: int, player):
    ray_direction = pygame.Vector2(player['look_vec'].rotate_rad(fov/2.0).x, player['look_vec'].rotate_rad(fov/2.0).y)
    iteration = 0
    offset = fov / resolution
    while iteration < resolution:
        (wall, wall_position, side) = render.ray(player['position'], ray_direction)
        if wall > 0:
            dist = wall_position.distance_to(player['position']) * math.cos(fov/2.0 - offset * iteration)
            display_wall(resolution, iteration, WALL_HEIGHT * math.atan2(WALL_SCALE, 2 * dist), side)
        ray_direction = ray_direction.rotate_rad(- offset)
        iteration += 1

def display_wall(resolution: int, iteration: int, height: float, side: int):
    global window
    rect = pygame.Rect(iteration * DIMENSIONS[0] / resolution, (DIMENSIONS[1] - height)/2.0, 2 + DIMENSIONS[0] / resolution, height)
    if side == 1:
        pygame.draw.rect(window, WHITE, rect)
    else:
        pygame.draw.rect(window, WHITE_GREY, rect)

def y_to_map(y: float) -> float:
    return 1024 - y

def display_map(map):
    y = 0
    for column in map:
        x = 0
        for object in column:
            result = render.map_position(x, y)
            if result == 1:
                rect = pygame.Rect(x*SIZE, y_to_map(y*SIZE) - SIZE, SIZE, SIZE)
                pygame.draw.rect(window, WHITE, rect)
            elif result == -1:
                print("error")
            x += 1
        y += 1

main()