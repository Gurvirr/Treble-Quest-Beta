import pygame as py
from tile_map import map

# Pygame setup
py.init()

clock = py.time.Clock()

# COLOURS
bg_colour = (110, 121, 228)
sky_colour = (190, 220, 255)
start_colour = (225, 225, 225)

screen_width = 1280
screen_height = 720
screen = py.display.set_mode((screen_width, screen_height))

p_sprite = py.image.load("plant_drone.png")
p_rect = p_sprite.get_rect()
p_rect.centery = screen_height - 32

grass_block = py.image.load("grass_block.png")
dirt_block = py.image.load("dirt_block.png")

# def collisions(rect, tiles):
# 	collider_list = []
# 	for tile in tiles:
# 		if rect.colliderect(tile):
# 			collider_list.append(tile)
# 	return collider_list
#
# def move(rect, movement, tiles):
# 	collision_types = {"top": False, "bottom": False, "right": False, "left": False}
#
# 	rect.x += movement[0]
# 	collider_list = collisions(rect, tile)
# 	for tile in collider_list:
# 		if movement[0] > 0:
# 			rect.right = tile.left
# 			collision_types["right"] = True
# 		elif movement[0] < 0:
# 			rect.left = tile.right
# 			collision_types["left"] = True
#
# 	rect.y += movement[1]
# 	collider_list = collisions(rect, tile)
# 	for tile in collider_list:
# 		if movement[1] > 0:
# 			rect.bottom = tile.top
# 			collision_types["bottom"] = True
# 		elif movement[1] < 0:
# 			rect.top = tile.bottom
# 			collision_types["top"] = True
#
# 	return rect, collision_types

# MAIN MENU
def menu():
	py.display.set_caption("Game Menu")
	while True:
		start()
		py.display.update()
		clock.tick(60)

# START OPTION (BLINKING TEXT)
def start():
	start_font = py.font.Font('Halogen.otf', 50)

	bg = py.image.load("GM Treble Quest V2.png")
	bg_rect = py.Rect((0, 0), bg.get_size())
	screen.blit(bg, bg_rect)

	n = 0
	while True:
		start = start_font.render(("Press Enter To Play"), True, start_colour)

		if n % 2 == 0:
			screen.blit(start, (450, 625))
			clock.tick(50000)

		else:
			screen.blit(bg, bg_rect)
		n += 0.5

		py.display.update()
		clock.tick(3)

		for event in py.event.get():
			if event.type == py.QUIT:
				exit()

			elif event.type == py.KEYDOWN:
				if event.key == py.K_RETURN:
					play()

# GAME
def play():
	py.display.set_caption("Treble Quest")
	player_y, player_x = p_rect.bottom, 32

	velocity_x, velocity_y = 5, 0
	ground = 480
	gravity_factor = 0.35
	acl_factor = -12

	while True:
		clock.tick(100)
		vertical_acl = gravity_factor
		screen.fill(sky_colour)
		screen.blit(p_sprite, p_rect)

# TILE MAP
		tile_collisions = []
		y = 0
		for row in map:
			x = 0
			for tile in row:
				if tile == 1:
					screen.blit(dirt_block, (x * 32, y * 32))
				if tile == 2:
					screen.blit(grass_block, (x * 32, y * 32))
				if tile != 0:
					tile_collisions.append(py.Rect(x * 32, y * 32, 32, 32))
				x += 1
			y += 1

		screen.blit(p_sprite, p_rect)

#	player_movement = [0, 0]
#		if moving_right == True:
#			player_movement[0] += 2
#		if moving_left == True:
#			player_movement[0] -= 2
#		player_movement[1] += player

# MOVEMENT
		for event in py.event.get():
			if event.type == py.QUIT:
				exit()

			if event.type == py.KEYDOWN:
				if velocity_y == 0 and event.key == py.K_w:
					vertical_acl = acl_factor

		velocity_y += vertical_acl
		player_y += velocity_y

		if player_y > ground:
			player_y = ground
			velocity_y = 0
			vertical_acl = 0

		p_rect.bottom = round(player_y)

		keys = py.key.get_pressed()

		player_x += (keys[py.K_d] - keys[py.K_a]) * velocity_x
		p_rect.centerx = player_x

		py.display.update()

menu()
