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


def move(self: dict, direction: pygame.Vector2, delta: float) -> None:
	direction = direction.normalize() if direction != pygame.Vector2(0.0, 0.0) else direction
	self["velocity"] = self["velocity"].lerp(direction * self["speed"], delta * 8)
	self["position"] = pygame.Vector2(self["position"]) + self["velocity"] * delta




def check_collision() -> bool:
	return False


