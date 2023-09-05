import unittest

from .test_sets import TEST_DATA_DIRS

from reader.constants import IndexType, DataType
from reader.data_reader import DataReader


class TestDataReader(unittest.TestCase):

    def test_read_data(self):
        """Тестирует, что по переданным, при конструировании параметрам, читаются данные"""
        data_reader = DataReader()
        data_reader.set_file_sets_container(TEST_DATA_DIRS)
        data_reader.set_index_type(IndexType.Number)
        data_reader.set_data_type(DataType.R2)

        data = data_reader.read_data()

        self.assertIsNotNone(data)

    def test_validate_init_data_without_file_set_container_raise_error(self):
        """Тестирует, что валидация инициированных значений без контейнера выборок файлов вызывает ошибку"""
        data_reader = DataReader()
        data_reader.set_index_type(IndexType.Number)
        data_reader.set_data_type(DataType.R2)

        self.assertRaises(ValueError, data_reader.validate_init_data)

    def test_validate_init_data_without_index_type_raise_error(self):
        """Тестирует, что валидация инициированных значений без типа индексов вызывает ошибку"""
        data_reader = DataReader()
        data_reader.set_file_sets_container(TEST_DATA_DIRS)
        data_reader.set_data_type(DataType.R2)

        self.assertRaises(ValueError, data_reader.validate_init_data)

    def test_validate_init_data_without_data_type_raise_error(self):
        """Тестирует, что валидация инициированных значений без типа данных вызывает ошибку"""
        data_reader = DataReader()
        data_reader.set_file_sets_container(TEST_DATA_DIRS)
        data_reader.set_index_type(IndexType.Number)

        self.assertRaises(ValueError, data_reader.validate_init_data)

    def test_read_data_without_validate_init_data_raise_error(self):
        """Тестирует, что чтение данных без инициированных значений вызывает ошибку"""
        data_reader = DataReader()

        self.assertRaises(Exception, data_reader.read_data)
