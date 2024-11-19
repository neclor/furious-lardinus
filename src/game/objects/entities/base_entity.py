import pygame

import game.game as Game
import game.objects.base_object as BaseObject


def new() -> dict:
	entity: dict = {
		"class": "BaseEntity",
		"collision": True,

		"velocity": pygame.Vector2(0.0, 0.0),
		"speed": 128,

		"max_health": 100,
		"health": 100}

	return BaseObject.new() | entity


def move_and_collide(self: dict, delta: float) -> None:
	next_position: pygame.Vector2 = pygame.Vector2(self["position"]) + self["velocity"] * delta
	if not check_collision(next_position, self["radius"]):
		self["position"] = next_position


def check_collision(position: pygame.Vector2, radius: int) -> bool:
	return check_level_collision(position, radius) or check_objects_collision(position, radius)


def check_level_collision(position: pygame.Vector2, radius: int) -> bool:
	level_size: pygame.Vector2 = Game.level["size"]
	tile_size: int = int(Game.level["tile_size"])
	tile_map: list[list] = Game.level["tile_map"]

	min_tile_index_x: int = int(max(0, (position.x - radius) // tile_size))
	max_tile_index_x: int = int(min((position.x + radius) // tile_size, level_size.x - 1))
	min_tile_index_y: int = int(max(0, (position.y - radius) // tile_size))
	max_tile_index_y: int = int(min((position.y + radius) // tile_size, level_size.y - 1))

	for y in range(min_tile_index_y, max_tile_index_y + 1):
		for x in range(min_tile_index_x, max_tile_index_x + 1):
			if tile_map[y][x] is not None:

				tile_position: pygame.Vector2 = pygame.Vector2(x * tile_size, y * tile_size)

				nearest_point_x: float = pygame.math.clamp(position.x, tile_position.x, tile_position.x + tile_size)
				nearest_point_y: float = pygame.math.clamp(position.y, tile_position.y, tile_position.y + tile_size)

				if position.distance_to(pygame.Vector2(nearest_point_x, nearest_point_y)) <= radius:
					return True
	return False


def check_objects_collision(position: pygame.Vector2, radius: int) -> bool:
	for object in Game.object_container:
		if object["collision"]:
			if BaseObject.circles_overlap(position, radius, object["position"], object["radius"]):
				return True
	return False
