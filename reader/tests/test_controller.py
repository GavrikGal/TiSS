import unittest

from .test_sets import test_data_dirs

from reader.constants import IndexType, DataType
from controller.controller import PlotController


class TestPlotController(unittest.TestCase):

    def test_plot_freq_and_signal(self):
        """Тестирует, построение графиков частоты и сигнала"""

        controller = PlotController(IndexType.Frequency,
                                    DataType.Signal,
                                    test_data_dirs)
        controller.plot()

    def test_plot_number_and_r2(self):
        """Тестирует, построение графиков серийного номера и R2"""

        controller = PlotController(IndexType.Number,
                                    DataType.R2,
                                    test_data_dirs)
        controller.plot()
