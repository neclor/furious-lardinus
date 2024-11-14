import pygame

import game.objects.entities.entity as Entity


def new() -> dict:
	player: dict = {
		"rotation": 0.0,
		"max_stamina": 100,
		"stamina": 100,
		"stamina_regen": 10}

	return Entity.new() | player


def update(self: dict, delta: float) -> None:
	pass


