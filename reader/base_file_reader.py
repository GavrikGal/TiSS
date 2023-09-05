from abc import ABC, abstractmethod
from typing import Union, List
from datetime import datetime

from base_file import BaseFile


class FileReader(ABC):
    """Абстракция чтеца данных из файла"""

    @abstractmethod
    def read(self, file: BaseFile) -> Union[List[float], float, datetime, str]:
        """Прочитать требуемый тип данных из файла"""
