import pandas as pd
from typing import List


from file_set import FileSet
from directory import Dir
from constants import IndexType, DataType


class DataReader:
    """Читает данные из переданных папок"""
    def __init__(self):
        self.file_set_container: List[FileSet] = []
        self.index_type = None
        self.data_type = None

    def set_index_type(self, index_type: IndexType):
        """Установить тип индекса"""
        self.index_type = index_type

    def set_data_type(self, data_type: DataType):
        """Установить тип индекса"""
        self.data_type = data_type

    def set_file_sets_container(self, dir_names: List[str]):
        """Установить контейнер выборок файлов"""
        self.file_set_container = [FileSet(Dir(dir_name))
                                   for dir_name in dir_names]

    def validate_file_set_container(self):
        if not len(self.file_set_container) > 0:
            raise ValueError("File_Set_Container is Empty")

    def validate_index_type(self):
        if not self.index_type:
            raise ValueError("Index_Type is ", self.index_type)

    def validate_data_type(self):
        if not self.data_type:
            raise ValueError("Data_Type is ", self.data_type)

    def validate_init_data(self) -> bool:
        """Проверяет правильность установки инициирующих данных"""
        self.validate_file_set_container()
        self.validate_index_type()
        self.validate_data_type()
        return True

    def read_data(self) -> List[pd.DataFrame]:
        """Прочитать и вернуть данные из заданных в контейнере выборок файлов"""
        self.validate_init_data()
        data = [file_set.read_all_from_file_set(self.index_type, self.data_type)
                for file_set in self.file_set_container]
        print(data)
        return data



