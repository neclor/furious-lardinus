import pygame

import game.game as Game
import game.objects.object as Object


def new() -> dict:
	entity: dict = {
		"max_health": 100,
		"health": 100,
		"speed": 64}

	return Object.new() | entity


def move(self: dict, direction: pygame.Vector2, delta: float) -> None:
	if direction == pygame.Vector2(0.0, 0.0):
		return
	next_position: pygame.Vector2 = self["position"] + direction.normalize() * self["speed"] * delta


	self["position"] = next_position


def check_collision() -> bool:
	return False




def take_damage() -> None:
