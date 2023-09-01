import numpy as np
import pandas as pd
from typing import List


from file_set import FileSet
from directory import Dir
from constants import INDEX_TYPE, DATA_TYPE
from .file_readers.factory import FileReaderFactory


class DataReader:
    """Читает данные из переданных папок"""
    def __init__(self):
        self.file_set_container: List[FileSet] = []
        self.index_type = None
        # self.reader: Reader = None

    def set_index_type(self, index_type: INDEX_TYPE):
        """Установить тип индекса"""
        self.index_type = index_type

    def set_file_sets_container(self, dir_names: List[str]):
        """Установить контейнер выборок файлов"""
        self.file_set_container = [FileSet(Dir(dir_name), FileReaderFactory())
                                   for dir_name in dir_names]

    # def set_reader(self, reader: Reader):
    #     """Установить чтеца данных"""
    #     self.reader = reader

    def validate_file_set_container(self):
        if not len(self.file_set_container) > 0:
            raise ValueError("File_Set_Container is Empty")

    def validate_index_type(self):
        if not self.index_type:
            raise ValueError("Index_Type is ", self.index_type)

    # def validate_reader(self):
    #     if not self.reader:
    #         raise EmptyReaderException("Empty Reader")

    def validate_init_data(self) -> bool:
        """Проверяет правильность установки инициирующих данных"""
        self.validate_file_set_container()
        self.validate_index_type()
        # self.validate_reader()
        return True

    def read_data(self) -> pd.DataFrame:
        """Прочитать и вернуть данные из заданных в контейнере выборок файлов"""
        self.validate_init_data()
        # data = self.reader.read()
        print("read_data():", INDEX_TYPE.ANGEL)
        print("read_data() hash():", hash(INDEX_TYPE.ANGEL))
        data = [file_set.read_data_all_set(INDEX_TYPE.ANGEL, DATA_TYPE.R2) for file_set in self.file_set_container]
        print(data)
        return data



