from typing import Callable, Union
from reader.constants import IndexType, DataType, ColumnType
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
    def get_attribute_reader(attribute_type: Union[IndexType, ColumnType]) -> BaseFileReader:
        """Возвращает экземпляр класса для чтения атрибутов"""

        if isinstance(attribute_type, IndexType):
            classes: dict[IndexType, Callable[..., BaseFileReader]] = {
                IndexType.Number: SerialNumberReader,
                IndexType.Angel: AngleReader,
                IndexType.Date: DateReader,
                IndexType.Frequency: FrequenciesReader,
            }
        else:
            classes: dict[ColumnType, Callable[..., BaseFileReader]] = {
                ColumnType.Number: SerialNumberReader,
                ColumnType.Angel: AngleReader,
                ColumnType.Date: DateReader,
            }

        class_ = classes.get(attribute_type, None)
        if class_ is not None:
            return class_()

        raise ClassNotFoundError(f'IndexReader with Type: [{attribute_type}] not Found')

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

        raise ClassNotFoundError(f'DataReader with Type: [{data_type}] not Found')
