import pygame

import game.game as Game
import game.objects.base_object as BaseObject





def take_damage(self: dict, damage: int) -> None:
	if damage < 0:
		return

	self["health"] = pygame.math.clamp(self["health"] - damage, 0, self["max_health"])

	if self["health"] == 0:
		die(self)


def take_heal(self: dict, heal: int) -> None:
	if heal < 0:
		return
	self["health"] = pygame.math.clamp(self["health"] + heal, 0, self["max_health"])\



def die(self: dict) -> None:
	pass

def free(self: dict) -> None:
	pass
