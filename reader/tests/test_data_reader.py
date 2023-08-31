import unittest

from reader.data_reader import DataReader
from .constants import TEST_DATA_DIRS
from reader.data_reader import INDEX_TYPE
from reader.readers.r2_reader import R2Reader


class TestDataReader(unittest.TestCase):

    def test_read_data(self):
        """Тестирует, что по переданным, при конструировании параметрам, читаются данные"""
        data_reader = DataReader()
        data_reader.set_file_sets_container(TEST_DATA_DIRS)
        data_reader.set_index_type(INDEX_TYPE.NUMBER)
        data_reader.set_reader(R2Reader())

        data = data_reader.read_data()

        self.assertIsNotNone(data)

    def test_read_data_without_file_set_container_raise_error(self):
        """Тестирует, чтение данных без контейнера выборок файлов вызывает ошибку"""
        data_reader = DataReader()
        data_reader.set_index_type(INDEX_TYPE.NUMBER)
        data_reader.set_reader(R2Reader())
        self.assertRaises(BaseException, data_reader.read_data)


