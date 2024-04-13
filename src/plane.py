from math import floor
from .celdas import Cell
from .aux_functions import create_video
import numpy as np
import matplotlib.pyplot as plt


class Plane:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.cells = {}

        self.x = np.asarray([x for x in range(1, width + 1)])
        self.y = np.asarray([y for y in range(1, height + 1)])

        self.plane = [(x, y) for y in self.y for x in self.x]

        self.generate_cells(self.plane)

    def generate_cells(self, plane):
        for position in plane:
            cell = Cell(position, str(position))
            self.cells[str(position)] = cell

        for cell in self.cells.values():
            cell.set_environment(self.cells)

    def awake_random(self):
        for _ in range(1, floor((len(self.cells) + 1) / 4)):
            self.cells[f'({np.random.randint(1, self.width)}, {np.random.randint(1, self.height)})'].awake()

    def plot(self, iteration, date, width, height, show_plot=False, save=True, size=20,
             color='red', background_color='white'):
        x, y = [], []

        for cell in self.cells.values():
            if cell.live:
                x.append(cell.pos[0])
                y.append(cell.pos[1])

        fig, ax = plt.subplots()

        ax.set_xlim(0, width + 1)
        ax.set_ylim(0, height + 1)
        ax.set_facecolor(background_color)

        ax.scatter(x, y, s=size, c=color, marker='s')

        ax.set_title(iteration)

        # fig = plt.plot(self.grid[0], self.grid[1], 'bs')

        if save:
            plt.savefig(f'./{date}/{iteration}.png')

        if show_plot:
            plt.show()
