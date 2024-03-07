from position import Position
from direction import Direction
from random import randint

class GameState:
    def __init__(self, snake, direction, food, field_size):
        self.snake = snake
        self.direction = direction
        self.food = food
        self.field_size = field_size

    def next_head(self, direction):
        pos = self.snake[-1]
        if direction == Direction.UP:
            return Position(pos.x, (pos.y - 1) % self.field_size)
        elif direction == Direction.DOWN:
            return Position(pos.x, (pos.y + 1) % self.field_size)
        elif direction == Direction.RIGHT:
            return Position((pos.x + 1) % self.field_size, pos.y)
        elif direction == Direction.LEFT:
            return Position((pos.x - 1) % self.field_size, pos.y)

    def step(self):
        new_head = self.next_head(self.direction)

        self.snake.append(new_head)

        if new_head == self.food:
            self.set_random_food_position()
        else:
            self.snake = self.snake[1:]

    def set_random_food_position(self):
        self.food = Position(
            randint(0, self.field_size - 1),
            randint(0, self.field_size - 1)
        )
        if self.food in self.snake:
            self.set_random_food_position()
