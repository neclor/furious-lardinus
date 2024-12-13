import math
import pygame


import settings as Settings
import core.events as Events


import game.game as Game
import game.object_manager as ObjectManager
import game.objects.dynamic_objects.projectiles.player_projectile as PlayerProjectile


PLAYER_PROJECTILE_SPEED: int = 256


gun: dict = {
	"available": True,
	"sprite": None,
	"damage": 100,
	"max_ammo": math.inf,
	"ammo": math.inf,
	"cooldown": 0.5,
}
shotgun: dict = {
	"available": True,
	"sprite": None,
	"damage": 25,
	"max_ammo": 100,
	"ammo": 100,
	"cooldown": 0.5,
}
assault: dict = {
	"available": True,
	"sprite": None,
	"damage": 15,
	"max_ammo": 200,
	"ammo": 200,
	"cooldown": 0.1,
}


current_weapon: dict = gun
cooldown_left: float = 0


def update(delta: float) -> None:
	update_cooldown(delta)
	check_events()


def add_ammo(ammo: int) -> None:
	if shotgun["available"] and shotgun["ammo"] < shotgun["max_ammo"]:
		shotgun["ammo"] = min(shotgun["ammo"] + ammo, shotgun["max_ammo"])
	if assault["available"] and assault["ammo"] < assault["max_ammo"]:
		assault["ammo"] = min(assault["ammo"] + ammo, assault["max_ammo"])


def update_cooldown(delta: float) -> None:
	global cooldown_left
	cooldown_left = max(cooldown_left - delta, 0)


def shoot() -> None:
	global cooldown_left
	if cooldown_left > 0: return
	if current_weapon["ammo"] <= 0: return
	cooldown_left = current_weapon["cooldown"]
	if current_weapon is gun:
		gun_shoot()
	elif current_weapon is shotgun:
		shotgun_shot()
	else:
		assault_shot()


def gun_shoot() -> None:
	position: pygame.Vector2 = Game.player["position"]
	velocity: pygame.Vector2 = pygame.Vector2(PLAYER_PROJECTILE_SPEED, 0).rotate_rad(Game.player["rotation"])
	ObjectManager.add_object(PlayerProjectile.new(current_weapon["damage"], position.copy(), velocity))


def shotgun_shot() -> None:
	pass


def assault_shot() -> None:
	pass


def change_weapon(new_weapon: dict) -> None:
	global current_weapon, cooldown_left
	if current_weapon is new_weapon: return
	if not new_weapon["available"]: return
	current_weapon = new_weapon
	cooldown_left = current_weapon["cooldown"]


def check_events() -> None:
	for event in Events.get():
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			shoot()
		elif event.type == pygame.KEYDOWN:
			match event.key:
				case Settings.gun:
					change_weapon(gun)
				case Settings.shotgun:
					change_weapon(shotgun)
				case Settings.assault:
					change_weapon(assault)
