from datetime import datetime
from io import StringIO

from game.const import MAX_MOVES
from game.errors import FieldNotSolvableException
from game.components.field import Field
from game.solver.equalrowschecker import EqualRowsChecker
from game.solver.rowchecker import RowChecker
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
        self.row_solver = RowChecker()
        self.equal_rows_solver = EqualRowsChecker()

    def solve(
            self,
            field: list[list[int]],
            max_moves: int = MAX_MOVES
    ) -> [int, list[list[int]]]:
        cleanup_logs()
        self.side_len = len(field)
        self.side_half = self.side_len // 2
        self.field_len = self.side_len * len(field[0])

        moves = 0

        """
        1. In puzzler we detect amount of empty cells
        2. Until solvable decrease amount of empty cells
        """

        while 1:
            moves += 1
            if moves > max_moves:
                break

            field = self.move(field)
            if Field.is_incomplete(field):
                continue

            if self.validator.validate(field)[0] is True:
                return moves, field

        raise FieldNotSolvableException

    def is_solvable(self, field: list[list[int]]) -> bool:
        try:
            self.solve(field.copy())
        except FieldNotSolvableException:
            return False

        return True

    def move(self, field) -> list[list[int]]:
        field = Field.rotate_ccw(self._move(field))
        field = Field.rotate_ccw(self._move(field))
        field = Field.rotate_ccw(self._move(field))
        field = Field.rotate_ccw(self._move(field))

        return field

    def _move(self, field) -> list[list[int]]:
        for y, row in enumerate(field):
            field[y] = self.row_solver.solve(row)
            field = self.equal_rows_solver.solve(field)

        return field
