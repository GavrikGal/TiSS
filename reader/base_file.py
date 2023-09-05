from abc import ABC, abstractmethod
from typing import Union, List

from reader.constants import IndexType, DataType
from reader.base_directory import BaseDirectory


class BaseFile(ABC):
    name: str
    dir: BaseDirectory

    @abstractmethod
    def get_index(self, index_type: IndexType) -> Union[float, List[float]]:
        """Получить индекс(ы) требуемого типа"""

    @abstractmethod
    def get_data(self, data_type: DataType) -> Union[float, List[float]]:
        """Получить данные требуемого типа"""