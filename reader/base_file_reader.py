from abc import ABC, abstractmethod


# class EmptyReaderException(Exception):
#     pass


class FileReader(ABC):
    """Абстракция чтеца данных из файла"""

    @abstractmethod
    def read(self):
        """Прочитать требуемый тип данных из файла"""
