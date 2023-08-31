import numpy as np
import pandas as pd
from collections import namedtuple
from typing import List


from file_set import FileSet
from base_reader import Reader


INDEX_TYPE = namedtuple('index', ['NUMBER', 'ANGEL', 'DATE'])
DATA_TYPE = namedtuple('data', ['R2', 'SIGNAL', 'NOISE'])





class DataReader:
    """Читает данные из переданных папок"""
    def __init__(self):
        self.file_set_container = []
        self.index_type = None
        self.reader: Reader = None

    def set_file_sets_container(self, file_set_container: List[FileSet]):
        """Установить контейнер выборок файлов"""
        self.file_set_container = file_set_container

    def set_index_type(self, index_type: INDEX_TYPE):
        """Установить тип индекса"""
        self.index_type = index_type

    def set_reader(self, reader: Reader):
        """Установить чтеца данных"""
        self.reader = reader

    def read_data(self) -> pd.DataFrame:
        """Прочитать и вернуть данные из заданных в контейнере выборок файлов"""
        data = self.reader.read()
        return data




print(INDEX_TYPE.NUMBER)
