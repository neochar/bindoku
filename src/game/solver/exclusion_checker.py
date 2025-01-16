import copy
import itertools
from typing import Self

from game.components.field import Field
from game.components.row import Row
from game.const import VALUES
from game.utils import one
from game.validator import Validator


class ExclusionChecker:
    field: list[list[int]]
    filled_rows: list[list[int]]
    side_len: int

    @classmethod
    def from_field(cls, field: list[list[int]]) -> Self:
        exclusion_checker = ExclusionChecker()
        exclusion_checker.set_field(field)

        return exclusion_checker

    def set_field(self, field):
        self.field = field
        self.side_len = len(field[0])
        self.filled_rows = Field.get_filled_rows(field)

    def solve(self, field: list[list[int]]) -> list[list[int]]:
        self.set_field(field)
        self.try_by_exclusion()

        return self.field

    def try_by_exclusion(self):
        for y, row in enumerate(self.field):
            self.field[y] = self.try_row_exclusion(Row.from_row(row))

        return self.field

    def try_row_exclusion(self, row: Row):
        if len(row.empty_cells) >= 3 and one([
            row.count_1 == (row.side_len // 2) - 1,
            row.count_2 == (row.side_len // 2) - 1,
        ]):
            return self._try_row_exclusion(row)

        return row.row

    def _try_row_exclusion(self, row: Row):
        val_to_put, cells_to_put = self._get_row_to_put(row)

        if cells_to_put < 2:
            return row.row

        valids = self._find_valids(
            self._get_variants(
                row,
                cells_to_put,
                val_to_put
            )
        )

        if len(valids) == 1:
            return valids[0]
        else:
            for x in row.empty_cells:
                vals = []
                for valid in valids:
                    vals.append(valid[x])

                if len(set(vals)) == 1:
                    row.row[x] = val_to_put

        return row.row

    @staticmethod
    def _find_valids(variants):
        valids = []
        validator = Validator()
        for i, variant in enumerate(variants):
            if validator.validate_row(variant, force_check=True):
                valids.append(variant)

        if len(valids) == len(variants):
            return []

        return valids

    @staticmethod
    def _get_variants(row, cells_to_put, val_to_put):
        variants = []

        for i, combination in enumerate(itertools.combinations(
                row.empty_cells,
                cells_to_put
        )):
            _row = copy.deepcopy(row.row)
            for x in combination:
                _row[x] = val_to_put
            variants.append(_row)

        return variants

    @staticmethod
    def _get_row_to_put(row):
        return (
            VALUES[1] if row.count_1 > row.count_2 else VALUES[0],
            len(row.empty_cells) - 1)
