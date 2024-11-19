import pygame


textures: list = []





wall: dict = {
	"collision": True,
	"texture": pygame.image.load("src/assets/sprites/wall_32.png"),
	"position_z": 16,
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
	"size": 4,
	"tile_size": 32,
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
