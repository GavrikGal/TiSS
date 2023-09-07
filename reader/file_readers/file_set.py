from typing import List

import pandas as pd

from reader.data_handler.data_frame import DataFrame
from reader.base_file_set import BaseFileSet
from reader.base_directory import BaseDirectory
from reader.constants import DataType, IndexType


from .file import File


class FileSet(BaseFileSet):
    """Выборка файлов"""
    def __init__(self, directory: BaseDirectory):
        self.directory = directory
        self.files = [File(file_name, directory) for file_name in directory.get_file_list()]

    def get_df_from_all_file_set(self, index_type: IndexType, data_type: DataType):
        data_set = [file.get_dataframe(index_type, data_type) for file in self.files]
        axis = 0
        if data_set[0].shape[0] > 1:  # в ДатаФрейме больше одного значения - объединять столбцами
            axis = 1
        data = pd.concat(data_set, axis=axis)
        df = DataFrame(data)
        df.name = str(self.directory)
        return df

    def __repr__(self):
        return str(self.files)

    def __str__(self):
        return str(self.files)
