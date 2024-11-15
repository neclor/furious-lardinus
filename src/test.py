import pygame
import timeit

import test2 as tst

window: pygame.Surface

b = 100

def main() -> None:
	init()

	print(timeit.timeit(close, number = 10000))
	print(timeit.timeit(far, number = 10000))



def init() -> None:
	global window
	window = pygame.display.set_mode((1280, 1024))


def use_var() -> None:
	a: pygame.Surface = window


def use_get() -> None:
	a: pygame.Surface = pygame.display.get_surface()


def dist() -> None:
	a = pygame.Vector2(100, 1).distance_to(pygame.Vector2(10, 350))
	b = a < (10 + 10)


def dist_sqr() -> None:
	a = pygame.Vector2(100, 1).distance_squared_to(pygame.Vector2(10, 350))
	b = a < (10 + 10) ** 2




def close() -> None:
	a = tst.abc
	for i in range(10000):
		c = a

def far() -> None:
	for i in range(10000):
		c = tst.abc







if __name__ == "__main__":
	main()
