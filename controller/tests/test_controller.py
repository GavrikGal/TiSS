import unittest

from reader.constants import IndexType, DataType
from controller.controller import PlotController
from plotter.constants import ChartType

from .test_sets import test_data_dirs


class TestPlotController(unittest.TestCase):

    def test_plot_freq_and_signal(self):
        """Построение графиков частоты и сигнала"""

        controller = PlotController(IndexType.Frequency,
                                    DataType.Signal,
                                    test_data_dirs, column_type=None,
                                    chart_type=ChartType.BoxPlot)
        controller.plot()

    def test_plot_number_and_r2(self):
        """Построение графиков серийного номера и R2"""

        controller = PlotController(IndexType.Number,
                                    DataType.R2,
                                    test_data_dirs, column_type=None,
                                    chart_type=ChartType.BoxPlot)
        controller.plot()

    def test_plot_error_bar_plot(self):
        """Построение графика доверительных интервалов"""

        controller = PlotController(IndexType.Number,
                                    DataType.R2,
                                    test_data_dirs, column_type=None,
                                    chart_type=ChartType.ErrorBar)

        controller.plot()

