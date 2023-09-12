from abc import ABC, abstractmethod
from typing import List, Union

from data.base_data_frame import BaseDataFrame
# from plotter.base_handler_factory import BaseHandlerFactory

from .constants import ChartType
from .style.grid_style import GridStyle
from .style.line_style import LineStyle


class BasePlotter(ABC):
    """Абстракция графопостроителя (плоттера)"""

    def __init__(self, data_container: List[BaseDataFrame], chart_type: ChartType,
                 grid_style: Union[None, GridStyle], line_styles: Union[None, List[LineStyle]]) -> None:
        """Инициализация плоттера"""
        self.chart_type = chart_type
        self.grid_style = grid_style
        self.line_styles = line_styles
        self.data_container = data_container
        self.unique_cols: List[object]  # todo: это должен делать контейнер и хранить там
        self.ncols: int
        self.nrows: int

    @abstractmethod
    def show(self, chart_type: ChartType) -> None:
        """Построить график"""
