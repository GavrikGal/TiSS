from abc import ABC, abstractmethod

from .constants import ChartType
from .base_handler import BaseHandler


class ClassNotFoundError(ValueError):
    ...


class BaseHandlerFactory(ABC):
    """Абстракция Фабрики обработчиков графиков"""

    @staticmethod
    @abstractmethod
    def get_handler(chart_type: ChartType) -> BaseHandler:
        """Возвращает экземпляр класса для построения графика нужного типа"""
