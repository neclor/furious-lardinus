import pygame

import game.objects.entities.base_entity as BaseEntity


def new() -> dict:
	player: dict = {
		"rotation": 0.0,
		"max_stamina": 100,
		"stamina": 100,
		"stamina_regen": 10}

	return BaseEntity.new() | player


def update(self: dict, delta: float) -> None:
	pass


