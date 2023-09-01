from directory import Dir
from file import File
from constants import DATA_TYPE, INDEX_TYPE
from base_factory import BaseFileReaderFactory


class FileSet:
    """Выборка файлов"""
    def __init__(self, directory: Dir, file_reader_factory: BaseFileReaderFactory):
        self.files = [File(file_name, file_reader_factory) for file_name in directory.get_file_list()]

    def read_data_all_set(self, index_type: INDEX_TYPE, data_type: DATA_TYPE):
        indexes = [file.get_index(index_type) for file in self.files]
        data = [file.get_data(data_type) for file in self.files]
        return

    def __repr__(self):
        return str(self.files)

    def __str__(self):
        return str(self.files)

