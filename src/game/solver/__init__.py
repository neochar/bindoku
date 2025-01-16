import copy

from game.components.field import Field
from game.const import MAX_TICKS
from game.errors import FieldNotSolvableException
from game.solver.equal_rows_checker import EqualRowsChecker
from game.solver.exclusion_checker import ExclusionChecker
from game.solver.row_checker import RowChecker
from game.utils.logger import file_log, cleanup_logs
from game.validator import Validator


class Solver:
    field: list[list[int]]
    side_len: int  # Length of side
    side_half: int  # Half of length of side
    field_len: int  # Square of field
    validator: Validator

    def __init__(self, validator: Validator):
        self.validator = validator
        self.row_checker = RowChecker()
        self.equal_rows_checker = EqualRowsChecker()
        self.exclusion_checker = ExclusionChecker()

    def solve(
            self,
            field: list[list[int]],
            max_ticks: int = MAX_TICKS
    ) -> [int, list[list[int]]]:
        cleanup_logs()

        self.side_len = len(field)
        self.side_half = self.side_len // 2
        self.field_len = self.side_len * len(field[0])
        self.field = copy.deepcopy(field)

        ticks = 0

        """
        TODO:
        1. Write more tests (there's a bug)
        2. Find the bug and fix it (in equal_rows_solver I guess)
        3. Implement brute force checker
        """

        while 1:
            ticks += 1
            if ticks > max_ticks:
                break

            field = self.move(field, ticks)
            if Field.is_incomplete(field):
                continue

            if self.validator.validate(field)[0] is True:
                return ticks, field

        self.field = field
        raise FieldNotSolvableException

    def is_solvable(self, field: list[list[int]]) -> bool:
        try:
            self.solve(field.copy())
        except FieldNotSolvableException:
            return False

        return True

    def move(self, field: list[list[int]], move: int) -> list[list[int]]:
        file_log(move, key='Before', data=field)
        field = Field.rotate_ccw(self._move(field))
        file_log(move, key='Middle', data=Field.rotate_cw(field))
        field = Field.rotate_cw(self._move(field))
        file_log(move, key='After', data=field)

        return field

    def _move(self, field) -> list[list[int]]:
        for y, row in enumerate(field):
            field[y] = self.row_checker.solve(row)
            field = self.equal_rows_checker.solve(field)
            field = self.exclusion_checker.solve(field)

        return field
