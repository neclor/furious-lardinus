import pygame

import game.game as Game
import game.objects.base_object as BaseObject


def new(position: pygame.Vector2 = pygame.Vector2()) -> dict:
	entity: dict = {
		"class": "BaseEntity",
		"collision": True,

		"velocity": pygame.Vector2(),
		"speed": 32,

		"max_health": 100,
		"health": 100}

	return BaseObject.new(position) | entity


def move_and_slide(self: dict, delta: float) -> None:
	position: pygame.Vector2 = self["position"]
	velocity: pygame.Vector2 = self["velocity"]
	radius: int = self["radius"]

	next_position: pygame.Vector2 = position + velocity * delta
	self["position"] = next_position
	self["position"], self["velocity"] = handle_collisions(next_position, velocity, radius)


def handle_collisions(position: pygame.Vector2, velocity: pygame.Vector2, radius: int) -> tuple[pygame.Vector2, pygame.Vector2]:
	position, velocity = handle_level_collision(position, velocity, radius)
	position, velocity = handle_objects_collisions(position, velocity, radius)
	return (position, velocity)


def handle_level_collision(position: pygame.Vector2, velocity: pygame.Vector2, radius: int) -> tuple[pygame.Vector2, pygame.Vector2]:

	def find_nearest_tile_point(entity_position: pygame.Vector2, tile_index_x: int, tile_index_y: int, tile_size: pygame.Vector2) -> pygame.Vector2:
		tile_position: pygame.Vector2 = pygame.Vector2(tile_index_x * tile_size.x, tile_index_y * tile_size.y)
		nearest_tile_point_x: float = pygame.math.clamp(entity_position.x, tile_position.x, tile_position.x + tile_size.x)
		nearest_tile_point_y: float = pygame.math.clamp(entity_position.y, tile_position.y, tile_position.y + tile_size.y)
		return pygame.Vector2(nearest_tile_point_x, nearest_tile_point_y)

	def handle_tile_collision(position: pygame.Vector2, velocity: pygame.Vector2, radius: int, nearest_tile_point: pygame.Vector2) -> tuple[pygame.Vector2, pygame.Vector2]:
		collision_vector: pygame.Vector2 = nearest_tile_point - position
		distance: float = collision_vector.length()
		overlap: float = radius - distance
		if overlap > 0:
			position, velocity = handle_collision(position, velocity, collision_vector, overlap)
		return (position, velocity)

	tile_size: pygame.Vector2 = Game.level["tile_size"]
	tile_map_size: pygame.Vector2 = Game.level["tile_map_size"]
	tile_map: list[list[dict | None]] = Game.level["tile_map"]

	min_tile_index_x: int = int(max(0, (position.x - radius) // tile_size.x))
	max_tile_index_x: int = int(min((position.x + radius) // tile_size.x, tile_map_size.x - 1))
	min_tile_index_y: int = int(max(0, (position.y - radius) // tile_size.y))
	max_tile_index_y: int = int(min((position.y + radius) // tile_size.y, tile_map_size.y - 1))

	for tile_index_y in range(min_tile_index_y, max_tile_index_y + 1):
		for tile_index_x in range(min_tile_index_x, max_tile_index_x + 1):
			if tile_map[tile_index_y][tile_index_x] is not None:
				nearest_tile_point: pygame.Vector2 = find_nearest_tile_point(position, tile_index_x, tile_index_y, tile_size)
				position, velocity = handle_tile_collision(position, velocity, radius, nearest_tile_point)

	return (position, velocity)


def handle_objects_collisions(position: pygame.Vector2, velocity: pygame.Vector2, radius: int) -> tuple[pygame.Vector2, pygame.Vector2]:

	def handle_object_collision(position: pygame.Vector2, velocity: pygame.Vector2, radius: int, object: dict) ->tuple[pygame.Vector2, pygame.Vector2]:
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


def handle_collision(position: pygame.Vector2, velocity: pygame.Vector2, collision_vector: pygame.Vector2, overlap: float) -> tuple[pygame.Vector2, pygame.Vector2]:
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
