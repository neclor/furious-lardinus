import pygame
import timeit

import test2 as tst

# TODO: Delete this file
window: pygame.Surface

abc = tst.abc
b = 100





def create_base_obj() -> dict:
	return {
		"class": "base_obj"
	}


def create_not_base_obj() -> dict:
	return {
		"class": "not_base_obj"
	}



objects: list[dict] = []

base_objects: list[dict] = []
not_base_objects: list[dict] = []




def main() -> None:
	init()
	lst = [1, 2, 3]
	print(timeit.timeit(objects_separate, number = 1000))
	print(timeit.timeit(all_objects, number = 1000))


def init() -> None:
	global window
	window = pygame.display.set_mode((1280, 1024))

	for i in range(10000):
		objects.append(create_base_obj())
		objects.append(create_not_base_obj())

		base_objects.append(create_base_obj())
		not_base_objects.append(create_not_base_obj())




def objects_separate() -> None:
	a = 0
	b = 0
	for obj in base_objects:
		a += 1
	for obj in not_base_objects:
		b += 1


def all_objects() -> None:
	a = 0
	b = 0
	for obj in objects:
		match obj["class"]:
			case "base_obj":
				a += 1
			case "not_base_obj":
				b += 1
			case "a":
				b += 1
			case "b":
				b += 1
			case "c":
				b += 1




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
	a = abc
	a = abc

def far() -> None:
	a = tst.abc
	a = tst.abc


if __name__ == "__main__":
	main()
