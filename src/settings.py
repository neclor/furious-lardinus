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


# Display
RESOLUTION: pygame.Vector2 = pygame.Vector2(1280, 720) # 16:9
FPS: int = 1000


# Rendering
CLEAR_COLOR: pygame.Color = pygame.Color("#181818")
DEBUG_COLOR: pygame.Color = pygame.Color("#0099b36b")


# 2D
SCALE: float = 1.0
VISIBLE_COLLISION: bool = True


# 3D
CAMERA_SENSITIVITY: float = 1.0
FOV_H: float = math.pi - 0.1
RAYS_NUMBER: int = 500


# Advanced
aspect_ratio: float = RESOLUTION.x / RESOLUTION.y

fov_v: float = 2 * math.atan(math.tan(FOV_H / 2) / aspect_ratio)
tan_half_fov_h: float = math.tan(FOV_H / 2)
tan_half_fov_v: float = math.tan(fov_v / 2)

ray_delta_angle: float = FOV_H / RAYS_NUMBER
