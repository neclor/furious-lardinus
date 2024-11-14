import pygame


textures: list = []





wall: dict = {
    "collision": True,
    "texture_index": 0,
    "position_z": 16,
    "height": 128}


level_1: dict = {
    "size": pygame.Vector2(5, 5),
	"tile_size": 64,
	"tile_map": [
		[wall, wall, wall, wall],
    	[wall, None, None, wall],
    	[wall, None, None, wall],
    	[wall, None, None, wall],
    	[wall, wall, wall, wall]]}


def generate_level() -> dict:
	return {}
