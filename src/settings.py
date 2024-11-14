from typing import Tuple
import math
import pygame


# Config
NAME: str = "Furious Lardinus"


# Display
RESOLUTION: Tuple[int, int] = (800, 600)
FPS: int = 60
FOV_H: float = math.pi / 2
RAYS_NUMBER: int = 300


# Input
FORWARD: int = pygame.K_w
BACKWARD: int = pygame.K_s
LEFT: int = pygame.K_a
RIGHT: int = pygame.K_d
SPRINT: int = pygame.K_LSHIFT
PAUSE: int = pygame.K_ESCAPE


# Other
aspect_ratio: float = RESOLUTION[0] / RESOLUTION[1]
fov_v: float = math.atan(math.tan(FOV_H / 2) / (aspect_ratio)) * 2
ray_delta_angle: float = FOV_H / RAYS_NUMBER
ray_width: int = RESOLUTION[0] // RAYS_NUMBER
