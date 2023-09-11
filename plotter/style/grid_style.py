from dataclasses import dataclass


@dataclass
class GridStyle:
    color: str
    linewidth: float
    alpha: float
    min_y_tick: int
    max_y_tick: int
    y_tick: int


default_major_grid = GridStyle('dimgray', 0.4, 0.5, 0, 50, 5)
default_minor_grid = GridStyle('gray', 0.3, 0.2, 0, 50, 1)
