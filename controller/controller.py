from typing import List, Union

from reader.constants import IndexType, DataType, ColumnType
from reader.file_readers.data_reader import DataReader
from plotter.plt.plotter import Plotter
from plotter.constants import ChartType


class PlotController:

    def __init__(self, index_type: IndexType, data_type: DataType,
                 dir_names: List[str], column_type: Union[None, ColumnType],
                 chart_type: ChartType):
        self.chart_type = chart_type
        self.data_reader = DataReader(index_type, data_type, dir_names, column_type)

    def plot(self) -> None:
        """Контроллер построения графиков"""

        data = self.data_reader.read_data()
        plotter = Plotter(data_container=data, chart_type=self.chart_type)
        plotter.show(self.chart_type)
        # print(data)
        # todo: доделать
