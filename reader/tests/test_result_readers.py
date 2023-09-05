import unittest

from .test_sets import (test_filename_set, test_data_r2_answer_set, test_file_name, test_dir,
                        test_data_signals_answer, test_data_noise_answer)

from reader.file_readers.result_reader import R2Reader, SignalsReader, NoisesReader
from reader.file_readers.file import File
from reader.file_readers.directory import Dir


class TestResultReaders(unittest.TestCase):

    def test_correct_value_r2_reader(self):
        """Тестирует, что чтец R2Reader возвращает корректные значения"""

        reader = R2Reader()
        for filename, answer in zip(test_filename_set, test_data_r2_answer_set):
            file = File(file_name=filename, directory=Dir(""))
            self.assertEqual(reader.read(file, ), answer)

    def test_correct_value_signal_reader(self):
        """Тестирует, что чтец SignalsReader возвращает корректные значения"""

        reader = SignalsReader()
        file = File(file_name=test_file_name, directory=Dir(test_dir))
        self.assertEqual(reader.read(file), test_data_signals_answer)

    def test_correct_value_noise_reader(self):
        """Тестирует, что чтец NoisesReader возвращает корректные значения"""

        reader = NoisesReader()
        file = File(file_name=test_file_name, directory=Dir(test_dir))
        self.assertEqual(reader.read(file), test_data_noise_answer)
