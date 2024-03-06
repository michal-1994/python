from position import Position
from direction import Direction

class GameState:
    def __init__(self, snake, direction, food, field_size):
        self.snake = snake
        self.direction = direction
        self.food = food
        self.field_size = field_size

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
