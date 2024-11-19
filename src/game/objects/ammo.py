import pygame

import game.game as Game
import game.objects.base_object as BaseObject
import game.objects.entities.player as Player


AMMO_AMOUNT: int = 50


def new() -> dict:
	ammo: dict = {
		"class": "Ammo",
		"sprite": pygame.image.load("assets/sprites/objects/ammo_16.png")}

	return BaseObject.new() | ammo


def update(self: dict, delta: float) -> None:
	if BaseObject.collides_object(self, Game.player):
		if Game.player["health"] < Game.player["max_health"]:
			Player.take_heal(Game.player, AMMO_AMOUNT)
			BaseObject.free(self)
