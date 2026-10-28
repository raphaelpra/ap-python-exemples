# Un Sprite miniature, et un Boid qui en hérite, à essayer dans la console :
#     uv run python -i boid_jouet.py
# Puis écrivez dans Boid une méthode update qui ajoute 10 à self.x, et relancez.


class Sprite:  # une version miniature de arcade.Sprite
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"dessiné en ({self.x}, {self.y})")

    def update(self):
        pass  # par défaut, un Sprite ne bouge pas


class Boid(Sprite):
    pass  # n'écrit rien, pour l'instant
