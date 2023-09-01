from typing import Hashable, Callable

from ..constants import INDEX_TYPE, DATA_TYPE
from ..base_file_reader import FileReader
from ..base_factory import BaseFileReaderFactory, ClassNotFoundError

from .result_reader import R2Reader, SignalsReader, NoisesReader
from .index_reader import NumberReader, AngelReader, DateReader, FrequenciesReader


class FileReaderFactory(BaseFileReaderFactory):
    """Фабрика для возвращения нужного типа чтеца данных"""

    @staticmethod
    def get_index_reader(index_type: INDEX_TYPE) -> FileReader:
        """Возвращает экземпляр класса для чтения индексов"""

        print("get_index_reader():", index_type)
        print("get_index_reader() hash():", hash(index_type))

        classes: dict[INDEX_TYPE, Callable[..., FileReader]] = {
            INDEX_TYPE.NUMBER: NumberReader,
            INDEX_TYPE.ANGEL: AngelReader,
            INDEX_TYPE.DATE: DateReader,
            INDEX_TYPE.FREQUENCY: FrequenciesReader,
        }

        print(classes)

        class_ = classes.get(index_type, None)
        if class_ is not None:
            return class_()

        raise ClassNotFoundError

    @staticmethod
    def get_data_reader(data_type: DATA_TYPE) -> FileReader:
        """Возвращает экземпляр класса для чтения данных"""

        classes: dict[DATA_TYPE, Callable[..., FileReader]] = {
            DATA_TYPE.R2: R2Reader,
            DATA_TYPE.SIGNAL: SignalsReader,
            DATA_TYPE.NOISE: NoisesReader,
        }

        class_ = classes.get(data_type, None)
        if class_ is not None:
            return class_

        raise ClassNotFoundError
