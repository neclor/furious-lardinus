import pygame


sprites: dict = {}


def load_sprite(path: str) -> pygame.Surface:
	sprite: pygame.Surface | None = sprites.get(path)
	if sprite is None:
		sprite = pygame.image.load(path)
		sprites[path] = sprite
	return sprite


