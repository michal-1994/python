import pygame
from position import Position

pygame.init()

# VARIABLES
CUBE_SIZE = 25
CUBE_NUM = 20
WIDTH = CUBE_SIZE * CUBE_NUM

snake = [
	Position(2, 2),
	Position(3, 2),
	Position(4, 2),
	Position(5, 2),
	Position(5, 1)
]

food = Position(11, 14)

# COLORS
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# SETTING GAME
screen = pygame.display.set_mode((WIDTH, WIDTH))
screen.fill(WHITE)

def draw_snake_part(pos):
	part_position = (pos.x * CUBE_SIZE, pos.y * CUBE_SIZE, CUBE_SIZE, CUBE_SIZE)
	pygame.draw.rect(screen, GREEN, part_position)

def draw_snake(snake):
    for part in snake:
        draw_snake_part(part)

def draw_food(pos):
	radius = float(CUBE_SIZE) / 2
	food_position = (pos.x * CUBE_SIZE + radius, pos.y * CUBE_SIZE + radius)
	pygame.draw.circle(screen, BLUE, food_position, radius)

def fill_bg():
	screen.fill(WHITE)

def draw(snake, food):
    fill_bg()
    draw_snake(snake)
    draw_food(food)
    pygame.display.update()

draw(snake, food)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
