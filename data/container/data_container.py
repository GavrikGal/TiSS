from typing import List

from data.base_data_container import BaseDataContainer


class DataContainer(BaseDataContainer):

    def get_unique_index(self) -> List[object]:

        unique_index = set()
        for data_frame in self.values():
            for index in data_frame.index.values:
                unique_index.add(index)

        return sorted(list(unique_index))
