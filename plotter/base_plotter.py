from abc import ABC, abstractmethod
from typing import List, Dict

from data.base_data_container import BaseDataContainer

from .constants import ChartType
from .style.grid_style import GridStyle
from .style.line_style import LineStyle
from .canvas.grid import Grid
from .canvas.rectangle import Rect
from .canvas.subplot import Subplot


class BasePlotter(ABC):
    """Абстракция графопостроителя (плоттера)"""

    chart_type: ChartType
    data_container: BaseDataContainer
    handle_factory: object
    size: Rect
    grid: Grid
    subplots: List[Subplot]

    @abstractmethod
    def transpose_data_in_container(self) -> None:
        """Транспонировать данные в контейнере"""

    @abstractmethod
    def plot(self, chart_type: ChartType) -> None:
        """Построить график"""

    @abstractmethod
    def show(self) -> None:
        """Показать график"""

    @abstractmethod
    def set_grid_styles(self, grid_styles: Dict[str, GridStyle]):
        """Установить стили сетки"""

    @abstractmethod
    def set_line_styles(self, line_styles: List[LineStyle]):
        """Установить стили линий"""
