import pygame


import game.game as Game
import game.level as Level
import game.objects.base_object as BaseObject


def new(position: pygame.Vector2 = pygame.Vector2(), velocity: pygame.Vector2 = pygame.Vector2()) -> dict:
	base_mobile_object: dict = {
		"group": "MobileObject",
		"class": "BaseMobileObject",
		"velocity": velocity,
	}
	return BaseObject.new(position) | base_mobile_object


def move_and_collide(self: dict, delta: float) -> tuple[list[dict], bool]:
	velocity: pygame.Vector2 = self["velocity"]
	next_position: pygame.Vector2 = self["position"] + velocity * delta
	self["position"] = next_position
	self["position"], self["velocity"], collided_objects, collides_with_tile_map = handle_collisions(next_position, velocity, self["radius"])
	return(collided_objects, collides_with_tile_map)


def handle_collisions(position: pygame.Vector2, velocity: pygame.Vector2, radius: int) -> tuple[pygame.Vector2, pygame.Vector2, list[dict], bool]:
	position, velocity, collided_objects = handle_objects_collisions(position, velocity, radius)
	position, velocity, collides_with_tile_map = handle_tile_map_collision(position, velocity, radius)
	return (position, velocity, collided_objects, collides_with_tile_map)


# Objects collisions
def handle_objects_collisions(position: pygame.Vector2, velocity: pygame.Vector2, radius: int) -> tuple[pygame.Vector2, pygame.Vector2, list[dict]]:
	collided_objects: list[dict] = []
	for game_object in Game.object_container:
		if game_object["has_collision"]:
			position, velocity, collided_object = handle_object_collision(position, velocity, radius, game_object)
			if collided_object is not None: collided_objects.append(collided_object)
	return (position, velocity, collided_objects)


def handle_object_collision(position: pygame.Vector2, velocity: pygame.Vector2, radius: int, game_object: dict) ->tuple[pygame.Vector2, pygame.Vector2, dict | None]:
	object_position: pygame.Vector2 = game_object["position"]
	object_radius: int = game_object["radius"]
	collision_vector: pygame.Vector2 = object_position - position
	distance: float = collision_vector.length()
	collided_object: dict | None = None
	if 0 < distance:
		overlap: float = radius + object_radius - distance
		if 0 < overlap:
			position, velocity = handle_collision(position, velocity, collision_vector, overlap)
			collided_object = game_object
	return (position, velocity, collided_object)


# Tile map collisions
def handle_tile_map_collision(position: pygame.Vector2, velocity: pygame.Vector2, radius: int) -> tuple[pygame.Vector2, pygame.Vector2, bool]:
	min_tile_index_x: int = int(max(0, (position.x - radius) // Level.tile_size.x))
	max_tile_index_x: int = int(min((position.x + radius) // Level.tile_size.x, Level.tile_map_size.x - 1))
	min_tile_index_y: int = int(max(0, (position.y - radius) // Level.tile_size.y))
	max_tile_index_y: int = int(min((position.y + radius) // Level.tile_size.y, Level.tile_map_size.y - 1))

	collides_with_tile_map: bool = False
	for tile_index_y in range(min_tile_index_y, max_tile_index_y + 1):
		for tile_index_x in range(min_tile_index_x, max_tile_index_x + 1):
			if Level.tile_map[tile_index_y][tile_index_x] is not None:
				nearest_tile_point: pygame.Vector2 = find_nearest_tile_point(position, tile_index_x, tile_index_y, Level.tile_size)
				position, velocity, collides_with_tile = handle_tile_collision(position, velocity, radius, nearest_tile_point)
				collides_with_tile_map = collides_with_tile_map or collides_with_tile
	return (position, velocity, collides_with_tile_map)


def find_nearest_tile_point(entity_position: pygame.Vector2, tile_index_x: int, tile_index_y: int, tile_size: pygame.Vector2) -> pygame.Vector2:
	tile_position: pygame.Vector2 = pygame.Vector2(tile_index_x * tile_size.x, tile_index_y * tile_size.y)
	nearest_tile_point_x: float = pygame.math.clamp(entity_position.x, tile_position.x, tile_position.x + tile_size.x)
	nearest_tile_point_y: float = pygame.math.clamp(entity_position.y, tile_position.y, tile_position.y + tile_size.y)
	return pygame.Vector2(nearest_tile_point_x, nearest_tile_point_y)


def handle_tile_collision(position: pygame.Vector2, velocity: pygame.Vector2, radius: int, nearest_tile_point: pygame.Vector2) -> tuple[pygame.Vector2, pygame.Vector2, bool]:
	collision_vector: pygame.Vector2 = nearest_tile_point - position
	distance: float = collision_vector.length()
	collides_with_tile: bool = False
	if 0 < distance:
		overlap: float = radius - distance
		if 0 < overlap:
			position, velocity = handle_collision(position, velocity, collision_vector, overlap)
			collides_with_tile = True
	return (position, velocity, collides_with_tile)


# Collisions
def handle_collision(position: pygame.Vector2, velocity: pygame.Vector2, collision_vector: pygame.Vector2, overlap: float) -> tuple[pygame.Vector2, pygame.Vector2]:
	collision_vector.normalize_ip()
	position -= collision_vector * overlap
	velocity -= collision_vector * velocity.dot(collision_vector)
	return (position, velocity)
