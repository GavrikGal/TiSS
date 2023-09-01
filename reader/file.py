from constants import DATA_TYPE, INDEX_TYPE
from base_factory import BaseFileReaderFactory


class File:
    """Файл"""
    def __init__(self, file_name: str, file_reader_factory: BaseFileReaderFactory):
        self.name = file_name
        self.file_reader_factory = file_reader_factory

    def get_index(self, index_type: INDEX_TYPE):
        index_reader = self.file_reader_factory.get_index_reader(index_type)
        index = index_reader.read() # todo: надо через абстракцию объяснить, что объект умееет читать
        print(f'Index [{index}] with type [{index_type}] has been read from file - {self.name}')
        # todo: тут надо звать парсеры
        return None

    def get_data(self, data_type: DATA_TYPE):
        print(f'Data with type [{data_type}] has been read from file - {self.name}')
        # todo: тут надо звать парсеры
        return None

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def find_serial_number_in_file_name(self): ...
    def find_angel_in_file_name(self): ...
    def find_date_in_file_attribute(self): ...
    def find_r2_in_file_name(self): ...
    def find_frequencies_in_file_body(self): ...
    def find_signal_in_file_body(self): ...
    def find_noise_in_file_body(self): ...

# angle = np.deg2rad(float(re.findall(r'\((\d+)\)', filename)[0]))
# r2 = float(re.findall(r'\) (\d+)', filename)[0])
