from abc import ABC, abstractmethod
from collections import UserDict
from typing import List


class BaseDataContainer(UserDict, ABC):

    @abstractmethod
    def get_unique_index(self) -> List[object]:
        """Возвращает список уникальных имен колонок из всего контейнера"""
