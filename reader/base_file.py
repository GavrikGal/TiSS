from abc import ABC, abstractmethod
from typing import Union, List

import pandas as pd

from reader.constants import IndexType, DataType, ColumnType
from reader.base_directory import BaseDirectory


class BaseFile(ABC):
    name: str
    dir: BaseDirectory

    @abstractmethod
    def get_index(self, index_type: IndexType) -> Union[float, List[float]]:
        """Получить индекс(ы) требуемого типа"""

    @abstractmethod
    def get_value(self, data_type: DataType) -> Union[float, List[float]]:
        """Получить данные требуемого типа"""

    @abstractmethod
    def get_dataframe(self, index_type: IndexType, data_type: DataType,
                      column_type: Union[None, ColumnType]) -> pd.DataFrame:
        """Получить ДатаФрейм с данными и индексами требуемого типа"""
