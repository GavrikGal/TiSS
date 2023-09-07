from abc import ABC, abstractmethod
from typing import List

from constants import IndexType, DataType
from data.base_data_frame import BaseDataFrame
from reader.base_file_set import BaseFileSet


class BaseDataReader(ABC):
    """Базовый класс чтения данных"""
    file_set_container: List[BaseFileSet]
    index_type: IndexType
    data_type: DataType

    @abstractmethod
    def set_index_type(self, index_type: IndexType):
        """Установить тип индекса"""

    @abstractmethod
    def set_data_type(self, data_type: DataType):
        """Установить тип данных"""

    @abstractmethod
    def init_file_sets_container(self, dir_names: List[str]):
        """Установить контейнер выборок файлов"""

    @abstractmethod
    def validate_file_set_container(self):
        """Проверить наличие контейнера выборок файлов"""

    @abstractmethod
    def validate_index_type(self):
        """Проверить наличие установленного типа индексов"""

    @abstractmethod
    def validate_data_type(self):
        """Проверить наличие установленного типа данных"""

    @abstractmethod
    def validate_init_data(self) -> bool:
        """Проверяет правильность установки всех инициирующих данных"""

    @abstractmethod
    def read_data(self) -> List[BaseDataFrame]:
        """Прочитать и вернуть данные из заданных в контейнере выборок файлов"""
