import math
import pygame

import settings as Settings
import game.objects.entities.base_entity as BaseEntity


def new() -> dict:
	player: dict = {
		"class": "Player",
		"sprite": pygame.image.load("src/assets/sprites/test_player_16.png"),

		"rotation": 0.0,

		"max_stamina": 100,
		"stamina": 100,
		"stamina_regen": 10,
		"sprint_speed": 100,

		"weapons": []}

	return BaseEntity.new() | player


def update(self: dict, delta: float) -> None:
	BaseEntity.move(self, get_move_direction(self), delta)


def get_move_direction(self: dict) -> pygame.Vector2:
	direction: pygame.Vector2 = pygame.Vector2(0.0, 0.0)

	keys = pygame.key.get_pressed()
	if keys[Settings.FORWARD]:
		direction.y -= 1
	if keys[Settings.BACKWARD]:
		direction.y += 1
	if keys[Settings.LEFT]:
		direction.x -= 1
	if keys[Settings.RIGHT]:
		direction.x += 1

	return direction.rotate_rad(self["rotation"] + math.pi / 2)


def check_collision() -> bool:
	return False


def take_damage(self: dict, damage: int) -> None:
	if damage < 0:
		return

	self["health"] = pygame.math.clamp(self["health"] - damage, 0, self["max_health"])

	if self["health"] == 0:
		die(self)


def take_heal(self: dict, heal: int) -> None:
	if heal < 0:
		return
	self["health"] = pygame.math.clamp(self["health"] + heal, 0, self["max_health"])


def die(self: dict) -> None:
	pass
