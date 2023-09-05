import os
import re
from datetime import datetime
from typing import List, Union

import pandas as pd

from reader.base_file_reader import FileReader
from reader.base_file import BaseFile


class SerialNumberReader(FileReader):
    def read(self, file: BaseFile) -> str:
        serial_number = str(re.search(r'[A-Za-z0-9]+', file.name)[0])
        return serial_number


class AngleReader(FileReader):
    def read(self, file: BaseFile) -> Union[float, None]:
        angle = re.findall(r'\((\d+)\)', file.name)
        if len(angle) > 0:
            return float(angle[0])
        return None


class DateReader(FileReader):
    def read(self, file: BaseFile) -> datetime:
        ...
        # print("Read Date from file attribute")


class FrequenciesReader(FileReader):
    def read(self, file: BaseFile) -> List[float]:
        frequencies = pd.read_csv(os.path.join(file.dir.path, file.name), sep='\t', encoding='cp1251', usecols=[1],
                                  skiprows=1, index_col=0)
        return frequencies.values

