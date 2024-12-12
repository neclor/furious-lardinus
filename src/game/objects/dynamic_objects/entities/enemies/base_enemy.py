import random
import pygame

import settings as Settings
import game.game as Game
import game.level_manager as LevelManager
import game.object_manager as ObjectManager
import game.object_class_manager as ObjectClassManager
import game.objects.dynamic_objects.entities.base_entity as BaseEntity
import game.objects.dynamic_objects.base_dynamic_object as BaseDynamicObject


DETECTION_RANGE: int = 320


def new(position: pygame.Vector2 = pygame.Vector2()) -> dict:
	return ObjectClassManager.new_object(BaseEntity.new(position), {
		"groups": {"Enemy"},
		"class": "BaseEnemy",

		"attack_cooldown": 1,
		"attack_cooldown_left": 0,

		"speed": 32,
		"max_health": 100,
		"health": 100,
	})


def update(self: dict, delta: float) -> None:
	self["velocity"] = get_direction_to_player(self) * self["speed"]
	BaseDynamicObject.move_and_slide(self, delta)


def get_direction_to_player(self: dict) -> pygame.Vector2:
	player_position: pygame.Vector2 = Game.player["position"]
	player_radius: int = Game.player["radius"]

	position: pygame.Vector2 = self["position"]
	radius: int = self["radius"]

	vector_to_player: pygame.Vector2 = player_position - position
	distance_to_player: float = vector_to_player.length()

	if radius + player_radius < distance_to_player < VISION_RANGE:
		return vector_to_player.normalize()

	return pygame.Vector2(0.0, 0.0)


def fast_ray_cast()


def drop_loot(self: dict) -> None:
	loot: dict = generate_loot()
	loot["position"] = self["position"]
	Game.object_container.append(loot)


def generate_loot() -> dict:
	if random.randrange(0, 3) == 0:
		return Medikit.new()
	else:
		return Ammo.new()
