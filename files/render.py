# map is an array of ints,
# map_example = [[a, b], [c, d]]
# int_at_xy   = map_example[x][y]
# 
# ^ y
# |
# |b|d|
# |a|c|
# +------> x

def vec_to_map(vec):
    return pygame.Vector2(vec.x, 1024 - vec.y)

# imports
import pygame
import math

# initialization

map = [[0], [0]]

def ray(ppos: pygame.Vector2, rdir: pygame.Vector2) -> tuple[int, pygame.Vector2]:
    iteration_max = 30
    result_v = 0
    result_h = 0
    result_vec_v = pygame.Vector2(0.0, 0.0)
    result_vec_h = pygame.Vector2(0.0, 0.0)

    # intersections with the vertical integer lines
    rpos = pygame.Vector2(ppos.x, ppos.y)
    if rdir.x != 0.0:
        rdir_vert = pygame.Vector2(rdir.x / abs(rdir.x), rdir.y / abs(rdir.x))
        if rdir.x > 0.0:
            rpos.x = math.ceil(ppos.x)
            rpos.y += rdir_vert.y * (rpos.x - ppos.x)

            iteration = 0
            while map_position(math.floor(rpos.x), math.floor(rpos.y)) == 0 and iteration < iteration_max:
                rpos += rdir_vert
                iteration += 1
            result_v = map_position(math.floor(rpos.x), math.floor(rpos.y))

        # rdir.x not 0 nor bigger, so it is smaller
        else:
            rpos.x = math.floor(ppos.x)
            rpos.y += rdir_vert.y * (ppos.x - rpos.x)

            iteration = 0
            while map_position(math.floor(rpos.x -1), math.floor(rpos.y)) == 0 and iteration < iteration_max:
                rpos += rdir_vert
                iteration += 1
            result_v = map_position(math.floor(rpos.x -1), math.floor(rpos.y))
        result_vec_v = rpos



    # intersections with the horizontal integer lines
    rpos = pygame.Vector2(ppos.x, ppos.y)
    if rdir.y != 0.0:
        rdir_vert = pygame.Vector2(rdir.x / abs(rdir.y), rdir.y / abs(rdir.y))
        if rdir.y > 0.0:
            rpos.y = math.ceil(ppos.y)
            rpos.x += rdir_vert.x * (rpos.y - ppos.y)

            iteration = 0
            while map_position(math.floor(rpos.x), math.floor(rpos.y)) == 0 and iteration < iteration_max:
                rpos += rdir_vert
                iteration += 1
            result_h = map_position(math.floor(rpos.x), math.floor(rpos.y))

        # rdir.y is not 0 nor bigger, so it is smaller
        else:
            rpos.y = math.floor(ppos.y)
            rpos.x += rdir_vert.x * (ppos.y - rpos.y)

            iteration = 0
            while map_position(math.floor(rpos.x), math.floor(rpos.y - 1)) == 0 and iteration < iteration_max:
                rpos += rdir_vert
                iteration += 1
            result_h = map_position(math.floor(rpos.x), math.floor(rpos.y - 1))
        result_vec_h = rpos
    
    if result_h <= 0:
        if result_v <= 0:
            return (0, pygame.Vector2(0.0, 0.0), 0)
        else:
            return (result_v, result_vec_v, 1)
    else:
        if result_v <= 0:
            return (result_h, result_vec_h, -1)
        else:
            if result_vec_v.distance_squared_to(ppos) < result_vec_h.distance_squared_to(ppos):
                return (result_v, result_vec_v, 1)
            else:
                return (result_h, result_vec_h, -1)


# returns the element at coordinates (x, y) in map, and if outside of map, returns -1
def map_position(x: int, y: int) -> int:
    global map
    if x >= 0 and x < len(map):
        if y >= 0 and y < len(map[x]):
            return map [x][y]
    return -1

def change_map(new_map):
    global map
    map = new_map

def raycast(
    fov: float,
    resolution: int,
    wall_height: int,
    player,
    dimensions: tuple[int, int],
    colors,
    window
):
    ray_direction = pygame.Vector2(player['look_vec'].rotate_rad(fov/2.0).x, player['look_vec'].rotate_rad(fov/2.0).y)
    iteration = 0
    offset = fov / resolution
    while iteration < resolution:
        (wall, wall_position, side) = ray(player['position'], ray_direction)
        if wall > 0:
            dist = wall_position.distance_to(player['position']) * math.cos(fov/2.0 - offset * iteration)
            display_wall(dimensions, resolution, iteration, wall_height * math.atan2(1.0, dist), side, colors[wall], window)
        ray_direction = ray_direction.rotate_rad(- offset)
        iteration += 1

def display_wall(
    dimensions: tuple[int, int],
    resolution: int,
    iteration: int,
    height: float,
    side: int,
    color: tuple[int, int, int],
    window
):
    rect = pygame.Rect(iteration * dimensions[0] / resolution, (dimensions[1] - height)/2.0, 2 + dimensions[0] / resolution, height)
    if side == 1:
        pygame.draw.rect(window, color, rect)
    else:
        pygame.draw.rect(window, (color[0]*0.9, color[1]*0.9, color[2]*0.9), rect)
