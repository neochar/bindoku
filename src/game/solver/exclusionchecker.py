from typing import Self

from game.components.cell import Cell
from game.components.field import Field
from game.components.row import Row
from game.const import EQUALITY_MIN_CELLS_COUNT


class ExclusionChecker:
    field: list[list[int]]
    filled_rows: list[list[int]]
    side_len: int

    @classmethod
    def from_field(cls, field: list[list[int]]) -> Self:
        equal_rows_checker = ExclusionChecker()
        equal_rows_checker.set_field(field)

        return equal_rows_checker

    def set_field(self, field):
        self.field = field
        self.side_len = len(field[0])
        self.filled_rows = Field.get_filled_rows(field)

    def solve(self, field: list[list[int]]) -> list[list[int]]:
        self.set_field(field)
        # self.try_semiequal_rows()

        return self.field

    def _find_equalities_number(self, y: int, row: list[int]) -> int:
        equalities = 0

        for x, filled_cell in enumerate(row):
            if self.field[y][x] != 0 and self.field[y][x] == row[x]:
                equalities += 1

        return equalities

    def _fill_empty(self, y, empty_cells, filled_row):
        for index in empty_cells:
            self.field[y][index] = Cell.invert(
                filled_row[index]
            )

    def try_by_exclusion(self):
        for y, row in enumerate(self.field):
            self.field[y] = self._try_by_exclusion(Row.from_row(row))

        return self.field

    def _try_by_exclusion(self, row: Row):
        if row.side_len - len(row.empty_cells) == EQUALITY_MIN_CELLS_COUNT + 1 \
                and abs(row.count_1 - row.count_2) == 1:
            for x in range(1, row.side_len - 2):
                row.row = self._try_exclusion(x, row)

        return row.row

    @staticmethod
    def _try_exclusion(x: int, row: Row):
        values = row.get_values(x)
        _prev, _this, _next = values
        realvalues = list(filter(
            lambda v: v is not None,
            values
        ))
        if len(realvalues) < 1:
            return row.row

        if _this is None and (_prev is None or _next is None):
            for cell in row.empty_cells:
                if cell < x - 1 or cell > x + 1:
                    row.row[cell] = realvalues.pop()

        return row.row
