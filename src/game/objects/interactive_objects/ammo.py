import pygame


import game.game as Game
import game.objects.mobile_objects.entities.player as Player
import game.objects.base_object as BaseObject
import game.objects.interactive_objects.base_interactive_object as BaseInteractiveObject


AMMO_SPRITE: pygame.Surface = pygame.image.load("assets/sprites/objects/ammo_16.png")
AMMO_AMOUNT: int = 25


def new(position: pygame.Vector2 = pygame.Vector2()) -> dict:
	ammo: dict = {
		"group": "InteractiveObject",
		"class": "Ammo",
		"sprite": AMMO_SPRITE,
	}
	return BaseInteractiveObject.new(position) | ammo


def update(self: dict) -> None:
	if not BaseInteractiveObject.overlaps_player(self): return
	BaseObject.free()
