import unittest

from .test_data_sets import (test_filename_set, test_data_r2_answer_set,)

from reader.file_readers.result_reader import R2Reader
from reader.file_readers.file import File
from reader.file_readers.directory import Dir


class TestResultReaders(unittest.TestCase):

    def test_correct_value_r2_reader(self):
        """Тестирует, что чтец R2Reader возвращает корректные значения"""

        reader = R2Reader()
        for filename, answer in zip(test_filename_set, test_data_r2_answer_set):
            file = File(file_name=filename, directory=Dir(""))
            self.assertEqual(reader.read(file, ), answer)
