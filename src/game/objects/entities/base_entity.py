import pygame
from ...objects import base_object


def new() -> dict:
	base_entity: dict = {
		"max_health": 100,
		"health": base_entity["max_health"],
		"speed": 64}

	return base_object.new() | base_entity


def move(entity: dict, velocity: pygame.Vector2, delta: float) -> None:



	pass






print(new())
