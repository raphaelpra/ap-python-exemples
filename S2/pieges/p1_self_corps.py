class Snake:
    def __init__(self, body):
        self.body = body

    def grow(self, tile):
        body.append(tile)


snake1 = Snake([(1, 1)])
print("créé")
snake1.grow((2, 1))
print(snake1.body)
