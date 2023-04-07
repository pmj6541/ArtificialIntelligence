from matplotlib import pyplot as plt
from celluloid import Camera
from util import Util
import paths


class VisPlot:
    def __init__(self):
        self.board = plt
        self.camera = Camera(self.board.figure())

    def set_size(self, x, y):
        self.board.xlim(0, x)
        self.board.ylim(0, y)

    def draw_point(self, x, y, color="blue", size=2):
        self.board.scatter(x, y, s=size, c=color, zorder=3)

    def draw_line(self, p1: list, p2: list):
        x_values = [p1[0], p2[0]]
        y_values = [p1[1], p2[1]]

        self.board.plot(x_values, y_values, linewidth=0.5)

    def show(self):
        self.board.grid(zorder=0)
        self.board.show()

    def save(self, name):
        Util.checkPath(paths.IMG)
        self.board.savefig(paths.IMG / name, dpi=300)
