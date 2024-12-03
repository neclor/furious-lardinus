import math
import random
import pygame

import settings as Settings
import game.rendering.display as Display
import game.game as Game
import game.level as Level


SKYBOX_COLOR: pygame.Color = pygame.Color("#03193f")
STAR_COLOR: pygame.Color = pygame.Color("f9e6cf")


position: pygame.Vector2 = pygame.Vector2()
rotation: float = 0.0
position_z: float = 0.0
height: int = 0

camera_position_z: float = 0.0

skybox: pygame.Surface


def init() -> None:
	generate_skybox()


def generate_skybox() -> None:
	global skybox
	skybox_size: pygame.Vector2 = pygame.Vector2(Settings.RESOLUTION.x, Settings.half_resolution.y)
	star_size: int = int(skybox_size.x // 64)
	skybox = pygame.Surface(skybox_size)
	skybox.fill(SKYBOX_COLOR)
	for _ in range(100):
		star_position_x: int = random.randrange(star_size, int(skybox_size.x - 2 * star_size), star_size)
		star_position_y: int = random.randrange(star_size, int(skybox_size.y - 2 * star_size), star_size)
		pygame.draw.rect(skybox, STAR_COLOR, (star_position_x, star_position_y, star_size, star_size))


def update() -> None:
	update_camera()
	draw_backgrond()
	draw_game()


def update_camera() -> None:
	global position, rotation, camera_position_z
	position = Game.player["position"]
	rotation = Game.player["rotation"]
	camera_position_z = Game.player["position_z"] + Game.player["height"]


def draw_backgrond() -> None:
	Display.surface.fill(Level.floor_color)
	skybox_offset: int = int((rotation % math.tau) / math.tau * Settings.RESOLUTION.x)
	Display.surface.blit(skybox, (Settings.RESOLUTION.x - skybox_offset, 0))
	Display.surface.blit(skybox, (skybox_offset, 0))


def draw_game() -> None:
	projections: list[tuple[pygame.Vector2, pygame.Surface, float]] = []
	projections += get_tile_map_projections() + get_object_projections()
	projections.sort(key = lambda a: a[2], reverse = True)
	for projection in projections:
		Display.surface.blit(projection[0], projection[1])


def get_tile_map_projections() -> list[tuple[pygame.Vector2, pygame.Surface, float]]:
	tile_projections: list[tuple[pygame.Vector2, pygame.Surface, float]] = []

	ray_rotation: float = rotation - Settings.half_fov_h
	for _ in range(Settings.RAYS_NUMBER):
		sin_ray: float = math.sin(ray_rotation)
		cos_ray: float = math.cos(ray_rotation)

		distance_to_vertical, vertical_tile, vertical_sprite_offset = check_intersections(False, sin_ray, cos_ray)
		distance_to_horizontal, horizontal_tile, horizontal_sprite_offset = check_intersections(True, sin_ray, cos_ray)

		ray_relative_angle: float = ray_rotation - rotation

		if (0 < distance_to_vertical) and (distance_to_vertical < distance_to_horizontal or distance_to_horizontal <= 0):
			draw_column(ray_relative_angle, distance_to_vertical, vertical_tile, int(Game.tile_size.y), vertical_sprite_offset)
		elif (0 < distance_to_horizontal):
			draw_column(ray_relative_angle, distance_to_horizontal, horizontal_tile, int(Game.tile_size.x), horizontal_sprite_offset)

		ray_rotation += Settings.ray_delta_angle

	return (pygame.Vector2(), pygame.Surface(), 0.0)


def check_intersections(horizontal: bool, sin_ray: float, cos_ray: float) -> tuple[float, dict, float]:
		X: int = int(not horizontal)
		Y: int = int(horizontal)
		sin_ray, cos_ray = (sin_ray, cos_ray) if horizontal else (cos_ray, sin_ray)

		distance: float = -1
		tile: dict | None = None
		sprite_offset: float = 0.0

		if sin_ray != 0.0:
			ray_direction_sign: int = 1 if sin_ray > 0 else -1
			start_tile_index: int = int(pygame.math.clamp(position[Y] // Game.tile_size[Y], -1, Game.tile_map_size[Y])) + ray_direction_sign
			end_tile_index: int = int(Game.tile_map_size[Y] - 1 if ray_direction_sign > 0 else 0)
			tile_offset: int = 1 if ray_direction_sign < 0 else 0

			for tile_index_y in range(start_tile_index, end_tile_index + ray_direction_sign, ray_direction_sign):
				ray_position_y: float = (tile_index_y + tile_offset) * Game.tile_size[Y]
				ray_length: float = (ray_position_y - position[Y]) / sin_ray
				ray_position_x: float = position[X] + ray_length * cos_ray
				tile_index_x: int = int(ray_position_x // Game.tile_size[X])

				if 0 <= tile_index_x < Game.tile_map_size[X]:
					tile = Game.tile_map[tile_index_y][tile_index_x] if horizontal else Game.tile_map[tile_index_x][tile_index_y]
					if tile is not None:
						distance = ray_length
						tile = tile
						sprite_offset = abs(abs(int(horizontal) - tile_offset) - abs(ray_position_x % Game.tile_size[X]) / Game.tile_size[X])
						break

		return (distance, tile if tile is not None else {}, sprite_offset)











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




def get_object_projections() -> list[tuple[pygame.Vector2, pygame.Surface, float]]:
	for game_object in Game.object_container:
		object_position: pygame.Vector2 = game_object["position"]
		object_radius: int = game_object["radius"]

		distance: float = position.distance_to(object_position)

		view_normal_angle: float = rotation + math.pi / 2
		view_normal_vector: pygame.Vector2 = pygame.Vector2(math.cos(view_normal_angle), math.sin(view_normal_angle))

		left_object_point: pygame.Vector2 = object_position - view_normal_vector * object_radius
		right_object_point: pygame.Vector2 = object_position + view_normal_vector * object_radius


		math.tan(object_relative_angle) / (Settings.tan_half_fov_h * 2) + 0.5


	return (pygame.Vector2(), pygame.Surface(), 0.0)


def calculate_projection(left_relative_angle: float, right_relative_angle: float, distance: float, object_position_z: float, object_height: int, texture: pygame.Surface) -> tuple[pygame.Vector2, pygame.Surface, float]:
	projection_position_x: float = math.tan(left_relative_angle) / Settings.double_tan_half_fov_h * Settings.RESOLUTION.x + Settings.half_resolution.x
	projection_width: float = math.tan(right_relative_angle) / Settings.double_tan_half_fov_h * Settings.RESOLUTION.x + Settings.half_resolution.x - projection_position_x

	projection_position_y: float = 0
	projection_height: float = 0
	if distance != 0:
		camera_position_z: float = position_z + height
		object_top_point: float = object_position_z + object_height
		projection_position_y = (camera_position_z - object_top_point) / (distance * Settings.double_tan_half_fov_v) * Settings.RESOLUTION.y + Settings.half_resolution.y
		projection_height = (camera_position_z - object_position_z)  / (distance * Settings.double_tan_half_fov_v) * Settings.RESOLUTION.y + Settings.half_resolution.y - projection_position_y

	projection_position: pygame.Vector2 = pygame.Vector2(math.floor(projection_position_x), math.floor(projection_position_y))
	projection_surface = pygame.transform.scale(texture, (math.ceil(projection_width), math.ceil(projection_height)))

	return (projection_position, projection_surface, distance)












