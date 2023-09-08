import enum


class IndexType(enum.IntFlag):
    Number = 1
    Angel = 2
    Date = 3
    Frequency = 4


class DataType(enum.IntFlag):
    R2 = 1
    Signal = 2
    Noise = 3


class ColumnType(enum.IntFlag):
    Number = 1
    Angel = 2
    Date = 3
    Frequency = 4
