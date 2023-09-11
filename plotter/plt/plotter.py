from typing import List, Union

from data.base_data_frame import BaseDataFrame
from plotter.base_plotter import BasePlotter
from plotter.constants import ChartType
from plotter.style.grid_style import GridStyle
from plotter.style.line_style import LineStyle

from .factory import HandlerFactory


class Plotter(BasePlotter):

    def __init__(self, data_container: List[BaseDataFrame], chart_type: ChartType,
                 grid_style: Union[None, GridStyle] = None,
                 line_styles: Union[None, List[LineStyle]] = None) -> None:
        """Инициализация плоттера"""
        super().__init__(data_container, chart_type, grid_style, line_styles)
        self.factory = HandlerFactory()

    def show(self, chart_type: ChartType) -> None:

        handler = self.factory.get_handler(chart_type)
        handler.plot(plotter=self)

        # todo: если есть НЕ дефолтные стили, то использовать их
