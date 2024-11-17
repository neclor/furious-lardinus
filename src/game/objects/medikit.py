import pygame

import game.game as Game
import game.objects.base_object as BaseObject
import game.objects.entities.player as Player


def new() -> dict:
	medikit: dict = {
		"class": "Health",
		"sprite": pygame.image.load("assets\sprites\medikit_32.png"),
		"heal": 20}

	return BaseObject.new() | medikit


def update(self: dict, delta: float) -> None:
	player: dict = Game.player
	if BaseObject.overlaps_object(self, player):
		if player["health"] < player["max_health"]:
			Player.take_heal(player, self["heal"])

