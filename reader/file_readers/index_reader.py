import os
import re
from datetime import datetime
from typing import List, Union

import pandas as pd

from reader.base_file_reader import FileReader
from reader.directory import Dir


class SerialNumberReader(FileReader):
    def read(self, filename, *args) -> str:
        serial_number = str(re.search(r'[A-Za-z0-9]+', filename)[0])
        return serial_number


class AngleReader(FileReader):
    def read(self, filename, *args) -> Union[float, None]:
        angle = re.findall(r'\((\d+)\)', filename)
        if len(angle) > 0:
            return float(angle[0])
        return None


class DateReader(FileReader):
    def read(self, filename, *args) -> datetime:
        ...
        # print("Read Date from file attribute")


class FrequenciesReader(FileReader):
    def read(self, filename, directory) -> List[float]:
        frequencies = pd.read_csv(os.path.join(directory.path, filename), sep='\t', encoding='cp1251', usecols=[1],
                                  skiprows=1, index_col=0)
        return frequencies.values

