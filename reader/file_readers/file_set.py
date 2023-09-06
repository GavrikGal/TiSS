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

    def read_all_from_file_set(self, index_type: IndexType, data_type: DataType):
        indexes = list({file.get_index(index_type) for file in self.files})  # set() обеспечивает уникальность индексов
        data = [file.get_data(data_type) for file in self.files]

        if not indexes or not data:
            raise ValueError("Error in Indexes when was creating DataFrame")
        if not data:
            raise ValueError("Error in Data when was creating DataFrame")

        df = DataFrame(data, index=indexes)
        df.name = str(self.directory)
        return df

    def __repr__(self):
        return str(self.files)

    def __str__(self):
        return str(self.files)

