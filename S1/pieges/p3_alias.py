RIGHT = (1, 0)

def move(snake, direction, fruit):
    """Avance le serpent d'une case, sur place ; il grandit s'il mange le fruit."""
    x, y = snake[-1]
    dx, dy = direction
    head = (x + dx, y + dy)
    snake.append(head)
    if head != fruit:
        snake.pop(0)

start = [(10, 15), (11, 15), (12, 15)]
snake = start
move(snake, RIGHT, (0, 0))
print(start)
