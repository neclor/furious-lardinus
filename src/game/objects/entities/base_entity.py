from typing import Optional
import pygame

import game.game as Game
import game.objects.base_object as BaseObject


def new(position: pygame.Vector2 = pygame.Vector2(0.0, 0.0)) -> dict:
	entity: dict = {
		"class": "BaseEntity",
		"collision": True,

		"velocity": pygame.Vector2(0.0, 0.0),
		"speed": 128,

		"max_health": 100,
		"health": 100}

	return BaseObject.new(position) | entity


def move_and_slide(self: dict, delta: float) -> None:

	collide_level(self, delta)


	self["position"] += self["velocity"] * delta


def collide_level(self: dict, delta: float) -> None:
	level_size: pygame.Vector2 = Game.level["size"]
	tile_size: int = int(Game.level["tile_size"])
	tile_map: list[list[Optional[dict]]] = Game.level["tile_map"]

	def find_nearest_tile_point(position: pygame.Vector2, tile_x: int, tile_y: int, tile_size: int) -> pygame.Vector2:
		tile_position: pygame.Vector2 = pygame.Vector2(x * tile_size, y * tile_size)
		nearest_tile_point_x: float = pygame.math.clamp(position.x, tile_position.x, tile_position.x + tile_size)
		nearest_tile_point_y: float = pygame.math.clamp(position.y, tile_position.y, tile_position.y + tile_size)
		return pygame.Vector2(nearest_tile_point_x, nearest_tile_point_y)


	next_position: pygame.Vector2 = self["position"] + self["velocity"] * delta

	min_tile_index_x: int = int(max(0, (min(self["position"].x, next_position.x) - self["radius"]) // tile_size))
	max_tile_index_x: int = int(min((max(self["position"].x, next_position.x) + self["radius"]) // tile_size, level_size.x - 1))
	min_tile_index_y: int = int(max(0, (min(self["position"].y, next_position.y) - self["radius"]) // tile_size))
	max_tile_index_y: int = int(min((max(self["position"].y, next_position.y) + self["radius"]) // tile_size, level_size.y - 1))

	for y in range(min_tile_index_y, max_tile_index_y + 1):
		for x in range(min_tile_index_x, max_tile_index_x + 1):
			if tile_map[y][x] is not None:

				nearest_p = find_nearest_tile_point(next_position, x, y, tile_size)

				dist = next_position.distance_to(nearest_p)
				if dist <= self["radius"]:

					collision_vector = next_position - nearest_p
					collision_vector = collision_vector.normalize() if collision_vector != pygame.Vector2(0.0, 0.0) else collision_vector

					next_position += collision_vector * (self["radius"] - dist)
					normal_vector = pygame.Vector2(-collision_vector.y, collision_vector.x)

					self["velocity"].dot(normal_vector)



				collide_vector = next_position - nearest_p
				tile_position: pygame.Vector2 = pygame.Vector2(x * tile_size, y * tile_size)
				nearest_tile_point_x: float = pygame.math.clamp(next_position.x, tile_position.x, tile_position.x + tile_size)
				nearest_tile_point_y: float = pygame.math.clamp(next_position.y, tile_position.y, tile_position.y + tile_size)

				if next_position.distance_to(pygame.Vector2(nearest_tile_point_x, nearest_tile_point_y)) <= self["radius"]:
					new_nearest_tile_point_y: float = pygame.math.clamp(self["position"].y, tile_position.y, tile_position.y + tile_size)
					next_position_x: pygame.Vector2 = pygame.Vector2(next_position.x, self["position"].y)
					collide_x: bool = next_position_x.distance_to(pygame.Vector2(nearest_tile_point_x, new_nearest_tile_point_y)) <= self["radius"]

					new_nearest_tile_point_x: float = pygame.math.clamp(self["position"].x, tile_position.x, tile_position.x + tile_size)
					next_position_y: pygame.Vector2 = pygame.Vector2(self["position"].x, next_position.y)
					collide_y: bool = next_position_y.distance_to(pygame.Vector2(new_nearest_tile_point_x, nearest_tile_point_y)) <= self["radius"]

					if collide_x: self["velocity"].x = 0.0
					if collide_y: self["velocity"].y = 0.0
					if not collide_x and not collide_y: self["velocity"] = pygame.Vector2(0.0, 0.0)



def collide(self: dict, collision_vector: pygame.Vector2):
	pass








def check_objects_collision(position: pygame.Vector2, radius: int) -> bool:
	for object in Game.object_container:
		if object["collision"]:
			if BaseObject.circles_overlap(position, radius, object["position"], object["radius"]):
				return True
	return False


def take_damage(self: dict, damage: int) -> None:
	if damage < 0:
		return

	self["health"] = pygame.math.clamp(self["health"] - damage, 0, self["max_health"])


def die(self: dict) -> None:
	BaseObject.free(self)
