import pandas as pd

from reader.base_data_frame import BaseDataFrame


class DataFrame(pd.DataFrame, BaseDataFrame):
    """Класс таблиц данных"""
