# ⌨️ À vous : le serpent de T1, rangé dans une classe.
# Écrivez grow, puis complétez les trois méthodes marquées TODO, puis :
#     uv run snake_objet.py
# Tout est juste quand le programme affiche OK.

UP, DOWN, LEFT, RIGHT = (0, -1), (0, 1), (-1, 0), (1, 0)


class Snake:
    def __init__(self, body, direction):
        self.body = body  # une liste de cases ; la tête est à la fin
        self.direction = direction

    def head(self):
        """La case de la tête."""
        return self.body[-1]

    # TODO: à écrire, en entier : la méthode grow, qui reçoit une case (tile) et
    # l'ajoute côté tête, si bien que le serpent s'allonge d'une case

    def next_head(self):
        """La case où arrivera la tête, sans rien modifier."""
        # TODO: à écrire (indice : self.head() et self.direction)

    def move(self):
        """Avance d'une case : la tête gagne une case, la queue en perd une."""
        # TODO: à écrire

    def turn(self, direction):
        """Prend la nouvelle direction, sauf si c'est un demi-tour."""
        # TODO: à écrire


# --- les vérifications ---------------------------------------------------------
# assert condition, "message" : si la condition est vraie, rien ne se passe ;
# si elle est fausse, Python s'arrête net : AssertionError: message.

short = Snake([(1, 1)], RIGHT)
short.grow((2, 1))
assert short.body == [(1, 1), (2, 1)], "grow"

snake1 = Snake([(10, 15), (11, 15), (12, 15)], RIGHT)
assert snake1.head() == (12, 15), "head"
assert snake1.next_head() == (13, 15), "next_head"
assert snake1.body == [(10, 15), (11, 15), (12, 15)], "next_head ne doit rien modifier"

snake1.move()
assert snake1.body == [(11, 15), (12, 15), (13, 15)], "move"

snake1.turn(LEFT)
assert snake1.direction == RIGHT, "pas de demi-tour"
snake1.turn(UP)
assert snake1.direction == UP, "turn"

# deux serpents, chacun ses données : plus de mélange possible
snake2 = Snake([(0, 0), (1, 0)], RIGHT)
snake2.move()
assert snake2.body == [(1, 0), (2, 0)], "move, sur snake2"
assert snake1.body == [(11, 15), (12, 15), (13, 15)], "snake1 n'a pas bougé"

print("OK")
