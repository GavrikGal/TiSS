from typing import Union, List

import pandas as pd

from reader.constants import DataType, IndexType
from reader.base_file import BaseFile
from reader.base_directory import BaseDirectory

from .factory import FileReaderFactory


class File(BaseFile):
    """Файл"""

    def __init__(self, file_name: str, directory: BaseDirectory):
        self.name = file_name
        self.dir = directory
        self.file_reader_factory = FileReaderFactory()

    def get_index(self, index_type: IndexType) -> Union[float, List[float]]:
        index_reader = self.file_reader_factory.get_index_reader(index_type)
        index = index_reader.read(file=self)
        return index

    def get_value(self, data_type: DataType) -> Union[float, List[float]]:
        data_reader = self.file_reader_factory.get_data_reader(data_type)
        data = data_reader.read(file=self)
        return data

    def get_dataframe(self, index_type: IndexType, data_type: DataType) -> pd.DataFrame:
        index = self.get_index(index_type)
        if not isinstance(index, list):
            index = [index]
        data = self.get_value(data_type)
        if not isinstance(data, list):
            data = [data]
        # todo: Можно задать имя, которое будет именем колонки
        df = pd.DataFrame(data, index=index)
        return df

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
