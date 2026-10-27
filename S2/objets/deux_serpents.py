# En procédural, chaque serpent, ce sont deux variables qu'il faut passer partout.
# Pour le duel du tournoi, il en faut deux…

RIGHT, LEFT = (1, 0), (-1, 0)


def next_head(snake, direction):
    x, y = snake[-1]
    dx, dy = direction
    return (x + dx, y + dy)


def move(snake, direction):
    snake.append(next_head(snake, direction))
    snake.pop(0)


snake1, direction1 = [(1, 5), (2, 5)], RIGHT
snake2, direction2 = [(9, 7), (8, 7)], LEFT

move(snake1, direction1)
move(snake2, direction1)  # ⚠️ oups : la direction de l'autre serpent
print(snake1)
print(snake2)
