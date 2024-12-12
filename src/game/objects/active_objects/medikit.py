import pygame


import game.game as Game
import game.objects.entities.player as Player
import game.object_system.base_object as BaseObject
import game.objects.interactive_objects.base_interactive_object as BaseInteractiveObject


MEDIKIT_SPRITE: pygame.Surface = pygame.image.load("src/assets/sprites/objects/medikit_16.png")
HEAL_AMOUNT: int = 25


def new(position: pygame.Vector2 = pygame.Vector2()) -> dict:
	medikit: dict = {
		"group": "InteractiveObject",
		"class": "Medikit",
		"sprite": MEDIKIT_SPRITE,
	}
	return BaseInteractiveObject.new(position) | medikit


def update(self: dict) -> None:
	if not BaseInteractiveObject.overlaps_player(self): return

	if Game.player["health"] < Game.player["max_health"]:
		Player.take_heal(Game.player, HEAL_AMOUNT)
		BaseObject.free(self)
