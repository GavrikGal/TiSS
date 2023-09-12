import unittest

from reader.file_readers.data_reader import DataReader
from reader.constants import IndexType, DataType, ColumnType
from plotter.constants import ChartType
from plotter.plt.plotter import Plotter

from .test_sets import test_data_dirs


class TestPlotter(unittest.TestCase):

    def test_plot_error_bar_plot(self):
        """Построение графика доверительных интервалов"""

        data_reader = DataReader(IndexType.Number, DataType.R2, test_data_dirs,
                                 column_type=None)
        data = data_reader.read_data()

        plotter = Plotter(data_container=data, chart_type=ChartType.ErrorBar)
        plotter.plot(ChartType.ErrorBar)

        plotter.show()

    def test_plot_error_bar_plot_with_freq(self):
        """Построение графика доверительных интервалов для различных частот"""

        data_reader = DataReader(IndexType.Frequency, DataType.Signal, test_data_dirs,
                                 column_type=ColumnType.Number)
        data = data_reader.read_data()

        plotter = Plotter(data_container=data, chart_type=ChartType.ErrorBar)
        plotter.plot(ChartType.ErrorBar)

        plotter.show()
