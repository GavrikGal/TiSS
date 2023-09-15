import math


class Grid:
    col: int
    row: int

    def __init__(self, item_count: int):
        self.col = self.calc_cols(item_count)
        self.row = self.calc_rows(item_count, self.col)

    @staticmethod
    def calc_cols(item_count: int) -> int:
        n_cols = 5
        if item_count < 26:
            n_cols = math.floor(item_count ** 0.5)
        return int(n_cols)

    @staticmethod
    def calc_rows(item_count: int, cols_count):
        return math.ceil(item_count / cols_count)
