import re
from typing import List

from reader.base_file_reader import FileReader
from reader.base_file import BaseFile


class R2Reader(FileReader):

    def read(self, file: BaseFile) -> float:
        if 'R2=' in file.name:
            part_with_r2 = file.name.split("R2=")[1].split(" ")[0]
            r2 = re.search(r'([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))', part_with_r2)[0]
            return float(r2)
        if len(re.findall(r' (\d+)', file.name)):
            r2 = re.findall(r' (\d+)', file.name)[-1]
            return float(r2)

        raise ValueError("R2 not found in filename")


class SignalsReader(FileReader):
    def read(self, file: BaseFile) -> List[float]:
        ...
        # print("Read Signal from file body")


class NoisesReader(FileReader):
    def read(self, file: BaseFile) -> List[float]:
        ...
        # print("Read Noise from file body")



    # def find_serial_number_in_file_name(self): ...
    # def find_angel_in_file_name(self): ...
    # def find_date_in_file_attribute(self): ...
    # def find_r2_in_file_name(self): ...
    # def find_frequencies_in_file_body(self): ...
    # def find_signal_in_file_body(self): ...
    # def find_noise_in_file_body(self): ...

# angle = np.deg2rad(float(re.findall(r'\((\d+)\)', filename)[0]))
# r2 = float(re.findall(r'\) (\d+)', filename)[0])
