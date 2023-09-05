from abc import ABC, abstractmethod

from constants import IndexType, DataType
from base_file_reader import BaseFileReader


class ClassNotFoundError(ValueError):
    ...


class BaseFileReaderFactory(ABC):
    """Абстракция чтеца данных из файла"""

    @staticmethod
    @abstractmethod
    def get_index_reader(index_type: IndexType) -> BaseFileReader:
        """Возвращает экземпляр класса для чтения индексов"""

    @staticmethod
    @abstractmethod
    def get_data_reader(data_type: DataType) -> BaseFileReader:
        """Возвращает экземпляр класса для чтения данных"""
