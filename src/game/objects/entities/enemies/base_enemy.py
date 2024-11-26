import random
import pygame

import game.game as Game
import game.objects.base_object as BaseObject
import game.objects.entities.base_entity as BaseEntity

import game.objects.medikit as Medikit
import game.objects.ammo as Ammo


VISION_RANGE: int = 500


def new(position: pygame.Vector2 = pygame.Vector2(0.0, 0.0)) -> dict:
	enemy: dict = {
		"class": "BaseEnemy",
		"sprite": pygame.image.load("src/assets/sprites/enemies/test_enemy_16.png")}

	return BaseEntity.new(position) | enemy


def update(self: dict, delta: float) -> None:
	self["velocity"] = get_direction_to_player(self) * self["speed"]
	BaseEntity.move_and_slide(self, delta)


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


def take_damage(self: dict, damage: int) -> None:
	BaseEntity.take_damage(self, damage)

	if self["health"] == 0:
		die(self)


def die(self: dict) -> None:
	drop_loot(self)
	BaseEntity.die(self)


def drop_loot(self: dict) -> None:
	loot: dict = generate_loot()
	loot["position"] = self["position"]
	Game.object_container.append(loot)


def generate_loot() -> dict:
	if random.randrange(0, 3) == 0:
		return Medikit.new()
	else:
		return Ammo.new()
