import pygame

import game.game as Game


def new() -> dict:
	object: dict = {
		"class": "BaseObject",
		"sprite": None,
		"collision": False,
		"position": pygame.Vector2(0.0, 0.0),
		"radius": 8,
		"position_z": 0.0,
		"height": 32}

	return object


def get_overlapping_enemies(self: dict) -> list[dict]:
	overlapping_enemies: list[dict] = []
	for enemy in Game.enemies_container:
		if overlaps_object(self, enemy):
			overlapping_enemies.append(enemy)
	return overlapping_enemies


def overlaps_object(self: dict, object: dict) -> bool:
	dist: float = self["position"].dist(object["position"])
	return dist <= self["radius"] + object["radius"]


def free(self: dict) -> None:
	Game.objects_container.remove(self)
