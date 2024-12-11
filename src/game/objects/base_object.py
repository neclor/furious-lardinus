import pygame


import game.game as Game


def new(position: pygame.Vector2 = pygame.Vector2()) -> dict:
	base_object: dict = {
		"group": "Object",
		"class": "BaseObject",
		"has_collision": False,

		"position": position,
		"radius": 4,

		"position_z": 0.0,
		"height": 16,

		"sprite": None,
		#"animation": [],
		#"frame_index": 0,
		#"frames_number": 0,
		#"frame_time": 1,
		#"frame_time_left": 1,
	}
	return base_object


#def animate(self: dict, delta: float) -> None: #TODO add animations
	#pass


def overlaps_object(self: dict, game_object: dict) -> bool:
	return self["position"].distance_to(game_object["position"]) < self["radius"] + game_object["radius"]


def free(self: dict) -> None:
	Game.object_container.remove(self)
