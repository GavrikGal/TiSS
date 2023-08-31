from abc import ABC, abstractmethod


class EmptyReaderException(Exception):
    pass


class Reader(ABC):
    """Абстракция чтеца данных"""

    @abstractmethod
    def read(self):
        """Прочитать соответствующие данные"""
