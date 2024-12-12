import pygame


# BaseObject
import game.objects.base_object as BaseObject
	# BaseActiveObject
import game.objects.active_objects.base_active_object as BaseActiveObject
		# Ammo
import game.objects.active_objects.ammo as Ammo
		# Medikit
import game.objects.active_objects.medikit as Medikit
		# BaseExit
import game.objects.active_objects.exits.base_exit as BaseExit
			# Door
import game.objects.active_objects.exits.door as Door

	# BaseDynamicObject
import game.objects.dynamic_objects.base_dynamic_object as BaseDynamicObject
		# BaseEntity
import game.objects.dynamic_objects.entities.base_entity as BaseEntity
			# Player
import game.objects.dynamic_objects.entities.player as Player
			# BaseEnemy
import game.objects.dynamic_objects.entities.enemies.base_enemy as BaseEnemy
				# --

		# BaseProjectile
import game.objects.dynamic_objects.projectiles.base_projectile as BaseProjectile
		# PlayerProjectile

		# WizzardProjectile


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


def object_collided(self: dict, object: dict) -> None:
	pass
