from typing import List, Dict, Union

from matplotlib import pyplot as plt

from data.base_data_container import BaseDataContainer
from plotter.base_plotter import BasePlotter
from plotter.constants import ChartType
from plotter.style.grid_style import GridStyle
from plotter.style.line_style import LineStyle
from plotter.canvas.rectangle import Rect, default_plotter_size
from plotter.canvas.grid import Grid
from plotter.canvas.subplot import Subplot

from .factory import HandlerFactory


class Plotter(BasePlotter):

    def __init__(self, data_container: BaseDataContainer, chart_type: ChartType,
                 size: Union[None, Rect] = None) -> None:
        """Инициализация плоттера"""

        self.data_container = data_container
        self.chart_type = chart_type
        self.handle_factory = HandlerFactory()
        self.subplots = [Subplot(name) for name in data_container.get_unique_columns()]
        self.grid = Grid(len(self.subplots))
        self.size = size
        if size is None:
            self.size = default_plotter_size.gridding(self.grid)

    def transpose_data_in_container(self) -> None:
        self.__init__(self.data_container.transpose_data(), self.chart_type)

    def set_grid_styles(self, grid_styles: Dict[str, GridStyle]):
        # todo: установить стиль в хэндлер
        pass

    def set_line_styles(self, line_styles: List[LineStyle]):
        # todo: установить стиль в хэндлер
        pass

    def plot(self, chart_type: ChartType) -> None:
        handler = self.handle_factory.get_handler(chart_type)
        handler.plot(plotter=self)

    def show(self) -> None:
        plt.show()
