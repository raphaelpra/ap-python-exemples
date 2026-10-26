def grow(snake, tile):
    snake.append(tile)

s = [(1, 1)]
t = grow(s, (2, 1))
print(s, t)
