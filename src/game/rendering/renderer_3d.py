
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



		ray_cos: float = math.cos(ray_rotation)
		if ray_cos != 0.0:
			ray_sign_x: int = 1 if ray_cos > 0 else -1
			ray_x: float = position.x



			for i in range(int(max(0, position.x // tile_size.x)), int(min(position.x // tile_size.x, level_size.x - 1)))
			min_tile_index_x: int = int(max(0, position.x // tile_size.x))
			max_tile_index_x: int = int(min((position.x + radius) // tile_size.x, level_size.x - 1))






		ray_sin: float = math.sin(ray_rotation)


		ray_rotation += Settings.ray_delta_angle
