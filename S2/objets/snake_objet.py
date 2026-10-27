# ⌨️ À vous : le serpent de T1, rangé dans une classe.
# Complétez les méthodes marquées « à écrire », puis : uv run snake_objet.py
# Tout est juste quand le programme affiche OK.

UP, DOWN, LEFT, RIGHT = (0, -1), (0, 1), (-1, 0), (1, 0)


class Snake:
    def __init__(self, body, direction):
        self.body = body  # une liste de cases ; la tête est à la fin
        self.direction = direction

    def head(self):
        """La case de la tête."""
        return self.body[-1]

    def next_head(self):
        """La case où arrivera la tête, sans rien modifier."""
        ...  # à écrire (indice : self.head() et self.direction)

    def move(self):
        """Avance d'une case : la tête gagne une case, la queue en perd une."""
        ...  # à écrire

    def turn(self, direction):
        """Prend la nouvelle direction, sauf si c'est un demi-tour."""
        ...  # à écrire


# --- les vérifications ---------------------------------------------------------

s = Snake([(10, 15), (11, 15), (12, 15)], RIGHT)
assert s.head() == (12, 15)
assert s.next_head() == (13, 15), "next_head"
assert s.body == [(10, 15), (11, 15), (12, 15)], "next_head ne doit rien modifier"

s.move()
assert s.body == [(11, 15), (12, 15), (13, 15)], "move"

s.turn(LEFT)
assert s.direction == RIGHT, "pas de demi-tour"
s.turn(UP)
assert s.direction == UP, "turn"

# deux serpents, chacun ses données : plus de mélange possible
other = Snake([(0, 0), (1, 0)], RIGHT)
other.move()
assert other.body == [(1, 0), (2, 0)]
assert s.body == [(11, 15), (12, 15), (13, 15)], "s n'a pas bougé"

print("OK")
