from abc import ABC, abstractmethod
from typing import Union, List

from .constants import IndexType, DataType


class BaseFile(ABC):

    @abstractmethod
    def get_index(self, index_type: IndexType) -> Union[float, List[float]]:
        """Получить индекс(ы) требуемого типа"""

    @abstractmethod
    def get_data(self, data_type: DataType) -> Union[float, List[float]]:
        """Получить данные требуемого типа"""
