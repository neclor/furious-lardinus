import pygame

import game.game as Game
import game.objects.base_object as BaseObject
import game.objects.entities.player as Player


AMMO_AMOUNT: int = 25


def new(position: pygame.Vector2 = pygame.Vector2()) -> dict:
	ammo: dict = {
		"group": "Object",
		"class": "Ammo",
		"sprite": pygame.image.load("assets/sprites/objects/ammo_16.png")}

	return BaseObject.new(position) | ammo


def update(self: dict, delta: float) -> None:
	if BaseObject.overlaps_object(self, Game.player):

		BaseObject.free(self)
