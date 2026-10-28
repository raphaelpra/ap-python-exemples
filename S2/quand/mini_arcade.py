# Une « bibliothèque de jeu » en quelques lignes : c'est elle qui a la boucle.
import time


# --- ce que fournit la bibliothèque --------------------------------------------


class Window:
    def on_update(self, delta_time):
        pass  # ne fait rien : à vous de la redéfinir

    def on_draw(self):
        pass


def run(window, fps=2, seconds=3):
    """La boucle de jeu : c'est elle qui appelle les méthodes de window."""
    last = time.perf_counter()
    for _ in range(fps * seconds):
        time.sleep(1 / fps)
        now = time.perf_counter()
        window.on_update(now - last)
        last = now
        window.on_draw()


# --- votre code : vous ne faites que redéfinir des méthodes -------------------


class MyWindow(Window):
    def on_update(self, delta_time):
        print(f"on_update({delta_time:.2f})")

    def on_draw(self):
        print("on_draw")


print("avant run")
run(MyWindow())  # ici, on donne la fenêtre à run ; arcade.run(), lui, la retrouve seul
print("après run")
