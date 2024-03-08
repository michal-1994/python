import pygame
from position import Position
from direction import Direction
from game_state import GameState

# VARIABLES
CUBE_SIZE = 25
CUBE_NUM = 20
WIDTH = CUBE_SIZE * CUBE_NUM

# COLORS
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

pygame.init()

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


state = GameState(
	snake = None,
	direction = None,
	food = None,
	field_size = CUBE_NUM
)

state.set_initial_position()

clock = pygame.time.Clock()

while True:
	clock.tick(10)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				state.direction = Direction.LEFT

			elif event.key == pygame.K_RIGHT:
				state.direction = Direction.RIGHT

			elif event.key == pygame.K_UP:
				state.direction = Direction.UP

			elif event.key == pygame.K_DOWN:
				state.direction = Direction.DOWN

		state.step()
		draw(state.snake, state.food)
