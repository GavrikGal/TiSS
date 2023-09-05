import os
import re
from typing import List

import pandas as pd

from reader.base_file_reader import BaseFileReader
from reader.base_file import BaseFile


class R2Reader(BaseFileReader):

    def read(self, file: BaseFile) -> float:
        if 'R2=' in file.name:
            part_with_r2 = file.name.split("R2=")[1].split(" ")[0]
            r2 = re.search(r'([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))', part_with_r2)[0]
            return float(r2)
        if len(re.findall(r' (\d+)', file.name)):
            r2 = re.findall(r' (\d+)', file.name)[-1]
            return float(r2)

        raise ValueError("R2 not found in filename")


class SignalsReader(BaseFileReader):
    def read(self, file: BaseFile) -> List[float]:
        signals = pd.read_csv(os.path.join(file.dir.path, file.name), sep='\t', encoding='cp1251',
                              usecols=[2], skiprows=2, names=['signal'])
        return signals['signal'].tolist()


class NoisesReader(BaseFileReader):
    def read(self, file: BaseFile) -> List[float]:
        noises = pd.read_csv(os.path.join(file.dir.path, file.name), sep='\t', encoding='cp1251',
                             usecols=[3], skiprows=2, names=['noise'])
        return noises['noise'].tolist()



    # def find_serial_number_in_file_name(self): ...
    # def find_angel_in_file_name(self): ...
    # def find_date_in_file_attribute(self): ...
    # def find_r2_in_file_name(self): ...
    # def find_frequencies_in_file_body(self): ...
    # def find_signal_in_file_body(self): ...
    # def find_noise_in_file_body(self): ...

# angle = np.deg2rad(float(re.findall(r'\((\d+)\)', filename)[0]))
# r2 = float(re.findall(r'\) (\d+)', filename)[0])
