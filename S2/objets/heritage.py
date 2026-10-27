# Une version miniature de arcade.Sprite, et un Boid qui en hérite.


class Sprite:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"dessiné en ({self.x}, {self.y})")

    def update(self):
        pass  # par défaut, un Sprite ne bouge pas


class Boid(Sprite):
    def __init__(self, x, y, speed):
        super().__init__(x, y)  # Sprite.__init__ range x et y
        self.speed = speed  # ce que Boid ajoute

    def update(self):  # on redéfinit : un Boid avance
        self.x += self.speed


boid = Boid(0, 0, 10)
boid.update()  # trouvée dans Boid
boid.draw()  # pas dans Boid : trouvée dans Sprite
print(isinstance(boid, Sprite))
