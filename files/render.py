# map is an array of ints,
# coordinates are bottom left of map,
# axes are x horizontal to the east,
#          y vertical   to the north
# map_example = [[a, b], [c, d]]
# map_example[x][y]
# 
# ^ y
# |
# |c|d|
# |a|b|
# +-----> x

# player is a dictionary
# 'position'    pygame.Vector2
# 'look_vec'    pygame.Vector2      it is a unit vector
# 'velocity'    float               intensity of the velocity vector


# imports
import pygame
import math

# initialization


