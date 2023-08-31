from abc import ABC, abstractmethod


class Reader(ABC):
    """Абстракция чтеца данных"""

    @abstractmethod
    def read(self):
        """Прочитать соответствующие данные"""
