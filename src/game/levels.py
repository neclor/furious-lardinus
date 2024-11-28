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
	"height": 128}




b37_0: dict = {
	"size": pygame.Vector2(4 ,4),
	"tile_size": 32,
	"tile_map": [
		[None, None, wall, None,],
		[None, None, wall, None,],
        [wall, wall, wall, None,],
        [None, None, None, wall,],]}

b37_1: dict = {
	"position": pygame.Vector2(),
	"size": 4,
	"tile_size": pygame.Vector2(32, 32),
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
