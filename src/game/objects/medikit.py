import pygame

import game.game as Game
import game.objects.base_object as BaseObject
import game.objects.entities.player as Player


HEAL_AMOUNT: int = 25


def new(position: pygame.Vector2 = pygame.Vector2()) -> dict:
	medikit: dict = {
		"class": "Medikit",
		"sprite": pygame.image.load("src/assets/sprites/objects/medikit_16.png")}

	return BaseObject.new(position) | medikit


def update(self: dict, delta: float) -> None:
	if BaseObject.overlaps_object(self, Game.player):
		if Game.player["health"] < Game.player["max_health"]:
			Player.take_heal(Game.player, HEAL_AMOUNT)
			BaseObject.free(self)
