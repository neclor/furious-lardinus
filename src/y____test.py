import math
import pygame
import timeit
import random

import settings as Settings
import y____test2 as tst

# TODO: Delete this file
window: pygame.Surface

abc = tst.abc
b = 100

result_int: int = 0
result_float: float = 0

angl: float = 0.33



print(314252.3423 // 1)

print(abs(0.3 - max(0, -1)) % 1)
print(abs(0.3 + min(0, 1)) % 1)

def main() -> None:
	init()
	lst = [1, 2, 3]

	print(timeit.timeit(ints, number = 100000))
	print(result_float)
	print(timeit.timeit(floats, number = 100000))
	print(result_float)



def init() -> None:
	global window
	window = pygame.display.set_mode((1280, 1024))

	for i in range(10000):
		objects.append(create_base_obj())
		objects.append(create_not_base_obj())

		base_objects.append(create_base_obj())
		not_base_objects.append(create_not_base_obj())


def angle_sum() -> None:
	global result_float
	result_float = 0
	for _ in range(10000):
		result_float += tst.angl


def angle_mul() -> None:
	global result_float
	result_float = 0
	for i in range(10000):
		result_float = i * tst.angl


def without_if() -> None:
	global result_int
	a = random.randint(-1, 1) < 0
	result_int += a


def with_if() -> None:
	global result_int
	a = 1 if random.randint(-1, 1) < 0 else 0
	result_int += a


def new_vector_empty() -> None:
	a = pygame.Vector2()


def new_vector_zero() -> None:
	a = pygame.Vector2(0.0, 0.0)


def ints() -> None:
	global result_int
	result_int = random.randint(0, 100)
	for i in range(1, 100):
		result_int = result_int * -2


def floats() -> None:
	global result_float
	result_float = random.random()
	for i in range(1, 100):
		result_float = result_float * -2.2


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
