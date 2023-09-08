import unittest

from reader.constants import IndexType, DataType, ColumnType
from reader.file_readers.file_set import FileSet
from reader.file_readers.directory import Dir

from .test_sets import test_dir, test_file_get_dataframe_columns_answer


class TestFileSet(unittest.TestCase):

    def test_columns_have_name(self):
        """Тестирует, что колонки прочитанного ДатаСета имеют имя"""
        file_set = FileSet(Dir(test_dir))
        data_set = file_set.get_df_from_all_file_set(IndexType.Frequency, DataType.Signal,
                                                     column_type=ColumnType.Number)
        self.assertListEqual(list(data_set.columns.values),
                             test_file_get_dataframe_columns_answer)
