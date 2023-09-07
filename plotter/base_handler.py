from abc import ABC, abstractmethod


class BaseHandler(ABC):
    """Абстракция обработчика построителя графиков"""

    @abstractmethod
    def plot(self) -> None:
        """Построить график"""
