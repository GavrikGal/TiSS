import unittest
from pandas.testing import assert_frame_equal

from .test_sets import test_data_dirs, test_data_read_answer_sets, test_df_name_answer_set

from reader.constants import IndexType, DataType
from reader.file_readers.data_reader import DataReader


class TestDataReader(unittest.TestCase):

    def test_after_read_data_df_has_name(self):
        """Тестирует, что прочитанные ДатаФреймы имеют имя"""
        data_reader = DataReader(IndexType.Number, DataType.R2, test_data_dirs, column_type=None)
        data = data_reader.read_data()
        names = [df.name for df in data.values()]
        self.assertEqual(names, test_df_name_answer_set)

    def test_read_data_(self):
        """Тестирует, что по переданным, при конструировании параметрам, читаются данные"""
        data_reader = DataReader(IndexType.Number, DataType.R2, test_data_dirs, column_type=None)
        data = data_reader.read_data()
        for df, answer in zip(data.values(), test_data_read_answer_sets):
            assert_frame_equal(df.reset_index(drop=True),
                               answer)
