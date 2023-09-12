import math
from typing import List, Dict

from data.base_data_container import BaseDataContainer
from plotter.base_plotter import BasePlotter
from plotter.constants import ChartType
from plotter.style.grid_style import GridStyle
from plotter.style.line_style import LineStyle

from .factory import HandlerFactory


class Plotter(BasePlotter):

    def __init__(self, data_container: BaseDataContainer, chart_type: ChartType) -> None:
        """Инициализация плоттера"""
        super().__init__(data_container, chart_type)
        self._n_subplots = self._get_n_subplots_from(data_container)
        self._n_cols = self._get_n_cols_from(self._n_subplots)
        self._n_rows = self._get_n_rows_from(self._n_subplots, self._n_cols)
        self._h_plot = None
        self._w_plot = None
        self.factory = HandlerFactory()
        self.subplot_sizes = {1: 9, 2: 4.5, 3: 3, 4: 2}
        self.subplot_names = self._get_subplot_names_from(data_container)

    @staticmethod
    def _get_subplot_names_from(data_container: BaseDataContainer) -> List[str]:
        return data_container.get_unique_columns()

    def get_subplot_names(self):
        return self.subplot_names

    @staticmethod
    def _get_n_rows_from(n_subplots: int, n_cols: int) -> int:
        return math.ceil(n_subplots / n_cols)

    @staticmethod
    def _get_n_cols_from(n_subplots: int) -> int:
        if n_subplots > 12:
            n_cols = 4
        elif n_subplots > 4:
            n_cols = 3
        elif n_subplots > 1:
            n_cols = 2
        else:
            n_cols = 1
        return n_cols

    @staticmethod
    def _get_n_subplots_from(data_container: BaseDataContainer) -> int:
        return len(data_container.get_unique_columns())

    def get_h_plot(self):
        if not self._h_plot:
            self._h_plot = self._n_rows * self.subplot_sizes[self._n_rows]
        return self._h_plot

    def get_w_plot(self):
        if not self._w_plot:
            self._w_plot = self._n_cols * self.subplot_sizes[self._n_cols]
        return self._w_plot

    def get_n_subplots(self) -> int:
        if not self._n_subplots:
            self._n_subplots = self._get_n_subplots_from(self.data_container)
        return self._n_subplots

    def get_n_cols(self) -> int:
        if not self._n_cols:
            self._n_cols = self._get_n_cols_from(self.get_n_subplots())
        return self._n_cols

    def set_n_cols(self, n_cols: int):
        self._n_cols = n_cols

    def set_n_rows(self, n_rows: int):
        self._n_rows = n_rows

    def get_n_rows(self) -> int:
        if not self._n_rows:
            self._n_rows = self._get_n_rows_from(self.get_n_subplots(), self.get_n_cols())
        return self._n_rows

    def set_grid_styles(self, grid_styles: Dict[str, GridStyle]):
        # todo: установить стиль в хэндлер
        pass

    def set_line_styles(self, line_styles: List[LineStyle]):
        # todo: установить стиль в хэндлер
        pass

    def show(self, chart_type: ChartType) -> None:

        handler = self.factory.get_handler(chart_type)
        handler.plot(plotter=self)
