from typing import Tuple
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
	position: pygame.Vector2 = self["position"]
	velocity: pygame.Vector2 = self["velocity"]
	radius: int = self["radius"]

	next_position = position + velocity * delta
	self["position"], self["velocity"] = handle_collisions(next_position, velocity, radius)


def handle_collisions(position: pygame.Vector2, velocity: pygame.Vector2, radius: int) -> Tuple[pygame.Vector2, pygame.Vector2]:
	position, velocity = handle_level_collision(position, velocity, radius)
	position, velocity = handle_objects_collisions(position, velocity, radius)
	return (position, velocity)


def handle_level_collision(position: pygame.Vector2, velocity: pygame.Vector2, radius: int) -> Tuple[pygame.Vector2, pygame.Vector2]:

	def find_nearest_tile_point(entity_position: pygame.Vector2, x: int, y: int, tile_size: int) -> pygame.Vector2:
		tile_position: pygame.Vector2 = pygame.Vector2(x * tile_size, y * tile_size)
		nearest_tile_point_x: float = pygame.math.clamp(entity_position.x, tile_position.x, tile_position.x + tile_size)
		nearest_tile_point_y: float = pygame.math.clamp(entity_position.y, tile_position.y, tile_position.y + tile_size)
		return pygame.Vector2(nearest_tile_point_x, nearest_tile_point_y)

	def handle_tile_collision(position: pygame.Vector2, velocity: pygame.Vector2, radius: int, nearest_tile_point: pygame.Vector2) -> Tuple[pygame.Vector2, pygame.Vector2]:
		collision_vector: pygame.Vector2 = nearest_tile_point - position
		distance: float = collision_vector.length()
		overlap: float = radius - distance
		if overlap > 0:
			position, velocity = handle_collision(position, velocity, collision_vector, overlap)
		return (position, velocity)

	level_size: pygame.Vector2 = Game.level["size"]
	tile_size: int = int(Game.level["tile_size"])
	tile_map: list[list[Optional[dict]]] = Game.level["tile_map"]

	min_tile_index_x: int = int(max(0, (position.x - radius) // tile_size))
	max_tile_index_x: int = int(min((position.x + radius) // tile_size, level_size.x - 1))
	min_tile_index_y: int = int(max(0, (position.y - radius) // tile_size))
	max_tile_index_y: int = int(min((position.y + radius) // tile_size, level_size.y - 1))

	for y in range(min_tile_index_y, max_tile_index_y + 1):
		for x in range(min_tile_index_x, max_tile_index_x + 1):
			if tile_map[y][x] is not None:
				nearest_tile_point: pygame.Vector2 = find_nearest_tile_point(position, x, y, tile_size)
				position, velocity = handle_tile_collision(position, velocity, radius, nearest_tile_point)

	return (position, velocity)


def handle_objects_collisions(position: pygame.Vector2, velocity: pygame.Vector2, radius: int) -> Tuple[pygame.Vector2, pygame.Vector2]:

	def handle_object_collision(position: pygame.Vector2, velocity: pygame.Vector2, radius: int, object: dict) -> Tuple[pygame.Vector2, pygame.Vector2]:
		object_position: pygame.Vector2 = object["position"]
		object_radius: int = object["radius"]
		collision_vector: pygame.Vector2 = object_position - position
		distance: float = collision_vector.length()
		overlap: float = radius + object_radius - distance
		if overlap > 0:
			position, velocity = handle_collision(position, velocity, collision_vector, overlap)
		return (position, velocity)

	for object in Game.object_container:
		if object["collision"]:
			position, velocity = handle_object_collision(position, velocity, radius, object)

	return (position, velocity)


def handle_collision(position: pygame.Vector2, velocity: pygame.Vector2, collision_vector: pygame.Vector2, overlap: float) -> Tuple[pygame.Vector2, pygame.Vector2]:
	if collision_vector.length() != 0.0: collision_vector.normalize_ip()
	position -= collision_vector * overlap
	velocity_projection_length: float = velocity.dot(collision_vector)
	velocity -= collision_vector * velocity_projection_length

	return (position, velocity)


def take_damage(self: dict, damage: int) -> None:
	if damage < 0:
		return

	self["health"] = pygame.math.clamp(self["health"] - damage, 0, self["max_health"])


def die(self: dict) -> None:
	BaseObject.free(self)
