from abc import ABC, abstractmethod

from plotter.base_plotter import BasePlotter
from plotter.style.grid_style import GridStyle, default_major_grid, default_minor_grid
from plotter.style.line_style import LineStyle, default_line_style_set


class BaseHandler(ABC):
    """Абстракция обработчика построителя графиков"""

    default_grid_style: GridStyle = {'major': default_major_grid, 'minor': default_minor_grid}
    default_line_styles: LineStyle = default_line_style_set

    @abstractmethod
    def plot(self, plotter: BasePlotter) -> None:
        """Построить график"""
