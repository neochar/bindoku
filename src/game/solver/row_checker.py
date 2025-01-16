from typing import Self

from game.components.cell import Cell
from game.components.row import Row
from game.const import VALUES


class RowChecker:
    row: Row
    row_len: int
    row_half: int

    @classmethod
    def from_row(cls, row: list[int]) -> Self:
        row_checker = RowChecker()
        row_checker.set_row(row)
        return row_checker

    def set_row(self, row):
        self.row = Row.from_row(row)
        self.row_len = len(row)
        self.row_half = len(row) // 2

    def solve(self, row: list[int]) -> list[int]:
        self.set_row(row)
        self.try_count()
        self.try_rules()

        return self.row.row

    def try_count(self):
        for value in VALUES:
            invert = Cell.invert(value)
            if self.row.row.count(value) >= self.row_half:
                for x, cell in enumerate(self.row.row):
                    if cell == 0:
                        self.row.row[x] = invert

        return self.row.row

    def try_rules(self):
        for x, cell in enumerate(self.row.row):
            if cell != 0:
                continue

            self.try_101(x)
            self.try_110(x)
            self.try_011(x)

        return self.row.row

    def try_101(self, x):
        _prev, _, _next = self.row.get_values(x)

        if _prev is not None and _next is not None and _prev == _next:
            self.row.row[x] = Cell.invert(_prev)

        return self.row.row

    def try_110(self, x):
        _prev, _this, _ = self.row.get_values(x)

        if _prev is not None:
            _preprev = self.row.try_value(x - 2)
            if _preprev is not None and _prev == _preprev:
                self.row.row[x] = Cell.invert(_prev)

        return self.row.row

    def try_011(self, x):
        _, _this, _next = self.row.get_values(x)

        if _next is not None:
            _pronext = self.row.try_value(x + 2)
            if _pronext is not None and _next == _pronext:
                self.row.row[x] = Cell.invert(_next)

        return self.row.row
