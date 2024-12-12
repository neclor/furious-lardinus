import pygame


import main_state_machine as StateMachine
import settings as Settings
import core.events as Events


MAIN_MENU = 0
MENU_SETTINGS = 1

button_action: list[int] = [] # index represents button position, int represents the actions to take in action()
surface: pygame.Surface
images: dict
menu_state = MAIN_MENU
selected: int = 1

def enter() -> None:
	init()

def init() -> None:
	global surface, images
	pygame.mouse.set_visible(True)
	pygame.event.set_grab(False)
	surface = pygame.display.get_surface()
	images = load_images()
	pygame.key.set_repeat(200, 200)

def load_images():
	images: dict = {}
	title_font = pygame.font.Font("src/assets/fonts/Pixel Game.otf", 200)
	button_font = pygame.font.Font("src/assets/fonts/Pixel Game.otf", 80)
	big_button_font = pygame.font.Font("src/assets/fonts/Pixel Game.otf", 120)
	images['bg'] = pygame.image.load("src/assets/sprites/menu/BG.png")
	images['bg'] = pygame.transform.scale(images['bg'], Settings.resolution)
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

def update(delta: float) -> None:
	menu_state_machine(menu_state)


def draw(bg: tuple[str, tuple[int, int]], title: tuple[str, tuple[int, int]], buttons: list[tuple[str, tuple[int, int]]]):
	global surface
	draw_image(bg)
	draw_image(title)
	button_count = 0
	for button in buttons:
		if button_count == selected:
			draw_image((button[0]+'selected', button[1]))
		else:
			draw_image(button)
		button_count += 1
	pygame.display.update()

def draw_image(image_info: tuple[str, tuple[int, int]]):
	global surface
	surface.blit(images[image_info[0]], position_image(image_info[1], images[image_info[0]].get_size()))

def button_init():
	pass

def action(action: int):
	global menu_state
	match action:
		case 0: StateMachine.change_state(1) 						# play
		case 1: menu_state = MENU_SETTINGS 							# settings
		case 2: pygame.event.post(pygame.event.Event(pygame.QUIT))	# quit
		case 3: print("sound")										# sound
		case 4: menu_state = MAIN_MENU

def input_menu(button_number: int):
	global selected
	events = Events.get()
	for event in events:
		if event.type == pygame.KEYDOWN:
			if event.key == Settings.move_forward:
				selected -= 1
			if event.key == Settings.move_backward:
				selected += 1
			if event.key == pygame.K_RETURN:
				action(button_action[selected])
	selected = selected % button_number


def menu_state_machine(state: int):
	match state:
		case 0: main_menu()
		case 1: settings_menu()

def main_menu():
	global button_action
	button_action = [0, 1, 2]
	input_menu(3)
	bg = ('bg', Settings.half_resolution)
	title = ('title', (Settings.half_resolution[0], 200))
	buttons = [
		('play', (Settings.half_resolution[0], 400)),
		('settings', (Settings.half_resolution[0], 500)),
		('quit', (Settings.half_resolution[0], 600)),
	]
	draw(bg, title, buttons)

def settings_menu():
	global button_action
	button_action = [3, 4]
	input_menu(2)
	bg = ('bg', Settings.half_resolution)
	title = ('settings', (Settings.half_resolution[0], 200))
	buttons = [
		('sound', (Settings.half_resolution[0], 400)),
		('return', (Settings.half_resolution[0], 500)),
	]
	draw(bg, title, buttons)

def position_image(position: tuple[int, int], dimensions: tuple[int, int]):
	return (position[0] - dimensions[0] / 2, position[1] - dimensions[1] / 2)

def exit() -> None:
	pass
