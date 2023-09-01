from ..base_file_reader import FileReader


class NumberReader(FileReader):
    def read(self):
        print("Read Number from filename")


class AngelReader(FileReader):
    def read(self):
        print("Read Angel from filename")


class DateReader(FileReader):
    def read(self):
        print("Read Date from file attribute")


class FrequenciesReader(FileReader):
    def read(self):
        print("Read Frequencies from file body")
