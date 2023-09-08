from typing import Union, List

import pandas as pd

from reader.constants import DataType, IndexType, ColumnType
from reader.base_file import BaseFile
from reader.base_directory import BaseDirectory

from .factory import FileReaderFactory


class File(BaseFile):
    """Файл"""

    def __init__(self, file_name: str, directory: BaseDirectory):
        self.name = file_name
        self.dir = directory
        self.file_reader_factory = FileReaderFactory()

    def get_dataframe(self, index_type: IndexType, data_type: DataType,
                      column_type: Union[None, ColumnType]) -> pd.DataFrame:

        index = self.get_index(index_type)
        data = self.get_value(data_type)
        columns = self.get_column(column_type)

        df = pd.DataFrame(data, columns=columns, index=index)
        return df

    def get_index(self, index_type: IndexType) -> Union[float, List[float]]:
        index_reader = self.file_reader_factory.get_attribute_reader(index_type)
        index = index_reader.read(file=self)
        if not isinstance(index, list):
            index = [index]
        return index

    def get_value(self, data_type: DataType) -> Union[float, List[float]]:
        data_reader = self.file_reader_factory.get_data_reader(data_type)
        data = data_reader.read(file=self)
        if not isinstance(data, list):
            data = [data]
        return data

    def get_column(self, column_type: Union[None, ColumnType]) -> Union[float, List[float]]:
        columns = None
        if column_type:
            column_reader = self.file_reader_factory.get_attribute_reader(column_type)
            columns = column_reader.read(file=self)
            if not isinstance(columns, list):
                columns = [columns]
        return columns

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
