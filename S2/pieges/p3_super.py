class Sprite:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"dessiné en ({self.x}, {self.y})")


class Boid(Sprite):
    def __init__(self, x, y, speed):
        self.speed = speed


boid = Boid(0, 0, 10)
print("créé")
boid.draw()
