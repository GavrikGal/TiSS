from typing import List, Union

from reader.constants import IndexType, DataType, ColumnType
from data.base_data_frame import BaseDataFrame
from reader.base_data_reader import BaseDataReader

from reader.file_readers.file_set import FileSet
from reader.file_readers.directory import Dir


class DataReader(BaseDataReader):
    """Читает данные из переданных папок"""

    def __init__(self, index_type: IndexType, data_type: DataType, dir_names: List[str],
                 column_type: Union[None, ColumnType]):
        self.index_type = index_type
        self.data_type = data_type
        self.column_type = column_type
        self.file_set_container: List[FileSet] = self.get_file_set_container(dir_names)

    def get_file_set_container(self, dir_names: List[str]) -> List[FileSet]:
        """Установить контейнер выборок файлов"""
        return [FileSet(Dir(dir_name)) for dir_name in dir_names]

    def read_data(self) -> List[BaseDataFrame]:
        """Прочитать и вернуть данные из заданных в контейнере выборок файлов"""
        data = [file_set.get_df_from_all_file_set(self.index_type, self.data_type, self.column_type)
                for file_set in self.file_set_container]

        return data
