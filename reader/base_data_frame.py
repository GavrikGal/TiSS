from abc import ABC, abstractmethod


class BaseDataFrame(ABC):
    """Базовый класс ДатаФрейма основанный на pd.DataFrame"""

    name: str

    @abstractmethod
    def reset_index(self, drop: bool):
        ...
