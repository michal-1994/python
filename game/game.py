import pygame

pygame.init()

# VARIABLES
CUBE_SIZE = 25
CUBE_NUM = 20
WIDTH = CUBE_SIZE * CUBE_NUM

# COLORS
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# SETTING GAME
screen = pygame.display.set_mode((WIDTH, WIDTH))
screen.fill(WHITE)

pygame.display.update()

def draw_snake_part(x, y):
	part_position = (x * CUBE_SIZE, y * CUBE_SIZE, CUBE_SIZE, CUBE_SIZE)

	pygame.draw.rect(screen, GREEN, part_position)
	pygame.display.update()

def draw_food(x, y):
	radius = float(CUBE_SIZE) / 2
	food_position = (x * CUBE_SIZE + radius, y * CUBE_SIZE + radius)

	pygame.draw.circle(screen, GREEN, food_position, radius)
	pygame.display.update()

draw_food(0, 0)
draw_food(13, 16)
draw_food(10, 10)
draw_food(12, 8)
draw_food(18, 18)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
