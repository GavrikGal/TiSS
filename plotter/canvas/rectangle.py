from .grid import Grid


class Rect:
    width: float
    height: float

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def gridding(self, grid: Grid) -> 'Rect':
        ratio = 0.9
        self.height = ratio * (self.width / grid.col) * grid.row
        return self


default_plotter_size = Rect(9, 12)
