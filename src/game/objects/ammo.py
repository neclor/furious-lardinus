import pygame

import game.game as Game
import game.objects.base_object as BaseObject


def new() -> dict:
	ammo: dict = {
		"class": "Ammo",
		"sprite": pygame.image.load("assets\sprites\medikit_32.png"),
		"ammo": 50}

	return BaseObject.new() | ammo


def update(self: dict, delta: float) -> None:
	player: dict = Game.player
	if BaseObject.collides_object(self, player):
		if player["health"] < player["max_health"]:
			Player.take_heal(player, self["heal"])

