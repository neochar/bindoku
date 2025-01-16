from typing import Self

from game.components.cell import Cell
from game.components.field import Field
from game.const import EQUALITY_MIN_CELLS_COUNT
from game.utils.logger import file_log


class EqualRowsChecker:
    field: list[list[int]]
    filled_rows: list[list[int]]
    side_len: int

    @classmethod
    def from_field(cls, field: list[list[int]]) -> Self:
        equal_rows_checker = EqualRowsChecker()
        equal_rows_checker.set_field(field)

        return equal_rows_checker

    def set_field(self, field):
        self.field = field
        self.side_len = len(field[0])
        self.filled_rows = Field.get_filled_rows(field)

    def solve(self, field: list[list[int]]) -> list[list[int]]:
        self.set_field(field)
        self.try_equal_rows()

        return self.field

    def try_equal_rows(self):
        for y, row in enumerate(self.field):
            empty_cells = Field.get_row_empty_cells(row)
            if len(empty_cells) == EQUALITY_MIN_CELLS_COUNT:  # Candidate
                for filled_row in self.filled_rows:
                    if self._find_equalities_number(
                            y,
                            filled_row
                    ) == self.side_len - EQUALITY_MIN_CELLS_COUNT:
                        self._fill_empty(
                            y,
                            empty_cells,
                            filled_row
                        )

    def _find_equalities_number(self, y: int, row: list[int]) -> int:
        equalities = 0

        for x, filled_cell in enumerate(row):
            if self.field[y][x] != 0 and self.field[y][x] == row[x]:
                equalities += 1

        return equalities

    def _fill_empty(self, y, empty_cells, filled_row):
        file_log(y, prefix='fill_empty', data=[self.field[y], filled_row, empty_cells])
        for index in empty_cells:
            if self.field[y][index] != 0:
                continue
            self.field[y][index] = Cell.invert(
                filled_row[index]
            )
