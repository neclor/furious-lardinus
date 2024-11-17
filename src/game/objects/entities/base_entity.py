import pygame

import game.game as Game
import game.objects.base_object as BaseObject


def new() -> dict:
	entity: dict = {
		"class": "BaseEntity",
		"collision": True,
		"velocity": pygame.Vector2(0.0, 0.0),
		"speed": 64,
		"max_health": 100,
		"health": 100}

	return BaseObject.new() | entity


def move(self: dict, direction: pygame.Vector2, delta: float) -> None:
	direction = direction.normalize() if direction != pygame.Vector2(0.0, 0.0) else direction

	velocity: pygame.Vector2 = self["velocity"].lerp(direction * self["speed"], 1)
	self["velocity"] = velocity
	self["position"] = pygame.Vector2(self["position"]) + velocity * delta


def check_collision() -> bool:
	return False


def take_damage(self: dict, damage: int) -> None:
	if damage < 0:
		return

	self["health"] = pygame.math.clamp(self["health"] - damage, 0, self["max_health"])

	if self["health"] == 0:
		die(self)


def take_heal(self: dict, heal: int) -> None:
	if heal < 0:
		return
	self["health"] = pygame.math.clamp(self["health"] + heal, 0, self["max_health"])


def die(self: dict) -> None:
	pass
