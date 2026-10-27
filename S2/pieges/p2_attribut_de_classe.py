class Snake:
    body = []

    def grow(self, tile):
        self.body.append(tile)


a = Snake()
b = Snake()
a.grow((1, 1))
print(f"{a.body=}")
print(f"{b.body=}")
