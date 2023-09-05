import unittest

from .test_sets import (test_filename_set, test_index_number_answer_set,
                        test_index_angle_answer_set)

from reader.file_readers.index_reader import SerialNumberReader, AngleReader
from reader.file_readers.file import File
from reader.file_readers.directory import Dir


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