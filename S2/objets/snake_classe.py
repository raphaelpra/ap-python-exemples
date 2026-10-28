# La classe Snake de la slide « Des méthodes », à essayer dans la console :
#     uv run python -i snake_classe.py
# -i : Python exécute le fichier, puis garde la console ouverte (sortir : exit()).

UP, DOWN, LEFT, RIGHT = (0, -1), (0, 1), (-1, 0), (1, 0)


class Snake:
    def __init__(self, body, direction):
        self.body = body  # une liste de cases ; la tête est à la fin
        self.direction = direction

    def head(self):  # renvoie une valeur
        return self.body[-1]

    def turn(self, direction):  # modifie l'objet
        dx, dy = direction
        # pas de demi-tour
        if (-dx, -dy) != self.direction:
            self.direction = direction
