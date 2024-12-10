import math
import pygame


# Math
HALF_PI: float = math.pi / 2
THREE_HALF_PI: float = 3 * HALF_PI


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
WINDOW_SIZE: tuple[int, int] = (1280, 720)
RESOLUTION: tuple[int, int] = (100, 100)#(640, 360)
FPS: int = 1000


# Rendering
CLEAR_COLOR: pygame.Color = pygame.Color("#181818")
DEBUG_COLOR: pygame.Color = pygame.Color("#0099b36b")


# 3D
CAMERA_SENSITIVITY: float = 1.0
FOV_H: float = HALF_PI
RAYS_NUMBER: int = 600


# Parameters
half_resolution: tuple[int, int] = (0, 0)
aspect_ratio: float = 0.0
ray_step_angle: float = 0.0
ray_step_angle_tan: float = 0.0
fov_v: float = 0.0
half_fov_h: float = 0.0
half_fov_v: float = 0.0
tan_half_fov_h: float = 0.0
tan_half_fov_v: float = 0.0
double_tan_half_fov_h: float = 0.0
double_tan_half_fov_v: float = 0.0
resolution_x_div_double_tan_half_fov_h: float = 0.0
resolution_y_div_double_tan_half_fov_v: float = 0.0


def calculate_parameters() -> None:
	global half_resolution, aspect_ratio, ray_step_angle, ray_step_angle_tan, fov_v, half_fov_h, half_fov_v, tan_half_fov_h, tan_half_fov_v, double_tan_half_fov_h, double_tan_half_fov_v, resolution_x_div_double_tan_half_fov_h, resolution_y_div_double_tan_half_fov_v
	half_resolution = (RESOLUTION[0] // 2, RESOLUTION[1] // 2)
	aspect_ratio = RESOLUTION[0] / RESOLUTION[1]
	ray_step_angle = FOV_H / RAYS_NUMBER
	ray_step_angle_tan = math.tan(ray_step_angle)
	fov_v = 2 * math.atan(math.tan(FOV_H / 2) / aspect_ratio)
	half_fov_h = FOV_H / 2
	half_fov_v = fov_v / 2
	tan_half_fov_h = math.tan(half_fov_h)
	tan_half_fov_v = math.tan(half_fov_v)
	double_tan_half_fov_h = tan_half_fov_h * 2
	double_tan_half_fov_v = tan_half_fov_v * 2
	resolution_x_div_double_tan_half_fov_h = RESOLUTION[0] / double_tan_half_fov_h
	resolution_y_div_double_tan_half_fov_v = RESOLUTION[1] / double_tan_half_fov_v


calculate_parameters()
