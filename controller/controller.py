from typing import List

from reader.constants import IndexType, DataType
from reader.file_readers.data_reader import DataReader


class PlotController:

    def __init__(self, index_type: IndexType, data_type: DataType,
                 dir_names: List[str]):
        self.data_reader = DataReader(index_type, data_type, dir_names)

    def plot(self) -> None:
        """Контроллер построения графиков"""

        data = self.data_reader.read_data()
        # todo: доделать
