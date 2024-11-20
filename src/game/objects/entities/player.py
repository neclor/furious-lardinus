import math
import pygame

import settings as Settings
import game.objects.base_object as BaseObject
import game.objects.entities.base_entity as BaseEntity


def new() -> dict:
	player: dict = {
		"class": "Player",
		"sprite": pygame.image.load("src/assets/sprites/test_player_16.png"),

		"rotation": 0.0,

		"weapons": []}

	return BaseEntity.new() | player


def update(self: dict, delta: float) -> None:
	direction: pygame.Vector2 = get_input_vector().rotate_rad(self["rotation"] + math.pi / 2)
	direction = direction.normalize() if direction != pygame.Vector2(0.0, 0.0) else direction

	self["velocity"] = self["velocity"].lerp(direction * self["speed"], max(delta * 8, 1))
	BaseEntity.move_and_collide(self, delta)


def get_input_vector() -> pygame.Vector2:
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

	return direction


def take_heal(self: dict, heal: int) -> None:
	if heal < 0:
		return
	self["health"] = pygame.math.clamp(self["health"] + heal, 0, self["max_health"])


def take_damage(self: dict, damage: int) -> None:
	BaseEntity.take_damage(self, damage)

	if self["health"] == 0:
		die(self)


def die(self: dict) -> None:
	pass
