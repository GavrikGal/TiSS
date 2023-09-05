import pathlib
from typing import List

from reader.base_directory import BaseDirectory


class Dir(BaseDirectory):
    def __init__(self, dir_path):
        self.path: pathlib.Path = pathlib.Path(dir_path).resolve()

    def get_file_list(self) -> List[str]:

        file_list = [file.name for file in self.path.iterdir()
                     if file.is_file() and file.name.endswith('.txt')]
        return file_list

    def __repr__(self):
        return self.path.name

    def __str__(self):
        return self.path.name
