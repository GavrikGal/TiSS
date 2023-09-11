from abc import ABC, abstractmethod
from typing import List

from data.base_data_frame import BaseDataFrame

from .constants import ChartType
from .style.grid_style import GridStyle
from .style.line_style import LineStyle


class BasePlotter(ABC):
    """Абстракция графопостроителя (плоттера)"""

    def __init__(self, data_container: List[BaseDataFrame], chart_type: ChartType,
                 grid_style: GridStyle, line_styles: List[LineStyle]) -> None:
        """Инициализация плоттера"""
        self.chart_type = chart_type
        self.grid_style = grid_style
        self.line_styles = line_styles
        self.data_container = data_container

    @abstractmethod
    def show(self) -> None:
        """Построить график"""
