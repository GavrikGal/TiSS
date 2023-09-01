from abc import ABC, abstractmethod
from typing import Union, List
from datetime import datetime

# class EmptyReaderException(Exception):
#     pass


class FileReader(ABC):
    """Абстракция чтеца данных из файла"""

    @abstractmethod
    def read(self, filename: str) -> Union[List[float], float, datetime, str]:
        """Прочитать требуемый тип данных из файла"""
