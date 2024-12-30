from typing import Self

from game.components.field import Field


class Row:
    row: list[int]
    side_len: int
    empty_cells: list[int]

    def set_row(self, _row: list[int]):
        self.row = _row
        self.side_len = len(_row)
        self.empty_cells = Field.get_row_empty_cells(_row)

    @classmethod
    def from_row(cls, _row: list[int]) -> Self:
        row = Row()
        row.set_row(_row)

        return row

    def get_values(self, x):
        return self.try_value(x - 1), self.try_value(x), self.try_value(x + 1)

    def try_value(self, index: int) -> int or None:
        if index < 0 or index > self.side_len - 1 or self.row[index] == 0:
            return None

        return self.row[index]
