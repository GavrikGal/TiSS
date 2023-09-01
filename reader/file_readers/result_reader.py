from ..base_file_reader import FileReader


class R2Reader(FileReader):

    def read(self):
        print("Read R2 from filename")


class SignalsReader(FileReader):
    def read(self):
        print("Read Signal from file body")


class NoisesReader(FileReader):
    def read(self):
        print("Read Noise from file body")
