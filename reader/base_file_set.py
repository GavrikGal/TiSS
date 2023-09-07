from abc import ABC, abstractmethod
from typing import List

from reader.base_data_frame import BaseDataFrame
from reader.base_directory import BaseDirectory
from reader.base_file import BaseFile
from reader.constants import DataType, IndexType


class BaseFileSet(ABC):
    """Выборка файлов"""
    directory = BaseDirectory
    files: List[BaseFile]

    @abstractmethod
    def get_df_from_all_file_set(self, index_type: IndexType, data_type: DataType) -> BaseDataFrame:
        """Чтение всех данных из всех файлов выборки"""
