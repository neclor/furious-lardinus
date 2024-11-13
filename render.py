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

# why??
# why not
# +-> x
# |
# v y



# player is a dictionary
# 'position'    pygame.Vector2
# 'look_vec'    pygame.Vector2      it is a unit vector
# 'velocity'    float               intensity of the velocity vector
# 
# derived from look_vec to avoid 1) :
# 'look_vec_len float   length of velocity
# 'direction'   float   angle of velocity, following the unit circle

# avoiding :
#           1) having to recalculate it each frame


# imports
import pygame
import math

# initialization


