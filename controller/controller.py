from typing import List, Union

from reader.constants import IndexType, DataType, ColumnType
from reader.file_readers.data_reader import DataReader


class PlotController:

    def __init__(self, index_type: IndexType, data_type: DataType,
                 dir_names: List[str], column_type: Union[None, ColumnType]):
        self.data_reader = DataReader(index_type, data_type, dir_names, column_type)

    def plot(self) -> None:
        """Контроллер построения графиков"""

        data = self.data_reader.read_data()
        # print(data)
        # todo: доделать
