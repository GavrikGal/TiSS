import unittest
from pandas.testing import assert_frame_equal

from .test_sets import TEST_DATA_DIRS, test_data_read_answer_sets, test_df_name_answer_set

from reader.constants import IndexType, DataType
from reader.data_reader import DataReader


class TestDataReader(unittest.TestCase):

    def test_after_read_data_df_has_name(self):
        """Тестирует, что прочитанные ДатаФреймы имеют имя"""
        data_reader = DataReader()
        data_reader.set_file_sets_container(TEST_DATA_DIRS)
        data_reader.set_index_type(IndexType.Number)
        data_reader.set_data_type(DataType.R2)
        data = data_reader.read_data()
        names = [df.name for df in data]
        self.assertEqual(names, test_df_name_answer_set)

    def test_read_data(self):
        """Тестирует, что по переданным, при конструировании параметрам, читаются данные"""
        data_reader = DataReader()
        data_reader.set_file_sets_container(TEST_DATA_DIRS)
        data_reader.set_index_type(IndexType.Number)
        data_reader.set_data_type(DataType.R2)
        data = data_reader.read_data()
        self.assertIsNotNone(data)
        for df, answer in zip(data, test_data_read_answer_sets):
            assert_frame_equal(df.reset_index(drop=True),
                               answer)

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
