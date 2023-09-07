from abc import ABC, abstractmethod
from typing import List

from data.base_data_frame import BaseDataFrame

from .constants import ChartType
from .style.grid_style import GridStyle
from .style.line_style import LineStyle


class BasePlotter(ABC):
    """Абстракция графопостроителя (плоттера)"""

    chart_type: ChartType
    grid_style: GridStyle
    line_styles: List[LineStyle]
    data_container: List[BaseDataFrame]

    @abstractmethod
    def __init__(self, data_container: List[BaseDataFrame], chart_type: ChartType,
                 grid_style: GridStyle, line_styles: List[LineStyle]) -> None:
        """Инициализация плоттера"""

    @abstractmethod
    def show(self) -> None:
        """Построить график"""
