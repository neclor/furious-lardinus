import math
import random
import pygame

import settings as Settings
import game.rendering.display as Display
import game.game as Game
import game.level as Level


position: pygame.Vector2 = pygame.Vector2()
rotation: float = 0.0
rotation_tan: float = 0.0
camera_position_z: float = 0.0


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
	#draw_backgrond()
	draw_game()


def update_camera() -> None:
	global position, rotation, rotation_tan, camera_position_z
	position = Game.player["position"]
	rotation = Game.player["rotation"]
	rotation_tan = math.tan(rotation)
	camera_position_z = Game.player["position_z"] - Game.player["height"]


def draw_backgrond() -> None:
	Display.surface.fill(Level.floor_color)
	skybox_offset: int = int(rotation / math.tau * Settings.RESOLUTION[0])
	Display.surface.blit(skybox, (Settings.RESOLUTION[0] - skybox_offset, 0))
	Display.surface.blit(skybox, (skybox_offset, 0))


def draw_game() -> None:
	projections: list[tuple[pygame.Surface, pygame.Vector2, float]] = []
	projections += get_tile_map_projections() #+ get_object_projections()
	projections.sort(key = lambda a: a[2], reverse = True)
	for projection in projections:
		Display.surface.blit(projection[0], projection[1])


def get_tile_map_projections() -> list[tuple[pygame.Surface, pygame.Vector2, float]]:
	tile_projections: list[tuple[pygame.Surface, pygame.Vector2, float]] = []

	ray_rotation: float = rotation - Settings.half_fov_h
	for _ in range(Settings.RAYS_NUMBER):
		tile_projections += cast_ray(ray_rotation)
		ray_rotation += Settings.ray_step_angle

	return tile_projections


def cast_ray(ray_rotation: float) -> list[tuple[pygame.Surface, pygame.Vector2, float]]:
	tile_projections: list[tuple[pygame.Surface, pygame.Vector2, float]] = []

	ray_rotation = ray_rotation % math.tau
	ray_sign: pygame.Vector2 = pygame.Vector2((Settings.THREE_HALF_PI < ray_rotation < math.tau or 0 < ray_rotation < Settings.HALF_PI) - (Settings.HALF_PI < ray_rotation < Settings.THREE_HALF_PI), (0 < ray_rotation < math.pi) - (math.pi < ray_rotation < math.tau))
	ray_tan: float = math.tan(ray_rotation)

	next_line: pygame.Vector2 = pygame.Vector2(
		(position.x // Level.tile_size.x + ((0 <= ray_sign.x) or (0 < position.x % Level.tile_size.x)) - (ray_sign.x < 0)) * Level.tile_size.x,
		(position.y // Level.tile_size.y + ((0 <= ray_sign.y) or (0 < position.y % Level.tile_size.y)) - (ray_sign.y < 0)) * Level.tile_size.y)


	left_relative_angle: float = ray_rotation - rotation
	cos_left_relative_angle: float = math.cos(left_relative_angle)


	ray_position: pygame.Vector2 = position

	tan_min_obscured_angle: float = Settings.tan_half_fov_v
	tan_max_obscured_angle: float = -1 * Settings.tan_half_fov_v
	while not line_out_of_bounds(ray_sign, next_line):
		tile_offset: pygame.Vector2 = pygame.Vector2()

		distance_to_next_line: pygame.Vector2 = next_line - ray_position
		distance_ratio: float = distance_to_next_line.y / distance_to_next_line.x
		if abs(ray_local_tan) < abs(distance_ratio):
			ray_local_position = pygame.Vector2(next_line.x, local_position.y + (next_line.x - local_position.x) * ray_local_tan)
			next_line.x += ray_sign.x
			tile_offset.x += min(ray_sign.x, 0)
		elif abs(distance_ratio) < abs(ray_local_tan):
			ray_local_position = pygame.Vector2(local_position.x + (next_line.y - local_position.y) / ray_local_tan, next_line.y)
			next_line.y += ray_sign.y
			tile_offset.y += min(ray_sign.y, 0)
		else:
			ray_local_position = pygame.Vector2(next_line.x, next_line.y)
			next_line += ray_sign
			tile_offset.x += min(ray_sign.x, 0)
			tile_offset.y += min(ray_sign.y, 0)

		local_ray_vector: pygame.Vector2 = ray_local_position - local_position
		distance: float = pygame.Vector2(local_ray_vector.x * Level.tile_size.x, local_ray_vector.y * Level.tile_size.y).length()

		relative_min_obscured_point: float = distance * tan_min_obscured_angle
		relative_max_obscured_point: float = distance * tan_max_obscured_angle
		if relative_min_obscured_point <= Level.min_point_z - camera_position_z and Level.max_point_z - camera_position_z <= relative_max_obscured_point: break

		tile_index: pygame.Vector2 = pygame.Vector2(ray_local_position.x // 1, ray_local_position.y // 1) + tile_offset
		if tile_index.x < 0 or Level.tile_map_size.x <= tile_index.x or tile_index.y < 0 or Level.tile_map_size.y <= tile_index.y: continue
		tile: dict | None = Level.tile_map[int(tile_index.y)][int(tile_index.x)]
		if tile is None: continue

		tile_height: int = tile["height"]

		relative_tile_bottom: float = tile["position_z"] - camera_position_z
		relative_tile_top: float = relative_tile_bottom - tile_height

		relative_min_tile_point: float = min(relative_tile_top, relative_tile_bottom)
		relative_max_tile_point: float = max(relative_tile_top, relative_tile_bottom)

		tile_hidden: bool = True
		if relative_min_tile_point < relative_min_obscured_point:
			tan_min_obscured_angle = relative_min_tile_point / distance
			tile_hidden = False
		if relative_max_obscured_point < relative_max_tile_point:
			tan_max_obscured_angle = relative_max_tile_point / distance
		elif tile_hidden:
			continue

		texture_offset_x: float = abs(ray_local_position.x % 1 - max(ray_sign.y, 0)) % 1
		texture_offset_y: float = abs(ray_local_position.y % 1 + min(ray_sign.x, 0)) % 1

		tile_side_length: int = 0
		texture_offset: float = 0
		if texture_offset_y < texture_offset_x:
			tile_side_length = Level.tile_size.x
			texture_offset = texture_offset_x
		else:
			tile_side_length = Level.tile_size.y
			texture_offset = texture_offset_y

		column_texture = pygame.transform.scale(tile["texture"], (abs(tile_side_length), abs(tile_height))).subsurface(abs(tile_side_length) * texture_offset, 0, 1, abs(tile_height))

		#texture: pygame.Surface = tile["texture"]
		#texture_size: tuple[int, int] = texture.get_size()
		#column_width = texture_size.x / abs(tile_side_length)
		#ceil_column_width = math.ceil(column_width)
		#scale_x = texture_size.x * ceil_subsurface_width / subsurface_width


		tile_projections.append(calculate_projection(left_relative_angle, left_relative_angle + Settings.ray_step_angle, distance * cos_left_relative_angle, relative_tile_top, relative_tile_bottom, column_texture))

	return tile_projections


def line_out_of_bounds(ray_sign: pygame.Vector2, next_line: pygame.Vector2) -> bool:
	return (
		(ray_sign.x < 0 and next_line.x < 0) or
		(ray_sign.y < 0 and next_line.y < 0) or
		(0 < ray_sign.x and Level.tile_map_size.x < next_line.x) or
		(0 < ray_sign.y and Level.tile_map_size.y < next_line.y))


def calculate_projection(left_relative_angle: float, right_relative_angle: float, distance: float, relative_top: float, relative_bottom: float, texture: pygame.Surface) -> tuple[pygame.Surface, pygame.Vector2, float]:
	projection_position_x: float = math.tan(left_relative_angle) * Settings.resolution_x_div_double_tan_half_fov_h + Settings.half_resolution.x
	projection_width: float = math.tan(right_relative_angle) * Settings.resolution_x_div_double_tan_half_fov_h + Settings.half_resolution.x - projection_position_x

	projection_position_y: float = 0
	projection_height: float = 0
	if distance >= 1:
		if relative_bottom < relative_top:
			relative_top, relative_bottom = relative_bottom, relative_top
			texture = pygame.transform.flip(texture, False, True)

		projection_y_factor: float = Settings.resolution_x_div_double_tan_half_fov_h / distance
		projection_position_y = relative_top * projection_y_factor + Settings.half_resolution.y
		projection_height = relative_bottom * projection_y_factor + Settings.half_resolution.y - projection_position_y

	projection_position: pygame.Vector2 = pygame.Vector2(math.floor(projection_position_x), math.floor(projection_position_y))
	projection_surface = pygame.transform.scale(texture, (math.ceil(projection_width), math.ceil(projection_height)))

	return (projection_surface, projection_position, distance)




def get_object_projections() -> list[tuple[pygame.Surface, pygame.Vector2, float]]:
	tile_projections: list[tuple[pygame.Surface, pygame.Vector2, float]] = []

	for game_object in Game.object_container:
		object_position: pygame.Vector2 = game_object["position"]
		object_radius: int = game_object["radius"]

		relative_object_position: pygame.Vector2 = pygame.Vector2(object_position - position).rotate_rad(-(rotation + math.pi / 2))
		relative_object_position.y *= -1

		if relative_object_position.y <= 0: continue

		left_relative_object_point_x: float = relative_object_position.x - object_radius
		left_relative_angle: float = math.atan2(left_relative_object_point_x, relative_object_position.y)
		right_relative_angle: float = math.atan2(relative_object_position.x + object_radius, relative_object_position.y)

		if object_out_of_view(left_relative_angle, right_relative_angle): continue

		relative_object_bottom: float = game_object["position_z"] - camera_position_z
		relative_object_top: float = relative_object_bottom - game_object["height"]
		distance: float = pygame.Vector2(left_relative_object_point_x, relative_object_position.y).length() * math.cos(left_relative_angle)

		tile_projections.append(calculate_projection(left_relative_angle, right_relative_angle, distance, relative_object_top, relative_object_bottom, game_object["sprite"]))

	return tile_projections


def object_out_of_view(left_relative_angle: float, right_relative_angle: float) -> bool:
	return (
		(max(left_relative_angle, right_relative_angle) < -Settings.half_fov_h) or
		(Settings.half_fov_h < min(left_relative_angle, right_relative_angle)))
