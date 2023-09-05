from abc import ABC, abstractmethod
from pathlib import Path
from typing import List


class BaseDirectory(ABC):
    path: Path

    @abstractmethod
    def get_file_list(self) -> List[str]:
        """
        Прочитать список файлов из папки
        :return: список текстовых файлов с данными
        """