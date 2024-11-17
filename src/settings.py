from typing import Tuple
import math
import pygame


# Config
NAME: str = "Furious Lardinus"


# Input
FULL_SCREEN: int = pygame.K_F11
PAUSE: int = pygame.K_ESCAPE
FORWARD: int = pygame.K_w
BACKWARD: int = pygame.K_s
LEFT: int = pygame.K_a
RIGHT: int = pygame.K_d
SPRINT: int = pygame.K_LSHIFT


# Display
RESOLUTION: Tuple[int, int] = (1280, 720) # 16:9
FPS: int = 60


# Rendering
CLEAR_COLOR: pygame.Color = pygame.Color("#000000")
DEBUG_COLOR: pygame.Color = pygame.Color("#0099b36b")


# 2D
SCALE: float = 2.0
VISIBLE_COLLISION: bool = True


# 3D
FOV_H: float = math.pi / 2
RAYS_NUMBER: int = 300


# Advanced
aspect_ratio: float = RESOLUTION[0] / RESOLUTION[1]
fov_v: float = math.atan(math.tan(FOV_H / 2) / (aspect_ratio)) * 2
ray_delta_angle: float = FOV_H / RAYS_NUMBER
ray_width: int = RESOLUTION[0] // RAYS_NUMBER
