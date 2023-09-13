import unittest

from reader.file_readers.data_reader import DataReader
from reader.constants import IndexType, DataType, ColumnType
from plotter.constants import ChartType
from plotter.plt.plotter import Plotter

from .test_sets import test_data_dirs, test_data_dirs_to_analyse


class TestPlotter(unittest.TestCase):

    def test_error_bar(self):
        """Построение графика доверительных интервалов"""

        data_reader = DataReader(IndexType.Number, DataType.R2, test_data_dirs,
                                 column_type=None)
        data = data_reader.read_data()

        plotter = Plotter(data_container=data, chart_type=ChartType.ErrorBar)
        plotter.plot(ChartType.ErrorBar)

        plotter.show()

    def test_error_bar_with_freq(self):
        """Построение графика доверительных интервалов для различных частот"""

        data_reader = DataReader(IndexType.Frequency, DataType.Signal, test_data_dirs,
                                 column_type=ColumnType.Number)
        data = data_reader.read_data()

        plotter = Plotter(data_container=data, chart_type=ChartType.ErrorBar)
        plotter.plot(ChartType.ErrorBar)

        plotter.show()

    def test_error_bar_for_analyse(self):
        """Построение графика доверительных интервалов для анализа данных"""

        data_reader = DataReader(IndexType.Number, DataType.R2, test_data_dirs_to_analyse,
                                 column_type=None)
        data = data_reader.read_data()

        plotter = Plotter(data_container=data, chart_type=ChartType.ErrorBar)
        plotter.plot(ChartType.ErrorBar)

        plotter.show()
