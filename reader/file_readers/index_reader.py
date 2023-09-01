import re
from datetime import datetime
from typing import List

from reader.base_file_reader import FileReader


class SerialNumberReader(FileReader):
    def read(self, filename) -> str:
        serial_number = str(re.search(r'[A-Za-z0-9]+', filename)[0])
        return serial_number


class AngelReader(FileReader):
    def read(self, filename) -> float:
        angle = float(re.findall(r'\((\d+)\)', filename)[0])
        # todo: test
        return angle


class DateReader(FileReader):
    def read(self, filename) -> datetime:
        ...
        # print("Read Date from file attribute")


class FrequenciesReader(FileReader):
    def read(self, filename) -> List[float]:
        ...
        # print("Read Frequencies from file body")
