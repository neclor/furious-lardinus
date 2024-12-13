import sys
import math
import pygame


# ----------------------------------------------------CORE
Events_events: list[pygame.event.Event] = []
def Events_update() -> None:
	global Events_events
	Events_events = pygame.event.get()
def Events_get() -> list[pygame.event.Event]:
	return Events_events
#------------------------------------------------------SETTINGS
# Config
Settings_NAME: str = "Furious Lardinus"
# Dispaly
Settings_resolution: tuple[int, int] = (2 * 640, 2 * 360)
Settings_fps: int = 60
# Game settings
Settings_camera_sensitivity: float = 1.0
Settings_fov_h: float = math.tau / 3
# Input
Settings_full_screen: int = pygame.K_F11
Settings_pause: int = pygame.K_ESCAPE
Settings_move_forward: int = pygame.K_w
Settings_move_backward: int = pygame.K_s
Settings_move_left: int = pygame.K_a
Settings_move_right: int = pygame.K_d
Settings_gun: int = pygame.K_1
Settings_shotgun: int = pygame.K_2
Settings_assault: int = pygame.K_3
# Advanced
Settings_MIN_FOV_H: float = math.pi / 3
Settings_MAX_FOV_H: float = math.tau / 3
Settings_fps_amplitude: int = 20
Settings_current_fps: float = Settings_fps
# Collision layers
Settings_WALL: int = 1
Settings_OBSTACLE: int = 2
Settings_ACTIVE: int = 4
Settings_ENEMY: int = 8
Settings_PLAYER: int = 16
Settings_PROJECTILE: int = 32
# Calculated parameters
Settings_half_resolution: tuple[int, int]
Settings_aspect_ratio: float
Settings_max_fps_limit: int
Settings_tick_fps: int
Settings_fov_v: float
Settings_half_fov_h: float
Settings_half_fov_v: float
Settings_tan_half_fov_h: float
Settings_tan_half_fov_v: float
Settings_double_tan_half_fov_h: float
Settings_double_tan_half_fov_v: float
Settings_resolution_x_div_double_tan_half_fov_h: float
Settings_resolution_y_div_double_tan_half_fov_v: float
# Math
Settings_HALF_PI: float = math.pi / 2
Settings_THREE_HALF_PI: float = 3 * Settings_HALF_PI
def calculate_resolution_parameters() -> None:
	global Settings_half_resolution, Settings_aspect_ratio
	Settings_half_resolution = (Settings_resolution[0] // 2, Settings_resolution[1] // 2)
	Settings_aspect_ratio = Settings_resolution[0] / Settings_resolution[1]
	calculate_fov_parameters()
def calculate_fov_parameters() -> None:
	global Settings_fov_h, Settings_fov_v, Settings_half_fov_h, Settings_half_fov_v, Settings_tan_half_fov_h, Settings_tan_half_fov_v, Settings_double_tan_half_fov_h, Settings_double_tan_half_fov_v, Settings_resolution_x_div_double_tan_half_fov_h, Settings_resolution_y_div_double_tan_half_fov_v
	Settings_fov_h = pygame.math.clamp(Settings_fov_h, Settings_MIN_FOV_H, Settings_MAX_FOV_H)
	Settings_fov_v = 2 * math.atan(math.tan(Settings_fov_h / 2) / Settings_aspect_ratio)
	Settings_half_fov_h = Settings_fov_h / 2
	Settings_half_fov_v = Settings_fov_v / 2

	Settings_tan_half_fov_h = math.tan(Settings_half_fov_h)
	Settings_tan_half_fov_v = math.tan(Settings_half_fov_v)
	Settings_double_tan_half_fov_h = Settings_tan_half_fov_h * 2
	Settings_double_tan_half_fov_v = Settings_tan_half_fov_v * 2
	Settings_resolution_x_div_double_tan_half_fov_h = Settings_resolution[0] / Settings_double_tan_half_fov_h
	Settings_resolution_y_div_double_tan_half_fov_v = Settings_resolution[1] / Settings_double_tan_half_fov_v
def calculate_fps_parameters() -> None:
	global Settings_max_fps_limit, Settings_tick_fps
	Settings_max_fps_limit = Settings_fps + Settings_fps_amplitude
	Settings_tick_fps = Settings_fps + 2 * Settings_fps_amplitude
calculate_resolution_parameters()
calculate_fps_parameters()
#---------------------------------------------------------------------

Main_clock: pygame.time.Clock


def Main_main() -> None:
	Main_init()
	Main_run()


def Main_init() -> None:
	global Main_clock
	pygame.init()
	pygame.display.set_mode(Settings_resolution, pygame.SCALED)
	pygame.display.set_caption(Settings_NAME)
	Main_clock = pygame.time.Clock()
	StateMachine_init()


def Main_run() -> None:
	while True:
		Main_update()
		Events_update()
		Main_check_events()
		StateMachine_update(Main_clock.get_time() / 1000)
		pygame.display.set_caption(str(int(Main_clock.get_fps())))


def Main_update():
	Main_clock.tick(Settings_tick_fps)
	Settings_current_fps = Main_clock.get_fps()


def Main_check_events() -> None:
	for event in Events_get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == Settings_full_screen:
				pygame.display.toggle_fullscreen()

#______________________________________________________________________________________________________STATEMACHINE
# States = {
StateMachine_MENU: int = 0
StateMachine_GAME: int = 1
# }
StateMachine_INITIAL_STATE: int = StateMachine_MENU
StateMachine_state: int = -1


def StateMachine_init() -> None:
	StateMachine_change_state(StateMachine_INITIAL_STATE)


def StateMachine_update(delta: float) -> None:
	match StateMachine_state:
		case 0: menu_update(delta)
		case 1: Game_update(delta)


def StateMachine_change_state(new_state: int) -> None:
	global StateMachine_state
	if (new_state == StateMachine_state) or not (0 <= new_state <= 1): return

	match StateMachine_state:
		case 0: menu_exit()
		case 1: Game_exit()

	StateMachine_state = new_state

	match new_state:
		case 0: menu_enter()
		case 1: Game_enter()


#____________________________________________________________________________MENU
MAIN_MENU: int = 0
MENU_SETTINGS: int = 1


button_action: list[int] = [] # index represents button position, int represents the actions to take in action()
surface: pygame.Surface
menu_images: dict
menu_state: int = MAIN_MENU
selected: int = 1
settings_temp: int = 0


def menu_enter() -> None:
	menu_init()


def menu_init() -> None:
	global surface, menu_images
	pygame.mouse.set_visible(True)
	pygame.event.set_grab(False)
	surface = pygame.display.get_surface()
	menu_images = menu_load_images()
	pygame.key.set_repeat(200, 200)


def menu_load_images() -> dict:
	images: dict = {}
	title_font = pygame.font.Font("src/assets/fonts/Pixel_Game.otf", 200)
	button_font = pygame.font.Font("src/assets/fonts/Pixel_Game.otf", 80)
	big_button_font = pygame.font.Font("src/assets/fonts/Pixel_Game.otf", 120)
	images['bg'] = pygame.image.load("src/assets/sprites/menu/BG.png")
	images['bg'] = pygame.transform.scale(images['bg'], Settings_resolution)
	images['title'] = title_font.render("furious lardinus", True, (0, 0, 0))
	images['settings'] = title_font.render("Settings", True, (0, 0, 0))
	images['play'] = button_font.render("Play", True, (255, 255, 255))
	images['playselected'] = big_button_font.render("Play", True, (0, 255, 0))
	images['settings'] = button_font.render("Settings", True, (255, 255, 255))
	images['settingsselected'] = big_button_font.render("Settings", True, (0, 255, 0))
	images['quit'] = button_font.render("quit", True, (255, 255, 255))
	images['quitselected'] = big_button_font.render("quit", True, (0, 255, 0))
	images['sound'] = button_font.render("Sound", True, (255, 255, 255))
	images['soundselected'] = big_button_font.render("Sound", True, (0, 255, 0))
	images['return'] = button_font.render("return", True, (255, 255, 255))
	images['returnselected'] = big_button_font.render("return", True, (0, 255, 0))
	return images


def menu_update(delta: float) -> None:
	menu_state_machine(menu_state)


def menu_draw(bg: tuple[str, tuple[int, int]], title: tuple[str, tuple[int, int]], buttons: list[tuple[str, tuple[int, int]]]):
	global surface
	menu_draw_image(bg)
	menu_draw_image(title)
	button_count = 0
	for button in buttons:
		if button_count == selected:
			menu_draw_image((button[0]+'selected', button[1]))
		else:
			menu_draw_image(button)
		button_count += 1
	pygame.display.update()


def menu_draw_image(image_info: tuple[str, tuple[int, int]]):
	global surface
	surface.blit(menu_images[image_info[0]], menu_position_image(image_info[1], menu_images[image_info[0]].get_size()))


def menu_position_image(position: tuple[int, int], dimensions: tuple[int, int]):
	return (position[0] - dimensions[0] / 2, position[1] - dimensions[1] / 2)


def menu_action(action: int) -> None:
	global menu_state
	match action:
		case 0: StateMachine_change_state(1) 						# play
		case 1: menu_state = MENU_SETTINGS 							# settings
		case 2: pygame.event.post(pygame.event.Event(pygame.QUIT))	# quit
		case 3: print("sound")										# sound
		case 4: menu_state = MAIN_MENU								# return to main menu
		case 5: menu_increase_temp()										# increase temporary variable for settings change
		case 6: menu_decrease_temp()										# decrease temporary variable for settings change


def menu_increase_temp() -> None:
	global settings_temp
	settings_temp += 1


def menu_decrease_temp() -> None:
	global settings_temp
	settings_temp -= 1


def menu_input(button_number: int) -> None:
	global selected
	events = Events_get()
	for event in events:
		if event.type == pygame.KEYDOWN:
			if event.key == Settings_move_forward:
				selected -= 1
			if event.key == Settings_move_backward:
				selected += 1
			if event.key == pygame.K_RETURN:
				menu_action(button_action[selected])
	selected = selected % button_number


def menu_state_machine(state: int) -> None:
	match state:
		case 0: menu_main()
		case 1: menu_settings()


def menu_main() -> None:
	global button_action
	button_action = [0, 1, 2]
	menu_input(3)
	bg = ('bg', Settings_half_resolution)
	title = ('title', (Settings_half_resolution[0], 200))
	buttons = [
		('play', (Settings_half_resolution[0], 400)),
		('settings', (Settings_half_resolution[0], 500)),
		('quit', (Settings_half_resolution[0], 600)),
	]
	menu_draw(bg, title, buttons)


def menu_settings() -> None:
	global button_action
	button_action = [3, 4]
	menu_input(2)
	bg = ('bg', Settings_half_resolution)
	title = ('settings', (Settings_half_resolution[0], 200))
	buttons = [
		('sound', (Settings_half_resolution[0], 400)),
		('return', (Settings_half_resolution[0], 500)),
	]
	menu_draw(bg, title, buttons)


def menu_exit() -> None:
	pass


#-------------------------------------------------------------------------GAME


timer: float
pause: bool


player: dict


def Game_enter() -> None:
	global timer, pause
	timer = 0.0
	pause = False
	mouse_visible(False)
	Display_init()

	start_game()


def toggle_pause() -> None:
	global pause
	pause = not pause
	mouse_visible(pause)


def mouse_visible(visible: bool) -> None:
	pygame.mouse.set_visible(visible)
	pygame.event.set_grab(not visible)


def start_game() -> None:
	global player
	player = Player_new()
	LevelManager_load_level()


def game_over() -> None:
	LevelManager_load_level()
	player["dead"] = False
	player["health"] = player["max_health"]


def Game_update(delta: float) -> None:
	global timer
	if not pause:
		timer += delta
		Weapon_update(delta)
		ObjectManager_update(delta)
	Display_update()
	check_events()


def check_events() -> None:
	for event in Events_get():
		if event.type == pygame.KEYDOWN:
			if event.key == Settings_pause:
				toggle_pause()



def Game_exit() -> None:
	pass


#------------------------------------------------------------ Level Manager



Level_manager_floor_color: pygame.Color

Level_manager_tile_size: pygame.Vector2
Level_manager_tile_map_size: pygame.Vector2
Level_manager_tile_map: list[list[dict | None]]

Level_manager_min_point_z: float
Level_manager_max_point_z: float


levels_list: list[str] = [Levels_TUTORIAL_ROOM, Levels_MIDDLE, Levels_B_37, Levels_END_ROOM]
current_level: int = 0


def next_level() -> None:
	global current_level
	if current_level < len(levels_list) + 1: current_level += 1
	load_level()


def load_level() -> None:
	global floor_color, tile_size, tile_map_size, tile_map, min_point_z, max_point_z

	level_data: dict = parse_level_string(levels_list[current_level], Levels.TILE_SET, Levels.OBJECT_SET)
	floor_color = level_data["floor_color"]
	tile_size = level_data["tile_size"]
	tile_map_size = level_data["tile_map_size"]
	tile_map = level_data["tile_map"]
	min_point_z = level_data["min_point_z"]
	max_point_z = level_data["max_point_z"]

	Game.player["position"] = level_data["spawn_point"]

	ObjectManager.game_objects = [Game.player] + level_data["level_objects"]
	ObjectManager.add_queue = []
	ObjectManager.remove_queue = []


def parse_level_string(string: str, tile_set: dict, object_set: dict) -> dict:
	tile_size: pygame.Vector2 = tile_set["tile_size"]
	tiles: dict = tile_set["tiles"]
	objects: dict = object_set["objects"]

	string = string.replace(" ", "").replace("\t", "").replace("\n", "").replace("\r", "")
	string = string.rstrip("/")
	rows: list[str] = string.split("/")

	name: str = rows[0]
	floor_color: pygame.Color = pygame.Color(rows[1])
	tile_map_size: pygame.Vector2 = pygame.Vector2(len(rows[2]), len(rows) - 2)

	spawn_point: pygame.Vector2 = pygame.Vector2()
	min_point_z: float = 0
	max_point_z: float = 0
	tile_map: list[list[dict | None]] = []
	level_objects: list[dict] = []
	for y, row in enumerate(rows[2:]):
		tile_row: list[dict | None] = []
		for x, char in enumerate(row):
			tile_center_position: pygame.Vector2 = pygame.Vector2(x * tile_size.x + tile_size.x // 2, y * tile_size.y + tile_size.y // 2)
			if char == "S": spawn_point = tile_center_position

			tile: dict | None = tiles.get(char)
			tile_row.append(tile)
			if tile is not None:
				tile_bottom: float = tile["position_z"]
				tile_top: float = tile_bottom - tile["height"]
				min_point_z = min(tile_top, tile_bottom, min_point_z)
				max_point_z = max(tile_top, tile_bottom, max_point_z)

			level_object: dict | None = new_level_object(objects.get(char), tile_center_position)
			if level_object is not None: level_objects.append(level_object)
		tile_map.append(tile_row)
	return {
		"floor_color": floor_color,
		"tile_size": tile_size,
		"tile_map_size": tile_map_size,
		"tile_map": tile_map,
		"min_point_z": min_point_z,
		"max_point_z": max_point_z,
		"spawn_point": spawn_point,
		"level_objects": level_objects,
	}


def new_level_object(class_name: str | None, position: pygame.Vector2) -> dict | None:
	match class_name:
		case "Ammo": return Ammo.new(position)
		case "Medikit": return Medikit.new(position)
		case "Knight": return Knight.new(position)
		case "Skull": return Skull.new(position)
		case "Summoner": return Summoner.new(position)
		case "Wizzard": return Wizzard.new(position)
		case "Exit": return Exit.new(position)
		case "Boss": return Boss.new(position)
	return None























































if __name__ == "__main__":
	Main_main()
