import pygame
import math

import settings as Settings
import game.rendering.display as Display
import game.game as Game

angle_init = 0

def init() -> None:
	pass


def update() -> None:
	pass




def ray_cast() -> None:
	ray_rotation: float = Game.player["rotation"] - Settings.FOV_H / 2
	for ray in range(Settings.RAYS_NUMBER):
		ray_rotation += Settings.FOV_H / Settings.RAYS_NUMBER
		draw_walls(ray_rotation, Game.player["position"])


def draw_walls(angle: float, player_position: pygame.Vector2) -> None:

	vertical_ray_arguments, horizontal_ray_arguments = ray_initial_values(player_position, angle)
	ray_intersection(vertical_ray_arguments)
	ray_intersection(horizontal_ray_arguments)


def ray_initial_values(position: pygame.Vector2, angle: float) -> tuple[tuple[pygame.Vector2, pygame.Vector2, int], tuple[pygame.Vector2, pygame.Vector2, int]]:
	direction_normalized = pygame.Vector2(math.cos(angle), math.sin(angle))

	if direction_normalized.x != 0:
		v_delta: pygame.Vector2 = pygame.Vector2(1, direction_normalized.y / direction_normalized.x)
		v_position: pygame.Vector2 = position.__copy__()
		v_position.y += v_delta.y * (math.ceil(v_position.x) - v_position.x)
		v_position.x = math.ceil(v_position.x)
		if 1.5*math.pi > angle > 0.5*math.pi:
			v_delta = pygame.Vector2(-v_delta.x, -v_delta.y)
			v_position += v_delta
		v_map_offset: int = -(direction_normalized.x < 0)
	else:
		v_position: pygame.Vector2 = pygame.Vector2(0, 0)
		v_delta: pygame.Vector2 = pygame.Vector2(0, 0)
		v_map_offset: int = 10

	if direction_normalized.y != 0:
		h_delta: pygame.Vector2 = pygame.Vector2(direction_normalized.x / direction_normalized.y, 1)
		h_position: pygame.Vector2 = position.__copy__()
		h_position.x += h_delta.x * (math.ceil(h_position.y) - h_position.y)
		h_position.y = math.ceil(h_position.y)
		if angle > math.pi:
			h_delta = pygame.Vector2(-h_delta.x, -h_delta.y)
			h_position += h_delta
		h_map_offset: int = -(direction_normalized.y < 0)
	else:
		h_position = pygame.Vector2(0, 0)
		h_delta = pygame.Vector2(0, 0)
		h_map_offset = 10

	# a map_offset of 10 means there was a fail (ex: slope of vertical line)

	return ((v_position, v_delta, v_map_offset), (h_position, h_delta, h_map_offset))


def ray_intersection(arguments):
	ray_position_init, ray_delta, map_offset = arguments
	pass
