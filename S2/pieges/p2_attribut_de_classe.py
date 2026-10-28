class Snake:
    body = []

    def grow(self, tile):
        self.body.append(tile)


snake1 = Snake()
snake2 = Snake()
snake1.grow((1, 1))
print(f"{snake1.body=}")
print(f"{snake2.body=}")
