from abc import ABC, abstractmethod
from typing import Union

from constants import IndexType, ColumnType, DataType
from base_file_reader import BaseFileReader


class ClassNotFoundError(ValueError):
    ...


class BaseFileReaderFactory(ABC):
    """Абстракция чтеца данных из файла"""

    @staticmethod
    @abstractmethod
    def get_attribute_reader(attribute_type: Union[IndexType, ColumnType]) -> BaseFileReader:
        """Возвращает экземпляр класса для чтения индексов"""

    @staticmethod
    @abstractmethod
    def get_data_reader(data_type: DataType) -> BaseFileReader:
        """Возвращает экземпляр класса для чтения данных"""
