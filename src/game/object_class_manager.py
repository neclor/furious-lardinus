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


def new_object(parent_object: dict, new_data: dict) -> dict:
	new_object: dict = parent_object | new_data
	new_groups: set | None = new_data.get("groups")
	if new_groups is not None: new_object["groups"] = parent_object["groups"] | new_groups
	return new_object


def update(self: dict, delta: float) -> None:
	groups: set = self["groups"]
	if "Object" in groups:
		if "DynamicObject" in groups:
			pass
		elif "ActiveObject" in groups:
			pass
		else:
			pass
	else:
		pass





	match self["group"]:

		case "Player":
			Player.update(self, delta)

		case "Enemy":
			update_enemy(self, delta)

		case "InteractiveObject":
			update_interactive_object(self, delta)


def die(self: dict) -> None:
	pass
