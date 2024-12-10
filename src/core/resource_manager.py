import pygame


images: dict = {}


def load_image(path: str) -> pygame.Surface:
	image: pygame.Surface | None = images.get(path)
	if image is None:
		image = pygame.image.load(path)
		images[path] = image
	return image
