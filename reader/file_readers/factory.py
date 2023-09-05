from typing import Callable

from reader.constants import IndexType, DataType
from reader.base_file_reader import BaseFileReader
from reader.base_factory import BaseFileReaderFactory, ClassNotFoundError

from .result_reader import R2Reader, SignalsReader, NoisesReader
from .index_reader import SerialNumberReader, AngleReader, DateReader, FrequenciesReader


class FileReaderFactory(BaseFileReaderFactory):
    """Фабрика для возвращения нужного типа чтеца данных"""
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(FileReaderFactory, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_index_reader(index_type: IndexType) -> BaseFileReader:
        """Возвращает экземпляр класса для чтения индексов"""

        classes: dict[IndexType, Callable[..., BaseFileReader]] = {
            IndexType.Number: SerialNumberReader,
            IndexType.Angel: AngleReader,
            IndexType.Date: DateReader,
            IndexType.Frequency: FrequenciesReader,
        }

        class_ = classes.get(IndexType.Number, None)
        if class_ is not None:
            return class_()

        raise ClassNotFoundError

    @staticmethod
    def get_data_reader(data_type: DataType) -> BaseFileReader:
        """Возвращает экземпляр класса для чтения данных"""

        classes: dict[DataType, Callable[..., BaseFileReader]] = {
            DataType.R2: R2Reader,
            DataType.Signal: SignalsReader,
            DataType.Noise: NoisesReader,
        }

        class_ = classes.get(data_type, None)
        if class_ is not None:
            return class_()

        raise ClassNotFoundError
