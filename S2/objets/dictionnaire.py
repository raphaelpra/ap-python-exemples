# Première idée : ranger les deux données d'un serpent dans un dictionnaire.
# Chaque serpent emporte sa direction : impossible de passer celle d'un autre.

RIGHT, LEFT = (1, 0), (-1, 0)


def new_snake(body, direction):
    return {"body": body, "direction": direction}


def move(snake):
    x, y = snake["body"][-1]
    dx, dy = snake["direction"]
    snake["body"].append((x + dx, y + dy))
    snake["body"].pop(0)


snake1 = new_snake([(1, 2), (2, 2)], RIGHT)
snake2 = new_snake([(9, 4), (8, 4)], LEFT)
move(snake1)
move(snake2)
print(snake1)
print(snake2)
