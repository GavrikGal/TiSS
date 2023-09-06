import unittest

from .test_sets import test_data_dirs

from reader.constants import IndexType, DataType
from reader.controller import PlotController
from reader.file_readers.data_reader import DataReader


class TestPlotController(unittest.TestCase):

    def test_after_read_data_df_has_name(self):
        """Тестирует, контроллер построения графиков"""

        controller = PlotController()
        controller.init_data_reader(IndexType.Frequency, DataType.Signal, test_data_dirs, DataReader())
        controller.plot()
