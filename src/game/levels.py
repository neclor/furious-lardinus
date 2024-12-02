import pygame


textures: list = []



def create_tile_map() -> dict:

	tile_map: dict = {
		"position": pygame.Vector2(),
		"size": pygame.Vector2(),
		"tiles": 1




	}

	return tile_map



wall: dict = {
	"texture": pygame.image.load("src/assets/sprites/wall_32.png"),
	"height": 32}

wakk: dict = {
	"texture": pygame.image.load("src/assets/sprites/wall_32.png"),
	"height": 64}


b37_0: dict = {
	"tile_size": pygame.Vector2(32, 32),
	"tile_map_size": pygame.Vector2(8, 8),
	"tile_map": [
		[None, None, wall, None, None, None, None, None,],
		[None, None, None, wakk, wakk, wakk, wakk, None,],
        [wall, None, None, None, None, None, wakk, None,],
        [wall, None, None, None, wakk, None, wakk, None,],
		[wall, None, wakk, None, None, None, wakk, None,],
		[wall, None, None, None, wakk, wakk, wakk, None,],
		[wall, wall, wall, wall, None, None, None, None,],
		[None, None, None, None, None, None, None, None,],]}

b37_1: dict = {
	"tile_size": pygame.Vector2(32, 32),
	"tile_map_size": pygame.Vector2(4, 4),
	"tile_map": [
		[None, None, None, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall,],
		[None, None, None, wall, None, None, None, None, None, None, None, None, None, None, None, None, None, wall,],
		[None, None, None, wall, None, None, None, None, None, None, None, None, None, None, None, None, None, wall,],
		[None, None, None, wall, None, None, None, None, None, None, None, None, None, None, None, None, None, wall,],
		[None, None, None, wall, None, None, None, None, None, None, None, None, None, None, None, None, None, wall,],
		[None, None, None, wall, None, None, None, None, None, None, None, None, None, None, None, None, None, wall,],
		[wall, wall, wall, wall, None, None, None, None, None, None, None, None, None, None, None, None, None, wall,],
		[wall, None, None, wall, None, None, None, None, None, None, None, None, None, None, None, None, None, wall,],
		[wall, None, None, wall, wall, None, wall, wall, wall, wall, wall, wall, wall, wall, wall, None, wall, wall,],
		[wall, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,],
		[wall, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,],
		[wall, wall, wall, wall, wall, None, wall, wall, wall, wall, wall, wall, None, wall, wall, wall, None, wall,],
		[None, None, None, wall, None, None, None, None, None, None, None, None, None, None, wall, None, None, None,],
		[None, None, None, wall, None, None, None, None, None, None, None, None, None, None, wall, None, None, None,],
		[None, None, None, wall, None, None, None, None, None, None, None, None, None, None, wall, None, None, None,],
		[None, None, None, wall, None, None, None, None, None, None, None, None, None, None, wall, None, None, None,],
		[None, None, None, wall, None, None, None, None, None, None, None, None, None, None, wall, None, None, None,],
		[None, None, None, wall, None, None, None, None, None, None, None, None, None, None, wall, None, None, None,],
		[None, None, None, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall,],]}


def generate_level() -> dict:
	return {}
