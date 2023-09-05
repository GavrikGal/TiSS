import pandas as pd

from reader.base_file_set import BaseFileSet
from reader.base_directory import BaseDirectory
from reader.constants import DataType, IndexType

from .file import File


class FileSet(BaseFileSet):
    """Выборка файлов"""
    def __init__(self, directory: BaseDirectory):
        self.files = [File(file_name, directory) for file_name in directory.get_file_list()]

    def read_all_from_file_set(self, index_type: IndexType, data_type: DataType):
        indexes = [file.get_index(index_type) for file in self.files]
        data = [file.get_data(data_type) for file in self.files]

        if not indexes or not data:
            raise ValueError("Error in Indexes when was creating DataFrame")
        if not data:
            raise ValueError("Error in Data when was creating DataFrame")
        return pd.DataFrame(data, index=indexes)

    def __repr__(self):
        return str(self.files)

    def __str__(self):
        return str(self.files)

