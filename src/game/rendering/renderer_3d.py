
import math
import pygame

import settings as Settings
import game.rendering.display as Display
import game.game as Game


tile_size: pygame.Vector2
tile_map_size: pygame.Vector2
tile_map: list[list[dict | None]]

position: pygame.Vector2
position_z: float
height: int
rotation: float


def init() -> None:
	pass


def update() -> None:
	update_data()
	draw_backgrond()
	draw_tile_map()


def update_data() -> None:
	global tile_size, tile_map_size, tile_map, position, position_z, height, rotation
	tile_size = Game.level["tile_size"]
	tile_map_size = Game.level["tile_map_size"]
	tile_map = Game.level["tile_map"]

	position = Game.player["position"]
	position_z = Game.player["position_z"]
	height = Game.player["height"]
	rotation = Game.player["rotation"]


def draw_backgrond() -> None:
	#Display.surface.fill()
	pass


def draw_tile_map() -> None:

	def check_intersections(horizontal: bool, sin_ray: float, cos_ray: float) -> tuple[float, dict, float]:
		X: int = int(not horizontal)
		Y: int = int(horizontal)
		sin_ray, cos_ray = (sin_ray, cos_ray) if horizontal else (cos_ray, sin_ray)

		distance: float = -1
		tile: dict | None = None
		texture_offset: float = 0.0

		if sin_ray != 0.0:
			ray_direction_sign: int = 1 if sin_ray > 0 else -1
			start_tile_index: int = int(pygame.math.clamp(position[Y] // tile_size[Y], -1, tile_map_size[Y])) + ray_direction_sign
			end_tile_index: int = int(tile_map_size[Y] - 1 if ray_direction_sign > 0 else 0)
			tile_offset: int = 1 if ray_direction_sign < 0 else 0

			for tile_index_y in range(start_tile_index, end_tile_index + ray_direction_sign, ray_direction_sign):
				ray_position_y: float = (tile_index_y + tile_offset) * tile_size[Y]
				ray_length: float = (ray_position_y - position[Y]) / sin_ray
				ray_position_x: float = position[X] + ray_length * cos_ray
				tile_index_x: int = int(ray_position_x // tile_size[X])

				if 0 <= tile_index_x < tile_map_size[X]:
					tile = tile_map[tile_index_y][tile_index_x] if horizontal else tile_map[tile_index_x][tile_index_y]
					if tile is not None:
						distance = ray_length
						tile = tile
						texture_offset = (ray_position_x % tile_size[X]) / tile_size[X]
						break

		return (distance, tile if tile is not None else {}, texture_offset)

	ray_rotation: float = rotation - Settings.FOV_H / 2
	for _ in range(Settings.RAYS_NUMBER):
		sin_ray: float = math.sin(ray_rotation)
		cos_ray: float = math.cos(ray_rotation)

		distance_to_vertical, vertical_tile, vertical_texture_offset = check_intersections(False, sin_ray, cos_ray)
		distance_to_horizontal, horizontal_tile, horizontal_texture_offset = check_intersections(True, sin_ray, cos_ray)

		ray_relative_angle: float = ray_rotation - rotation

		if (0 < distance_to_vertical) and (distance_to_vertical < distance_to_horizontal or distance_to_horizontal <= 0):
			draw_column(ray_relative_angle, distance_to_vertical, vertical_tile, int(tile_size.y), vertical_texture_offset)
		elif (0 < distance_to_horizontal):
			draw_column(ray_relative_angle, distance_to_horizontal, horizontal_tile, int(tile_size.x), horizontal_texture_offset)

		ray_rotation += Settings.ray_delta_angle


def draw_column(ray_relative_angle: float, distance: float, tile: dict, tile_side_size: int, texture_offset: float) -> None:
	tile_texture: pygame.Surface = tile["texture"]
	tile_height: int = tile["height"]

	column_texture: pygame.Surface = pygame.transform.scale(tile_texture, (tile_side_size, tile_height))
	column_texture = column_texture.subsurface(tile_side_size * texture_offset, 0, 1, tile_height)

	column_position_x_normalized: float = math.tan(ray_relative_angle) / (Settings.tan_half_fov_h * 2) + 0.5
	column_width_normalized: float = ((math.tan(ray_relative_angle + Settings.ray_delta_angle)) / (Settings.tan_half_fov_h * 2) + 0.5) - column_position_x_normalized

	distance *= math.cos(ray_relative_angle)

	column_position_y_normalized: float = 0
	column_height_normalized: float = 0
	if distance != 0:
		camera_position_z: float = position_z + height
		column_position_y_normalized = (camera_position_z - tile_height) / (distance * Settings.tan_half_fov_v * 2) + 0.5
		column_height_normalized = camera_position_z / (distance * Settings.tan_half_fov_v * 2) + 0.5 - column_position_y_normalized

	column_texture = pygame.transform.scale(column_texture, (math.ceil(column_width_normalized * Settings.RESOLUTION.x), math.ceil(column_height_normalized * Settings.RESOLUTION.y)))
	column_position: pygame.Vector2 = pygame.Vector2(math.floor(column_position_x_normalized * Settings.RESOLUTION.x), math.floor(column_position_y_normalized * Settings.RESOLUTION.y))

	Display.surface.blit(column_texture, column_position)
