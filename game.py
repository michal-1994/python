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

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()