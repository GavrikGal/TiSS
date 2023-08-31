from directory import Dir
from file import File
from constants import DATA_TYPE, INDEX_TYPE


class FileSet:
    """Выборка файлов"""
    def __init__(self, directory: Dir):
        self.files = [File(file_name) for file_name in directory.get_file_list()]

    def read_data_set(self, index_type: INDEX_TYPE, data_type: DATA_TYPE):
        return [file.read_data(data_type) for file in self.files]

    def __repr__(self):
        return str(self.files)

    def __str__(self):
        return str(self.files)

