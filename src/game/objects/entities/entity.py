import pygame
import game.objects.game_object as game_object


def new() -> dict:
	new_entity: dict = game_object.new()
	new_entity["max_health"] = 100
	new_entity["health"] = new_entity["max_health"]
	new_entity["speed"] = 64

	return new_entity


def move(entity: dict, velocity: pygame.Vector2, delta: float) -> None:



	pass

