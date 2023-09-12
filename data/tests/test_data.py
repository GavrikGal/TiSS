import unittest


from reader.file_readers.data_reader import DataReader
from reader.constants import IndexType, DataType, ColumnType
from controller.controller import PlotController
from plotter.constants import ChartType

from .test_sets import test_data_dirs, test_unique_index_answer


class TestData(unittest.TestCase):

    def test_unique_index(self):
        """Получение уникальных индексов (частот)"""

        data_reader = DataReader(IndexType.Frequency, DataType.Signal, test_data_dirs,
                                 column_type=ColumnType.Number)
        data = data_reader.read_data()
        expected = data.get_unique_columns()
        self.assertListEqual(expected, test_unique_index_answer)
