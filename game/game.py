import pygame
from position import Position

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

snake = [
	Position(2, 2),
	Position(3, 2),
	Position(4, 2),
	Position(5, 2),
	Position(5, 1)
]

food = Position(11, 14)

pygame.display.update()

def draw_snake_part(pos):
	part_position = (pos.x * CUBE_SIZE, pos.y * CUBE_SIZE, CUBE_SIZE, CUBE_SIZE)

	pygame.draw.rect(screen, GREEN, part_position)
	pygame.display.update()

def draw_food(pos):
	radius = float(CUBE_SIZE) / 2
	food_position = (pos.x * CUBE_SIZE + radius, pos.y * CUBE_SIZE + radius)

	pygame.draw.circle(screen, GREEN, food_position, radius)
	pygame.display.update()

def draw_snake(snake):
    for part in snake:
        draw_snake_part(part)

draw_snake(snake)
draw_food(food)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
