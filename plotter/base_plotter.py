from abc import ABC, abstractmethod
from typing import List, Union, Dict

from data.base_data_container import BaseDataContainer

from .constants import ChartType
from .style.grid_style import GridStyle
from .style.line_style import LineStyle


class BasePlotter(ABC):
    """Абстракция графопостроителя (плоттера)"""

    _n_subplots: int
    _n_cols: int
    _n_rows: int
    _h_plot: Union[None, float]
    _w_plot: Union[None, float]
    _subplots_names: Union[None, List[object]]

    def __init__(self, data_container: BaseDataContainer, chart_type: ChartType) -> None:
        """Инициализация плоттера"""
        self.chart_type = chart_type
        self.data_container = data_container

    @abstractmethod
    def get_subplot_names(self) -> List[object]:
        """Получить имена подграфиков"""

    @abstractmethod
    def show(self, chart_type: ChartType) -> None:
        """Построить график"""

    @abstractmethod
    def get_h_plot(self):
        """Получить высоту графика"""

    @abstractmethod
    def get_w_plot(self):
        """Получить ширину графика"""

    @abstractmethod
    def get_n_subplots(self) -> int:
        """Получить количество подграфиков"""

    @abstractmethod
    def get_n_cols(self) -> int:
        """Получить количество колонок с подграфиками"""

    @abstractmethod
    def set_n_cols(self, n_cols: int):
        """Установить количество колонок с подграфиками"""

    @abstractmethod
    def set_n_rows(self, n_rows: int):
        """Установить количество строк с подграфиками"""

    @abstractmethod
    def get_n_rows(self) -> int:
        """Получить количество строк с подграфиками"""

    @abstractmethod
    def set_grid_styles(self, grid_styles: Dict[str, GridStyle]):
        """Установить стили сетки"""

    @abstractmethod
    def set_line_styles(self, line_styles: List[LineStyle]):
        """Установить стили линий"""
