import pygame

import game.game as Game
import game.objects.base_object as BaseObject


def new() -> dict:
	health: dict = {
		"class": "Health"}

	return BaseObject.new() | health


def update(self: dict, delta: float) -> None:
	pass
