from abc import ABC, abstractmethod
from typing import List

import pandas as pd

from reader.base_file import BaseFile
from reader.constants import DataType, IndexType


class BaseFileSet(ABC):
    """Выборка файлов"""

    files: List[BaseFile]

    @abstractmethod
    def read_all_from_file_set(self, index_type: IndexType, data_type: DataType) -> pd.DataFrame:
        """Чтение всех данных из всех файлов выборки"""
