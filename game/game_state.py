from position import Position
from direction import Direction

class GameState:
    def __init__(self, snake, direction, food, field_size):
        self.snake = snake
        self.direction = direction
        self.food = food
        self.field_size = field_size

    def next_head(self, direction):
        pos = self.snake[-1]
        if direction == Direction.UP:
            return Position(pos.x, pos.y - 1)
        elif direction == Direction.DOWN:
            return Position(pos.x, pos.y + 1)
        elif direction == Direction.RIGHT:
            return Position(pos.x + 1, pos.y)
        elif direction == Direction.LEFT:
            return Position(pos.x - 1, pos.y)

    def step(self):
        new_head = self.next_head(self.direction)
        self.snake.append(new_head)
        self.snake = self.snake[1:]

# state = GameState(
# 	snake = [
# 		Position(4, 0),
# 		Position(4, 1),
# 		Position(4, 2)
# 	],
# 	direction = Direction.DOWN,
# 	food = Position(10, 10),
# 	field_size = 20
# )

# state.step()

# expected_state = [
# 	Position(4, 1),
# 	Position(4, 2),
# 	Position(4, 3)
# ]

# self.assertEqual(expected_state, state.snake)
