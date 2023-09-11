from abc import ABC, abstractmethod

from plotter.base_plotter import BasePlotter


class BaseHandler(ABC):
    """Абстракция обработчика построителя графиков"""

    @abstractmethod
    def plot(self, plotter: BasePlotter) -> None:
        """Построить график"""
