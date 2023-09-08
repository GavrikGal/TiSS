import unittest
from pandas.testing import assert_frame_equal

from reader.file_readers.file import File
from reader.file_readers.directory import Dir
from reader.constants import IndexType, DataType

from .test_sets import (test_file_name, test_dir, test_file_get_dataframe_answer,
                        test_file_get_dataframe_freq_and_signal_answer)


class TestFile(unittest.TestCase):

    def test_correct_value_serial_number_and_r2_get_dataframe(self):
        """Тестирует, что файл возвращает корректный ДатаФрейм с серийными номерами и R2"""

        file = File(file_name=test_file_name, directory=Dir(test_dir))
        df = file.get_dataframe(IndexType.Number, DataType.R2, column_type=None)
        assert_frame_equal(df, test_file_get_dataframe_answer)

    def test_correct_value_frequency_and_signal_get_dataframe(self):
        """Тестирует, что файл возвращает корректный ДатаФрейм с частотами и сигналами"""

        file = File(file_name=test_file_name, directory=Dir(test_dir))
        df = file.get_dataframe(IndexType.Frequency, DataType.Signal, column_type=None)

        assert_frame_equal(df, test_file_get_dataframe_freq_and_signal_answer)
