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
	tile_size_ratio: float = Level.tile_size.x / Level.tile_size.y
	local_position: pygame.Vector2 = pygame.Vector2(position.x / Level.tile_size.x, position.y / Level.tile_size.y)

	tile_projections: list[tuple[pygame.Vector2, pygame.Surface, float]] = []

	ray_rotation: float = rotation - Settings.half_fov_h
	for _ in range(Settings.RAYS_NUMBER):
		ray_sin: float = math.sin(ray_rotation)
		ray_cos: float = math.cos(ray_rotation)
		ray_sign: pygame.Vector2 = pygame.Vector2(1 if ray_cos > 0 else (-1 if ray_cos < 0 else 0), 1 if ray_sin > 0 else (-1 if ray_sin < 0 else 0))
		ray_local_tan: float = math.tan(ray_rotation) * tile_size_ratio

		ray_local_position: pygame.Vector2 = local_position

		next_line: pygame.Vector2 = pygame.Vector2(
			math.ceil(ray_local_position.x) - 1 if ray_sign.x < 0 else math.floor(ray_local_position.x) + ray_sign.x,
			math.ceil(ray_local_position.y) - 1 if ray_sign.y < 0 else math.floor(ray_local_position.y) + ray_sign.y)
		tile_index_offset: pygame.Vector2 = pygame.Vector2(
			-1 if ray_sign.x < 0 else 0,
			-1 if ray_sign.y < 0 else 0)

		while not (
			(ray_sign.x < 0 and next_line.x < 1) or
			(ray_sign.y < 0 and next_line.y < 1) or
			(0 < ray_sign.x and Game.tile_map_size.x <= next_line.x) or
			(0 < ray_sign.y and Game.tile_map_size.y <= next_line.y)
		):

			if ray_sign.x == 0:
				ray_local_position.y = next_line.y
				next_line.y += ray_sign.y
			elif ray_sign.y == 0:
				ray_local_position.x = next_line.x
				next_line.x += ray_sign.x
			else:
				delta_to_next_line: pygame.Vector2 = next_line - ray_local_position # -0.4, 0
				delta rayio
				tile_index







			local_delta: pygame.Vector2 = pygame.Vector2(
				next_line.x - ray_local_position.x,
				next_line.y - ray_local_position.y)

			if abs(local_delta.x) < abs(local_delta.y):
				ray_local_position =




			local_position

			max_point: float = camera_position_
			min_point: float


			local_position: pygame.Vector2

		ray_rotation += Settings.ray_delta_angle


def check_intersections(ray_local_position: pygame.Vector2) -> None:
	pass




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












