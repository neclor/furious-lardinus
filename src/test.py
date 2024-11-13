import pygame
import timeit


window: pygame.Surface


def main() -> None:
	init()

	print(timeit.timeit(use_get, number = 10000000))
	print(timeit.timeit(use_var, number = 10000000))



def init() -> None:
	global window
	window = pygame.display.set_mode((1280, 1024))


def use_var() -> None:
	a: pygame.Surface = window


def use_get() -> None:
	a: pygame.Surface = pygame.display.get_surface()


if __name__ == "__main__":
	main()
