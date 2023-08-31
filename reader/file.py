from constants import DATA_TYPE


class File:
    """Файл"""
    def __init__(self, file_name: str):
        self.name = file_name

    def read_data(self, data_type: DATA_TYPE):
        print(f'Data with type [{data_type}] has been read from file - {self.name}')
        # todo: тут надо звать парсеры
        return None

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
