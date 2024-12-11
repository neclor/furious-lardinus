import pygame


import game.objects.base_object as BaseObject




import game.objects.entities
import game.objects.entities
import game.objects.entities.player as Player
import game.objects.entities




import game.objects.interactive_objects.ammo as Ammo
import game.objects.interactive_objects.medikit as Medikit
import game.objects.interactive_objects



def update(self: dict, delta: float) -> None:
	match self["group"]:
		case "Player":
			Player.update(self, delta)

		case "Enemy":
			update_enemy(self, delta)

		case "InteractiveObject":
			update_interactive_object(self, delta)


def update_enemy(self: dict, delta: float) -> None:
	match self["class"]:
		case "":
			pass


def update_interactive_object(self: dict, delta: float) -> None:
	match self["class"]:
		case "Ammo":
			Ammo.update(self)
		case "Medikit":
			Medikit.update(self)


