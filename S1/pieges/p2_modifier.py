def grow(snake, tile):
    return snake.append(tile)

s = [(1, 1)]
t = grow(s, (2, 1))
print(f"{s=}")
print(f"{t=}")
