import random
import pygame

import game.game as Game
import game.objects.base_object as BaseObject
import game.objects.entities.base_entity as BaseEntity

import game.objects.medikit as Medikit
import game.objects.ammo as Ammo


def new() -> dict:
	enemy: dict = {
		"class": "BaseEnemy"}

	return BaseObject.new() | enemy


def update(self: dict, delta: float) -> None:
	direction: pygame.Vector2 = self["position"].direction_to(Game.player["position"])
	direction = direction.normalize() if direction != pygame.Vector2(0.0, 0.0) else direction

	self["velocity"] = direction * self["speed"]
	BaseEntity.move_and_collide(self, delta)


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
