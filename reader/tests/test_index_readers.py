import unittest
from datetime import timedelta

from .test_sets import (test_filename_set, test_index_number_answer_set,
                        test_index_angle_answer_set, test_file_name, test_dir,
                        test_index_frequencies_answer, test_index_date_answer)

from reader.file_readers.index_reader import (SerialNumberReader, AngleReader,
                                              FrequenciesReader, DateReader)
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

    def test_correct_value_frequencies_reader(self):
        """Тестирует, что чтец FrequenciesReader возвращает корректные значения"""

        reader = FrequenciesReader()
        file = File(file_name=test_file_name, directory=Dir(test_dir))
        self.assertEqual(reader.read(file), test_index_frequencies_answer)

    def test_correct_value_date_reader(self):
        """Тестирует, что чтец DateReader возвращает корректные значения"""

        reader = DateReader()
        file = File(file_name=test_file_name, directory=Dir(test_dir))
        self.assertAlmostEqual(reader.read(file), test_index_date_answer,
                               delta=timedelta(minutes=1))
