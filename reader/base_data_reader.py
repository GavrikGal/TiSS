from abc import ABC, abstractmethod
from typing import List, Union

from .constants import IndexType, DataType, ColumnType
from data.base_data_frame import BaseDataFrame
from data.base_data_container import BaseDataContainer
from reader.base_file_set import BaseFileSet


class BaseDataReader(ABC):
    """Базовый класс чтения данных"""
    file_set_container: List[BaseFileSet]
    index_type: IndexType
    data_type: DataType

    @abstractmethod
    def __init__(self, index_type: IndexType, data_type: DataType,
                 dir_names: List[str], column_type: Union[None, ColumnType]):
        """Инициализация чтеца данных"""

    @abstractmethod
    def get_file_set_container(self, dir_names: List[str]):
        """Установить контейнер выборок файлов"""

    @abstractmethod
    def read_data(self) -> BaseDataContainer:
        """Прочитать и вернуть данные из заданных в контейнере выборок файлов"""

    # @abstractmethod
    # def read_data(self) -> List[BaseDataFrame]:
    #     """Прочитать и вернуть данные из заданных в контейнере выборок файлов"""
