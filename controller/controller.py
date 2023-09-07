from typing import List

from reader.constants import IndexType, DataType
from reader.base_data_reader import BaseDataReader


class PlotController:

    def __init__(self, index_type: IndexType, data_type: DataType,
                 dir_names: List[str], data_reader: BaseDataReader):
        self.data_reader = data_reader
        self.data_reader.set_index_type(index_type)
        self.data_reader.set_data_type(data_type)
        self.data_reader.init_file_sets_container(dir_names)

    def plot(self) -> None:
        """Контроллер построения графиков"""

        data = self.data_reader.read_data()

        # todo: доделать
