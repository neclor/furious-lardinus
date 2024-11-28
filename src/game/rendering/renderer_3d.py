
import math
import pygame

import settings as Settings
import game.rendering.display as Display
import game.game as Game


def init() -> None:
	pass


def update() -> None:
	draw_backgrond()
	pass


def draw_backgrond() -> None:
	#Display.surface.fill()
	pass


def draw_level() -> None:
	level_size: pygame.Vector2 = Game.level["size"]
	tile_size: pygame.Vector2 = Game.level["tile_size"]
	tile_map: list[list[dict | None]] = Game.level["tile_map"]

	position: pygame.Vector2 = Game.player["position"]
	position_z: float = Game.player["position_z"]
	height_z: int = Game.player["height"]
	rotation: float = Game.player["rotation"]

	ray_rotation: float = rotation - Settings.FOV_H / 2
	for ray in range(Settings.RAYS_NUMBER):
		sin_ray: float = math.sin(ray_rotation)

		distance_to_vertical: float = -1
		cos_ray: float = math.cos(ray_rotation)
		if cos_ray != 0.0:
			ray_direction_sign_x: int = 1 if cos_ray > 0 else -1

			start_tile_index: int = int(pygame.math.clamp(position.x // tile_size.x, 0, level_size.x - 1))
			end_tile_index: int = int(level_size.x - 1 if ray_direction_sign_x > 0 else 0)

			for tile_index_x in range(start_tile_index + ray_direction_sign_x, end_tile_index + ray_direction_sign_x, ray_direction_sign_x):


				ray_position_x: float = tile_index_x * tile_size.x

				ray_length: float = (ray_position_x - position) / cos_ray

				ray_position_y: float = position + ray_length * sin_ray


				tile_index_y =
				pass









		ray_rotation += Settings.ray_delta_angle
