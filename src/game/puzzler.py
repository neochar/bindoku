import copy
import random

from game.components.field import Field
from game.const import PUZZLE_MAX_THRESHOLD, PUZZLE_MIN_THRESHOLD
from game.solver import Solver


class Puzzler:
    original: list[list[int]]
    field: list[list[int]]
    solver: Solver
    seed: int

    def __init__(
            self,
            solver: Solver,
    ):
        self.solver = solver

    def puzzle(self, _field: list[list[int]]) -> list[list[int]]:
        field_len = len(_field)
        side_len = len(_field[0])

        cells_to_hide = int(PUZZLE_MIN_THRESHOLD * field_len * side_len)
        max_cells_to_hide = int(PUZZLE_MAX_THRESHOLD * field_len * side_len)

        field = copy.deepcopy(_field)

        moves = 0
        while 1:
            candidate = self.hide_cells(
                copy.deepcopy(field),
                cells_to_hide
            )
            if any([
                not self.solver.is_solvable(candidate),
                cells_to_hide >= max_cells_to_hide,
            ]):
                if not Field.is_incomplete(field):
                    return self.puzzle(_field)

                return field

            field = candidate

            cells_to_hide += 1
            moves += 1

    @staticmethod
    def hide_cells(_field: list[list[int]], cells_to_hide: int) -> list[list[int]]:
        side_len = len(_field[0])

        hidden_cells = 0
        for y, row in enumerate(_field):
            for x, cell in enumerate(row):
                if cell == 0:
                    hidden_cells += 1

        while hidden_cells < cells_to_hide:
            x = random.randint(0, side_len - 1)
            y = random.randint(0, side_len - 1)
            if _field[y][x] == 0:
                continue

            _field[y][x] = 0
            hidden_cells += 1

        return _field
