from position import Position
from direction import Direction
from random import randint

# VARIABLES
INITIAL_SNAKE = [
    Position(1, 2),
    Position(2, 2),
    Position(3, 2)
]
INITIAL_DIRECTION = Direction.RIGHT

class GameState:
    def __init__(self, snake = None, direction = INITIAL_DIRECTION, food = None, field_size = 20):

        if snake is None:
            snake = INITIAL_SNAKE[:]

        self.snake = snake
        self.direction = direction
        self.field_size = field_size

        if food is None:
            self.set_random_food_position()
        else:
            self.food = food

    def set_initial_position(self):
        self.snake = INITIAL_SNAKE
        self.direction = INITIAL_DIRECTION
        self.set_random_food_position()

    def next_head(self, direction):
        pos = self.snake[-1]
        if direction == Direction.UP:
            return Position(
                pos.x,
                (pos.y - 1) % self.field_size
            )
        elif direction == Direction.DOWN:
            return Position(
                pos.x,
                (pos.y + 1) % self.field_size
            )
        elif direction == Direction.RIGHT:
            return Position(
                (pos.x + 1) % self.field_size,
                pos.y
            )
        elif direction == Direction.LEFT:
            return Position(
                (pos.x - 1) % self.field_size,
                pos.y
            )

    def set_random_food_position(self):
        self.food = Position(
            randint(0, self.field_size - 1),
            randint(0, self.field_size - 1)
        )
        if self.food in self.snake:
            self.set_random_food_position()

    def step(self):
        new_head = self.next_head(self.direction)

        collision = new_head in self.snake

        if collision:
            self.set_initial_position()
            return

        self.snake.append(new_head)

        if new_head == self.food:
            self.set_random_food_position()
        else:
            self.snake = self.snake[1:]
