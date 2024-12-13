import pygame

# TODO: Delete this file
abc = 100
angl: float = 0.33


matrix: list[list[int]] = [
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
]



def bez_alg() -> None:
	global matrix
	start_x = 0
	start_y = 0
	end_x = 7
	end_y = 0

	dx = abs(end_x - start_x)
	dy = abs(end_y - start_y)
	sx = 1 if start_x < end_x else -1
	sy = 1 if start_y < end_y else -1

	err = dx - dy

	x = start_x
	y = start_y

	while True:
		matrix[y][x] = 1
		if x == end_x and y == end_y: break
		print(x, y)
		print(err)
		if err >= 0:
			err -= dy
			x += sx
		if err <= 0:
			err += dx
			y += sy

	for row in matrix:
		print(row)

bez_alg()
