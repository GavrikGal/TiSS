import unittest

from .test_data_sets import (TEST_DATA_DIRS, test_filename_set, test_index_number_answer_set, test_data_r2_answer_set,
                             test_index_angle_answer_set)

from reader.file_readers.index_reader import SerialNumberReader, AngleReader
from reader.file_readers.result_reader import R2Reader
from reader.file_readers.file import File

from reader.constants import IndexType, DataType
from reader.data_reader import DataReader
from reader.file_readers.directory import Dir


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


class TestIndexReaders(unittest.TestCase):

    def test_correct_value_serial_number_reader(self):
        """Тестирует, что чтец SerialNumberReader возвращает корректные значения"""

        reader = SerialNumberReader()
        for filename, answer in zip(test_filename_set, test_index_number_answer_set):
            file = File(file_name=filename, directory=Dir(""))
            self.assertEqual(reader.read(file), answer)

    def test_correct_value_angle_reader(self):
        """Тестирует, что чтец AngleReader возвращает корректные значения"""

        reader = AngleReader()
        for filename, answer in zip(test_filename_set, test_index_angle_answer_set):
            file = File(file_name=filename, directory=Dir(""))
            self.assertEqual(reader.read(file), answer)


class TestResultReaders(unittest.TestCase):

    def test_correct_value_r2_reader(self):
        """Тестирует, что чтец R2Reader возвращает корректные значения"""

        reader = R2Reader()
        for filename, answer in zip(test_filename_set, test_data_r2_answer_set):
            file = File(file_name=filename, directory=Dir(""))
            self.assertEqual(reader.read(file, ), answer)
