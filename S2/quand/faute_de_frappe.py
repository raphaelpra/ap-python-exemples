# La même mini-bibliothèque, mais une faute de frappe dans votre code.
import time


class Window:
    def on_update(self, delta_time):
        pass

    def on_draw(self):
        pass


def run(window, fps=2, seconds=2):
    for _ in range(fps * seconds):
        time.sleep(1 / fps)
        window.on_update(1 / fps)
        window.on_draw()


class MyWindow(Window):
    def on_update(self, delta_time):
        print("on_update")

    def on_drow(self):
        print("on_draw")


run(MyWindow())
