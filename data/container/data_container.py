from typing import List

from data.base_data_container import BaseDataContainer


class DataContainer(BaseDataContainer):

    def get_unique_columns(self) -> List[str]:

        unique_columns = set()
        for data_frame in self.values():
            for column in data_frame.columns.values:
                unique_columns.add(column)

        return sorted(list(unique_columns))
